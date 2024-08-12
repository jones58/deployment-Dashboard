from fasthtml.common import *

app, rt = fast_app(hdrs=(picolink))

@rt("/")
def get():
    return (
        Socials(
            title="Deployment Dashboard",
            site_name="Deployment Dashboard",
            description="A tool to check Jack's Deployments",
            image="https://vercel.fyi/fasthtml-og",
            url="https://fasthtml-template.vercel.app",
        ),
        Container(
            Card(
                Group(

                ),
                header=(Titled("Deployment Dashboard")),
                footer=(
                    P(
                        A(
                            "View Code",
                            href="https://github.com/jones58/fasthtml-test",
                            target="_blank",
                        ),
                          A(
                            "View LinkedIn",
                            href="https://vercel.com/templates/python/fasthtml-python-boilerplate",
                            target="_blank",
                        ),
                    )
                ),
            ),
        ),
    )


serve()
