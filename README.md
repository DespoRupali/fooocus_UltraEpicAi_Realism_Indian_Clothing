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
!wget -O /content/Fooocus/models/checkpoints/UltraEpicAi_Realism.safetensors "https://civitai.com/api/download/models/1947685?type=Model&format=SafeTensor&size=full&fp=fp16&token=[API Token]"
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
