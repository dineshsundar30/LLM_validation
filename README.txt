pip install -U deepeval
uv pip install -U deepeval or uv add deepeval (recomended) ---> with UV


deepeval test run test_file.py  --> to run the TC


curl -fsSL https://ollama.com/install.sh | sh  --> to install the ollma


sudo systemctl stop ollama
systemctl status ollama

sudo systemctl start ollama
systemctl status ollama

sudo systemctl restart ollama

sudo systemctl disable ollama  Prevent it from starting automatically at boot:




ollama list                 --> to list the models
ollama run llama3.2         --> to install model
ollama show llama3.2:1b     --> to see the metadata of the model


ollama serve                --> to expose to local


