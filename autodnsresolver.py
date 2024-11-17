import argparse
import dns.resolver
import json

def get_spf_record(domain, server=None):
    resolver = dns.resolver.Resolver()
    if server:
        resolver.nameservers = [server]
    try:
        answers = resolver.resolve(domain, 'TXT')
        for rdata in answers:
            if 'v=spf1' in str(rdata):
                return str(rdata)
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.exception.Timeout):
        return None

def get_dkim_record(domain, selector, server=None):
    resolver = dns.resolver.Resolver()
    if server:
        resolver.nameservers = [server]
    try:
        dkim_domain = f"{selector}._domainkey.{domain}"
        answers = resolver.resolve(dkim_domain, 'TXT')
        for rdata in answers:
            return str(rdata)
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.exception.Timeout):
        return None

def get_dmarc_record(domain, server=None):
    resolver = dns.resolver.Resolver()
    if server:
        resolver.nameservers = [server]
    try:
        dmarc_domain = f"_dmarc.{domain}"
        answers = resolver.resolve(dmarc_domain, 'TXT')
        for rdata in answers:
            return str(rdata)
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.exception.Timeout):
        return None

def process_domain(domain, dkim_selector, server):
    result = {
        'Name': domain,
        'SpfRecord': None,
        'SpfEnabled': False,
        'DkimRecord': None,
        'DkimEnabled': False,
        'DmarcRecord': None,
        'DmarcEnabled': False,
    }

    spf_record = get_spf_record(domain, server)
    result['SpfRecord'] = spf_record
    result['SpfEnabled'] = bool(spf_record)

    if dkim_selector:
        dkim_record = get_dkim_record(domain, dkim_selector, server)
        result['DkimRecord'] = dkim_record
        result['DkimEnabled'] = bool(dkim_record)

    dmarc_record = get_dmarc_record(domain, server)
    result['DmarcRecord'] = dmarc_record
    result['DmarcEnabled'] = bool(dmarc_record)

    return result

def main():
    parser = argparse.ArgumentParser(description="Resolver registros SPF, DKIM y DMARC para un dominio.")
    parser.add_argument('-n', '--name', type=str, required=True, help="Especifica el dominio para resolver los registros.")
    parser.add_argument('-d', '--dkim-selector', type=str, help="Especifica un selector DKIM personalizado.")
    parser.add_argument('-s', '--server', type=str, help="Servidor DNS a utilizar.")
    parser.add_argument('-o', '--output', type=str, required=True, help="Archivo de salida para guardar los resultados en formato JSON.")

    args = parser.parse_args()

    result = process_domain(args.name, args.dkim_selector, args.server)

    with open(args.output, 'w') as outfile:
        json.dump(result, outfile, indent=4)

    print(f"Resultados guardados en {args.output}")

if __name__ == "__main__":
    main()
