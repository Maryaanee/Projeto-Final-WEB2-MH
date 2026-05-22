# 🎬 Nome do Projeto
**MH Cine** - Lista de filmes

---

## 👥 Integrantes da Equipe
- Francisca Mariane Sousa da Silva ( sa.mariane08@aluno.ifce.edu.br )
- José Hadriel Miranda dos Santos ( jose.hadriel10@aluno.ifce.edu.br )

---

## 🛠️ Tecnologias Utilizadas
- **Python 3.x**
- **Django 4.x**
- **SQLite**
- **HTML5 / CSS3**

---

# 🚀 Como Executar o Projeto

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/seu-usuario/mh-cine.git
    ```

2.  **Crie um ambiente virtual:**
    ```bash
    python -m venv venv
    ```

3.  **Ative o ambiente virtual:**
    * **Windows:** `.\venv\Scripts\activate`
    * **Linux/Mac:** `source venv/bin/activate`

4.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Execute as migrações:**
    ```bash
    python manage.py migrate
    ```

6.  **Crie um superusuário:**
    ```bash
    python manage.py createsuperuser
    ```

7.  **Rode o servidor:**
    ```bash
    python manage.py runserver
    ```

---
  
## 📌 Descrição do Problema
Atualmente, muitas pessoas têm dificuldade em escolher filmes para assistir devido à grande quantidade de opções disponíveis nas plataformas de streaming. Além disso, nem todas as aplicações oferecem avaliações confiáveis, organizadas e fáceis de interpretar, o que pode gerar indecisão e perda de tempo.

---

## 💡 Solução Proposta
O projeto consiste no desenvolvimento de um aplicativo de avaliação e recomendação de filmes, inspirado em plataformas como o Rotten Tomatoes. A aplicação permitirá que usuários consultem notas, críticas e classificações de filmes de forma simples e intuitiva.

### Funcionalidades principais:
- Listagem de filmes populares  
- Sistema de avaliação (notas dos usuários)  
- Filtros por gênero, ano e avaliação  
 
---

# ✅ Funcionalidades Implementadas

- [x] **Model criado com 4 campos:** ( Título, Sinopse, Data de lançamento, duração).
- [x] **CRUD via shell:** Manipulação de dados via terminal.
- [x] **Admin configurado:** Interface para gerenciamento de filmes.
- [x] **MVP e wireframes definidos.**
- [x] Sistema de cadastro de usuários com foto de perfil funcionando
- [x] Validação de e-mail via token (link aparece no console)
- [x] Login/Logout funcionando
- [x] Todas as páginas do trabalho final protegidas com @login_required
- [x] Página home/dashboard mostrando informações do
- [x] usuário logado
- [x] O trabalho final continua funcionando, agora com autenticação
- [] **Filtros no admin:** Filtragem por gênero, ano e avaliação.
- [] **Listagem de filmes populares:** Exibição principal da aplicação.


---

## 🎯 Público-Alvo
O aplicativo é voltado para:
- Pessoas que gostam de assistir filmes e séries  
- Usuários de plataformas de streaming (Netflix, Prime Video, etc.)  
- Jovens e adultos que buscam recomendações rápidas e confiáveis  
- Pessoas que desejam compartilhar suas opiniões  

---

