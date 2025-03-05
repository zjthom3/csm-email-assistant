# Email Generator for Customer Success Managers

## Overview
This application is designed to help Customer Success Managers generate professional and helpful email responses efficiently. The tool uses OpenAI's GPT model to refine drafts, ensure appropriate tone, and structure replies effectively.

## Features
- **Input Fields**: Provide the sender's email, draft notes, and optional keywords.
- **Tone Selection**: Choose from different response tones (Helpful, Professional, Friendly, or match the sender's tone).
- **AI-Powered Email Generation**: Uses OpenAI's GPT model to improve and finalize email drafts.
- **Save Drafts**: Store generated emails locally for future reference.
- **Load Previous Drafts**: Retrieve and review saved drafts anytime.

## Installation
1. Ensure you have Python installed (>=3.7).
2. Install required dependencies:
   ```sh
   pip install streamlit openai python-dotenv
   ```
3. Set up your OpenAI API key in a `.env` file:
   ```sh
   OPENAI_API_KEY=your_api_key_here
   ```

## Running the Application
Start the application using:
```sh
streamlit run app.py
```
This will launch a local Streamlit web interface where you can generate emails.

## How to Use
1. **Enter Email Content**:
   - Paste the sender's email.
   - Write your draft or key points.
   - (Optional) Enter additional keywords.
2. **Select a Tone**: Choose from Helpful, Professional, Friendly, or match the sender's tone.
3. **Generate Email**: Click the "Generate Email" button to get AI-powered suggestions.
4. **Save Draft**: Save the generated email for later use.
5. **Load Previous Drafts**: Retrieve saved drafts anytime.

## Error Handling
- If required fields are missing, the app will show a warning.
- If no drafts are found when trying to load, an error message will be displayed.

## Notes
- Ensure that your OpenAI API key is active and has sufficient credits.
- Drafts are saved in `drafts.json` within the application directory.

## License
This project is intended for internal use. Modify and extend it as needed.

