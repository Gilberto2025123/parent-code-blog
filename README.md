### Parent Code Blog App

This site was submitted as part of Code Institute's final project, utilising Django, Python, JavaScript, HTML, and CSS. This web application is a blog that is dedicated to helping those on the parenthood journey navigate the challenges and joys of being a parent in the tech sector. 



##### Deployed Live link: 
https://parent-code-app-e92a092d91bc.herokuapp.com/


---

<img width="1506" height="857" alt="Parent Code Amiresponsive fireship image" src="https://github.com/user-attachments/assets/04d511cb-e23a-46e2-a5e9-b2c9acec8832" />

---
## Contents

- [Design and Planning](#design-and-planning)
  - [User Stories](#user-stories)
  - [Agile Methodology](#agile-methodology)
  - [Wireframes](#wireframes)
  - [Typography](#typography)
  - [Colour Scheme](#colour-scheme)
  - [Database Diagram ERD](#database-diagram-erd)

- [Features](#features)
  - [Navigation](#navigation)
  - [Footer](#footer)
  - [Landing Page](#landing-page)
  - [Additional Pages](#additional-pages)
    - [About Us](#about-us)
    - [Contact Us](#contact-us)
    - [Sign Up](#sign-up)
    - [Blog Page](#blog-page)
  - [CRUD](#crud)
    - [Authentication and Authorisation](#authentication-and-authorisation)

- [Technologies Used](#technologies-used)
  - [Development and Programming](#development-and-programming)
  - [Tools and Workflow](#tools-and-workflow)
  - [Database and Hosting](#database-and-hosting)
  - [Design and UI/UX](#design-and-uiux)
  - [AI and Learning Resources](#ai-and-learning-resources)
  - [Validation and Standards](#validation-and-standards)

- [Testing](#testing)
  - [Google Lighthouse Performance](#google-lighthouse-performance)
    - [Mobile](#mobile)
    - [Desktop](#desktop)
  - [Manual Testing – User Stories](#manual-testing--user-stories)
  - [Manual Testing – Features](#manual-testing--features)
  - [Browser Compatibility](#browser-compatibility)
    - [Cross-browser testing](#cross-browser-testing)
      - [Chrome](#chrome)
      - [Firefox](#firefox)
      - [Edge](#edge)
      - [Safari](#safari)
  - [Code Validation](#code-validation)

- [Bugs](#bugs)

- [Deployment](#deployment)
  - [Creating a Repository on GitHub](#creating-a-repository-on-github)
  - [Creating an App on Heroku](#creating-an-app-on-heroku)
  - [Create a Database](#create-a-database)
  - [Deploying to Heroku](#deploying-to-heroku)

- [Credits](#credits)


---

## Design and Planning

### User Stories
The user stories were created with busy parents in mind, providing a quick and efficient way to connect with others in the tech sector. Use the issue number links in the table to view the acceptance criteria.

| Priority | Issue | User Story |
| --- | --- | --- |
| Must | [#1](https://github.com/Gilberto2025123/parent-code-blog/issues/1) | As a parent working in tech, I can create a comment on a blog post so that I can share advice or experiences with  |
| Must | [#2](https://github.com/Gilberto2025123/parent-code-blog/issues/2) | As a site user, I can view a paginated list of posts so that I can select which post I want to view. |
| Must | [#3](https://github.com/Gilberto2025123/parent-code-blog/issues/3)| As a site user, I can view a detailed blog post so that I can read advice and insights from other parents.  |
| Must | [#4](https://github.com/Gilberto2025123/parent-code-blog/issues/4)  | As a blog author, I can edit my post so that I can update or correct information.  |
| Must | [#5](https://github.com/Gilberto2025123/parent-code-blog/issues/5) | As a blog author, I can delete my blog post so that I can remove content I no longer want visible. |
| Must | [#6](https://github.com/Gilberto2025123/parent-code-blog/issues/6)  | As a blog author, I can upload images with my posts so that my content is more engaging. |
| Must | [#7](https://github.com/Gilberto2025123/parent-code-blog/issues/7) | As a site user, I can comment on blog posts so that I can contribute to the discussion.  |
| Must | [#8](https://github.com/Gilberto2025123/parent-code-blog/issues/8) | As a site user, I can like blog posts so that I can show appreciation for helpful content. |
| Must | [#9](https://github.com/Gilberto2025123/parent-code-blog/issues/9)  | As a site user, I see success notifications after completing actions so that I know my action worked.  |
| Could | [#10](https://github.com/Gilberto2025123/parent-code-blog/issues/10) | As a site user, I can bookmark posts so that I can read them later. :contentReference[oaicite:19]{index=19} |
| Could | [#11](https://github.com/Gilberto2025123/parent-code-blog/issues/11) | As a site user, I can share posts to social media so that I can spread valuable advice.  |
| Should | [#12](https://github.com/Gilberto2025123/parent-code-blog/issues/12) | As a new site user, I can register and log in so that I can create posts and interact with others. |
| Should | [#13](https://github.com/Gilberto2025123/parent-code-blog/issues/13)  | As a parent in tech, I can have a profile page so that I can share my background with the community.  |
| Should | [#14](https://github.com/Gilberto2025123/parent-code-blog/issues/14) | As a site user, I can search blog posts so that I can quickly find relevant advice. |
| Should | [#15](https://github.com/Gilberto2025123/parent-code-blog/issues/15) | As a site user, I can filter posts by categories (e.g., job hunting, parenting tips, remote work) so that I can browse specific topics. |
| Should | [#16](https://github.com/Gilberto2025123/parent-code-blog/issues/16) | As a site user, I can sort posts so that I can view the newest or most liked content first. |
| Could | [#17](https://github.com/Gilberto2025123/parent-code-blog/issues/17) | As a parent in tech, I can browse job opportunities so that I can balance family life with career growth. |
| Won’t | [#18](https://github.com/Gilberto2025123/parent-code-blog/issues/18)  | As a site user, I would like to send private messages to other parents so that I can connect more personally. |
| Must | [#19](https://github.com/Gilberto2025123/parent-code-blog/issues/19) | As a site user, I can use the app across devices and browsers so that I can access content easily. |
| Won’t | [#20](https://github.com/Gilberto2025123/parent-code-blog/issues/20) | As a site user, I would like AI suggestions for parenting and tech advice so that I get instant guidance.  |
| Must | [#21](https://github.com/Gilberto2025123/parent-code-blog/issues/21) | As a user, I must be notified when I have not accessed the correct webpage so that I can find the correct deployed link.|
| Must | [#22](https://github.com/Gilberto2025123/parent-code-blog/issues/22) | As a Site Admin, I can approve or disapprove comments so that I can filter out objectionable comments  |
| Must | [#23](https://github.com/Gilberto2025123/parent-code-blog/issues/23) | As a user, I want to access an "About Us" page to discover more information about the website. |


---
### Agile Methodology

The project utilised an Agile methodology approach, as shown below with the Kanban board. I also used MoSCoW prioritisation to ensure that User stories were tracked accordingly. During the development of the application, it served as a guide to ensure that I was keeping with the project brief and ensure effective time management, and meeting the respective acceptance criteria for each time. As an initial sprint, I am happy with how the web app functions and looks, but as seen from the unfinished tasks in the backlog, there were more ideas I did not manage to complete and so are left for future development. In this case, there is placeholder code which will help with the next iteration and sprint. 

I also highly recommend using the Magic Goblin Tool To Do list generator: https://goblin.tools/ToDo - I used this to help me manage my time in the early stages of planning and development. 

**Project Board can be found here:** https://github.com/users/Gilberto2025123/projects/7

  <img width="1492" height="799" alt="Screenshot 2025-10-13 at 06 20 49" src="https://github.com/user-attachments/assets/38e53713-e1ae-49d6-a604-3600d9503abb" />
  <img width="1491" height="805" alt="Screenshot 2025-10-06 at 22 09 19" src="https://github.com/user-attachments/assets/72a58fa4-c4b7-4f35-bc5f-63c3ee19041e" />
  <img width="1495" height="814" alt="Screenshot 2025-10-13 at 12 31 42" src="https://github.com/user-attachments/assets/a52e3385-d37e-446a-821d-b92748cf67ae" />


---

### Wireframes
I used Balsamiq to create the wireframe designs. A landing page was added later (not shown here) to provide a clear call to action for new users and site visitors.

<img width="967" height="813" alt="Desktop" src="https://github.com/user-attachments/assets/1a30eab1-27c5-406e-89d0-4913598f06b1" />

<img width="616" height="916" alt="Tablet view" src="https://github.com/user-attachments/assets/38fd0f32-db98-4ae3-bd3f-f63ce7a8f607" />

<img width="436" height="867" alt="Mobile view" src="https://github.com/user-attachments/assets/370c63be-8db8-4c7f-8965-1a64758483d2" />


---

### Typography
These fonts were used to provide an attractive and playful interface but one that is also accessible to all. Fitting in with the project brief. I used Google Fonts to explore possible options that would fit with my vision of the design. 

Funnel Display - Used for headings and section intros

Comforta - Used for the main body of the text and can be viewed easily across devices.

  <img width="1483" height="678" alt="Screenshot 2025-10-13 at 13 45 27" src="https://github.com/user-attachments/assets/093f4029-4627-4503-aaac-7c44de838925" />


---
  ### Colour Scheme
  This colour palette was chosen to provide a bright and calming space to ensure accessibility for all. These colours are muted to provide space for creativity, which should help the user to spend as much time on the site without causing overstimulation. I used Coolors to develop the right palette: https://coolors.co/

  <img width="1600" height="1200" alt="Parent Code" src="https://github.com/user-attachments/assets/504d3434-741e-45a5-8fac-7fd6ec593e6d" />



---

 ### Database Diagram ERD
 Below is a screenshot of the entity relationship diagram data structure for the project. Not all models are present in the current version of the app, and are left in there for future development. 

  <img width="2283" height="1268" alt="Parent Code ERD" src="https://github.com/user-attachments/assets/0c7656ab-4dec-43b3-a2d1-5b9edc21f901" />


---

## Features
Across the application, there is JavaScript, Bootstrap and custom CSS styling to improve the interactivity of the site. These take the form of highlighted buttons, raised boxes, modals and hover effects. These are there to help the user navigate the site with ease.  

### Navigation
The Navigation bar has links to About Us, Contact Us, Sign Up and Login, as well as a link to the landing page when the logo is clicked. The Blog appears only to those who are logged in and authenticated to encourage sign-ups, but also for security. 
<img width="1512" height="72" alt="Screenshot 2026-01-30 at 02 48 38" src="https://github.com/user-attachments/assets/f0cf2700-e707-4380-b3be-8c2d89054385" />

<img width="1503" height="64" alt="Screenshot 2026-01-30 at 02 47 52" src="https://github.com/user-attachments/assets/84dfd4b4-7af3-4c0e-a481-2b9224660736" />

### Footer
The footer has links to external social media sites to allow for sharing content. They open in separate windows. 
<img width="1512" height="100" alt="Screenshot 2026-01-30 at 02 57 04" src="https://github.com/user-attachments/assets/1575a313-7bd3-4881-992c-72cecdfdcce8" />

 
### Landing Page
The landing page provides a call to action to new users and returning users. It has a clear description of the purpose of the website, and the Join Our Community button will change to Explore Posts once a user is authenticated and signed up. 
<img width="1512" height="982" alt="Landing Page ParentCode" src="https://github.com/user-attachments/assets/d9074f9b-3450-4460-8e40-ff25a6d9f06a" />


### Additional Pages
#### About Us
Here, I have included a page to explain the purpose of the application for all users and provided an image to bring a human element to the site. 
<img width="1512" height="982" alt="AboutUs ParentCode" src="https://github.com/user-attachments/assets/595de549-0ef3-4957-a7fa-220f36b88cd3" />

#### Contact Us 
Here is call to action for those seeking further correspondence with the Admins of the site by providing a form to contact them. This is using Bootstrap forms. 
<img width="1512" height="982" alt="ContactUs ParentCode" src="https://github.com/user-attachments/assets/e780894c-acfa-4350-84e2-7600a5272de9" />

#### Sign Up
Here is a call to action to those who are ready to engage with the community and request that the criteria be met when creating new user accounts. This is using Bootstrap forms.
<img width="1512" height="982" alt="Sign Up ParentCode" src="https://github.com/user-attachments/assets/11a8414a-3290-41b8-8329-388f0751a0bd" />


#### Blog Page
##### Main Blog page 
Upon successful user authentication, users will be able to access all blog posts as shown below. They will also see a success notification telling them they are logged in. 
<img width="1512" height="982" alt="Login Success Notification Blog Page" src="https://github.com/user-attachments/assets/27990d45-92cc-41fe-9862-e0abbecc7376" />

##### Individual Blog page 
Users will be able to browse through the posts as shown here. They will be able to see the category, the number of comments made, whether they have made a comment(depending on approval) and have the option to leave a new comment or go back to the main blog page via the button at the bottom of the post. 
<img width="1508" height="859" alt="Individual Blog Post 1" src="https://github.com/user-attachments/assets/d4c66ddf-7522-44d9-bad4-e9451d2b0001" />

<img width="1491" height="862" alt="Individual Blog Post 2" src="https://github.com/user-attachments/assets/89866a31-80cc-4692-976c-4f5afead7173" />

  
### CRUD 

  #### Create 
  Users can leave a comment by writing in the box provided and submitting it for approval. 
  <img width="1506" height="860" alt="CRUD - Create a comment and submit notification" src="https://github.com/user-attachments/assets/16096d86-3c03-445e-b6d0-acbc611c6d8a" />

  #### Read 
   Users will be able to read all comments made on the post by them as well as other users. They will only have the option of editing or deleing their own comments on each post.  As shown with the buttons provided. They will see an approval pending notification
  <img width="1502" height="851" alt="CRUD - Edit, Delete buttons, Approval Pending Notification" src="https://github.com/user-attachments/assets/465e324b-5b15-437f-9b81-4a43200b41a6" />

  #### Update
  Users will be able to update their comments on each post, as shown belo,w and will see a notification to say that their comment has been updated. 
  <img width="1504" height="588" alt="CRUD - Update:Edit Comment Form" src="https://github.com/user-attachments/assets/2c5b64e8-dbed-4dd3-a369-603b26bea535" />
<img width="1505" height="854" alt="CRUD - Comment Updated notification" src="https://github.com/user-attachments/assets/c408415d-fdd9-4341-9536-afab4d336148" />

  #### Delete
  Users will be able to delete their unwanted comments via the delete button, which will provide a modal, giving the user a chance to change their mind. Once they have deleted a comment, they will receive a comment deleted notification. 
<img width="1511" height="849" alt="CRUD - Delete Modal " src="https://github.com/user-attachments/assets/c87a2ade-fd75-4044-9000-58ac7db48aa4" />

<img width="1507" height="854" alt="CRUD - Comment Deleted notification" src="https://github.com/user-attachments/assets/7b0579c1-6b80-410d-8573-f1d7ef7cdddb" />

#### Authentication and Authorisation
Users using the back-end Django framework and Bootstrap design are now able to sign up confidently to the site. The Admin also has authentication and authorisation tools, as shown below. 

  -  Admin User authentication with secure registration and login
    <img width="1512" height="982" alt="Django Admin " src="https://github.com/user-attachments/assets/79441d28-7b18-4173-a529-1ed4123d6122" />

  - Admin functionality for managing user data, comments, and user accounts. 
<img width="1512" height="982" alt="Django Admin Interface" src="https://github.com/user-attachments/assets/50bfebfb-7bb4-4a25-a5d6-fdb8c26a5d01" />
<img width="1512" height="982" alt="Django Admin (Users)" src="https://github.com/user-attachments/assets/64eaf95a-c12b-47c9-b262-a49d2266a270" />

---

## Technologies Used

### Development and Programming
- **Python:** Core programming language used to implement back-end logic.
- **Django:** Web framework used to structure the application and support rapid development.
- **JavaScript:** Used to enhance interactivity and support front-end behaviour where required.
- **HTML and CSS:** Used to structure and style the front-end interface.

### Tools and Workflow
- **Visual Studio Code (VS Code):** Primary integrated development environment used during implementation.
- **Git and GitHub:** Used for version control and repository management.
- **GitHub Projects (Kanban board):** Used to plan, prioritise, and monitor development tasks.
- **Lucidchart:** Used to design and present the entity–relationship diagram (ERD).
- **Magic ToDo Goblin Tools:** Used to break down tasks into manageable steps and support workflow planning.

### Database and Hosting
- **PostgreSQL:** Adopted for production deployment to support a scalable relational database environment.
- **Heroku:** Platform used to deploy and host the live application.

### Design and UI/UX
- **Coolors:** Used to explore and refine colour palettes in support of a consistent visual design.
- **Google Fonts:** Used to select typography aligned with branding and readability requirements.
- **Font Awesome:** Used to incorporate consistent iconography across the user interface.
- **Bootstrap:** For responsive design and styling.
- **Balsamiq:** Used to produce wireframes and iterate on user interface concepts.
- **TinyPNG Converter:** Used to compress and optimise images to support performance and load times.
- **Pexels:** Used as a source of royalty-free imagery, where appropriate.

### AI and Learning Resources
- **VSCode Copilot:** Used to support development through code suggestions and debugging.
- **ChatGPT:** Used to support problem-solving, documentation drafting, and project planning, logo design
- **Perplexity:** Used for collecting post content with real-world references. 
- **CS50W Harvard Lectures:** Used to reinforce understanding of web application development concepts and best practices.
- **YouTube Tutorials:** Used to supplement learning and inform implementation approaches where appropriate.
- **W3Schools:** Used to troubleshoot and problem solve. 

### Validation and Standards
- **W3C Validator:** Used to validate HTML for semantic structure and accessibility considerations.
- **Jigsaw CSS Validator:** Used to verify CSS compliance and identify errors.
- **JSHint:** Used to validate JavaScript code quality and identify potential issues.
- **PEP 8 Validator:** Used to ensure Python code consistency, readability, and adherence to style conventions.
- **Google Lighthouse:** Used to audit performance, accessibility, SEO, and adherence to best practices on the deployed site.


---

## Testing

### Google Lighthouse Performance
The website passed its performance testing using Google Lighthouse to ensure accessibility for all. This shows that the application is fully responsive across all media devices. 

#### Mobile
<img width="986" height="817" alt="Screenshot 2026-01-30 at 01 15 30" src="https://github.com/user-attachments/assets/6f09b55e-be09-494b-a35a-83c1cc4179fe" />

#### Desktop
<img width="980" height="819" alt="Screenshot 2026-01-30 at 01 17 19" src="https://github.com/user-attachments/assets/7eb707c5-5e43-46be-935d-b1acaab52a4c" />

---
## Manual Testing – User Stories

| User Story | Test | Pass |
|---|---|---|
| As a parent working in tech, I can create a comment on a blog post so that I can share advice or experiences. | Log in (required). Open a blog post. Enter text into the comment box and click **Submit**. Confirm the new comment appears on the post (immediately or after refresh) and is linked to your user/account if applicable. | Yes |
| As a site user, I can view a paginated list of posts so that I can select which post I want to view. | Go to the blog listing page. Confirm a limited number of posts show per page. Click **Next/Previous** buttons. Confirm the list updates and you can navigate back and forth correctly. | Yes |
| As a site user, I can view a detailed blog post so that I can read advice and insights from other parents. | From the blog list, click a post title. Confirm you land on a post detail page showing title, author, date, content, and any images/comments. | Yes |
| As a blog author, I can edit my post so that I can update or correct information. | Create or open one of your posts. Click **Edit**. Update the body and click **Update Comment**. Confirm the post displays the updated content. | Yes |
| As a blog author, I can delete my blog post so that I can remove content I no longer want visible. | Open one of your posts. Click **Delete** (and confirm if prompted). Confirm you are redirected appropriately and the post no longer appears in the posts list or via direct URL. | Yes |
| As a blog author, I can upload images with my posts so that my content is more engaging. | Create/edit a post. Use the image upload control to select an image file and save the post. Confirm the image displays on the post detail page and loads correctly. | No - feature not yet developed |
| As a site user, I can comment on blog posts so that I can contribute to the discussion. | Open a blog post. Add a comment and submit. Confirm the comment is displayed (or queued for approval if moderation is enabled). | Yes |
| As a site user, I can like blog posts so that I can show appreciation for helpful content. | Open a blog post. Click the **Like** button/icon. Confirm the like count increases (or icon changes state). Refresh the page and confirm the like persists. | No - feature not yet developed |
| As a site user, I see success notifications after completing actions so that I know my action worked. | Perform an action (e.g., create post, delete comment, login, update comment). Confirm a success message/toast/banner appears with appropriate wording and disappears/behaves correctly. | Yes |
| As a site user, I can bookmark posts so that I can read them later. | Open a blog post. Click **Bookmark/Save**. Go to bookmarks/saved items area (or profile section). Confirm the post appears there. Remove the bookmark and confirm it disappears. | No - feature not yet developed |
| As a site user, I can share posts to social media so that I can spread valuable advice. | Open a blog post. Click a social share button/link. Confirm it opens the correct platform share flow (or copies a shareable link) and that the URL/title preview is correct. | No - feature not yet developed |
| As a new site user, I can register and log in so that I can create posts and interact with others. | Go to **Sign up**. Create an account with valid details. Log out, then log in with the new credentials. Confirm you can access logged-in features (e.g., Create comments). | Yes |
| As a parent in tech, I can have a profile page so that I can share my background with the community. | Log in and navigate to **Profile**. Confirm profile fields display (bio/role/etc.). Update profile details and save. Confirm the updated details show on your profile page. | No - feature not yet developed |
| As a site user, I can search blog posts so that I can quickly find relevant advice. | Use the search bar on the posts page. Search for a keyword that exists. Confirm relevant results appear. Search for a random term and confirm that “no results” behaviour is user-friendly. | No - feature not yet developed |
| As a site user, I can filter posts by categories (e.g., job hunting, parenting tips, remote work) so that I can browse specific topics. | From the posts listing, apply a category filter. Confirm only posts in that category appear. Clear the filter and confirm all posts return. | No - feature not yet developed |
| As a site user, I can sort posts so that I can view the newest or most liked content first. | On the posts listing page, apply sort options (e.g., **Newest**, **Most liked**). Confirm ordering changes correctly and stays consistent after refresh/navigation. | No - feature not yet developed |
| As a parent in tech, I can browse job opportunities so that I can balance family life with career growth. | Navigate to the jobs/opportunities section. Confirm a list of jobs is visible with key details. Open a job to view more information. Confirm links and navigation work correctly. | No - feature not yet developed|
| As a site user, I would like to send private messages to other parents so that I can connect more personally. | Navigate to user profiles (if available). Confirm there is **no** private messaging feature available (no message button/inbox). | No - feature not yet developed |
| As a site user, I can use the app across devices and browsers so that I can access content easily. | Test core pages (home, posts list, post detail, login/register) on multiple browsers (e.g., Chrome/Firefox/Edge/Safari) and at different screen sizes (mobile/tablet/desktop). Confirm layout is responsive and key actions work without visual or functional issues. | Yes |
| As a site user, I would like AI suggestions for parenting and tech advice so that I get instant guidance. | Confirm there is **no** AI suggestions feature present in the UI (no AI button/panel/auto-suggestions area). | No - feature not yet developed|
| As a user, I must be notified when I have not accessed the correct webpage so that I can find the correct deployed link. | Enter an invalid URL route (e.g., `/randompage`). Confirm a clear error page/message appears (404 or custom), guiding users to the correct page/link (e.g., home button). | Yes |
| As a Site Admin, I can approve or disapprove comments so that I can filter out objectionable comments. | Log in as admin. Go to the admin panel. Locate a pending comment and approve it. Confirm it appears publicly. Disapprove/delete another comment and confirm it does not appear publicly. | Yes |
| As a user, I want to access an "About Us" page to discover more information about the website. | From the navigation/menu/footer, click **About Us**. Confirm the page loads and displays relevant site information. Test direct URL access to the About page as well. | Yes |


---

## Manual Testing – Features

### Navigation
| Test Case | Expected Result | Outcome |
|---|---|---|
| Click Logo/Landing Page | Redirects to the landing page | Pass |
| Click About Us Page | Redirects to the About Us page | Pass |
| Click Contact Us Page | Redirects to the Contact Us page | Pass |
| Click Blog Page | Redirects to the Blog page | Pass |
| Click Explore Posts | Loads the posts listing/explore view | Pass |
| Click Next and Previous Navigation buttons | Navigates between pages of posts where applicable | Pass |
| Click Back to Blog button | Returns to the Blog page/posts listing | Pass |
| Open new page from social media links | Opens the relevant social link in a new tab/window | Pass |

### Authentication (Login / Logout / Register)
| Test Case | Expected Result | Outcome |
|---|---|---|
| Click Login/Logout | User can log in and log out successfully | Pass |
| Click Sign Up/Register for new account | Registration completes successfully and account is created | Pass |
| Access admin interface | Admin users can access the admin interface successfully | Pass |

### Blog Interaction (Posts, Comments, Responsiveness)
| Test Case | Expected Result | Outcome |
|---|---|---|
| Click Individual Blog Post/Read | Opens the selected post and displays full content | Pass |
| Create, Update/Edit and Delete Personal Comment | User can create, edit, and delete their own comment successfully | Pass |
| Responsiveness | Layout and functionality remain usable across screen sizes | Pass |



---

### Browser Compatibility

#### Cross-browser testing
I used a website called Browserling: https://www.browserling.com/ (It gives you 3 minutes at a time to test the features of your website on different web browsers. This is especially useful if you do not have a Windows system. 

##### Chrome
| Test | Expected Result | Actual Result |
|---|---|---|
| Click Logo/Landing Page | Success | Success |
| Click About Us Page | Success | Success |
| Click Contact Us Page | Success | Success |
| Click Blog Page | Success | Success |
| Click Login/Logout | Success | Success |
| Click Sign Up/Register for new account | Success | Success |
| Click Explore Posts | Success | Success |
| Click Individual Blog Post/Read | Success | Success |
| Click Back to Blog button | Success | Success |
| Create, Update/Edit and Delete Personal Comment | Success | Success |
| Click Next and Previous Navigation buttons | Success | Success |
| Access admin interface | Success | Success |
| Responsiveness | Success | Success |
| Open new page from social media links | Success | Success |

##### Firefox
| Test | Expected Result | Actual Result |
|---|---|---|
| Click Logo/Landing Page | Success | Success |
| Click About Us Page | Success | Success |
| Click Contact Us Page | Success | Success |
| Click Blog Page | Success | Success |
| Click Login/Logout | Success | Success |
| Click Sign Up/Register for new account | Success | Success |
| Click Explore Posts | Success | Success |
| Click Individual Blog Post/Read | Success | Success |
| Click Back to Blog button | Success | Success |
| Create, Update/Edit and Delete Personal Comment | Success | Success |
| Click Next and Previous Navigation buttons | Success | Success |
| Access admin interface | Success | Success |
| Responsiveness | Success | Success |
| Open new page from social media links | Success | Success |

##### Edge
| Test | Expected Result | Actual Result |
|---|---|---|
| Click Logo/Landing Page | Success | Success |
| Click About Us Page | Success | Success |
| Click Contact Us Page | Success | Success |
| Click Blog Page | Success | Success |
| Click Login/Logout | Success | Success |
| Click Sign Up/Register for new account | Success | Success |
| Click Explore Posts | Success | Success |
| Click Individual Blog Post/Read | Success | Success |
| Click Back to Blog button | Success | Success |
| Create, Update/Edit and Delete Personal Comment | Success | Success |
| Click Next and Previous Navigation buttons | Success | Success |
| Access admin interface | Success | Success |
| Responsiveness | Success | Success |
| Open new page from social media links | Success | Success |


##### Safari
| Test | Expected Result | Actual Result |
|---|---|---|
| Click Logo/Landing Page | Success | Success |
| Click About Us Page | Success | Success |
| Click Contact Us Page | Success | Success |
| Click Blog Page | Success | Success |
| Click Login/Logout | Success | Success |
| Click Sign Up/Register for new account | Success | Success |
| Click Explore Posts | Success | Success |
| Click Individual Blog Post/Read | Success | Success |
| Click Back to Blog button | Success | Success |
| Create, Update/Edit and Delete Personal Comment | Success | Success |
| Click Next and Previous Navigation buttons | Success | Success |
| Access admin interface | Success | Success |
| Responsiveness | Success | Success |
| Open new page from social media links | Success | Success |

### Code Validation
Code validation was carried out to ensure the integrity of the code and compliance with PEP8 guidelines, HTML, CSS and JavaScript standards. This enabled the code to be accessible for testing and deployment. 

#### HTML 
W3C Validator: https://validator.w3.org/detailed.html
<img width="1495" height="582" alt="HTML Validation ParentCode" src="https://github.com/user-attachments/assets/995f33ec-f3a3-4d24-83ec-befeaf99f84b" />

#### CSS 
Validated via W3C CSS Validator: https://jigsaw.w3.org/css-validator/
<img width="1482" height="859" alt="CSS Validation ParentCode" src="https://github.com/user-attachments/assets/d4028dec-6351-45bd-9285-ba6149b71834" />

#### JavaScript 
To test the JavaScript code, I used the JS Hint website. https://jshint.com/  I also used Google Chrome Developer Tools.  
<img width="1512" height="864" alt="JavaScript Test" src="https://github.com/user-attachments/assets/a099f912-6a62-4f1f-9ecb-0f316e99f01f" />

#### Python 
All Python code was tested, and results show no errors were found, utilising the CI Python Linter. Below are a few screenshots to show sections of the code with their results. 

<img width="1327" height="682" alt="Models py Test(Pass)" src="https://github.com/user-attachments/assets/4584743e-b3fa-4027-a80c-0b9aeec2d14f" />

<img width="1223" height="677" alt="Models py Test 2 " src="https://github.com/user-attachments/assets/96de84f9-7fd8-4b85-b2d6-eba2a93cb58c" />

<img width="1322" height="649" alt="Views py Test" src="https://github.com/user-attachments/assets/8df050dc-66d1-40b4-b8e9-572ad01eda47" />

 <img width="1227" height="716" alt="Urls py Test" src="https://github.com/user-attachments/assets/f469c2f2-03cc-4f36-9409-b0e6b2b1e514" />

 <img width="1130" height="395" alt="Urls py Test 2 " src="https://github.com/user-attachments/assets/84579a49-054f-432b-9b98-579651885f29" />

 <img width="1152" height="656" alt="Forms py Test" src="https://github.com/user-attachments/assets/fe56707d-8d29-422a-ac48-a596059fd790" />

<img width="1156" height="644" alt="Admin py Test" src="https://github.com/user-attachments/assets/268d02c9-a73d-4984-b11f-a1b880a8ede2" />



## Bugs

### 500 Server Error 

<img width="475" height="84" alt="Screenshot 2025-10-13 at 14 04 27" src="https://github.com/user-attachments/assets/560699a9-ede3-4588-81ea-44bdb22e07d8" />
This was the major issue with my initial submission of the project as it prevented much of the site to function. This was especially true when loading the page, attempting to sign up/ login to the admin site. 

To resolve this, I contacted my facilitator at the Code Institute, who helped provide feedback on how to test iteratively. I then utilised Chrome Developer Tools and AI to identify where the source of the problem was and discovered that it had been an issue in the base HTML file, and the site was trying to authenticate before the new user was saved and using request.POST.get('field') instead of the form’s cleaned data. I made changes to views/forms and the template to fix this.  It now runs as intended. 


---

## Deployment

This website is deployed to Heroku from a GitHub repository.  
Follow these steps:

### Creating a Repository on GitHub

1. Sign in to GitHub and go to the Code Institute’s template.
2. Click **Use this template** then **Create a new repository**.
3. Enter a name for the repository and click **Create repository from template**.
4. Click the green **Gitpod** button to open a workspace and begin development.

### Creating an App on Heroku 

  1. After creating the repository, sign in to Heroku.
  2. Click **New** then **Create new app**.
  3. Enter a unique app name and select a region (for example, Europe).
  4. Click **Create app**.


### Create a Database

  1. Log into PostgreSQL(CIdatabase maker).
  2. Add your email address and submit the form.
  3. Open the database link sent to your email.
  4. Copy the database URL and paste it into:
     - `DATABASE_URL` variable in `env.py`
     - Heroku Config Vars


### Deploying to Heroku 

<img width="1512" height="828" alt="Deployment Screenshot" src="https://github.com/user-attachments/assets/dd259ff3-4338-4fdb-a5c2-ea10a697ffbf" />

  1. Go to your app in Heroku and open the **Settings** tab.
  2. Scroll to **Config Vars** and set:
     - `DATABASE_URL` (your database URL)
     - `SECRET_KEY` (a unique secret key)
     - `CLOUDINARY_URL` (your Cloudinary URL)
     - `PORT` as `8000`
  3. Go to the **Deploy** tab and select **GitHub** as your deployment method.
  4. Connect your GitHub account and repository.
  5. Scroll to **Manual Deploy** and click **Deploy Branch**.
  6. Once deployment finishes, click **View App** to open your live site.

  **Note:** When deploying manually, redeploy after each repository update.


---

## Credits

**Personal Note:** 
I'd like to thank my wife and baby daughter for their patience and support for me throughout this journey. It wasn't easy, but having you both by my side has made each moment worth fighting through. 

Another thank you to the course convenors and facilitators at the Code Institute(you know who you are),for the resources and sessions and the personal help received in moments of crisis. 

I also send a huge thank you to my cohort group, where I not only made professional links but genuine friendships along the way! Thank you for pushing me again, you know who you are!

### Resources Used:

### AI 
AI was an instrumental tool that helped me to debug errors during development, planning and testing phases. I utilised a variety of LLM's to diversify the quality of the code and to ensure I was building appropriately. I have used it to generate User story ideas, which were edited to suit my specific desire and brief for the project, and find relevant content for some of the posts with reference to real-world events. 

### Code 
- Code Institute Learning Management System - Used to recap coding concepts on HTML, CSS, JavaScript, Python, and Databases. 
- Code Star Walkthrough project - This was a major tool in building the entire site, as step-by-step instructions were presented, especially when tackling more of the back-end technical aspects of Django, PostgreSQL, and deployment.  
- Kaleidoscope Learning Project - Used for some of the CSS Styling  
- Dev Hawks Quiz Project - Used for some of the CSS Styling
  
### YouTube/Media Tutorials
- CS50W Lecture 2 -  Python: https://www.youtube.com/watch?v=EOLPQdVj5Ac&list=PLhQjrBD2T380xvFSUmToMMzERZ3qB5Ueu&index=4
- CS50W Lecture 3 -  Django: https://www.youtube.com/watch?v=w8q0C-C1js4&list=PLhQjrBD2T380xvFSUmToMMzERZ3qB5Ueu&index=6
- CS50W Lecture 4 -  SQL, Models and Migrations: https://www.youtube.com/watch?v=YzP164YANAU&t=2s
- CS50W Lecture 5 - JavaScript: https://www.youtube.com/watch?v=x5trGVMKTdY&list=PLhQjrBD2T380xvFSUmToMMzERZ3qB5Ueu&index=7

### Images
Most images were sourced using Pexels. I added a personal image for the About Us page, and the logo was an AI-generated design with a specific prompt that required using the colour palette to facilitate consistency and a strong theme across the app.  

- **Logo**: AI-generated design. 

- Image used as a placeholder for all blog posts: 
![pexels-mikael-blomkvist-6476783](https://github.com/user-attachments/assets/89ea2944-6b13-446b-b5b4-616ebd87c30b) - Photo by Mikael Blomkvist from Pexels: https://www.pexels.com/photo/a-woman-in-red-long-sleeve-shirt-6476783/





