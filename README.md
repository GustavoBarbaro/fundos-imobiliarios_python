# Fundos Imobiliários - Python 📊🏢

---

Este projeto foi desenvolvido com o objetivo de analisar e acompanhar Fundos Imobiliários (FIIs) listados na B3. A aplicação permite buscar dados de múltiplos FIIs, calcular indicadores relevantes e gerar relatórios em formato CSV com as informações organizadas para análise.



---


# Tecnologias Utilizadas 💻

* Python
* Selenium
* Streamlit
* Pandas
* Numpy

---

# Funcionalidades ⚙️

* Busca automatizada de informações sobre FIIs.
* Geração de relatório em CSV contendo indicadores como:
    * Preço atual
    * Dividend Yield (DY)
    * Valor Patrimonial por Cota (VPC)
    * P/VP
    * Setor
    * Liquidez
    
* Código modular e fácil de expandir para novas análises.


---

# Como Usar 🚀

## 1. Clone o repositório

```bash
git clone https://github.com/GustavoBarbaro/fundos-imobiliarios_python.git
cd fundos-imobiliarios_python
```

## 2. Instale as dependências

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## 3. Execute o script principal

```bash
cd fundos/
streamlit run app.py
```

# Exemplo de Saída 📄

| Código | Preço Atual | DY (%) | P/VP | Setor |
|:---:|:---:|:---:|:---:|:---:|
| HGLG11 | 150.25 | 0.85 | 1.05 | Logística |
| KNRI11 | 170.10 | 0.75 | 0.95 | Escritórios |
| VISC11 | 120.00 | 0.90 | 1.10 | Shoppings |

---

# Objetivo 📌

Este projeto tem fins educacionais e visa auxiliar investidores e entusiastas do mercado financeiro a analisarem rapidamente dados relevantes de Fundos Imobiliários utilizando Python.
