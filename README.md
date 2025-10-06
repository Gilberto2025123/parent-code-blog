###Parent Code Blog App
# 🧭 Design & Planning

<details>
<summary><h2>User Stories</h2></summary>

Write your user stories in this section.

</details>

---

<details>
<summary><h2>Wireframes</h2></summary>

Attach wireframes in this section.

</details>

---

<details>
<summary><h2>Agile Methodology</h2></summary>

Explain your agile approach to your project and insert screenshots of your Kanban board (iterations, user stories, tasks, acceptance criteria, labels, story points...).

</details>

---

<details>
<summary><h2>Typography</h2></summary>

Explain the font(s) you've used for your project.

</details>

---

<details>
<summary><h2>Colour Scheme</h2></summary>

Include a screenshot of the colour scheme for your project.

</details>

---

<details>
<summary><h2>Database Diagram</h2></summary>

Include an image of your database diagram.  
List your models and describe how they are connected.

</details>

---

# 🌟 Features

Explain your website’s features such as navigation, pages, links, forms, input fields, and CRUD operations.

<details>
<summary><h3>Navigation</h3></summary>

Describe your navigation bar and links.

</details>

<details>
<summary><h3>Footer</h3></summary>

Describe your footer contents and functionality.

</details>

<details>
<summary><h3>Home Page</h3></summary>

Explain the purpose and layout of your home page.

</details>

<details>
<summary><h3>Additional Pages</h3></summary>

Describe any other pages in your project.

</details>

<details>
<summary><h3>CRUD</h3></summary>

Explain how Create, Read, Update, and Delete functionalities work in your project.

</details>

<details>
<summary><h3>Authentication & Authorisation</h3></summary>

Explain how user authentication and permissions are handled.

</details>

---

# 🧰 Technologies Used

List all technologies, frameworks, and tools used in your project.

---

## 📚 Libraries

List all external libraries or packages used.

---

# 🧪 Testing

This is an **important part** of your README!

<details>
<summary><h3>Google Lighthouse Performance</h3></summary>

Include screenshots of performance scores (mobile and desktop).

</details>

<details>
<summary><h3>Browser Compatibility</h3></summary>

Test and list which browsers your website works with.

</details>

<details>
<summary><h3>Responsiveness</h3></summary>

Add screenshots showing responsiveness on various devices.

</details>

<details>
<summary><h3>Code Validation</h3></summary>

Validate your HTML, CSS, JS, and Python code (all files!).  
Include validation screenshots.

</details>

---

## 🧩 Manual Testing – User Stories

| User Story | Test | Pass | Screenshot |
|-------------|------|------|-------------|
| *Paste your user story here* | Describe what is visible to the user and what action they should perform | ✅ | *Attach screenshot* |

---

## 🧩 Manual Testing – Features

| Feature | Action | Status | Screenshot |
|----------|---------|---------|-------------|
| *Feature description* | *User steps* | ✅ | *Attach screenshot* |

---

# 🐞 Bugs

List all bugs found and how they were fixed.  
If any remain unresolved, document them here.

---

# 🚀 Deployment

This website is deployed to **Heroku** from a **GitHub repository**.  
Follow these steps:

---

<details>
<summary><h3>1️⃣ Creating Repository on GitHub</h3></summary>

1. Sign into GitHub and go to the Code Institute’s template.  
2. Click **“Use this template”** → **“Create a new repository”**.  
3. Enter a name for the repository and click **Create repository from template**.  
4. Click the green **Gitpod** button to open a workspace and begin development.

</details>

---

<details>
<summary><h3>2️⃣ Creating an App on Heroku</h3></summary>

1. After creating the repository, sign into **Heroku**.  
2. Click **New → Create new app**.  
3. Enter a unique app name and select a region (e.g., Europe).  
4. Click **Create app**.

</details>

---

<details>
<summary><h3>3️⃣ Create a Database</h3></summary>

1. Log into **CI Database Maker**.  
2. Add your email address and submit the form.  
3. Open the database link sent to your email.  
4. Copy the database URL and paste it into:
   - `DATABASE_URL` variable in `env.py`
   - Heroku Config Vars.

</details>

---

<details>
<summary><h3>4️⃣ Deploying to Heroku</h3></summary>

1. Go to your app in Heroku → **Settings** tab.  
2. Scroll to **Config Vars** and set:
   - `DATABASE_URL` → your ElephantSQL URL  
   - `SECRET_KEY` → a unique secret key  
   - `CLOUDINARY_URL` → your Cloudinary URL  
   - `PORT` → `8000`  
3. Go to the **Deploy** tab → select **GitHub** as your deployment method.  
4. Connect your GitHub account and repository.  
5. Scroll to **Manual Deploy** and click **Deploy Branch**.  
6. Once deployment finishes, click **View App** to open your live site.

> **Note:** When deploying manually, redeploy after each repository update.

</details>

---

# 🙌 Credits

List all resources used in your project:
- Text sources  
- Images  
- Code snippets  
- Tutorials or example projects  

---

