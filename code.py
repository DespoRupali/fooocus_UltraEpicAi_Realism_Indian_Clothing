!pip install pygit2==1.15.1
%cd /content
!git clone https://github.com/lllyasviel/Fooocus.git
%cd /content/Fooocus

!wget -O /content/Fooocus/models/checkpoints/UltraEpicAi_Realism.safetensors "https://civitai.com/api/download/models/1947685?type=Model&format=SafeTensor&size=full&fp=fp16&token=[API Token]"

!wget -O /content/Fooocus/models/loras/Indian_Clothing.safetensors "https://civitai.com/api/download/models/2063056?type=Model&format=SafeTensor&token=[API Token]"

!python entry_with_update.py --share --always-high-vram
