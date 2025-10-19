# pages/2_Emoji_List.py
import streamlit as st
import json
from pathlib import Path

# --- データ読み込み (変更なし) ---
@st.cache_data
def load_emoji_data():
    """JSONファイルから絵文字データを読み込み、キャッシュする"""
    try:
        json_path = Path(__file__).parent.parent / "emoji_data.json"
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        st.error("`emoji_data.json` not found. Please create it in the root directory.")
        return []

# --- メインのUI (シンプル版に修正) ---
st.title("SGG Custom Emoji Code List")

emoji_data = load_emoji_data()

if emoji_data:
    # --- カテゴリによる絞り込み機能 ---
    st.write("You can filter the list by selecting a category below.")
    categories = ["All"] + sorted(list(set(item['category'] for item in emoji_data)))
    selected_category = st.selectbox("Filter by category:", categories)
    
    st.divider()

    # --- フィルタリングロジック ---
    if selected_category != "All":
        filtered_list = [item for item in emoji_data if item['category'] == selected_category]
    else:
        filtered_list = emoji_data

    # --- リスト表示 ---
    display_categories = sorted(list(set(item['category'] for item in filtered_list)))

    if not filtered_list:
        st.info("Select a category to see the emoji list.")
    else:
        for category in display_categories:
            st.subheader(category)
            
            items_in_category = [item for item in filtered_list if item['category'] == category]
            
            # 2列表示にする
            col1, col2 = st.columns(2)
            
            for i, item in enumerate(items_in_category):
                # ★★★ 変更点 ★★★
                # データに含まれる 'name' を、そのまま表示するだけ
                emoji_code_to_display = item['name']
                
                # 画像があれば表示する
                if "image_url" in item and item["image_url"]:
                    display_html = f'<div style="display: flex; align-items: center; margin-bottom: 8px;">' \
                                 f'<img src="{item["image_url"]}" width="28" height="28" style="margin-right: 10px;">' \
                                 f'<span>{emoji_code_to_display}</span>' \
                                 f'</div>'
                    
                    # 交互に列に配置していく
                    if i % 2 == 0:
                        col1.markdown(display_html, unsafe_allow_html=True)
                    else:
                        col2.markdown(display_html, unsafe_allow_html=True)
                else:
                    # 画像がない場合はコードだけ表示
                    if i % 2 == 0:
                        col1.markdown(f"`{emoji_code_to_display}`")
                    else:
                        col2.markdown(f"`{emoji_code_to_display}`")