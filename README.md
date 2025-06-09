# Hugging-face-learning

Hugging Face is an open-source AI library for using pre-trained models in:<br/>

NLP (text classification, summarization, translation, etc.)<br/>
Vision (image classification, object detection)<br/>
Audio, and more.<br/>


Provides pretrained models, datasets, tools -> build, fine-tune, deploy "state-of-the-art" model.<br/>


Virtual environment : python -m venv venv_name<br/>
activate : ./venv_name/scripts/activate<br/>

Pipeline : way of running various models<br/>
model = pipeline("enter task", "enter model name")<br/>

cuda : for using nvidia gpu (cuda toolkit)  [ check installed or not using "nvcc --version" ]<br/>

for using model from HF : Libraries -> "Transformers" and then "Tasks" will show different models to use<br/>

Langchain : allows to use multiple models together & make more advanced application<br/>

create venv -> activate it -> install requirements.txt {transformers, langchain, langchain-huggingface} -> hugging face login with token -> Install CUDA -> activate GPU -> create main.py -> code in main.py ->
install cuda -> install pytorch for GPU 
