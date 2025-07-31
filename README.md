# fooocus UltraEpicAi Realism Indian Clothing
---

# Fooocus Setup on Google Colab

This guide sets up the **Fooocus** AI image generation tool with a custom model and LoRA for enhanced realism and Indian clothing styles.

## 🔧 Installation Steps

### Step 1: Install Required Packages

```bash
!pip install pygit2==1.15.1
```

### Step 2: Clone Fooocus Repository

```bash
%cd /content
!git clone https://github.com/lllyasviel/Fooocus.git
%cd /content/Fooocus
```

### Step 3: Download the Checkpoint Model

```bash
!wget -O /content/Fooocus/models/checkpoints/UltraEpicAi_Realism.safetensors "https://civitai-delivery-worker-prod.5ac0637cfd0766c97916cefa3764fbdf.r2.cloudflarestorage.com/model/237671/hamburgerhelperexplu.yCjU.safetensors?X-Amz-Expires=86400&response-content-disposition=attachment%3B%20filename%3D%22ultraepicaiRealism_v10.safetensors%22&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=e01358d793ad6966166af8b3064953ad/20250731/us-east-1/s3/aws4_request&X-Amz-Date=20250731T041637Z&X-Amz-SignedHeaders=host&X-Amz-Signature=c740ae23d8bbdafc5baf8147af988b264d52dbafbfbd29899188e54b476873a4"
```

### Step 4: Download LoRA for Indian Clothing

> ⚠️ Replace `[API Token]` with your actual CivitAI token.

```bash
!wget -O /content/Fooocus/models/loras/Indian_Clothing.safetensors "https://civitai.com/api/download/models/2063056?type=Model&format=SafeTensor&token=[API Token]"
```

### Step 5: Run Fooocus

```bash
!python entry_with_update.py --share --always-high-vram
```

## 🧠 Notes

* **Checkpoint models** go in `/content/Fooocus/models/checkpoints/`.
* **LoRA files** go in `/content/Fooocus/models/loras/`.
* The `--share` flag will create a public link to access Fooocus UI.
* `--always-high-vram` ensures better quality for systems with more VRAM.

---
