The directory contains various program files showing different prompt engineering techniques- zero_shot, one_shot, few_shot, chain_of_thought, react, role_prompt.

And lastly there is a file named Combined_techniques that consists all of the six prompt engineering techniques integrated in one file, user can select one of them and ask questions, the system will generate response based on the selected technique.


Requirements:
Python 3.11.9

Ollama installation, Run this command in cmd - pip install ollama

Streamlit installation, Run this command in cmd - pip install streamlit


For running the programs:-
Firstly pull the ollama model, run: ollama pull llama3.2
Replace llama3.2 with the model you have installed
Then select the program

python -m streamlit run [file_name.py]
This will open up a window in the browser and the program should run through streamlit framework UI.

Replace file_name placeholder with actual name of the file

