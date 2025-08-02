#@title 🎨 UltraEpicAi Realism Fooocus { display-mode: "form" }
#@markdown ---
#@markdown 💡 *Connect to GPU (T4/A100/V100) before running.*
#@markdown #### Customize Your Settings:

theme = "dark"  #@param ["dark", "light"]
main_model = "UltraEpicAi_Realism"  #@param ["UltraEpicAi_Realism"]
use_indian_clothing = True  #@param {type:"boolean"}
use_perfect_eyes = False  #@param {type:"boolean"}
use_hourglass = False  #@param {type:"boolean"}
use_detailers = False  #@param {type:"boolean"}
civitai_token = ""  #@param {type:"string"}
extra_args = "--share --always-high-vram"  #@param {type:"string"}

# ======================
# ⚙️ Hidden Setup Logic
# ======================
print("🔧 Setting up Fooocus...")

args = f"{extra_args} --theme {theme}"

# Install and clone
!pip install -q "pip<24"
!pip install -q pygit2==1.15.1
%cd /content
!git clone https://github.com/lllyasviel/Fooocus.git
%cd Fooocus
!mkdir -p models/checkpoints models/loras

# Download main model
if main_model == "UltraEpicAi_Realism":
  !wget -q -O models/checkpoints/UltraEpicAi_Realism.safetensors "https://civitai.com/api/download/models/1947685?type=Model&format=SafeTensor&token={civitai_token}"

# Optional LoRAs
if use_indian_clothing:
  !wget -q -O models/loras/Indian_Clothing.safetensors "https://civitai.com/api/download/models/2063056?type=Model&format=SafeTensor&token={civitai_token}"
if use_perfect_eyes:
  !wget -q -O models/loras/Perfect_Eyes.safetensors "https://civitai.com/api/download/models/129711?type=Model&format=SafeTensor&token={civitai_token}"
if use_hourglass:
  !wget -q -O models/loras/Hourglass_Body_Shape.safetensors "https://civitai.com/api/download/models/911708?type=Model&format=SafeTensor&token={civitai_token}"
if use_detailers:
  !wget -q -O models/loras/Detailers_By_Stable_Yogi.safetensors "https://civitai.com/api/download/models/1071060?type=Model&format=SafeTensor&token={civitai_token}"

print("🚀 Launching Fooocus...")
!python entry_with_update.py {args}
