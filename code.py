!pip install pygit2==1.15.1
%cd /content
!git clone https://github.com/lllyasviel/Fooocus.git
%cd /content/Fooocus

!wget -O /content/Fooocus/models/checkpoints/UltraEpicAi_Realism.safetensors "https://civitai-delivery-worker-prod.5ac0637cfd0766c97916cefa3764fbdf.r2.cloudflarestorage.com/model/237671/hamburgerhelperexplu.yCjU.safetensors?X-Amz-Expires=86400&response-content-disposition=attachment%3B%20filename%3D%22ultraepicaiRealism_v10.safetensors%22&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=e01358d793ad6966166af8b3064953ad/20250731/us-east-1/s3/aws4_request&X-Amz-Date=20250731T041637Z&X-Amz-SignedHeaders=host&X-Amz-Signature=c740ae23d8bbdafc5baf8147af988b264d52dbafbfbd29899188e54b476873a4"

!wget -O /content/Fooocus/models/loras/Indian_Clothing.safetensors "https://civitai.com/api/download/models/2063056?type=Model&format=SafeTensor&token=[API Token]"

!python entry_with_update.py --share --always-high-vram
