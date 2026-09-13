# How My Portfolio Gets to Your Browser (A Simple DNS Walkthrough)

When I deployed my portfolio, I put all my code on Vercel. But code sitting on a server isn't very useful unless people can actually find it. That's where DNS comes in.

Here is a simple breakdown of how the internet connects you to my work.

## What is DNS?
DNS stands for Domain Name System. It's essentially the phonebook of the internet. Computers talk to each other using IP addresses (which are just long strings of numbers like `192.168.1.1`), but humans prefer memorable names like `google.com` or `krish.dev`. DNS translates the human-readable name into the machine-readable IP address.

## The Full Journey
When you type a URL into your browser and hit Enter, a lot happens behind the scenes in milliseconds:

1. **The Browser:** Your browser first checks if it already knows the IP address for that URL. If it doesn't, it asks a DNS Resolver.
2. **The DNS Resolver:** This is usually provided by your internet service provider (like Comcast or AT&T). It acts like a helpful assistant that goes out to find the right IP address for you.
3. **The Nameserver:** The resolver asks specialized servers called Nameservers. Nameservers hold the actual "records" that point a specific domain name to a specific destination.
4. **The Hosting Provider:** Once the resolver gets the destination address from the nameserver, it hands it back to your browser. Your browser then connects directly to the server where the website lives (in my case, Vercel).
5. **The Website:** Vercel sees the request, grabs the compiled HTML/CSS/JS for my portfolio, and sends it back to your browser to display.

## DNS Records (The Details)
Inside a nameserver, there are **DNS records**. These are just rules that tell the internet exactly where different parts of a domain should go. 

If I wanted to connect a custom domain (like `krishmistry.com`) to my Vercel site, I would use a specific type of record called a **CNAME record** (Canonical Name). A CNAME basically says, "If someone looks for *this* name, send them over to *that* name." It's perfect for pointing a custom domain to a platform like Vercel because Vercel's actual server IP addresses might change over time, but their underlying routing address (like `cname.vercel-dns.com`) stays the same.

## My Current Setup
Right now, my live portfolio URL is:
`https://portfolio-eta-pied-17.vercel.app/`

I haven't purchased or configured a custom domain yet. I'm just using the default, free subdomain that Vercel provides. Because of this, Vercel handles all the nameservers and DNS records automatically. When you go to that `.vercel.app` link, Vercel's own DNS tells your browser exactly which of their servers holds my project.

## A Note on HTTPS
You'll notice my URL starts with `https://`. The "S" stands for Secure. This means the connection between your browser and Vercel's servers is encrypted using a TLS certificate. Vercel automatically generates and renews this certificate for me. It ensures that any data passed back and forth (like a recruiter sending me a message) can't be easily intercepted or read by someone else on the network.
