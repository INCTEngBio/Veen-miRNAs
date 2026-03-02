import pandas as pd
from venn import venn
import matplotlib.pyplot as plt

# 1. Carregar os dados
df = pd.read_csv('familias_mirna.txt', sep='\t', dtype=str, engine='python')

# 2. Criar o dicionário de conjuntos
data_dict = {}
for col in df.columns:
    clean_values = df[col].dropna().str.strip().unique()
    if len(clean_values) > 0:
        data_dict[col] = set(clean_values)

# 3. Preparar a figura
plt.figure(figsize=(12, 12))
ax = venn(data_dict, fmt="{size}")

# 4. Ajustar os textos (remover zeros, aumentar números e nomes)
for text in ax.texts:
    valor = text.get_text()
    if valor == '0':
        text.set_text('')
    elif valor.isdigit():
        text.set_fontsize(14)
        text.set_fontweight('bold')
    else:
        text.set_fontsize(16)

# 5. O TRUQUE DA LEGENDA CORRIGIDO:
# Pega a legenda que a biblioteca 'venn' gerou sozinha
legenda_original = ax.get_legend()

if legenda_original:
    # Extrai as cores (handles) e os nomes (labels) dessa legenda
    try:
        handles = legenda_original.legend_handles # Matplotlib mais novo
    except AttributeError:
        handles = legenda_original.legendHandles  # Matplotlib mais antigo
        
    labels = [t.get_text() for t in legenda_original.get_texts()]
    
    # Recria a legenda exatamente igual, mas na nossa posição e formatação
    ax.legend(handles, labels, bbox_to_anchor=(1.15, 0.5), loc='center left', fontsize=14, title="Biomas", title_fontsize=16)

plt.title('Diagrama de Venn - Famílias de miRNA por Bioma', fontsize=18, pad=20)

# 6. Salvar a imagem final
# O bbox_inches='tight' garante que a imagem salve a legenda extra
plt.savefig('venn_mirna_final.png', dpi=300, bbox_inches='tight')
print("Diagrama salvo como 'venn_mirna_final.png'!")
plt.show()