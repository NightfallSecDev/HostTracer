import socket
import dns.resolver
import whois

def get_nameservers(domain):
    try:
        ns = dns.resolver.resolve(domain, 'NS')
        nameservers = [str(server.target) for server in ns]
        return nameservers
    except Exception as e:
        return [f"Error retrieving nameservers: {e}"]

def get_hosting_provider(domain):
    try:
        info = whois.whois(domain)
        if 'org' in info:
            return info['org']
        elif 'registrar' in info:
            return info['registrar']
        else:
            return "Hosting provider not found."
    except Exception as e:
        return f"Error retrieving hosting provider: {e}"

def main():
    domain = input("Enter domain: ")
    
    print("\n🔍 Checking Name Servers...")
    nameservers = get_nameservers(domain)
    for ns in nameservers:
        print(f"➡️ {ns}")
    
    print("\n🌐 Finding Hosting Provider...")
    hosting_provider = get_hosting_provider(domain)
    print(f"➡️ {hosting_provider}")

if __name__ == "__main__":
    main()
