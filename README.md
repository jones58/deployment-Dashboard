# Planning

- As part of learning FastHTML, I wanted to build an app to check my deployments, with similar functionality to this [deployments dashboard](https://jamesdiffeycoding-pythonlivedashboard.vercel.app/).
- I planned a table website design with Figma.

# Building

- I used the Vercel fasthtml template as a starting point.
- After watching the [getting started video](https://www.youtube.com/watch?v=Auqrm7WFc0I) and refreshing my Python knowledge, I was ready to start building the app.
- I used what I learnt in the video above (a todo list) to apply the same logic to a table, from which sites could be added or deleted as needed.
- Checking for typos helped me debug issues.

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
