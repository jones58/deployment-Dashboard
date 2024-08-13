# Planning

- As part of learning FastHTML, I wanted to build an app to check my deployments, with similar functionality to this [deployments dashboard](https://jamesdiffeycoding-pythonlivedashboard.vercel.app/).
- I planned a table website design with Figma.

# Building

- I used the Vercel fasthtml template as a starting point.
- After watching the [getting started video](https://www.youtube.com/watch?v=Auqrm7WFc0I) and refreshing my Python knowledge, I was ready to start building the app.
- I used what I learnt in the video above (a todo list) to apply the same logic to a table, from which sites could be added or deleted as needed.
- Checking for typos helped me debug issues.
- I wanted to add an URL to the inputs, which would wrap around the name as an anchor tag. This proved difficult, as when i added a new input it would not show up in the table. I resolved this by stopping the app, deleting the database and restarting.
- Next I wanted to check that the URL responded to 200, which would be a good indicator that the site is online. I implemented this by adding a status column to the table, and a function to check the URL. I used asyncio to check the URL in the background every minute and update as needed.
- I wanted to add Tailwind to the app, since it was not included in fasthtml by default. Whilst PicoCSS is good, Tailwind is much better. I used the [Chatbot example](https://github.com/AnswerDotAI/fasthtml-example/blob/main/02_chatbot/basic.py) for how to add Tailwind to my app.
- Added a title to my app using Title(). I originally used Titled, as in the learning doc but since I wanted to style the H1 using Tailwind, I used Title to add this separately.

# Debugging

## Local development

- Install the required dependencies:

```bash
pip install -r requirements.txt
```

- Start the development server on http://0.0.0.0:5001

```bash
python main.py
```

When you make changes to your project, the server will automatically reload.

## Deploying to Vercel

Deploy your project to Vercel with the following command:

```bash
npm install -g vercel
vercel --prod
```

Or `git push` to your repostory with our [git integration](https://vercel.com/docs/deployments/git).
