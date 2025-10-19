# Discordlit Tools 🛠️

A collection of web-based utilities built with Streamlit to make managing and formatting content for Discord easier. This app is designed for contents creators and users who want to create clean, well-formatted messages without manually fighting with Markdown. — BirksG

## 👉 [Live Demo](https://discordlit.streamlit.app/)

You can use the live version of the app hosted on Streamlit Community Cloud.

---

## Features

This multi-page application currently includes the following tools:

*   **📝 Table Formatter**: Converts table data (copied from sources like Google Sheets or Excel) into a perfectly aligned, monospaced format that looks great on both desktop and mobile Discord.
*   **😂 Emoji List**: Displays a filterable and categorized list of all custom server emojis, making it easy to find and view their codes.
*   **🕒 Timestamp Generator**: Creates dynamic timestamps that automatically adjust to each user's local time zone, perfect for coordinating international events.

---

## How to Use

### 📝 Table Formatter

1.  **Copy Data**: Copy a range of cells from your spreadsheet (e.g., Google Sheets).
2.  **Paste into App**: Paste the copied data into the large text area under "Input Data".
3.  **Adjust Settings**:
    *   **Max column width**: Sets the maximum character width for any column before text wraps to a new line.
    *   **Spacing**: The number of spaces between each column.
    *   **Padding**: The number of spaces at the very beginning and end of each line.
4.  **Choose Format Style**:
    *   **Code block (` ``` `)**: Recommended for tables with multi-line text. Wraps the entire table in one block.
    *   **Inline code (` `)**: Wraps each line individually. Best for simple, single-line tables.
    *   **Add [ ] brackets**: An optional style to enclose each line in square brackets.
5.  **Convert**: Click the **"Convert Table"** button.
6.  **Copy Result**: The formatted table will appear below. The output box has a convenient copy button in the top-right corner.

### 😂 Emoji List

1.  **Navigate**: Select "Emoji List" from the sidebar.
2.  **Filter by Category**: Use the dropdown menu to view emojis from a specific category.
3.  **View and Copy**: The page displays the emoji image and its full Discord code. Simply select and copy the code you need.

### 🕒 Timestamp Generator
1.  **Navigate**: Select "Timestamp Generator" from the sidebar.
2.  **Enter Date & Time**: Use the calendar and time inputs to set your event time.
3.  **Select Your Time Zone**: Choose the time zone that your input corresponds to (e.g., `Asia/Tokyo`, `US/Pacific`).
4.  **Generate**: Click the **"Generate Timestamps"** button.
5.  **Copy a Style**: A list of different timestamp formats will appear. Copy the code for the style you want (e.g., "Relative Time" for "in 2 hours").

---

## Local Development

If you want to run this project on your own machine:

1.  **Prerequisites**:
    *   Python 3.8+
    *   An IDE like VSCode

2.  **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/discordlit.git
    cd discordlit
    ```

3.  **Create and activate a virtual environment**:
    ```bash
    # Create the venv
    python -m venv .venv

    # Activate on Windows (PowerShell)
    .venv\Scripts\Activate.ps1

    # Activate on macOS/Linux
    source .venv/bin/activate
    ```

4.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

5.  **Run the Streamlit app**:
    ```bash
    streamlit run app.py
    ```
    The application will open in your web browser.

## Adding a New Tool

This project is structured as a multi-page Streamlit app. To add a new tool:

1.  Create a new Python file inside the `/pages` directory.
2.  Name the file using the pattern `number_Tool_Name.py` (e.g., `3_New_Tool.py`). The number determines the order in the sidebar.
3.  Write your Streamlit code in that file. Streamlit will automatically detect it and add it to the sidebar navigation.

## License

This project is licensed under the MIT License.