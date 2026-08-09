The directory contains various program files showing different prompt engineering techniques.

There is a folder named terminal_version which contains python file that directly runs on the terminal.

Then there is a folder named streamlit_version which contains python files thet uses the streamlit framework for the UI, and runs the program on localhost in browser.

And lastly there is a file named Combined_techniques that consists all of the six prompt engineering techniques integrated in one file, user can select one of them and ask questions, the system will generate response based on the selected technique.


Requirements:
Python 3.11.9
Ollama installation, Run this command in cmd - pip install ollama
Streamlit installation, Run this command in cmd - pip install streamlit


For running the programs:-
Firstly pull the ollama model, run: ollama pull llama3.2
Replace llama3.2 with the model you have installed
Then select the program

For terminal_version programs, simply run the python file:
python [file_name.py]
This will run the program in terminal directly

For streamlit_version programs, run this command:
python -m streamlit run [file_name.py]
This will open up a window in the browser and the program should run through streamlit framework UI.

Replace file_name placeholder with actual name of the file

