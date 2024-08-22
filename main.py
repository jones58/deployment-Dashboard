import requests
import asyncio
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from fasthtml.common import *

tlink = Script(src="https://cdn.tailwindcss.com")

favicon = Link(rel="icon", type="image/x-icon", href="/public/favicon.ico")

def render(site):
    sid= f'site-{site.ROWID}'
    delete = A("Delete", cls="hover:text-gray-700", hx_delete=f"/{site.ROWID}",hx_swap="outerHTML", target_id=f'{sid}')
    name_link = A(site.name, href=site.url, target="_blank", cls="hover:text-gray-700")
    return Tr(Td(name_link), Td(site.tech), Td(site.service), Td(site.status), Td(delete), id=sid)

app, rt, sites, Site= fast_app("mysites.db", live=True, ROWID=int, name=str, tech=str, service=str, status=str, pk='ROWID', url=str, render=render, hdrs=(tlink,picolink, favicon))

def add_inputs(): return Input(placeholder="Site name", id="name", hx_swap_oob="true"), Input(placeholder="Tech", id="tech", hx_swap_oob="true"), Input(placeholder="Service", id="service", hx_swap_oob="true"), Input(placeholder="URL", id="url", hx_swap_oob="true")

@rt("/")
def get():
    Socials(
            title="Deployment Dashboard",
            site_name="Deployment Dashboard",
            description="A tool to check Jack's Deployments",
            image="public/favicon.ico",
            url="https://fasthtml-template.vercel.app",
        ),

    frm = Form (Group(add_inputs(), Button("Add", cls="px-5 bg-green-600 hover:bg-green-700") ),
        hx_post ="/", target_id="sites-table", hx_swap="beforeend", cls="w-[50%] mx-auto py-10"
    )
    footer= P(
                        A(
                            "View Code",
                            href="https://github.com/jones58/fasthtml-test",
                            target="_blank", cls="text-blue-600 hover:text-blue-700 px-20 text-center"
                        ),
                        )
    table = Table(
    Thead(Tr(Th("Name"), Th("Tech"), Th("Service"), Th("Status"), Th("Edit"))),
    Tbody(*sites(), id="sites-table"),cls="w-[50%] mx-auto py-10",
)
    return  Title('Deployment Dashboard'), Div(H1("Deployment Dashboard", cls="text-4xl font-bold text-white-600 px-4 py-6 mx-auto w-[50%] text-center"),P("A tool to check Jack's Deployments"), frm, table, footer)



@rt("/{sid}")
def delete(sid: int): sites.delete(sid)


def check_url(url):
    try:
        response = requests.get(url, timeout=5)
        return response.status_code == 200
    except:
        return False

async def update_statuses():
    while True:
        for site in sites():
            site.status = "OK" if check_url(site.url) else "Down"
            sites.update(site)
        await asyncio.sleep(60)  # Check every minute

@app.on_event("startup")
async def start_status_updater():
    asyncio.create_task(update_statuses())

@rt("/")
def post (site: Site): # type: ignore
    if site.url and not site.url.startswith('https://'):
        site.url = 'https://' + site.url
    site.status = "OK" if check_url(site.url) else "Down"
    return sites.insert(site), add_inputs()

serve()
