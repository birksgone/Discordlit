# pages/1_Table_Formatter.py
import streamlit as st
import csv
import io
import unicodedata

# --- 処理ロジック (変更なし) ---
def get_east_asian_width_count(text):
    count = 0
    for char in text:
        if unicodedata.east_asian_width(char) in 'FWA':
            count += 2
        else:
            count += 1
    return count

def wrap_text(text, width):
    lines = []
    current_line = ""
    current_width = 0
    for char in text:
        char_width = get_east_asian_width_count(char)
        if current_width + char_width > width:
            lines.append(current_line)
            current_line = char
            current_width = char_width
        else:
            current_line += char
            current_width += char_width
    if current_line:
        lines.append(current_line)
    return lines if lines else [""]

def create_formatted_lines(tsv_text, max_width_per_column, column_spacing, line_padding):
    if not tsv_text.strip(): return None
    reader = csv.reader(io.StringIO(tsv_text), delimiter='\t')
    data = [row for row in reader if any(field.strip() for field in row)]
    if not data: return None
    num_columns = max(len(row) for row in data)
    for row in data:
        while len(row) < num_columns: row.append("")
    last_real_column = -1
    for row in data:
        for i in range(len(row) - 1, -1, -1):
            if row[i].strip():
                if i > last_real_column: last_real_column = i
                break
    num_columns = last_real_column + 1
    data = [row[:num_columns] for row in data]
    col_widths = [0] * num_columns
    for row in data:
        for i, cell in enumerate(row):
            width = get_east_asian_width_count(cell)
            col_widths[i] = max(col_widths[i], width)
    for i in range(num_columns):
        if col_widths[i] > max_width_per_column: col_widths[i] = max_width_per_column
    wrapped_data = [[wrap_text(cell, col_widths[i]) for i, cell in enumerate(row)] for row in data]
    row_heights = [max(len(cell_lines) for cell_lines in row) for row in wrapped_data]
    output_lines = []
    spacing_str = ' ' * column_spacing
    padding_str = ' ' * line_padding
    for i, row in enumerate(wrapped_data):
        for line_num in range(row_heights[i]):
            line_parts = []
            for j, cell_lines in enumerate(row):
                text_part = cell_lines[line_num] if line_num < len(cell_lines) else ""
                width = get_east_asian_width_count(text_part)
                padding = ' ' * (col_widths[j] - width)
                line_parts.append(text_part + padding)
            full_line = padding_str + spacing_str.join(line_parts) + padding_str
            output_lines.append(full_line)
    return output_lines

def format_for_discord_inline(lines, use_brackets=False):
    if lines is None: return ""
    if use_brackets: lines = [f"[{line}]" for line in lines]
    return "\n".join([f"`{line}`" for line in lines])

def format_for_discord_block(lines, use_brackets=False):
    if lines is None: return ""
    if use_brackets: lines = [f"[{line}]" for line in lines]
    return "```\n" + "\n".join(lines) + "\n```"

# --- ここからが修正されたUI部分 ---

st.title("Discord Table Formatter")

# セッション状態を初期化して、前の結果を保持できるようにする
if 'output_text' not in st.session_state:
    st.session_state.output_text = ""

# --- 設定項目 ---
st.header("1. Settings")
max_width = st.number_input("Max column width (35 is easy for mobile device):", min_value=10, value=35)
spacing = st.number_input("Spacing (between columns):", min_value=0, value=2)
padding = st.number_input("Padding (start/end of line):", min_value=0, value=0)

st.header("2. Format Style")
format_style = st.radio(
    "Choose format style",
    ("Code block (```) for full width", "Inline code (` `) for narrow width"),
    label_visibility="collapsed"
)
use_brackets = st.checkbox("Add [ ] brackets")

# --- 入力エリア ---
st.header("3. Input Data")
st.write("Paste your table data from Google Sheets or CSV below.")
input_text = st.text_area("Input Data", height=250, label_visibility="collapsed")

# --- 実行ボタン ---
if st.button("Convert Table"):
    if input_text:
        try:
            # ボタンが押されたら変換処理を実行
            formatted_lines = create_formatted_lines(input_text, max_width, spacing, padding)

            if format_style == "Inline code (` `)":
                # 結果をセッション状態に保存
                st.session_state.output_text = format_for_discord_inline(formatted_lines, use_brackets)
            else:
                st.session_state.output_text = format_for_discord_block(formatted_lines, use_brackets)

        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        # 入力が空の場合
        st.warning("Please paste some data into the input area first.")
        st.session_state.output_text = ""

# --- 結果表示 ---
# セッション状態に結果があれば、それを表示する
if st.session_state.output_text:
    st.header("4. Result")
    st.code(st.session_state.output_text, language="")