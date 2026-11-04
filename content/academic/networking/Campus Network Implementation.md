## Diagram

![[image.png]]

## IP Addressing

### Overall calculation

| Segment / Role | VLAN | Prefix | Network Addr | Subnet Mask | Wildcard | Usable Host Range | Broadcast | Usable Hosts |
| :--- | :---: | :---: | :--- | :--- | :--- | :--- | :--- | :---: |
| **MLS-CSE Student** | 10 | `/21` | `192.168.0.0` | `255.255.248.0` | `0.0.7.255` | `192.168.0.1 – 192.168.7.254` | `192.168.7.255` | 2046 |
| **MLS-CSE Teacher** | 20 | `/22` | `192.168.24.0` | `255.255.252.0` | `0.0.3.255` | `192.168.24.1 – 192.168.27.254` | `192.168.27.255` | 1022 |
| **MLS-CSE Academic** | 30 | `/23` | `192.168.36.0` | `255.255.254.0` | `0.0.1.255` | `192.168.36.1 – 192.168.37.254` | `192.168.37.255` | 510 |
| **MLS-BBA Student** | 10 | `/21` | `192.168.8.0` | `255.255.248.0` | `0.0.7.255` | `192.168.8.1 – 192.168.15.254` | `192.168.15.255` | 2046 |
| **MLS-BBA Teacher** | 20 | `/22` | `192.168.28.0` | `255.255.252.0` | `0.0.3.255` | `192.168.28.1 – 192.168.31.254` | `192.168.31.255` | 1022 |
| **MLS-BBA Academic** | 30 | `/23` | `192.168.38.0` | `255.255.254.0` | `0.0.1.255` | `192.168.38.1 – 192.168.39.254` | `192.168.39.255` | 510 |
| **MLS-NFS Student** | 10 | `/21` | `192.168.16.0` | `255.255.248.0` | `0.0.7.255` | `192.168.16.1 – 192.168.23.254` | `192.168.23.255` | 2046 |
| **MLS-NFS Teacher** | 20 | `/22` | `192.168.32.0` | `255.255.252.0` | `0.0.3.255` | `192.168.32.1 – 192.168.35.254` | `192.168.35.255` | 1022 |
| **MLS-NFS Academic** | 30 | `/23` | `192.168.40.0` | `255.255.254.0` | `0.0.1.255` | `192.168.40.1 – 192.168.41.254` | `192.168.41.255` | 510 |
| **DIST -- MLS-CSE** | N/A | `/29` | `192.168.42.0` | `255.255.255.248` | `0.0.0.7` | `192.168.42.1 – 192.168.42.6` | `192.168.42.7` | 6 |
| **DIST -- MLS-BBA** | N/A | `/29` | `192.168.42.8` | `255.255.255.248` | `0.0.0.7` | `192.168.42.9 – 192.168.42.14` | `192.168.42.15` | 6 |
| **DIST -- MLS-NFS** | N/A | `/29` | `192.168.42.16` | `255.255.255.248` | `0.0.0.7` | `192.168.42.17 – 192.168.42.22` | `192.168.42.23` | 6 |
| **Core -- DIST Link** | N/A | `/24` | `103.133.254.0` | `255.255.255.0` | `0.0.0.255` | `103.133.254.1 – 103.133.254.254` | `103.133.254.255` | 254 |

### Device Interfaces

| Device | Interface | IP Address | OSPF Area | Description |
| :--- | :--- | :--- | :---: | :--- |
| **Core Router (MikroTik)** | `sfp2` (`to-DIST`) | `103.133.254.2/24` | 0 (Backbone) | Interconnect to Dist Router & Campus DNS Resolver |
| **DIST Router (Cisco 4321)** | `GigabitEthernet0/0/0` | `103.133.254.1/24` | 0 (Backbone) | Uplink to Core Router (MikroTik) |
| **DIST Router (Cisco 4321)** | `GigabitEthernet0/0/1` | `192.168.42.1/29` | 0 | Downlink to MLS-CSE |
| **MLS-CSE** | `GigabitEthernet1/0/1` | `192.168.42.2/29` | 0 | Uplink to DIST Router (`no switchport`) |
| **MLS-CSE** | `Vlan 10` | `192.168.0.1/21` | 0 | Default Gateway (`Student`) |
| **MLS-CSE** | `Vlan 20` | `192.168.24.1/22` | 0 | Default Gateway (`Teacher`) |
| **MLS-CSE** | `Vlan 30` | `192.168.36.1/23` | 0 | Default Gateway (`Academic`) |
| **MLS-BBA (Planned)** | `GigabitEthernet1/0/1` | `192.168.42.10/29` | 1 | Uplink to DIST Router (`no switchport`) |
| **MLS-BBA (Planned)** | `Vlan 10` | `192.168.8.1/21` | 1 | Default Gateway (`Student`) |
| **MLS-BBA (Planned)** | `Vlan 20` | `192.168.28.1/22` | 1 | Default Gateway (`Teacher`) |
| **MLS-BBA (Planned)** | `Vlan 30` | `192.168.38.1/23` | 1 | Default Gateway (`Academic`) |
| **MLS-NFS (Planned)** | `GigabitEthernet1/0/1` | `192.168.42.18/29` | 2 | Uplink to DIST Router (`no switchport`) |
| **MLS-NFS (Planned)** | `Vlan 10` | `192.168.16.1/21` | 2 | Default Gateway (`Student`) |
| **MLS-NFS (Planned)** | `Vlan 20` | `192.168.32.1/22` | 2 | Default Gateway (`Teacher`) |
| **MLS-NFS (Planned)** | `Vlan 30` | `192.168.40.1/23` | 2 | Default Gateway (`Academic`) |
| **Internet / Upstream** | DNS Upstream | `8.8.8.8, 1.1.1.1` | N/A | External Public DNS Forwarders |

## VLANs

| Pool Name | Network / Subnet | Default Gateway | DNS Server |
| :--- | :--- | :--- | :--- |
| **`CSE_STUDENT`** | `192.168.0.0/21` | `192.168.0.1` | `103.133.254.2` |
| **`CSE_TEACHER`** | `192.168.24.0/22` | `192.168.24.1` | `103.133.254.2` |
| **`CSE_ACADEMIC`** | `192.168.36.0/23` | `192.168.36.1` | `103.133.254.2` |
| **`BBA_STUDENT`** | `192.168.8.0/21` | `192.168.8.1` | `103.133.254.2` |
| **`BBA_TEACHER`** | `192.168.28.0/22` | `192.168.28.1` | `103.133.254.2` |
| **`BBA_ACADEMIC`** | `192.168.38.0/23` | `192.168.38.1` | `103.133.254.2` |
| **`NFS_STUDENT`** | `192.168.16.0/21` | `192.168.16.1` | `103.133.254.2` |
| **`NFS_TEACHER`** | `192.168.32.0/22` | `192.168.32.1` | `103.133.254.2` |
| **`NFS_ACADEMIC`** | `192.168.40.0/23` | `192.168.40.1` | `103.133.254.2` |

> **DHCP Excluded Addresses on MLS-CSE:**
> - `192.168.0.1` (SVI Vlan 10)
> - `192.168.24.1` (SVI Vlan 20)
> - `192.168.36.1` (SVI Vlan 30)
## Commands

### Core Router

আমরা Core router হিসেবে Cisco ISR এবং Microtik cloud core router চেষ্টা করেছি। 

Microtik  এর router এর ক্ষেত্রে সাধারনত GUI দিয়েই সব কাজ করা যায়। এর জন্য আলাদা করে console cable এর প্রয়োজন হয় না। LAN port এ কোনো পিসি কানেক্ট করে winbox (Microtik এর তৈরিকৃত সফটওয়্যার) এর মাধ্যমে সরাসরি GUI access করা যায়।

```
!# ===== 1. Clean up earlier attempts =====
/ip address remove [find address="103.133.254.2/24"]
/ip route remove [find dst-address="0.0.0.0/0" gateway="103.133.254.1"]
/routing ospf network remove [find]
/routing ospf interface remove [find dynamic=no]
/interface bridge port remove [find interface~"sfp1|sfp2|to-CSE"]
/interface ethernet set [find default-name=sfp1] name=sfp1

!# ===== 2. Identity and link port =====
/system identity set name=CORE

/interface ethernet set [find default-name=sfp2] name=to-DIST mtu=1500  !# the interface must be correct(eg: sfp2 here)

!# ===== 3. IP address on the link to the 4321 =====
/ip address add address=103.133.254.2/24 interface=to-CSE comment="Link to CSE 4321"

!# ===== 4. OSPF (area 0 / backbone) =====
/routing ospf instance set [find default=yes] router-id=1.2.3.0
/routing ospf network add network=103.133.254.0/24 area=backbone

!# ===== 5. Allow OSPF through the firewall =====
/ip firewall filter add chain=input protocol=ospf action=accept comment="Allow OSPF"

!# ===== 6. DNS for campus hosts (DHCP gives 103.133.254.2 as DNS) =====
/ip dns set servers=8.8.8.8,1.1.1.1 allow-remote-requests=yes



!# ===== 7. Testing the connection =====
/interface print
/ping 103.133.254.1 count=4
/routing ospf interface print
/routing ospf neighbor print
/ip route print where ospf
/ping 192.168.0.1 count=4
```

### Distribution Router
```
enable
configure terminal
! Link to Core
interface GigabitEthernet0/0/0
 ip address 103.133.254.1 255.255.255.0
 no shutdown

exit

interface GigabitEthernet0/0/1
 ip address 192.168.42.1 255.255.255.248
 no shutdown
exit

! Static route for the campus VLSM block
ip route 192.168.0.0 255.255.0.0 103.133.254.2


router ospf 1
 router-id 2.2.2.2
 network 192.168.42.0 0.0.0.7 area 0
 no passive-interface GigabitEthernet0/0/1
exit

end
```

### MLS-CSE 

এটা একটি Multilayer switch, তাই এর মাধ্যমে আমরা Layer 3 এর কাজও করতে পারি। এবং routing alogorithm গুলো কার্যকর হয়,

```
enable
configure terminal
ip routing

vlan 10
 name Student
vlan 20
 name Teacher
vlan 30
 name Academic
exit

interface range GigabitEthernet 1/0/1 - 12
 switchport mode access
 switchport access vlan 10
interface range GigabitEthernet 1/0/13 - 24
 switchport mode access
 switchport access vlan 20
interface range GigabitEthernet 1/0/25 - 36
 switchport mode access
 switchport access vlan 30
exit

interface vlan 10
 ip address 192.168.0.1 255.255.248.0
 no shutdown
interface vlan 20
 ip address 192.168.24.1 255.255.252.0
 no shutdown
interface vlan 30
 ip address 192.168.36.1 255.255.254.0
 no shutdown
exit

ip dhcp excluded-address 192.168.0.1
ip dhcp excluded-address 192.168.24.1
ip dhcp excluded-address 192.168.36.1

ip dhcp pool CSE_STUDENT
 network 192.168.0.0 255.255.248.0
 default-router 192.168.0.1
 dns-server 103.133.254.2
ip dhcp pool CSE_TEACHER
 network 192.168.24.0 255.255.252.0
 default-router 192.168.24.1
 dns-server 103.133.254.2
ip dhcp pool CSE_ACADEMIC
 network 192.168.36.0 255.255.254.0
 default-router 192.168.36.1
 dns-server 103.133.254.2
exit


interface GigabitEthernet 1/0/1
 no switchport
 ip address 192.168.42.2 255.255.255.248
 no shutdown
exit


router ospf 1
 router-id 1.1.1.1
 network 192.168.0.0 0.0.7.255 area 0
 network 192.168.24.0 0.0.3.255 area 0
 network 192.168.36.0 0.0.1.255 area 0
 network 192.168.42.0 0.0.0.7 area 0
exit
```