# IP Blocklist

![GitHub Repo stars](https://img.shields.io/github/stars/bitwire-it/ipblocklist)
[![Update IP Lists](https://github.com/bitwire-it/ipblocklist/actions/workflows/update.yml/badge.svg)](https://github.com/bitwire-it/ipblocklist/actions/workflows/update.yml)
[![Update History Stats](https://github.com/bitwire-it/ipblocklist/actions/workflows/stats.yml/badge.svg)](https://github.com/bitwire-it/ipblocklist/actions/workflows/stats.yml)

<a href="https://www.buymeacoffee.com/Matis7" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>

This project provides aggregated IP blocklists for inbound and outbound traffic, updated every 2 hours. It includes exclusions for major public DNS resolvers to prevent legitimate services from being blocked.

---

## Live Statistics

[![Stats Dashboard](https://i.imgur.com/Ry8gI44.png)](https://bitwire.it/blocklist-stats)

[![Live Dashboard](https://img.shields.io/badge/Live%20Dashboard-bitwire.it-blue?style=for-the-badge)](https://bitwire.it/blocklist-stats)

---

## Download

| List | URL |
|------|-----|
| `inbound.txt` | `https://raw.githubusercontent.com/bitwire-it/ipblocklist/main/inbound.txt` |
| `outbound.txt` | `https://raw.githubusercontent.com/bitwire-it/ipblocklist/main/outbound.txt` |

---

## How to Use These Lists

These are standard text files and can be used with most modern firewalls, ad-blockers, and security tools.

### 🛡️ `inbound.txt` (Inbound Blocklist)

* **What it is:** A list of IPs/networks with a bad reputation for *initiating* malicious connections. This includes sources of spam, scanning, brute-force attacks (SSH, RDP), and web exploits.
* **Use Case:** Protect your public-facing servers and services (web servers, mail servers, game servers, etc.).
* **How to use:** Apply this list to your firewall's **WAN IN** or **INPUT** chain to **DROP** or **REJECT** all incoming traffic *from* these sources.

### ☢️ `outbound.txt` (Outbound Blocklist)

* **What it is:** A list of known malicious destination IPs. This includes C2 (Command & Control) servers, botnet controllers, malware drop sites, and phishing hosts.
* **Use Case:** Prevent compromised devices on your *internal* network (like a laptop or IoT device) from *contacting* malicious servers.
* **How to use:** Apply this list to your firewall's **LAN OUT** or **OUTPUT** chain to **BLOCK** or **LOG** all outgoing traffic *to* these destinations.

---

## Self-hosted runners

The `update.yml` workflow takes a long time to complete. I run it on a self-hosted runner. If you fork this repo and want to use the same workflow, set up a self-hosted runner:
[Setup Self-hosted runners](https://docs.github.com/en/actions/how-tos/manage-runners/self-hosted-runners/add-runners)

---

## Acknowledgements

🪨 **[borestad](https://www.github.com/borestad)** • *foundational blocklists* 🚀 **Code contributions**
- [David](https://github.com/dvdctn)
- [Garrett Laman](https://github.com/garrettlaman)

❤️ **Our sponsors** • *making this project possible*
- [mraxu](https://www.github.com/mraxu)
- Hareen
- Alexandru Balmus
- blockstreamtechnologies.llc

---

## License

### Code
The source code (including `update_tables.py`) is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.

### Data
The aggregated blocklists (`inbound.txt`, `outbound.txt`, etc.) are derivative works containing data from multiple sources.

**Usage of these lists is subject to the licenses of the original data providers.** Many sources (e.g., Spamhaus) **prohibit commercial use** of their data without a separate agreement.

Therefore, the aggregated data in this repository is provided under the **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)** license.

**Attribution:**
This project relies on data from:

- [borestad/blocklist-abuseipdb](https://github.com/borestad/blocklist-abuseipdb)
- [borestad/firehol-mirror](https://github.com/borestad/firehol-mirror)
- [duggytuxy/Data-Shield_IPv4_Blocklist](https://github.com/duggytuxy/Data-Shield_IPv4_Blocklist)
- [stamparm/ipsum](https://github.com/stamparm/ipsum) *(via [bitwire-it/ipsum-clean](https://github.com/bitwire-it/ipsum-clean))*
- [ShadowWhisperer/IPs](https://github.com/ShadowWhisperer/IPs)
- [romainmarcoux/malicious-ip](https://github.com/romainmarcoux/malicious-ip)
- [romainmarcoux/malicious-outgoing-ip](https://github.com/romainmarcoux/malicious-outgoing-ip)
- [elliotwutingfeng/ThreatFox-IOC-IPs](https://github.com/elliotwutingfeng/ThreatFox-IOC-IPs)
- [CriticalPathSecurity/Public-Intelligence-Feeds](https://github.com/CriticalPathSecurity/Public-Intelligence-Feeds)
- [T145/black-mirror](https://github.com/T145/black-mirror)
- [drb-ra/C2IntelFeeds](https://github.com/drb-ra/C2IntelFeeds)
- [SecOps-Institute/Tor-IP-Addresses](https://github.com/SecOps-Institute/Tor-IP-Addresses)
- [mitchellkrogza/nginx-ultimate-bad-bot-blocker](https://github.com/mitchellkrogza/nginx-ultimate-bad-bot-blocker)
- [hagezi/dns-blocklists](https://github.com/hagezi/dns-blocklists)
- [malware-filter/malware-filter](https://gitlab.com/malware-filter/malware-filter) *(botnet-filter)*
- [binarydefense.com](https://www.binarydefense.com/banlist.txt)
- [bruteforceblocker.com](https://danger.rulez.sk/projects/bruteforceblocker/blist.php)
- [darklist.de](https://www.darklist.de/raw.php)
- [Emerging Threats](https://rules.emergingthreats.net/blockrules/compromised-ips.txt)
- [Spamhaus DROP](https://www.spamhaus.org/drop/drop.txt)
- [CINSscore / CINSArmy](https://cinsscore.com/list/ci-badguys.txt)
- [dataplane.org](https://dataplane.org)
- [greensnow.co](https://blocklist.greensnow.co/greensnow.txt)
- [vxvault.net](http://vxvault.net/URL_List.php)
- [blackip.ustc.edu.cn](https://blackip.ustc.edu.cn/list.php?txt)
- [sblam.com](https://sblam.com/blacklist.txt)
- [stopforumspam.com](https://www.stopforumspam.com/downloads/toxic_ip_cidr.txt)
- [multiproxy.org](https://multiproxy.org/txt_all/proxy.txt)
- [myip.ms](https://myip.ms/files/blacklist/htaccess/latest_blacklist.txt)
- [AlienVault OTX](https://reputation.alienvault.com/reputation.generic)
- [Rutgers DROP](https://report.rutgers.edu/DROP/attackers)
- [Checkpoint TOR list](https://secureupdates.checkpoint.com/IP-list/TOR.txt)
- [opendbl.net](https://www.opendbl.net/lists/bruteforce.list)

---

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=bitwire-it/ipblocklist&type=Date)](https://star-history.com/#bitwire-it/ipblocklist&Date)
