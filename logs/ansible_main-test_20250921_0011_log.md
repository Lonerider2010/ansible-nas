<pre>[<span style="color:#00AA00">2025-09-21 00:11:01</span>] (venv) [<span style="color:#55FF55"><b>dietmar@MiraPi</b></span>] [<span style="color:#5555FF"><b>.../</b></span>ansible-playbook -i inventories/RaspiNAS/inventory nas.yml -b -K<span style="background-color:#FFFFFF"><span style="color:#2D2D2D">nventory nas.yml -b -K</span></span>
<span style="color:#0000AA">ansible-playbook [core 2.16.14]</span>
<span style="color:#0000AA">  config file = /media/IT/repos/github/forked/ansible-nas/ansible.cfg</span>
<span style="color:#0000AA">  configured module search path = [&apos;/home/dietmar/.ansible/plugins/modules&apos;, &apos;/usr/share/ansible/plugins/modules&apos;]</span>
<span style="color:#0000AA">  ansible python module location = /media/web/projects/common/venv/lib/python3.11/site-packages/ansible</span>
<span style="color:#0000AA">  ansible collection location = /home/dietmar/.ansible/collections:/usr/share/ansible/collections</span>
<span style="color:#0000AA">  executable location = /media/web/projects/common/venv/bin/ansible-playbook</span>
<span style="color:#0000AA">  python version = 3.11.2 (main, Apr 28 2025, 14:11:48) [GCC 12.2.0] (/media/web/projects/common/venv/bin/python)</span>
<span style="color:#0000AA">  jinja version = 3.1.4</span>
<span style="color:#0000AA">  libyaml = True</span>
<span style="color:#0000AA">Using /media/IT/repos/github/forked/ansible-nas/ansible.cfg as config file</span>
BECOME password: 
<span style="color:#0000AA">statically imported: /media/IT/repos/github/forked/ansible-nas/roles/stats/tasks/prometheus.yml</span>
<span style="color:#0000AA">statically imported: /media/IT/repos/github/forked/ansible-nas/roles/stats/tasks/telegraf.yml</span>
<span style="color:#0000AA">statically imported: /media/IT/repos/github/forked/ansible-nas/roles/stats/tasks/exporters.yml</span>
<span style="color:#0000AA">statically imported: /media/IT/repos/github/forked/ansible-nas/roles/stats/tasks/grafana.yml</span>
<span style="color:#0000AA">redirecting (type: callback) ansible.builtin.debug to ansible.posix.debug</span>
<span style="color:#0000AA">redirecting (type: callback) ansible.builtin.debug to ansible.posix.debug</span>
<span style="color:#0000AA">Skipping callback &apos;default&apos;, as we already have a stdout callback.</span>
<span style="color:#0000AA">Skipping callback &apos;minimal&apos;, as we already have a stdout callback.</span>
<span style="color:#0000AA">Skipping callback &apos;oneline&apos;, as we already have a stdout callback.</span>

PLAYBOOK: nas.yml *************************************************************************************************************************************************************************************************
<span style="color:#0000AA">1 plays in nas.yml</span>

PLAY [Ansible-NAS] ************************************************************************************************************************************************************************************************
Sonntag 21 September 2025  00:11:40 +0200 (0:00:00.179)       0:00:00.179 ***** 

TASK [Gathering Facts] ********************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/nas.yml:2</b></span>
<span style="color:#00AA00">ok: [ansible-nas]</span>
Sonntag 21 September 2025  00:11:42 +0200 (0:00:02.077)       0:00:02.257 ***** 

TASK [ansible-nas-users : Create ansible-nas group] ***************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-users/tasks/main.yml:2</b></span>
<span style="color:#AA5500">changed: [ansible-nas] =&gt; {</span>
<span style="color:#AA5500">    &quot;changed&quot;: true,</span>
<span style="color:#AA5500">    &quot;gid&quot;: 1001,</span>
<span style="color:#AA5500">    &quot;name&quot;: &quot;ansible-nas&quot;,</span>
<span style="color:#AA5500">    &quot;state&quot;: &quot;present&quot;,</span>
<span style="color:#AA5500">    &quot;system&quot;: false</span>
<span style="color:#AA5500">}</span>
Sonntag 21 September 2025  00:11:42 +0200 (0:00:00.599)       0:00:02.857 ***** 

TASK [ansible-nas-users : Create ansible-nas user] ****************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-users/tasks/main.yml:7</b></span>
<span style="color:#AA5500">changed: [ansible-nas] =&gt; {</span>
<span style="color:#AA5500">    &quot;changed&quot;: true,</span>
<span style="color:#AA5500">    &quot;comment&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">    &quot;create_home&quot;: false,</span>
<span style="color:#AA5500">    &quot;group&quot;: 1001,</span>
<span style="color:#AA5500">    &quot;home&quot;: &quot;/home/ansible-nas&quot;,</span>
<span style="color:#AA5500">    &quot;name&quot;: &quot;ansible-nas&quot;,</span>
<span style="color:#AA5500">    &quot;shell&quot;: &quot;/usr/sbin/nologin&quot;,</span>
<span style="color:#AA5500">    &quot;state&quot;: &quot;present&quot;,</span>
<span style="color:#AA5500">    &quot;system&quot;: true,</span>
<span style="color:#AA5500">    &quot;uid&quot;: 994</span>
<span style="color:#AA5500">}</span>
Sonntag 21 September 2025  00:11:43 +0200 (0:00:00.729)       0:00:03.586 ***** 

TASK [vladgh.samba.server : Include OS specific variables] ********************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/collections/ansible_collections/vladgh/samba/roles/server/tasks/main.yml:2</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;ansible_facts&quot;: {</span>
<span style="color:#00AA00">        &quot;nmb_service&quot;: &quot;nmbd&quot;,</span>
<span style="color:#00AA00">        &quot;samba_configuration&quot;: &quot;{{ samba_configuration_dir }}/smb.conf&quot;,</span>
<span style="color:#00AA00">        &quot;samba_configuration_dir&quot;: &quot;/etc/samba&quot;,</span>
<span style="color:#00AA00">        &quot;samba_packages&quot;: [</span>
<span style="color:#00AA00">            &quot;samba&quot;,</span>
<span style="color:#00AA00">            &quot;smbclient&quot;</span>
<span style="color:#00AA00">        ],</span>
<span style="color:#00AA00">        &quot;samba_username_map_file&quot;: &quot;{{ samba_configuration_dir }}/smbusers&quot;,</span>
<span style="color:#00AA00">        &quot;samba_vfs_packages&quot;: [</span>
<span style="color:#00AA00">            &quot;samba-vfs-modules&quot;</span>
<span style="color:#00AA00">        ],</span>
<span style="color:#00AA00">        &quot;samba_www_documentroot&quot;: &quot;/var/www&quot;,</span>
<span style="color:#00AA00">        &quot;smb_service&quot;: &quot;smbd&quot;</span>
<span style="color:#00AA00">    },</span>
<span style="color:#00AA00">    &quot;ansible_included_var_files&quot;: [</span>
<span style="color:#00AA00">        &quot;/home/dietmar/.ansible/collections/ansible_collections/vladgh/samba/roles/server/vars/os_Debian.yml&quot;</span>
<span style="color:#00AA00">    ],</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  00:11:43 +0200 (0:00:00.051)       0:00:03.638 ***** 

TASK [vladgh.samba.server : Install Samba packages] ***************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/collections/ansible_collections/vladgh/samba/roles/server/tasks/main.yml:12</b></span>
<span style="color:#AA5500">changed: [ansible-nas] =&gt; {</span>
<span style="color:#AA5500">    &quot;cache_update_time&quot;: 1758331880,</span>
<span style="color:#AA5500">    &quot;cache_updated&quot;: false,</span>
<span style="color:#AA5500">    &quot;changed&quot;: true</span>
<span style="color:#AA5500">}</span>

<span style="color:#AA5500">STDOUT:</span>

<span style="color:#AA5500">Reading package lists...</span>
<span style="color:#AA5500">Building dependency tree...</span>
<span style="color:#AA5500">Reading state information...</span>
<span style="color:#AA5500">The following package was automatically installed and is no longer required:</span>
<span style="color:#AA5500">  rpicam-apps-lite</span>
<span style="color:#AA5500">Use &apos;sudo apt autoremove&apos; to remove it.</span>
<span style="color:#AA5500">The following additional packages will be installed:</span>
<span style="color:#AA5500">  attr libarchive13 libcephfs2 libldb2 liblmdb0 libsmbclient libtdb1</span>
<span style="color:#AA5500">  libtevent0 python3-anyio python3-cffi-backend python3-click python3-colorama</span>
<span style="color:#AA5500">  python3-cryptography python3-dnspython python3-gpg python3-h11 python3-h2</span>
<span style="color:#AA5500">  python3-hpack python3-httpcore python3-httpx python3-hyperframe python3-ldb</span>
<span style="color:#AA5500">  python3-markdown python3-markdown-it python3-mdurl python3-pygments</span>
<span style="color:#AA5500">  python3-requests-toolbelt python3-rfc3986 python3-rich python3-samba</span>
<span style="color:#AA5500">  python3-sniffio python3-talloc python3-tdb samba-ad-provision samba-common</span>
<span style="color:#AA5500">  samba-common-bin samba-dsdb-modules samba-libs samba-vfs-modules tdb-tools</span>
<span style="color:#AA5500">Suggested packages:</span>
<span style="color:#AA5500">  lrzip python-cryptography-doc python3-cryptography-vectors python3-trio</span>
<span style="color:#AA5500">  python3-aioquic python-markdown-doc python-pygments-doc ttf-bitstream-vera</span>
<span style="color:#AA5500">  bind9 bind9utils ctdb ldb-tools ntp | chrony ufw winbind heimdal-clients</span>
<span style="color:#AA5500">The following NEW packages will be installed:</span>
<span style="color:#AA5500">  attr libarchive13 libcephfs2 libldb2 liblmdb0 libsmbclient libtdb1</span>
<span style="color:#AA5500">  libtevent0 python3-anyio python3-cffi-backend python3-click python3-colorama</span>
<span style="color:#AA5500">  python3-cryptography python3-dnspython python3-gpg python3-h11 python3-h2</span>
<span style="color:#AA5500">  python3-hpack python3-httpcore python3-httpx python3-hyperframe python3-ldb</span>
<span style="color:#AA5500">  python3-markdown python3-markdown-it python3-mdurl python3-pygments</span>
<span style="color:#AA5500">  python3-requests-toolbelt python3-rfc3986 python3-rich python3-samba</span>
<span style="color:#AA5500">  python3-sniffio python3-talloc python3-tdb samba samba-ad-provision</span>
<span style="color:#AA5500">  samba-common samba-common-bin samba-dsdb-modules samba-libs</span>
<span style="color:#AA5500">  samba-vfs-modules smbclient tdb-tools</span>
<span style="color:#AA5500">0 upgraded, 42 newly installed, 0 to remove and 8 not upgraded.</span>
<span style="color:#AA5500">Need to get 15.8 MB of archives.</span>
<span style="color:#AA5500">After this operation, 110 MB of additional disk space will be used.</span>
<span style="color:#AA5500">Get:1 http://deb.debian.org/debian bookworm/main arm64 python3-dnspython all 2.3.0-1 [152 kB]</span>
<span style="color:#AA5500">Get:2 http://deb.debian.org/debian bookworm/main arm64 liblmdb0 arm64 0.9.24-1 [43.7 kB]</span>
<span style="color:#AA5500">Get:3 http://deb.debian.org/debian bookworm/main arm64 libtdb1 arm64 1.4.8-2 [43.6 kB]</span>
<span style="color:#AA5500">Get:4 http://deb.debian.org/debian bookworm/main arm64 libtevent0 arm64 0.14.1-1 [35.6 kB]</span>
<span style="color:#AA5500">Get:5 http://deb.debian.org/debian bookworm/main arm64 libldb2 arm64 2:2.6.2+samba4.17.12+dfsg-0+deb12u2 [155 kB]</span>
<span style="color:#AA5500">Get:6 http://deb.debian.org/debian bookworm/main arm64 python3-ldb arm64 2:2.6.2+samba4.17.12+dfsg-0+deb12u2 [60.4 kB]</span>
<span style="color:#AA5500">Get:7 http://deb.debian.org/debian bookworm/main arm64 python3-tdb arm64 1.4.8-2 [16.2 kB]</span>
<span style="color:#AA5500">Get:8 http://deb.debian.org/debian bookworm/main arm64 samba-libs arm64 2:4.17.12+dfsg-0+deb12u2 [5266 kB]</span>
<span style="color:#AA5500">Get:9 http://deb.debian.org/debian bookworm/main arm64 python3-talloc arm64 2.4.0-f2 [14.6 kB]</span>
<span style="color:#AA5500">Get:10 http://deb.debian.org/debian bookworm/main arm64 python3-samba arm64 2:4.17.12+dfsg-0+deb12u2 [2636 kB]</span>
<span style="color:#AA5500">Get:11 http://deb.debian.org/debian bookworm/main arm64 samba-common all 2:4.17.12+dfsg-0+deb12u2 [88.3 kB]</span>
<span style="color:#AA5500">Get:12 http://deb.debian.org/debian bookworm/main arm64 samba-common-bin arm64 2:4.17.12+dfsg-0+deb12u2 [1095 kB]</span>
<span style="color:#AA5500">Get:13 http://deb.debian.org/debian bookworm/main arm64 tdb-tools arm64 1.4.8-2 [26.6 kB]</span>
<span style="color:#AA5500">Get:14 http://deb.debian.org/debian bookworm/main arm64 samba arm64 2:4.17.12+dfsg-0+deb12u2 [888 kB]</span>
<span style="color:#AA5500">Get:15 http://deb.debian.org/debian bookworm/main arm64 attr arm64 1:2.5.1-4 [40.5 kB]</span>
<span style="color:#AA5500">Get:16 http://deb.debian.org/debian bookworm/main arm64 libarchive13 arm64 3.6.2-1+deb12u3 [317 kB]</span>
<span style="color:#AA5500">Get:17 http://deb.debian.org/debian bookworm/main arm64 libcephfs2 arm64 16.2.15+ds-0+deb12u1 [621 kB]</span>
<span style="color:#AA5500">Get:18 http://deb.debian.org/debian bookworm/main arm64 libsmbclient arm64 2:4.17.12+dfsg-0+deb12u2 [79.0 kB]</span>
<span style="color:#AA5500">Get:19 http://deb.debian.org/debian bookworm/main arm64 python3-sniffio all 1.2.0-1 [6372 B]</span>
<span style="color:#AA5500">Get:20 http://deb.debian.org/debian bookworm/main arm64 python3-anyio all 3.6.2-1 [54.0 kB]</span>
<span style="color:#AA5500">Get:21 http://deb.debian.org/debian bookworm/main arm64 python3-cffi-backend arm64 1.15.1-5+b1 [84.4 kB]</span>
<span style="color:#AA5500">Get:22 http://deb.debian.org/debian bookworm/main arm64 python3-colorama all 0.4.6-2 [36.8 kB]</span>
<span style="color:#AA5500">Get:23 http://deb.debian.org/debian bookworm/main arm64 python3-click all 8.1.3-2 [92.2 kB]</span>
<span style="color:#AA5500">Get:24 http://deb.debian.org/debian bookworm/main arm64 python3-cryptography arm64 38.0.4-3+deb12u1 [590 kB]</span>
<span style="color:#AA5500">Get:25 http://deb.debian.org/debian bookworm/main arm64 python3-gpg arm64 1.18.0-3+b1 [352 kB]</span>
<span style="color:#AA5500">Get:26 http://deb.debian.org/debian bookworm/main arm64 python3-h11 all 0.14.0-1.1~deb12u1 [50.6 kB]</span>
<span style="color:#AA5500">Get:27 http://deb.debian.org/debian bookworm/main arm64 python3-hpack all 4.0.0-2 [25.0 kB]</span>
<span style="color:#AA5500">Get:28 http://deb.debian.org/debian bookworm/main arm64 python3-hyperframe all 6.0.0-1 [14.5 kB]</span>
<span style="color:#AA5500">Get:29 http://deb.debian.org/debian bookworm/main arm64 python3-h2 all 4.1.0-4 [80.8 kB]</span>
<span style="color:#AA5500">Get:30 http://deb.debian.org/debian bookworm/main arm64 python3-httpcore all 0.16.3-1 [38.4 kB]</span>
<span style="color:#AA5500">Get:31 http://deb.debian.org/debian bookworm/main arm64 python3-pygments all 2.14.0+dfsg-1 [783 kB]</span>
<span style="color:#AA5500">Get:32 http://deb.debian.org/debian bookworm/main arm64 python3-mdurl all 0.1.2-1 [9444 B]</span>
<span style="color:#AA5500">Get:33 http://deb.debian.org/debian bookworm/main arm64 python3-markdown-it all 2.1.0-5 [58.8 kB]</span>
<span style="color:#AA5500">Get:34 http://deb.debian.org/debian bookworm/main arm64 python3-rich all 13.3.1-1 [202 kB]</span>
<span style="color:#AA5500">Get:35 http://deb.debian.org/debian bookworm/main arm64 python3-rfc3986 all 1.5.0-2 [22.2 kB]</span>
<span style="color:#AA5500">Get:36 http://deb.debian.org/debian bookworm/main arm64 python3-httpx all 0.23.3-1 [72.3 kB]</span>
<span style="color:#AA5500">Get:37 http://deb.debian.org/debian bookworm/main arm64 python3-markdown all 3.4.1-2 [64.7 kB]</span>
<span style="color:#AA5500">Get:38 http://deb.debian.org/debian bookworm/main arm64 python3-requests-toolbelt all 0.10.1-1 [41.3 kB]</span>
<span style="color:#AA5500">Get:39 http://deb.debian.org/debian bookworm/main arm64 samba-ad-provision all 2:4.17.12+dfsg-0+deb12u2 [416 kB]</span>
<span style="color:#AA5500">Get:40 http://deb.debian.org/debian bookworm/main arm64 samba-dsdb-modules arm64 2:4.17.12+dfsg-0+deb12u2 [298 kB]</span>
<span style="color:#AA5500">Get:41 http://deb.debian.org/debian bookworm/main arm64 samba-vfs-modules arm64 2:4.17.12+dfsg-0+deb12u2 [406 kB]</span>
<span style="color:#AA5500">Get:42 http://deb.debian.org/debian bookworm/main arm64 smbclient arm64 2:4.17.12+dfsg-0+deb12u2 [432 kB]</span>
<span style="color:#AA5500">Preconfiguring packages ...</span>
<span style="color:#AA5500">Fetched 15.8 MB in 2s (10000 kB/s)</span>
<span style="color:#AA5500">Selecting previously unselected package python3-dnspython.</span>
<span style="color:#AA5500">(Reading database ... 95195 files and directories currently installed.)</span>
<span style="color:#AA5500">Preparing to unpack .../00-python3-dnspython_2.3.0-1_all.deb ...</span>
<span style="color:#AA5500">Unpacking python3-dnspython (2.3.0-1) ...</span>
<span style="color:#AA5500">Selecting previously unselected package liblmdb0:arm64.</span>
<span style="color:#AA5500">Preparing to unpack .../01-liblmdb0_0.9.24-1_arm64.deb ...</span>
<span style="color:#AA5500">Unpacking liblmdb0:arm64 (0.9.24-1) ...</span>
<span style="color:#AA5500">Selecting previously unselected package libtdb1:arm64.</span>
<span style="color:#AA5500">Preparing to unpack .../02-libtdb1_1.4.8-2_arm64.deb ...</span>
<span style="color:#AA5500">Unpacking libtdb1:arm64 (1.4.8-2) ...</span>
<span style="color:#AA5500">Selecting previously unselected package libtevent0:arm64.</span>
<span style="color:#AA5500">Preparing to unpack .../03-libtevent0_0.14.1-1_arm64.deb ...</span>
<span style="color:#AA5500">Unpacking libtevent0:arm64 (0.14.1-1) ...</span>
<span style="color:#AA5500">Selecting previously unselected package libldb2:arm64.</span>
<span style="color:#AA5500">Preparing to unpack .../04-libldb2_2%3a2.6.2+samba4.17.12+dfsg-0+deb12u2_arm64.deb ...</span>
<span style="color:#AA5500">Unpacking libldb2:arm64 (2:2.6.2+samba4.17.12+dfsg-0+deb12u2) ...</span>
<span style="color:#AA5500">Selecting previously unselected package python3-ldb.</span>
<span style="color:#AA5500">Preparing to unpack .../05-python3-ldb_2%3a2.6.2+samba4.17.12+dfsg-0+deb12u2_arm64.deb ...</span>
<span style="color:#AA5500">Unpacking python3-ldb (2:2.6.2+samba4.17.12+dfsg-0+deb12u2) ...</span>
<span style="color:#AA5500">Selecting previously unselected package python3-tdb.</span>
<span style="color:#AA5500">Preparing to unpack .../06-python3-tdb_1.4.8-2_arm64.deb ...</span>
<span style="color:#AA5500">Unpacking python3-tdb (1.4.8-2) ...</span>
<span style="color:#AA5500">Selecting previously unselected package samba-libs:arm64.</span>
<span style="color:#AA5500">Preparing to unpack .../07-samba-libs_2%3a4.17.12+dfsg-0+deb12u2_arm64.deb ...</span>
<span style="color:#AA5500">Unpacking samba-libs:arm64 (2:4.17.12+dfsg-0+deb12u2) ...</span>
<span style="color:#AA5500">Selecting previously unselected package python3-talloc:arm64.</span>
<span style="color:#AA5500">Preparing to unpack .../08-python3-talloc_2.4.0-f2_arm64.deb ...</span>
<span style="color:#AA5500">Unpacking python3-talloc:arm64 (2.4.0-f2) ...</span>
<span style="color:#AA5500">Selecting previously unselected package python3-samba.</span>
<span style="color:#AA5500">Preparing to unpack .../09-python3-samba_2%3a4.17.12+dfsg-0+deb12u2_arm64.deb ...</span>
<span style="color:#AA5500">Unpacking python3-samba (2:4.17.12+dfsg-0+deb12u2) ...</span>
<span style="color:#AA5500">Selecting previously unselected package samba-common.</span>
<span style="color:#AA5500">Preparing to unpack .../10-samba-common_2%3a4.17.12+dfsg-0+deb12u2_all.deb ...</span>
<span style="color:#AA5500">Unpacking samba-common (2:4.17.12+dfsg-0+deb12u2) ...</span>
<span style="color:#AA5500">Selecting previously unselected package samba-common-bin.</span>
<span style="color:#AA5500">Preparing to unpack .../11-samba-common-bin_2%3a4.17.12+dfsg-0+deb12u2_arm64.deb ...</span>
<span style="color:#AA5500">Unpacking samba-common-bin (2:4.17.12+dfsg-0+deb12u2) ...</span>
<span style="color:#AA5500">Selecting previously unselected package tdb-tools.</span>
<span style="color:#AA5500">Preparing to unpack .../12-tdb-tools_1.4.8-2_arm64.deb ...</span>
<span style="color:#AA5500">Unpacking tdb-tools (1.4.8-2) ...</span>
<span style="color:#AA5500">Selecting previously unselected package samba.</span>
<span style="color:#AA5500">Preparing to unpack .../13-samba_2%3a4.17.12+dfsg-0+deb12u2_arm64.deb ...</span>
<span style="color:#AA5500">Unpacking samba (2:4.17.12+dfsg-0+deb12u2) ...</span>
<span style="color:#AA5500">Selecting previously unselected package attr.</span>
<span style="color:#AA5500">Preparing to unpack .../14-attr_1%3a2.5.1-4_arm64.deb ...</span>
<span style="color:#AA5500">Unpacking attr (1:2.5.1-4) ...</span>
<span style="color:#AA5500">Selecting previously unselected package libarchive13:arm64.</span>
<span style="color:#AA5500">Preparing to unpack .../15-libarchive13_3.6.2-1+deb12u3_arm64.deb ...</span>
<span style="color:#AA5500">Unpacking libarchive13:arm64 (3.6.2-1+deb12u3) ...</span>
<span style="color:#AA5500">Selecting previously unselected package libcephfs2.</span>
<span style="color:#AA5500">Preparing to unpack .../16-libcephfs2_16.2.15+ds-0+deb12u1_arm64.deb ...</span>
<span style="color:#AA5500">Unpacking libcephfs2 (16.2.15+ds-0+deb12u1) ...</span>
<span style="color:#AA5500">Selecting previously unselected package libsmbclient:arm64.</span>
<span style="color:#AA5500">Preparing to unpack .../17-libsmbclient_2%3a4.17.12+dfsg-0+deb12u2_arm64.deb ...</span>
<span style="color:#AA5500">Unpacking libsmbclient:arm64 (2:4.17.12+dfsg-0+deb12u2) ...</span>
<span style="color:#AA5500">Selecting previously unselected package python3-sniffio.</span>
<span style="color:#AA5500">Preparing to unpack .../18-python3-sniffio_1.2.0-1_all.deb ...</span>
<span style="color:#AA5500">Unpacking python3-sniffio (1.2.0-1) ...</span>
<span style="color:#AA5500">Selecting previously unselected package python3-anyio.</span>
<span style="color:#AA5500">Preparing to unpack .../19-python3-anyio_3.6.2-1_all.deb ...</span>
<span style="color:#AA5500">Unpacking python3-anyio (3.6.2-1) ...</span>
<span style="color:#AA5500">Selecting previously unselected package python3-cffi-backend:arm64.</span>
<span style="color:#AA5500">Preparing to unpack .../20-python3-cffi-backend_1.15.1-5+b1_arm64.deb ...</span>
<span style="color:#AA5500">Unpacking python3-cffi-backend:arm64 (1.15.1-5+b1) ...</span>
<span style="color:#AA5500">Selecting previously unselected package python3-colorama.</span>
<span style="color:#AA5500">Preparing to unpack .../21-python3-colorama_0.4.6-2_all.deb ...</span>
<span style="color:#AA5500">Unpacking python3-colorama (0.4.6-2) ...</span>
<span style="color:#AA5500">Selecting previously unselected package python3-click.</span>
<span style="color:#AA5500">Preparing to unpack .../22-python3-click_8.1.3-2_all.deb ...</span>
<span style="color:#AA5500">Unpacking python3-click (8.1.3-2) ...</span>
<span style="color:#AA5500">Selecting previously unselected package python3-cryptography.</span>
<span style="color:#AA5500">Preparing to unpack .../23-python3-cryptography_38.0.4-3+deb12u1_arm64.deb ...</span>
<span style="color:#AA5500">Unpacking python3-cryptography (38.0.4-3+deb12u1) ...</span>
<span style="color:#AA5500">Selecting previously unselected package python3-gpg.</span>
<span style="color:#AA5500">Preparing to unpack .../24-python3-gpg_1.18.0-3+b1_arm64.deb ...</span>
<span style="color:#AA5500">Unpacking python3-gpg (1.18.0-3+b1) ...</span>
<span style="color:#AA5500">Selecting previously unselected package python3-h11.</span>
<span style="color:#AA5500">Preparing to unpack .../25-python3-h11_0.14.0-1.1~deb12u1_all.deb ...</span>
<span style="color:#AA5500">Unpacking python3-h11 (0.14.0-1.1~deb12u1) ...</span>
<span style="color:#AA5500">Selecting previously unselected package python3-hpack.</span>
<span style="color:#AA5500">Preparing to unpack .../26-python3-hpack_4.0.0-2_all.deb ...</span>
<span style="color:#AA5500">Unpacking python3-hpack (4.0.0-2) ...</span>
<span style="color:#AA5500">Selecting previously unselected package python3-hyperframe.</span>
<span style="color:#AA5500">Preparing to unpack .../27-python3-hyperframe_6.0.0-1_all.deb ...</span>
<span style="color:#AA5500">Unpacking python3-hyperframe (6.0.0-1) ...</span>
<span style="color:#AA5500">Selecting previously unselected package python3-h2.</span>
<span style="color:#AA5500">Preparing to unpack .../28-python3-h2_4.1.0-4_all.deb ...</span>
<span style="color:#AA5500">Unpacking python3-h2 (4.1.0-4) ...</span>
<span style="color:#AA5500">Selecting previously unselected package python3-httpcore.</span>
<span style="color:#AA5500">Preparing to unpack .../29-python3-httpcore_0.16.3-1_all.deb ...</span>
<span style="color:#AA5500">Unpacking python3-httpcore (0.16.3-1) ...</span>
<span style="color:#AA5500">Selecting previously unselected package python3-pygments.</span>
<span style="color:#AA5500">Preparing to unpack .../30-python3-pygments_2.14.0+dfsg-1_all.deb ...</span>
<span style="color:#AA5500">Unpacking python3-pygments (2.14.0+dfsg-1) ...</span>
<span style="color:#AA5500">Selecting previously unselected package python3-mdurl.</span>
<span style="color:#AA5500">Preparing to unpack .../31-python3-mdurl_0.1.2-1_all.deb ...</span>
<span style="color:#AA5500">Unpacking python3-mdurl (0.1.2-1) ...</span>
<span style="color:#AA5500">Selecting previously unselected package python3-markdown-it.</span>
<span style="color:#AA5500">Preparing to unpack .../32-python3-markdown-it_2.1.0-5_all.deb ...</span>
<span style="color:#AA5500">Unpacking python3-markdown-it (2.1.0-5) ...</span>
<span style="color:#AA5500">Selecting previously unselected package python3-rich.</span>
<span style="color:#AA5500">Preparing to unpack .../33-python3-rich_13.3.1-1_all.deb ...</span>
<span style="color:#AA5500">Unpacking python3-rich (13.3.1-1) ...</span>
<span style="color:#AA5500">Selecting previously unselected package python3-rfc3986.</span>
<span style="color:#AA5500">Preparing to unpack .../34-python3-rfc3986_1.5.0-2_all.deb ...</span>
<span style="color:#AA5500">Unpacking python3-rfc3986 (1.5.0-2) ...</span>
<span style="color:#AA5500">Selecting previously unselected package python3-httpx.</span>
<span style="color:#AA5500">Preparing to unpack .../35-python3-httpx_0.23.3-1_all.deb ...</span>
<span style="color:#AA5500">Unpacking python3-httpx (0.23.3-1) ...</span>
<span style="color:#AA5500">Selecting previously unselected package python3-markdown.</span>
<span style="color:#AA5500">Preparing to unpack .../36-python3-markdown_3.4.1-2_all.deb ...</span>
<span style="color:#AA5500">Unpacking python3-markdown (3.4.1-2) ...</span>
<span style="color:#AA5500">Selecting previously unselected package python3-requests-toolbelt.</span>
<span style="color:#AA5500">Preparing to unpack .../37-python3-requests-toolbelt_0.10.1-1_all.deb ...</span>
<span style="color:#AA5500">Unpacking python3-requests-toolbelt (0.10.1-1) ...</span>
<span style="color:#AA5500">Selecting previously unselected package samba-ad-provision.</span>
<span style="color:#AA5500">Preparing to unpack .../38-samba-ad-provision_2%3a4.17.12+dfsg-0+deb12u2_all.deb ...</span>
<span style="color:#AA5500">Unpacking samba-ad-provision (2:4.17.12+dfsg-0+deb12u2) ...</span>
<span style="color:#AA5500">Selecting previously unselected package samba-dsdb-modules:arm64.</span>
<span style="color:#AA5500">Preparing to unpack .../39-samba-dsdb-modules_2%3a4.17.12+dfsg-0+deb12u2_arm64.deb ...</span>
<span style="color:#AA5500">Unpacking samba-dsdb-modules:arm64 (2:4.17.12+dfsg-0+deb12u2) ...</span>
<span style="color:#AA5500">Selecting previously unselected package samba-vfs-modules:arm64.</span>
<span style="color:#AA5500">Preparing to unpack .../40-samba-vfs-modules_2%3a4.17.12+dfsg-0+deb12u2_arm64.deb ...</span>
<span style="color:#AA5500">Unpacking samba-vfs-modules:arm64 (2:4.17.12+dfsg-0+deb12u2) ...</span>
<span style="color:#AA5500">Selecting previously unselected package smbclient.</span>
<span style="color:#AA5500">Preparing to unpack .../41-smbclient_2%3a4.17.12+dfsg-0+deb12u2_arm64.deb ...</span>
<span style="color:#AA5500">Unpacking smbclient (2:4.17.12+dfsg-0+deb12u2) ...</span>
<span style="color:#AA5500">Setting up liblmdb0:arm64 (0.9.24-1) ...</span>
<span style="color:#AA5500">Setting up python3-sniffio (1.2.0-1) ...</span>
<span style="color:#AA5500">Setting up python3-requests-toolbelt (0.10.1-1) ...</span>
<span style="color:#AA5500">Setting up python3-anyio (3.6.2-1) ...</span>
<span style="color:#AA5500">Setting up python3-hyperframe (6.0.0-1) ...</span>
<span style="color:#AA5500">Setting up python3-hpack (4.0.0-2) ...</span>
<span style="color:#AA5500">Setting up python3-colorama (0.4.6-2) ...</span>
<span style="color:#AA5500">Setting up libarchive13:arm64 (3.6.2-1+deb12u3) ...</span>
<span style="color:#AA5500">Setting up python3-talloc:arm64 (2.4.0-f2) ...</span>
<span style="color:#AA5500">Setting up attr (1:2.5.1-4) ...</span>
<span style="color:#AA5500">Setting up libtdb1:arm64 (1.4.8-2) ...</span>
<span style="color:#AA5500">Setting up samba-common (2:4.17.12+dfsg-0+deb12u2) ...</span>

<span style="color:#AA5500">Creating config file /etc/samba/smb.conf with new version</span>
<span style="color:#AA5500">Setting up python3-click (8.1.3-2) ...</span>
<span style="color:#AA5500">Setting up libcephfs2 (16.2.15+ds-0+deb12u1) ...</span>
<span style="color:#AA5500">Setting up python3-tdb (1.4.8-2) ...</span>
<span style="color:#AA5500">Setting up python3-pygments (2.14.0+dfsg-1) ...</span>
<span style="color:#AA5500">Setting up python3-rfc3986 (1.5.0-2) ...</span>
<span style="color:#AA5500">Setting up libtevent0:arm64 (0.14.1-1) ...</span>
<span style="color:#AA5500">Setting up python3-gpg (1.18.0-3+b1) ...</span>
<span style="color:#AA5500">Setting up tdb-tools (1.4.8-2) ...</span>
<span style="color:#AA5500">update-alternatives: using /usr/bin/tdbbackup.tdbtools to provide /usr/bin/tdbbackup (tdbbackup) in auto mode</span>
<span style="color:#AA5500">Setting up python3-mdurl (0.1.2-1) ...</span>
<span style="color:#AA5500">Setting up python3-markdown (3.4.1-2) ...</span>
<span style="color:#AA5500">Setting up python3-h11 (0.14.0-1.1~deb12u1) ...</span>
<span style="color:#AA5500">Setting up python3-markdown-it (2.1.0-5) ...</span>
<span style="color:#AA5500">Setting up python3-dnspython (2.3.0-1) ...</span>
<span style="color:#AA5500">Setting up samba-ad-provision (2:4.17.12+dfsg-0+deb12u2) ...</span>
<span style="color:#AA5500">Setting up python3-h2 (4.1.0-4) ...</span>
<span style="color:#AA5500">Setting up libldb2:arm64 (2:2.6.2+samba4.17.12+dfsg-0+deb12u2) ...</span>
<span style="color:#AA5500">Setting up python3-cffi-backend:arm64 (1.15.1-5+b1) ...</span>
<span style="color:#AA5500">Setting up python3-httpcore (0.16.3-1) ...</span>
<span style="color:#AA5500">Setting up python3-rich (13.3.1-1) ...</span>
<span style="color:#AA5500">Setting up samba-libs:arm64 (2:4.17.12+dfsg-0+deb12u2) ...</span>
<span style="color:#AA5500">Setting up python3-httpx (0.23.3-1) ...</span>
<span style="color:#AA5500">Setting up python3-cryptography (38.0.4-3+deb12u1) ...</span>
<span style="color:#AA5500">Setting up python3-ldb (2:2.6.2+samba4.17.12+dfsg-0+deb12u2) ...</span>
<span style="color:#AA5500">Setting up libsmbclient:arm64 (2:4.17.12+dfsg-0+deb12u2) ...</span>
<span style="color:#AA5500">Setting up smbclient (2:4.17.12+dfsg-0+deb12u2) ...</span>
<span style="color:#AA5500">Setting up samba-dsdb-modules:arm64 (2:4.17.12+dfsg-0+deb12u2) ...</span>
<span style="color:#AA5500">Setting up python3-samba (2:4.17.12+dfsg-0+deb12u2) ...</span>
<span style="color:#AA5500">Setting up samba-vfs-modules:arm64 (2:4.17.12+dfsg-0+deb12u2) ...</span>
<span style="color:#AA5500">Setting up samba-common-bin (2:4.17.12+dfsg-0+deb12u2) ...</span>
<span style="color:#AA5500">Setting up samba (2:4.17.12+dfsg-0+deb12u2) ...</span>
<span style="color:#AA5500">Created symlink /etc/systemd/system/multi-user.target.wants/nmbd.service → /lib/systemd/system/nmbd.service.</span>
<span style="color:#AA5500">Created symlink /etc/systemd/system/multi-user.target.wants/samba-ad-dc.service → /lib/systemd/system/samba-ad-dc.service.</span>
<span style="color:#AA5500">Created symlink /etc/systemd/system/multi-user.target.wants/smbd.service → /lib/systemd/system/smbd.service.</span>
<span style="color:#AA5500">Processing triggers for man-db (2.11.2-2) ...</span>
<span style="color:#AA5500">Processing triggers for libc-bin (2.36-9+rpt2+deb12u12) ...</span>

Sonntag 21 September 2025  00:12:00 +0200 (0:00:17.120)       0:00:20.759 ***** 

TASK [vladgh.samba.server : Install Samba VFS extensions packages] ************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/collections/ansible_collections/vladgh/samba/roles/server/tasks/main.yml:19</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;cache_update_time&quot;: 1758331880,</span>
<span style="color:#00AA00">    &quot;cache_updated&quot;: false,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  00:12:02 +0200 (0:00:01.441)       0:00:22.200 ***** 

TASK [vladgh.samba.server : Register Samba version] ***************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/collections/ansible_collections/vladgh/samba/roles/server/tasks/main.yml:26</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;cmd&quot;: &quot;set -o nounset -o pipefail -o errexit &amp;&amp; smbd --version | sed &apos;s/Version //&apos;\n&quot;,</span>
<span style="color:#00AA00">    &quot;delta&quot;: &quot;0:00:00.046413&quot;,</span>
<span style="color:#00AA00">    &quot;end&quot;: &quot;2025-09-21 00:12:02.758409&quot;,</span>
<span style="color:#00AA00">    &quot;rc&quot;: 0,</span>
<span style="color:#00AA00">    &quot;start&quot;: &quot;2025-09-21 00:12:02.711996&quot;</span>
<span style="color:#00AA00">}</span>

<span style="color:#00AA00">STDOUT:</span>

<span style="color:#00AA00">4.17.12-Debian</span>
Sonntag 21 September 2025  00:12:02 +0200 (0:00:00.642)       0:00:22.842 ***** 
Sonntag 21 September 2025  00:12:02 +0200 (0:00:00.066)       0:00:22.908 ***** 
Sonntag 21 September 2025  00:12:02 +0200 (0:00:00.034)       0:00:22.942 ***** 
Sonntag 21 September 2025  00:12:02 +0200 (0:00:00.053)       0:00:22.996 ***** 
Sonntag 21 September 2025  00:12:03 +0200 (0:00:00.038)       0:00:23.034 ***** 
<span style="color:#0000AA">Notification for handler Restart SMB service has been saved.</span>
<span style="color:#0000AA">Notification for handler Restart NMB service has been saved.</span>

TASK [vladgh.samba.server : Samba configuration] ******************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/collections/ansible_collections/vladgh/samba/roles/server/tasks/main.yml:80</b></span>
<span style="color:#AA5500">changed: [ansible-nas] =&gt; {</span>
<span style="color:#AA5500">    &quot;changed&quot;: true,</span>
<span style="color:#AA5500">    &quot;checksum&quot;: &quot;353157b186814dd24425adcce53a023a2361a2e5&quot;,</span>
<span style="color:#AA5500">    &quot;dest&quot;: &quot;/etc/samba/smb.conf&quot;,</span>
<span style="color:#AA5500">    &quot;gid&quot;: 0,</span>
<span style="color:#AA5500">    &quot;group&quot;: &quot;root&quot;,</span>
<span style="color:#AA5500">    &quot;md5sum&quot;: &quot;48cb08a75593383fe7b378763fce4309&quot;,</span>
<span style="color:#AA5500">    &quot;mode&quot;: &quot;0644&quot;,</span>
<span style="color:#AA5500">    &quot;owner&quot;: &quot;root&quot;,</span>
<span style="color:#AA5500">    &quot;size&quot;: 509,</span>
<span style="color:#AA5500">    &quot;src&quot;: &quot;/home/dietmar/.ansible/tmp/ansible-tmp-1758406323.0547354-84716-26934232745795/source&quot;,</span>
<span style="color:#AA5500">    &quot;state&quot;: &quot;file&quot;,</span>
<span style="color:#AA5500">    &quot;uid&quot;: 0</span>
<span style="color:#AA5500">}</span>
Sonntag 21 September 2025  00:12:04 +0200 (0:00:01.291)       0:00:24.325 ***** 
Sonntag 21 September 2025  00:12:04 +0200 (0:00:00.042)       0:00:24.368 ***** 
Sonntag 21 September 2025  00:12:04 +0200 (0:00:00.040)       0:00:24.409 ***** 
Sonntag 21 September 2025  00:12:04 +0200 (0:00:00.045)       0:00:24.454 ***** 
Sonntag 21 September 2025  00:12:04 +0200 (0:00:00.039)       0:00:24.494 ***** 

TASK [vladgh.samba.server : Start SMB service] ********************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/collections/ansible_collections/vladgh/samba/roles/server/tasks/main.yml:141</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;enabled&quot;: true,</span>
<span style="color:#00AA00">    &quot;name&quot;: &quot;smbd&quot;,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;started&quot;,</span>
<span style="color:#00AA00">    &quot;status&quot;: {</span>
<span style="color:#00AA00">        &quot;ActiveEnterTimestamp&quot;: &quot;Sun 2025-09-21 00:11:59 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;ActiveEnterTimestampMonotonic&quot;: &quot;678293390975&quot;,</span>
<span style="color:#00AA00">        &quot;ActiveExitTimestampMonotonic&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;ActiveState&quot;: &quot;active&quot;,</span>
<span style="color:#00AA00">        &quot;After&quot;: &quot;network-online.target system.slice basic.target nmbd.service sysinit.target network.target winbind.service systemd-journald.socket&quot;,</span>
<span style="color:#00AA00">        &quot;AllowIsolate&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;AssertResult&quot;: &quot;yes&quot;,</span>
<span style="color:#00AA00">        &quot;AssertTimestamp&quot;: &quot;Sun 2025-09-21 00:11:59 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;AssertTimestampMonotonic&quot;: &quot;678293262530&quot;,</span>
<span style="color:#00AA00">        &quot;Before&quot;: &quot;shutdown.target multi-user.target&quot;,</span>
<span style="color:#00AA00">        &quot;BlockIOAccounting&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;BlockIOWeight&quot;: &quot;[not set]&quot;,</span>
<span style="color:#00AA00">        &quot;CPUAccounting&quot;: &quot;yes&quot;,</span>
<span style="color:#00AA00">        &quot;CPUAffinityFromNUMA&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;CPUQuotaPerSecUSec&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;CPUQuotaPeriodUSec&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;CPUSchedulingPolicy&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;CPUSchedulingPriority&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;CPUSchedulingResetOnFork&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;CPUShares&quot;: &quot;[not set]&quot;,</span>
<span style="color:#00AA00">        &quot;CPUUsageNSec&quot;: &quot;79073000&quot;,</span>
<span style="color:#00AA00">        &quot;CPUWeight&quot;: &quot;[not set]&quot;,</span>
<span style="color:#00AA00">        &quot;CacheDirectoryMode&quot;: &quot;0755&quot;,</span>
<span style="color:#00AA00">        &quot;CanFreeze&quot;: &quot;yes&quot;,</span>
<span style="color:#00AA00">        &quot;CanIsolate&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;CanReload&quot;: &quot;yes&quot;,</span>
<span style="color:#00AA00">        &quot;CanStart&quot;: &quot;yes&quot;,</span>
<span style="color:#00AA00">        &quot;CanStop&quot;: &quot;yes&quot;,</span>
<span style="color:#00AA00">        &quot;CapabilityBoundingSet&quot;: &quot;cap_chown cap_dac_override cap_dac_read_search cap_fowner cap_fsetid cap_kill cap_setgid cap_setuid cap_setpcap cap_linux_immutable cap_net_bind_service cap_net_broadcast cap_net_admin cap_net_raw cap_ipc_lock cap_ipc_owner cap_sys_module cap_sys_rawio cap_sys_chroot cap_sys_ptrace cap_sys_pacct cap_sys_admin cap_sys_boot cap_sys_nice cap_sys_resource cap_sys_time cap_sys_tty_config cap_mknod cap_lease cap_audit_write cap_audit_control cap_setfcap cap_mac_override cap_mac_admin cap_syslog cap_wake_alarm cap_block_suspend cap_audit_read cap_perfmon cap_bpf cap_checkpoint_restore&quot;,</span>
<span style="color:#00AA00">        &quot;CleanResult&quot;: &quot;success&quot;,</span>
<span style="color:#00AA00">        &quot;CollectMode&quot;: &quot;inactive&quot;,</span>
<span style="color:#00AA00">        &quot;ConditionResult&quot;: &quot;yes&quot;,</span>
<span style="color:#00AA00">        &quot;ConditionTimestamp&quot;: &quot;Sun 2025-09-21 00:11:59 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;ConditionTimestampMonotonic&quot;: &quot;678293262528&quot;,</span>
<span style="color:#00AA00">        &quot;ConfigurationDirectoryMode&quot;: &quot;0755&quot;,</span>
<span style="color:#00AA00">        &quot;Conflicts&quot;: &quot;shutdown.target&quot;,</span>
<span style="color:#00AA00">        &quot;ControlGroup&quot;: &quot;/system.slice/smbd.service&quot;,</span>
<span style="color:#00AA00">        &quot;ControlGroupId&quot;: &quot;46290&quot;,</span>
<span style="color:#00AA00">        &quot;ControlPID&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;CoredumpFilter&quot;: &quot;0x33&quot;,</span>
<span style="color:#00AA00">        &quot;DefaultDependencies&quot;: &quot;yes&quot;,</span>
<span style="color:#00AA00">        &quot;DefaultMemoryLow&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;DefaultMemoryMin&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;Delegate&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;Description&quot;: &quot;Samba SMB Daemon&quot;,</span>
<span style="color:#00AA00">        &quot;DevicePolicy&quot;: &quot;auto&quot;,</span>
<span style="color:#00AA00">        &quot;Documentation&quot;: &quot;\&quot;man:smbd(8)\&quot; \&quot;man:samba(7)\&quot; \&quot;man:smb.conf(5)\&quot;&quot;,</span>
<span style="color:#00AA00">        &quot;DynamicUser&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;EnvironmentFiles&quot;: &quot;/etc/default/samba (ignore_errors=yes)&quot;,</span>
<span style="color:#00AA00">        &quot;ExecCondition&quot;: &quot;{ path=/usr/share/samba/is-configured ; argv[]=/usr/share/samba/is-configured smb ; ignore_errors=no ; start_time=[Sun 2025-09-21 00:11:59 CEST] ; stop_time=[Sun 2025-09-21 00:11:59 CEST] ; pid=1369428 ; code=exited ; status=0 }&quot;,</span>
<span style="color:#00AA00">        &quot;ExecConditionEx&quot;: &quot;{ path=/usr/share/samba/is-configured ; argv[]=/usr/share/samba/is-configured smb ; flags= ; start_time=[Sun 2025-09-21 00:11:59 CEST] ; stop_time=[Sun 2025-09-21 00:11:59 CEST] ; pid=1369428 ; code=exited ; status=0 }&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainCode&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainExitTimestampMonotonic&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainPID&quot;: &quot;1369431&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainStartTimestamp&quot;: &quot;Sun 2025-09-21 00:11:59 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainStartTimestampMonotonic&quot;: &quot;678293322691&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainStatus&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;ExecReload&quot;: &quot;{ path=/bin/kill ; argv[]=/bin/kill -HUP $MAINPID ; ignore_errors=no ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }&quot;,</span>
<span style="color:#00AA00">        &quot;ExecReloadEx&quot;: &quot;{ path=/bin/kill ; argv[]=/bin/kill -HUP $MAINPID ; flags= ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }&quot;,</span>
<span style="color:#00AA00">        &quot;ExecStart&quot;: &quot;{ path=/usr/sbin/smbd ; argv[]=/usr/sbin/smbd --foreground --no-process-group $SMBDOPTIONS ; ignore_errors=no ; start_time=[Sun 2025-09-21 00:11:59 CEST] ; stop_time=[n/a] ; pid=1369431 ; code=(null) ; status=0/0 }&quot;,</span>
<span style="color:#00AA00">        &quot;ExecStartEx&quot;: &quot;{ path=/usr/sbin/smbd ; argv[]=/usr/sbin/smbd --foreground --no-process-group $SMBDOPTIONS ; flags= ; start_time=[Sun 2025-09-21 00:11:59 CEST] ; stop_time=[n/a] ; pid=1369431 ; code=(null) ; status=0/0 }&quot;,</span>
<span style="color:#00AA00">        &quot;ExecStartPre&quot;: &quot;{ path=/usr/share/samba/update-apparmor-samba-profile ; argv[]=/usr/share/samba/update-apparmor-samba-profile ; ignore_errors=no ; start_time=[Sun 2025-09-21 00:11:59 CEST] ; stop_time=[Sun 2025-09-21 00:11:59 CEST] ; pid=1369430 ; code=exited ; status=0 }&quot;,</span>
<span style="color:#00AA00">        &quot;ExecStartPreEx&quot;: &quot;{ path=/usr/share/samba/update-apparmor-samba-profile ; argv[]=/usr/share/samba/update-apparmor-samba-profile ; flags= ; start_time=[Sun 2025-09-21 00:11:59 CEST] ; stop_time=[Sun 2025-09-21 00:11:59 CEST] ; pid=1369430 ; code=exited ; status=0 }&quot;,</span>
<span style="color:#00AA00">        &quot;ExitType&quot;: &quot;main&quot;,</span>
<span style="color:#00AA00">        &quot;FailureAction&quot;: &quot;none&quot;,</span>
<span style="color:#00AA00">        &quot;FileDescriptorStoreMax&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;FinalKillSignal&quot;: &quot;9&quot;,</span>
<span style="color:#00AA00">        &quot;FragmentPath&quot;: &quot;/lib/systemd/system/smbd.service&quot;,</span>
<span style="color:#00AA00">        &quot;FreezerState&quot;: &quot;running&quot;,</span>
<span style="color:#00AA00">        &quot;GID&quot;: &quot;[not set]&quot;,</span>
<span style="color:#00AA00">        &quot;GuessMainPID&quot;: &quot;yes&quot;,</span>
<span style="color:#00AA00">        &quot;IOAccounting&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;IOReadBytes&quot;: &quot;18446744073709551615&quot;,</span>
<span style="color:#00AA00">        &quot;IOReadOperations&quot;: &quot;18446744073709551615&quot;,</span>
<span style="color:#00AA00">        &quot;IOSchedulingClass&quot;: &quot;2&quot;,</span>
<span style="color:#00AA00">        &quot;IOSchedulingPriority&quot;: &quot;4&quot;,</span>
<span style="color:#00AA00">        &quot;IOWeight&quot;: &quot;[not set]&quot;,</span>
<span style="color:#00AA00">        &quot;IOWriteBytes&quot;: &quot;18446744073709551615&quot;,</span>
<span style="color:#00AA00">        &quot;IOWriteOperations&quot;: &quot;18446744073709551615&quot;,</span>
<span style="color:#00AA00">        &quot;IPAccounting&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;IPEgressBytes&quot;: &quot;[no data]&quot;,</span>
<span style="color:#00AA00">        &quot;IPEgressPackets&quot;: &quot;[no data]&quot;,</span>
<span style="color:#00AA00">        &quot;IPIngressBytes&quot;: &quot;[no data]&quot;,</span>
<span style="color:#00AA00">        &quot;IPIngressPackets&quot;: &quot;[no data]&quot;,</span>
<span style="color:#00AA00">        &quot;Id&quot;: &quot;smbd.service&quot;,</span>
<span style="color:#00AA00">        &quot;IgnoreOnIsolate&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;IgnoreSIGPIPE&quot;: &quot;yes&quot;,</span>
<span style="color:#00AA00">        &quot;InactiveEnterTimestampMonotonic&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;InactiveExitTimestamp&quot;: &quot;Sun 2025-09-21 00:11:59 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;InactiveExitTimestampMonotonic&quot;: &quot;678293263998&quot;,</span>
<span style="color:#00AA00">        &quot;InvocationID&quot;: &quot;3f83abb020524418881b0a57a5fb672a&quot;,</span>
<span style="color:#00AA00">        &quot;JobRunningTimeoutUSec&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;JobTimeoutAction&quot;: &quot;none&quot;,</span>
<span style="color:#00AA00">        &quot;JobTimeoutUSec&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;KeyringMode&quot;: &quot;private&quot;,</span>
<span style="color:#00AA00">        &quot;KillMode&quot;: &quot;control-group&quot;,</span>
<span style="color:#00AA00">        &quot;KillSignal&quot;: &quot;15&quot;,</span>
<span style="color:#00AA00">        &quot;LimitAS&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;LimitASSoft&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;LimitCORE&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;LimitCORESoft&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;LimitCPU&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;LimitCPUSoft&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;LimitDATA&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;LimitDATASoft&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;LimitFSIZE&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;LimitFSIZESoft&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;LimitLOCKS&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;LimitLOCKSSoft&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;LimitMEMLOCK&quot;: &quot;8388608&quot;,</span>
<span style="color:#00AA00">        &quot;LimitMEMLOCKSoft&quot;: &quot;8388608&quot;,</span>
<span style="color:#00AA00">        &quot;LimitMSGQUEUE&quot;: &quot;819200&quot;,</span>
<span style="color:#00AA00">        &quot;LimitMSGQUEUESoft&quot;: &quot;819200&quot;,</span>
<span style="color:#00AA00">        &quot;LimitNICE&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;LimitNICESoft&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;LimitNOFILE&quot;: &quot;16384&quot;,</span>
<span style="color:#00AA00">        &quot;LimitNOFILESoft&quot;: &quot;16384&quot;,</span>
<span style="color:#00AA00">        &quot;LimitNPROC&quot;: &quot;31916&quot;,</span>
<span style="color:#00AA00">        &quot;LimitNPROCSoft&quot;: &quot;31916&quot;,</span>
<span style="color:#00AA00">        &quot;LimitRSS&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;LimitRSSSoft&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;LimitRTPRIO&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;LimitRTPRIOSoft&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;LimitRTTIME&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;LimitRTTIMESoft&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;LimitSIGPENDING&quot;: &quot;31916&quot;,</span>
<span style="color:#00AA00">        &quot;LimitSIGPENDINGSoft&quot;: &quot;31916&quot;,</span>
<span style="color:#00AA00">        &quot;LimitSTACK&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;LimitSTACKSoft&quot;: &quot;8388608&quot;,</span>
<span style="color:#00AA00">        &quot;LoadState&quot;: &quot;loaded&quot;,</span>
<span style="color:#00AA00">        &quot;LockPersonality&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;LogLevelMax&quot;: &quot;-1&quot;,</span>
<span style="color:#00AA00">        &quot;LogRateLimitBurst&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;LogRateLimitIntervalUSec&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;LogsDirectoryMode&quot;: &quot;0755&quot;,</span>
<span style="color:#00AA00">        &quot;MainPID&quot;: &quot;1369431&quot;,</span>
<span style="color:#00AA00">        &quot;ManagedOOMMemoryPressure&quot;: &quot;auto&quot;,</span>
<span style="color:#00AA00">        &quot;ManagedOOMMemoryPressureLimit&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;ManagedOOMPreference&quot;: &quot;none&quot;,</span>
<span style="color:#00AA00">        &quot;ManagedOOMSwap&quot;: &quot;auto&quot;,</span>
<span style="color:#00AA00">        &quot;MemoryAccounting&quot;: &quot;yes&quot;,</span>
<span style="color:#00AA00">        &quot;MemoryAvailable&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;MemoryCurrent&quot;: &quot;[not set]&quot;,</span>
<span style="color:#00AA00">        &quot;MemoryDenyWriteExecute&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;MemoryHigh&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;MemoryLimit&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;MemoryLow&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;MemoryMax&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;MemoryMin&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;MemorySwapMax&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;MountAPIVFS&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;NFileDescriptorStore&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;NRestarts&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;NUMAPolicy&quot;: &quot;n/a&quot;,</span>
<span style="color:#00AA00">        &quot;Names&quot;: &quot;smbd.service smb.service&quot;,</span>
<span style="color:#00AA00">        &quot;NeedDaemonReload&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;Nice&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;NoNewPrivileges&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;NonBlocking&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;NotifyAccess&quot;: &quot;main&quot;,</span>
<span style="color:#00AA00">        &quot;OOMPolicy&quot;: &quot;stop&quot;,</span>
<span style="color:#00AA00">        &quot;OOMScoreAdjust&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;OnFailureJobMode&quot;: &quot;replace&quot;,</span>
<span style="color:#00AA00">        &quot;OnSuccessJobMode&quot;: &quot;fail&quot;,</span>
<span style="color:#00AA00">        &quot;PIDFile&quot;: &quot;/run/samba/smbd.pid&quot;,</span>
<span style="color:#00AA00">        &quot;Perpetual&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;PrivateDevices&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;PrivateIPC&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;PrivateMounts&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;PrivateNetwork&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;PrivateTmp&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;PrivateUsers&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;ProcSubset&quot;: &quot;all&quot;,</span>
<span style="color:#00AA00">        &quot;ProtectClock&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;ProtectControlGroups&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;ProtectHome&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;ProtectHostname&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;ProtectKernelLogs&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;ProtectKernelModules&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;ProtectKernelTunables&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;ProtectProc&quot;: &quot;default&quot;,</span>
<span style="color:#00AA00">        &quot;ProtectSystem&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;RefuseManualStart&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;RefuseManualStop&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;ReloadResult&quot;: &quot;success&quot;,</span>
<span style="color:#00AA00">        &quot;RemainAfterExit&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;RemoveIPC&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;Requires&quot;: &quot;sysinit.target system.slice&quot;,</span>
<span style="color:#00AA00">        &quot;Restart&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;RestartKillSignal&quot;: &quot;15&quot;,</span>
<span style="color:#00AA00">        &quot;RestartUSec&quot;: &quot;100ms&quot;,</span>
<span style="color:#00AA00">        &quot;RestrictNamespaces&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;RestrictRealtime&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;RestrictSUIDSGID&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;Result&quot;: &quot;success&quot;,</span>
<span style="color:#00AA00">        &quot;RootDirectoryStartOnly&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;RuntimeDirectoryMode&quot;: &quot;0755&quot;,</span>
<span style="color:#00AA00">        &quot;RuntimeDirectoryPreserve&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;RuntimeMaxUSec&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;RuntimeRandomizedExtraUSec&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;SameProcessGroup&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;SecureBits&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;SendSIGHUP&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;SendSIGKILL&quot;: &quot;yes&quot;,</span>
<span style="color:#00AA00">        &quot;Slice&quot;: &quot;system.slice&quot;,</span>
<span style="color:#00AA00">        &quot;StandardError&quot;: &quot;inherit&quot;,</span>
<span style="color:#00AA00">        &quot;StandardInput&quot;: &quot;null&quot;,</span>
<span style="color:#00AA00">        &quot;StandardOutput&quot;: &quot;journal&quot;,</span>
<span style="color:#00AA00">        &quot;StartLimitAction&quot;: &quot;none&quot;,</span>
<span style="color:#00AA00">        &quot;StartLimitBurst&quot;: &quot;5&quot;,</span>
<span style="color:#00AA00">        &quot;StartLimitIntervalUSec&quot;: &quot;10s&quot;,</span>
<span style="color:#00AA00">        &quot;StartupBlockIOWeight&quot;: &quot;[not set]&quot;,</span>
<span style="color:#00AA00">        &quot;StartupCPUShares&quot;: &quot;[not set]&quot;,</span>
<span style="color:#00AA00">        &quot;StartupCPUWeight&quot;: &quot;[not set]&quot;,</span>
<span style="color:#00AA00">        &quot;StartupIOWeight&quot;: &quot;[not set]&quot;,</span>
<span style="color:#00AA00">        &quot;StateChangeTimestamp&quot;: &quot;Sun 2025-09-21 00:11:59 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;StateChangeTimestampMonotonic&quot;: &quot;678293390975&quot;,</span>
<span style="color:#00AA00">        &quot;StateDirectoryMode&quot;: &quot;0755&quot;,</span>
<span style="color:#00AA00">        &quot;StatusErrno&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;StatusText&quot;: &quot;smbd: ready to serve connections...&quot;,</span>
<span style="color:#00AA00">        &quot;StopWhenUnneeded&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;SubState&quot;: &quot;running&quot;,</span>
<span style="color:#00AA00">        &quot;SuccessAction&quot;: &quot;none&quot;,</span>
<span style="color:#00AA00">        &quot;SyslogFacility&quot;: &quot;3&quot;,</span>
<span style="color:#00AA00">        &quot;SyslogLevel&quot;: &quot;6&quot;,</span>
<span style="color:#00AA00">        &quot;SyslogLevelPrefix&quot;: &quot;yes&quot;,</span>
<span style="color:#00AA00">        &quot;SyslogPriority&quot;: &quot;30&quot;,</span>
<span style="color:#00AA00">        &quot;SystemCallErrorNumber&quot;: &quot;2147483646&quot;,</span>
<span style="color:#00AA00">        &quot;TTYReset&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;TTYVHangup&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;TTYVTDisallocate&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;TasksAccounting&quot;: &quot;yes&quot;,</span>
<span style="color:#00AA00">        &quot;TasksCurrent&quot;: &quot;3&quot;,</span>
<span style="color:#00AA00">        &quot;TasksMax&quot;: &quot;9574&quot;,</span>
<span style="color:#00AA00">        &quot;TimeoutAbortUSec&quot;: &quot;1min 30s&quot;,</span>
<span style="color:#00AA00">        &quot;TimeoutCleanUSec&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;TimeoutStartFailureMode&quot;: &quot;terminate&quot;,</span>
<span style="color:#00AA00">        &quot;TimeoutStartUSec&quot;: &quot;1min 30s&quot;,</span>
<span style="color:#00AA00">        &quot;TimeoutStopFailureMode&quot;: &quot;terminate&quot;,</span>
<span style="color:#00AA00">        &quot;TimeoutStopUSec&quot;: &quot;1min 30s&quot;,</span>
<span style="color:#00AA00">        &quot;TimerSlackNSec&quot;: &quot;50000&quot;,</span>
<span style="color:#00AA00">        &quot;Transient&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;Type&quot;: &quot;notify&quot;,</span>
<span style="color:#00AA00">        &quot;UID&quot;: &quot;[not set]&quot;,</span>
<span style="color:#00AA00">        &quot;UMask&quot;: &quot;0022&quot;,</span>
<span style="color:#00AA00">        &quot;UnitFilePreset&quot;: &quot;enabled&quot;,</span>
<span style="color:#00AA00">        &quot;UnitFileState&quot;: &quot;enabled&quot;,</span>
<span style="color:#00AA00">        &quot;UtmpMode&quot;: &quot;init&quot;,</span>
<span style="color:#00AA00">        &quot;WantedBy&quot;: &quot;multi-user.target&quot;,</span>
<span style="color:#00AA00">        &quot;Wants&quot;: &quot;network-online.target&quot;,</span>
<span style="color:#00AA00">        &quot;WatchdogSignal&quot;: &quot;6&quot;,</span>
<span style="color:#00AA00">        &quot;WatchdogTimestampMonotonic&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;WatchdogUSec&quot;: &quot;0&quot;</span>
<span style="color:#00AA00">    }</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  00:12:05 +0200 (0:00:01.050)       0:00:25.544 ***** 

TASK [vladgh.samba.server : Start NMB service] ********************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/collections/ansible_collections/vladgh/samba/roles/server/tasks/main.yml:148</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;enabled&quot;: true,</span>
<span style="color:#00AA00">    &quot;name&quot;: &quot;nmbd&quot;,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;started&quot;,</span>
<span style="color:#00AA00">    &quot;status&quot;: {</span>
<span style="color:#00AA00">        &quot;ActiveEnterTimestamp&quot;: &quot;Sun 2025-09-21 00:11:59 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;ActiveEnterTimestampMonotonic&quot;: &quot;678293262184&quot;,</span>
<span style="color:#00AA00">        &quot;ActiveExitTimestampMonotonic&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;ActiveState&quot;: &quot;active&quot;,</span>
<span style="color:#00AA00">        &quot;After&quot;: &quot;sysinit.target network.target basic.target network-online.target systemd-journald.socket system.slice&quot;,</span>
<span style="color:#00AA00">        &quot;AllowIsolate&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;AssertResult&quot;: &quot;yes&quot;,</span>
<span style="color:#00AA00">        &quot;AssertTimestamp&quot;: &quot;Sun 2025-09-21 00:11:58 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;AssertTimestampMonotonic&quot;: &quot;678293122472&quot;,</span>
<span style="color:#00AA00">        &quot;Before&quot;: &quot;multi-user.target smbd.service shutdown.target&quot;,</span>
<span style="color:#00AA00">        &quot;BlockIOAccounting&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;BlockIOWeight&quot;: &quot;[not set]&quot;,</span>
<span style="color:#00AA00">        &quot;CPUAccounting&quot;: &quot;yes&quot;,</span>
<span style="color:#00AA00">        &quot;CPUAffinityFromNUMA&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;CPUQuotaPerSecUSec&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;CPUQuotaPeriodUSec&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;CPUSchedulingPolicy&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;CPUSchedulingPriority&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;CPUSchedulingResetOnFork&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;CPUShares&quot;: &quot;[not set]&quot;,</span>
<span style="color:#00AA00">        &quot;CPUUsageNSec&quot;: &quot;82224000&quot;,</span>
<span style="color:#00AA00">        &quot;CPUWeight&quot;: &quot;[not set]&quot;,</span>
<span style="color:#00AA00">        &quot;CacheDirectoryMode&quot;: &quot;0755&quot;,</span>
<span style="color:#00AA00">        &quot;CanFreeze&quot;: &quot;yes&quot;,</span>
<span style="color:#00AA00">        &quot;CanIsolate&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;CanReload&quot;: &quot;yes&quot;,</span>
<span style="color:#00AA00">        &quot;CanStart&quot;: &quot;yes&quot;,</span>
<span style="color:#00AA00">        &quot;CanStop&quot;: &quot;yes&quot;,</span>
<span style="color:#00AA00">        &quot;CapabilityBoundingSet&quot;: &quot;cap_chown cap_dac_override cap_dac_read_search cap_fowner cap_fsetid cap_kill cap_setgid cap_setuid cap_setpcap cap_linux_immutable cap_net_bind_service cap_net_broadcast cap_net_admin cap_net_raw cap_ipc_lock cap_ipc_owner cap_sys_module cap_sys_rawio cap_sys_chroot cap_sys_ptrace cap_sys_pacct cap_sys_admin cap_sys_boot cap_sys_nice cap_sys_resource cap_sys_time cap_sys_tty_config cap_mknod cap_lease cap_audit_write cap_audit_control cap_setfcap cap_mac_override cap_mac_admin cap_syslog cap_wake_alarm cap_block_suspend cap_audit_read cap_perfmon cap_bpf cap_checkpoint_restore&quot;,</span>
<span style="color:#00AA00">        &quot;CleanResult&quot;: &quot;success&quot;,</span>
<span style="color:#00AA00">        &quot;CollectMode&quot;: &quot;inactive&quot;,</span>
<span style="color:#00AA00">        &quot;ConditionResult&quot;: &quot;yes&quot;,</span>
<span style="color:#00AA00">        &quot;ConditionTimestamp&quot;: &quot;Sun 2025-09-21 00:11:58 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;ConditionTimestampMonotonic&quot;: &quot;678293122470&quot;,</span>
<span style="color:#00AA00">        &quot;ConfigurationDirectoryMode&quot;: &quot;0755&quot;,</span>
<span style="color:#00AA00">        &quot;Conflicts&quot;: &quot;shutdown.target&quot;,</span>
<span style="color:#00AA00">        &quot;ControlGroup&quot;: &quot;/system.slice/nmbd.service&quot;,</span>
<span style="color:#00AA00">        &quot;ControlGroupId&quot;: &quot;46252&quot;,</span>
<span style="color:#00AA00">        &quot;ControlPID&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;CoredumpFilter&quot;: &quot;0x33&quot;,</span>
<span style="color:#00AA00">        &quot;DefaultDependencies&quot;: &quot;yes&quot;,</span>
<span style="color:#00AA00">        &quot;DefaultMemoryLow&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;DefaultMemoryMin&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;Delegate&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;Description&quot;: &quot;Samba NMB Daemon&quot;,</span>
<span style="color:#00AA00">        &quot;DevicePolicy&quot;: &quot;auto&quot;,</span>
<span style="color:#00AA00">        &quot;Documentation&quot;: &quot;\&quot;man:nmbd(8)\&quot; \&quot;man:samba(7)\&quot; \&quot;man:smb.conf(5)\&quot;&quot;,</span>
<span style="color:#00AA00">        &quot;DynamicUser&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;EnvironmentFiles&quot;: &quot;/etc/default/samba (ignore_errors=yes)&quot;,</span>
<span style="color:#00AA00">        &quot;ExecCondition&quot;: &quot;{ path=/usr/share/samba/is-configured ; argv[]=/usr/share/samba/is-configured nmb ; ignore_errors=no ; start_time=[Sun 2025-09-21 00:11:58 CEST] ; stop_time=[Sun 2025-09-21 00:11:59 CEST] ; pid=1369421 ; code=exited ; status=0 }&quot;,</span>
<span style="color:#00AA00">        &quot;ExecConditionEx&quot;: &quot;{ path=/usr/share/samba/is-configured ; argv[]=/usr/share/samba/is-configured nmb ; flags= ; start_time=[Sun 2025-09-21 00:11:58 CEST] ; stop_time=[Sun 2025-09-21 00:11:59 CEST] ; pid=1369421 ; code=exited ; status=0 }&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainCode&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainExitTimestampMonotonic&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainPID&quot;: &quot;1369426&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainStartTimestamp&quot;: &quot;Sun 2025-09-21 00:11:59 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainStartTimestampMonotonic&quot;: &quot;678293232166&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainStatus&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;ExecReload&quot;: &quot;{ path=/bin/kill ; argv[]=/bin/kill -HUP $MAINPID ; ignore_errors=no ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }&quot;,</span>
<span style="color:#00AA00">        &quot;ExecReloadEx&quot;: &quot;{ path=/bin/kill ; argv[]=/bin/kill -HUP $MAINPID ; flags= ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }&quot;,</span>
<span style="color:#00AA00">        &quot;ExecStart&quot;: &quot;{ path=/usr/sbin/nmbd ; argv[]=/usr/sbin/nmbd --foreground --no-process-group $NMBDOPTIONS ; ignore_errors=no ; start_time=[Sun 2025-09-21 00:11:59 CEST] ; stop_time=[n/a] ; pid=1369426 ; code=(null) ; status=0/0 }&quot;,</span>
<span style="color:#00AA00">        &quot;ExecStartEx&quot;: &quot;{ path=/usr/sbin/nmbd ; argv[]=/usr/sbin/nmbd --foreground --no-process-group $NMBDOPTIONS ; flags= ; start_time=[Sun 2025-09-21 00:11:59 CEST] ; stop_time=[n/a] ; pid=1369426 ; code=(null) ; status=0/0 }&quot;,</span>
<span style="color:#00AA00">        &quot;ExitType&quot;: &quot;main&quot;,</span>
<span style="color:#00AA00">        &quot;FailureAction&quot;: &quot;none&quot;,</span>
<span style="color:#00AA00">        &quot;FileDescriptorStoreMax&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;FinalKillSignal&quot;: &quot;9&quot;,</span>
<span style="color:#00AA00">        &quot;FragmentPath&quot;: &quot;/lib/systemd/system/nmbd.service&quot;,</span>
<span style="color:#00AA00">        &quot;FreezerState&quot;: &quot;running&quot;,</span>
<span style="color:#00AA00">        &quot;GID&quot;: &quot;[not set]&quot;,</span>
<span style="color:#00AA00">        &quot;GuessMainPID&quot;: &quot;yes&quot;,</span>
<span style="color:#00AA00">        &quot;IOAccounting&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;IOReadBytes&quot;: &quot;18446744073709551615&quot;,</span>
<span style="color:#00AA00">        &quot;IOReadOperations&quot;: &quot;18446744073709551615&quot;,</span>
<span style="color:#00AA00">        &quot;IOSchedulingClass&quot;: &quot;2&quot;,</span>
<span style="color:#00AA00">        &quot;IOSchedulingPriority&quot;: &quot;4&quot;,</span>
<span style="color:#00AA00">        &quot;IOWeight&quot;: &quot;[not set]&quot;,</span>
<span style="color:#00AA00">        &quot;IOWriteBytes&quot;: &quot;18446744073709551615&quot;,</span>
<span style="color:#00AA00">        &quot;IOWriteOperations&quot;: &quot;18446744073709551615&quot;,</span>
<span style="color:#00AA00">        &quot;IPAccounting&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;IPEgressBytes&quot;: &quot;[no data]&quot;,</span>
<span style="color:#00AA00">        &quot;IPEgressPackets&quot;: &quot;[no data]&quot;,</span>
<span style="color:#00AA00">        &quot;IPIngressBytes&quot;: &quot;[no data]&quot;,</span>
<span style="color:#00AA00">        &quot;IPIngressPackets&quot;: &quot;[no data]&quot;,</span>
<span style="color:#00AA00">        &quot;Id&quot;: &quot;nmbd.service&quot;,</span>
<span style="color:#00AA00">        &quot;IgnoreOnIsolate&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;IgnoreSIGPIPE&quot;: &quot;yes&quot;,</span>
<span style="color:#00AA00">        &quot;InactiveEnterTimestampMonotonic&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;InactiveExitTimestamp&quot;: &quot;Sun 2025-09-21 00:11:58 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;InactiveExitTimestampMonotonic&quot;: &quot;678293156547&quot;,</span>
<span style="color:#00AA00">        &quot;InvocationID&quot;: &quot;e76b6d580c874c1b8817b6abef8da1c0&quot;,</span>
<span style="color:#00AA00">        &quot;JobRunningTimeoutUSec&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;JobTimeoutAction&quot;: &quot;none&quot;,</span>
<span style="color:#00AA00">        &quot;JobTimeoutUSec&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;KeyringMode&quot;: &quot;private&quot;,</span>
<span style="color:#00AA00">        &quot;KillMode&quot;: &quot;control-group&quot;,</span>
<span style="color:#00AA00">        &quot;KillSignal&quot;: &quot;15&quot;,</span>
<span style="color:#00AA00">        &quot;LimitAS&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;LimitASSoft&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;LimitCORE&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;LimitCORESoft&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;LimitCPU&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;LimitCPUSoft&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;LimitDATA&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;LimitDATASoft&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;LimitFSIZE&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;LimitFSIZESoft&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;LimitLOCKS&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;LimitLOCKSSoft&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;LimitMEMLOCK&quot;: &quot;8388608&quot;,</span>
<span style="color:#00AA00">        &quot;LimitMEMLOCKSoft&quot;: &quot;8388608&quot;,</span>
<span style="color:#00AA00">        &quot;LimitMSGQUEUE&quot;: &quot;819200&quot;,</span>
<span style="color:#00AA00">        &quot;LimitMSGQUEUESoft&quot;: &quot;819200&quot;,</span>
<span style="color:#00AA00">        &quot;LimitNICE&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;LimitNICESoft&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;LimitNOFILE&quot;: &quot;524288&quot;,</span>
<span style="color:#00AA00">        &quot;LimitNOFILESoft&quot;: &quot;1024&quot;,</span>
<span style="color:#00AA00">        &quot;LimitNPROC&quot;: &quot;31916&quot;,</span>
<span style="color:#00AA00">        &quot;LimitNPROCSoft&quot;: &quot;31916&quot;,</span>
<span style="color:#00AA00">        &quot;LimitRSS&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;LimitRSSSoft&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;LimitRTPRIO&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;LimitRTPRIOSoft&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;LimitRTTIME&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;LimitRTTIMESoft&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;LimitSIGPENDING&quot;: &quot;31916&quot;,</span>
<span style="color:#00AA00">        &quot;LimitSIGPENDINGSoft&quot;: &quot;31916&quot;,</span>
<span style="color:#00AA00">        &quot;LimitSTACK&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;LimitSTACKSoft&quot;: &quot;8388608&quot;,</span>
<span style="color:#00AA00">        &quot;LoadState&quot;: &quot;loaded&quot;,</span>
<span style="color:#00AA00">        &quot;LockPersonality&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;LogLevelMax&quot;: &quot;-1&quot;,</span>
<span style="color:#00AA00">        &quot;LogRateLimitBurst&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;LogRateLimitIntervalUSec&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;LogsDirectoryMode&quot;: &quot;0755&quot;,</span>
<span style="color:#00AA00">        &quot;MainPID&quot;: &quot;1369426&quot;,</span>
<span style="color:#00AA00">        &quot;ManagedOOMMemoryPressure&quot;: &quot;auto&quot;,</span>
<span style="color:#00AA00">        &quot;ManagedOOMMemoryPressureLimit&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;ManagedOOMPreference&quot;: &quot;none&quot;,</span>
<span style="color:#00AA00">        &quot;ManagedOOMSwap&quot;: &quot;auto&quot;,</span>
<span style="color:#00AA00">        &quot;MemoryAccounting&quot;: &quot;yes&quot;,</span>
<span style="color:#00AA00">        &quot;MemoryAvailable&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;MemoryCurrent&quot;: &quot;[not set]&quot;,</span>
<span style="color:#00AA00">        &quot;MemoryDenyWriteExecute&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;MemoryHigh&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;MemoryLimit&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;MemoryLow&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;MemoryMax&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;MemoryMin&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;MemorySwapMax&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;MountAPIVFS&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;NFileDescriptorStore&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;NRestarts&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;NUMAPolicy&quot;: &quot;n/a&quot;,</span>
<span style="color:#00AA00">        &quot;Names&quot;: &quot;nmbd.service nmb.service&quot;,</span>
<span style="color:#00AA00">        &quot;NeedDaemonReload&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;Nice&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;NoNewPrivileges&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;NonBlocking&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;NotifyAccess&quot;: &quot;main&quot;,</span>
<span style="color:#00AA00">        &quot;OOMPolicy&quot;: &quot;stop&quot;,</span>
<span style="color:#00AA00">        &quot;OOMScoreAdjust&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;OnFailureJobMode&quot;: &quot;replace&quot;,</span>
<span style="color:#00AA00">        &quot;OnSuccessJobMode&quot;: &quot;fail&quot;,</span>
<span style="color:#00AA00">        &quot;PIDFile&quot;: &quot;/run/samba/nmbd.pid&quot;,</span>
<span style="color:#00AA00">        &quot;Perpetual&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;PrivateDevices&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;PrivateIPC&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;PrivateMounts&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;PrivateNetwork&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;PrivateTmp&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;PrivateUsers&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;ProcSubset&quot;: &quot;all&quot;,</span>
<span style="color:#00AA00">        &quot;ProtectClock&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;ProtectControlGroups&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;ProtectHome&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;ProtectHostname&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;ProtectKernelLogs&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;ProtectKernelModules&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;ProtectKernelTunables&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;ProtectProc&quot;: &quot;default&quot;,</span>
<span style="color:#00AA00">        &quot;ProtectSystem&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;RefuseManualStart&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;RefuseManualStop&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;ReloadResult&quot;: &quot;success&quot;,</span>
<span style="color:#00AA00">        &quot;RemainAfterExit&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;RemoveIPC&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;Requires&quot;: &quot;sysinit.target system.slice&quot;,</span>
<span style="color:#00AA00">        &quot;Restart&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;RestartKillSignal&quot;: &quot;15&quot;,</span>
<span style="color:#00AA00">        &quot;RestartUSec&quot;: &quot;100ms&quot;,</span>
<span style="color:#00AA00">        &quot;RestrictNamespaces&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;RestrictRealtime&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;RestrictSUIDSGID&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;Result&quot;: &quot;success&quot;,</span>
<span style="color:#00AA00">        &quot;RootDirectoryStartOnly&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;RuntimeDirectoryMode&quot;: &quot;0755&quot;,</span>
<span style="color:#00AA00">        &quot;RuntimeDirectoryPreserve&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;RuntimeMaxUSec&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;RuntimeRandomizedExtraUSec&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;SameProcessGroup&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;SecureBits&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;SendSIGHUP&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;SendSIGKILL&quot;: &quot;yes&quot;,</span>
<span style="color:#00AA00">        &quot;Slice&quot;: &quot;system.slice&quot;,</span>
<span style="color:#00AA00">        &quot;StandardError&quot;: &quot;inherit&quot;,</span>
<span style="color:#00AA00">        &quot;StandardInput&quot;: &quot;null&quot;,</span>
<span style="color:#00AA00">        &quot;StandardOutput&quot;: &quot;journal&quot;,</span>
<span style="color:#00AA00">        &quot;StartLimitAction&quot;: &quot;none&quot;,</span>
<span style="color:#00AA00">        &quot;StartLimitBurst&quot;: &quot;5&quot;,</span>
<span style="color:#00AA00">        &quot;StartLimitIntervalUSec&quot;: &quot;10s&quot;,</span>
<span style="color:#00AA00">        &quot;StartupBlockIOWeight&quot;: &quot;[not set]&quot;,</span>
<span style="color:#00AA00">        &quot;StartupCPUShares&quot;: &quot;[not set]&quot;,</span>
<span style="color:#00AA00">        &quot;StartupCPUWeight&quot;: &quot;[not set]&quot;,</span>
<span style="color:#00AA00">        &quot;StartupIOWeight&quot;: &quot;[not set]&quot;,</span>
<span style="color:#00AA00">        &quot;StateChangeTimestamp&quot;: &quot;Sun 2025-09-21 00:11:59 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;StateChangeTimestampMonotonic&quot;: &quot;678293262184&quot;,</span>
<span style="color:#00AA00">        &quot;StateDirectoryMode&quot;: &quot;0755&quot;,</span>
<span style="color:#00AA00">        &quot;StatusErrno&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;StatusText&quot;: &quot;nmbd: ready to serve connections...&quot;,</span>
<span style="color:#00AA00">        &quot;StopWhenUnneeded&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;SubState&quot;: &quot;running&quot;,</span>
<span style="color:#00AA00">        &quot;SuccessAction&quot;: &quot;none&quot;,</span>
<span style="color:#00AA00">        &quot;SyslogFacility&quot;: &quot;3&quot;,</span>
<span style="color:#00AA00">        &quot;SyslogLevel&quot;: &quot;6&quot;,</span>
<span style="color:#00AA00">        &quot;SyslogLevelPrefix&quot;: &quot;yes&quot;,</span>
<span style="color:#00AA00">        &quot;SyslogPriority&quot;: &quot;30&quot;,</span>
<span style="color:#00AA00">        &quot;SystemCallErrorNumber&quot;: &quot;2147483646&quot;,</span>
<span style="color:#00AA00">        &quot;TTYReset&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;TTYVHangup&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;TTYVTDisallocate&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;TasksAccounting&quot;: &quot;yes&quot;,</span>
<span style="color:#00AA00">        &quot;TasksCurrent&quot;: &quot;1&quot;,</span>
<span style="color:#00AA00">        &quot;TasksMax&quot;: &quot;9574&quot;,</span>
<span style="color:#00AA00">        &quot;TimeoutAbortUSec&quot;: &quot;1min 30s&quot;,</span>
<span style="color:#00AA00">        &quot;TimeoutCleanUSec&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;TimeoutStartFailureMode&quot;: &quot;terminate&quot;,</span>
<span style="color:#00AA00">        &quot;TimeoutStartUSec&quot;: &quot;1min 30s&quot;,</span>
<span style="color:#00AA00">        &quot;TimeoutStopFailureMode&quot;: &quot;terminate&quot;,</span>
<span style="color:#00AA00">        &quot;TimeoutStopUSec&quot;: &quot;1min 30s&quot;,</span>
<span style="color:#00AA00">        &quot;TimerSlackNSec&quot;: &quot;50000&quot;,</span>
<span style="color:#00AA00">        &quot;Transient&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;Type&quot;: &quot;notify&quot;,</span>
<span style="color:#00AA00">        &quot;UID&quot;: &quot;[not set]&quot;,</span>
<span style="color:#00AA00">        &quot;UMask&quot;: &quot;0022&quot;,</span>
<span style="color:#00AA00">        &quot;UnitFilePreset&quot;: &quot;enabled&quot;,</span>
<span style="color:#00AA00">        &quot;UnitFileState&quot;: &quot;enabled&quot;,</span>
<span style="color:#00AA00">        &quot;UtmpMode&quot;: &quot;init&quot;,</span>
<span style="color:#00AA00">        &quot;WantedBy&quot;: &quot;multi-user.target&quot;,</span>
<span style="color:#00AA00">        &quot;Wants&quot;: &quot;network-online.target&quot;,</span>
<span style="color:#00AA00">        &quot;WatchdogSignal&quot;: &quot;6&quot;,</span>
<span style="color:#00AA00">        &quot;WatchdogTimestampMonotonic&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;WatchdogUSec&quot;: &quot;0&quot;</span>
<span style="color:#00AA00">    }</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  00:12:06 +0200 (0:00:00.551)       0:00:26.096 ***** 
Sonntag 21 September 2025  00:12:06 +0200 (0:00:00.046)       0:00:26.143 ***** 

TASK [geerlingguy.nfs : Include OS-specific variables.] ***********************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.nfs/tasks/main.yml:3</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;ansible_facts&quot;: {</span>
<span style="color:#00AA00">        &quot;nfs_server_daemon&quot;: &quot;nfs-kernel-server&quot;</span>
<span style="color:#00AA00">    },</span>
<span style="color:#00AA00">    &quot;ansible_included_var_files&quot;: [</span>
<span style="color:#00AA00">        &quot;/home/dietmar/.ansible/roles/geerlingguy.nfs/vars/Debian.yml&quot;</span>
<span style="color:#00AA00">    ],</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  00:12:06 +0200 (0:00:00.057)       0:00:26.200 ***** 
Sonntag 21 September 2025  00:12:06 +0200 (0:00:00.027)       0:00:26.228 ***** 
Sonntag 21 September 2025  00:12:06 +0200 (0:00:00.039)       0:00:26.268 ***** 

TASK [geerlingguy.nfs : include_tasks] ****************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.nfs/tasks/main.yml:16</b></span>
<span style="color:#00AAAA">included: /home/dietmar/.ansible/roles/geerlingguy.nfs/tasks/setup-Debian.yml for ansible-nas</span>
Sonntag 21 September 2025  00:12:06 +0200 (0:00:00.047)       0:00:26.315 ***** 

TASK [geerlingguy.nfs : Ensure NFS utilities are installed.] ******************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.nfs/tasks/setup-Debian.yml:2</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;cache_update_time&quot;: 1758331880,</span>
<span style="color:#00AA00">    &quot;cache_updated&quot;: false,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  00:12:07 +0200 (0:00:01.362)       0:00:27.677 ***** 

TASK [geerlingguy.nfs : Ensure directories to export exist] *******************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.nfs/tasks/main.yml:19</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; (item=/mnt/Volume1/local/Books *(rw,async,no_root_squash,no_subtree_check)) =&gt; {</span>
<span style="color:#00AA00">    &quot;ansible_loop_var&quot;: &quot;item&quot;,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;gid&quot;: 1001,</span>
<span style="color:#00AA00">    &quot;group&quot;: &quot;ansible-nas&quot;,</span>
<span style="color:#00AA00">    &quot;item&quot;: &quot;/mnt/Volume1/local/Books *(rw,async,no_root_squash,no_subtree_check)&quot;,</span>
<span style="color:#00AA00">    &quot;mode&quot;: &quot;0777&quot;,</span>
<span style="color:#00AA00">    &quot;owner&quot;: &quot;ansible-nas&quot;,</span>
<span style="color:#00AA00">    &quot;path&quot;: &quot;/mnt/Volume1/local/Books&quot;,</span>
<span style="color:#00AA00">    &quot;size&quot;: 4096,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;directory&quot;,</span>
<span style="color:#00AA00">    &quot;uid&quot;: 994</span>
<span style="color:#00AA00">}</span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; (item=/mnt/Volume1/local/Audiobooks *(rw,async,no_root_squash,no_subtree_check)) =&gt; {</span>
<span style="color:#00AA00">    &quot;ansible_loop_var&quot;: &quot;item&quot;,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;gid&quot;: 1001,</span>
<span style="color:#00AA00">    &quot;group&quot;: &quot;ansible-nas&quot;,</span>
<span style="color:#00AA00">    &quot;item&quot;: &quot;/mnt/Volume1/local/Audiobooks *(rw,async,no_root_squash,no_subtree_check)&quot;,</span>
<span style="color:#00AA00">    &quot;mode&quot;: &quot;0777&quot;,</span>
<span style="color:#00AA00">    &quot;owner&quot;: &quot;ansible-nas&quot;,</span>
<span style="color:#00AA00">    &quot;path&quot;: &quot;/mnt/Volume1/local/Audiobooks&quot;,</span>
<span style="color:#00AA00">    &quot;size&quot;: 4096,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;directory&quot;,</span>
<span style="color:#00AA00">    &quot;uid&quot;: 994</span>
<span style="color:#00AA00">}</span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; (item=/mnt/Volume1/local/Comics *(rw,async,no_root_squash,no_subtree_check)) =&gt; {</span>
<span style="color:#00AA00">    &quot;ansible_loop_var&quot;: &quot;item&quot;,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;gid&quot;: 1001,</span>
<span style="color:#00AA00">    &quot;group&quot;: &quot;ansible-nas&quot;,</span>
<span style="color:#00AA00">    &quot;item&quot;: &quot;/mnt/Volume1/local/Comics *(rw,async,no_root_squash,no_subtree_check)&quot;,</span>
<span style="color:#00AA00">    &quot;mode&quot;: &quot;0777&quot;,</span>
<span style="color:#00AA00">    &quot;owner&quot;: &quot;ansible-nas&quot;,</span>
<span style="color:#00AA00">    &quot;path&quot;: &quot;/mnt/Volume1/local/Comics&quot;,</span>
<span style="color:#00AA00">    &quot;size&quot;: 4096,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;directory&quot;,</span>
<span style="color:#00AA00">    &quot;uid&quot;: 994</span>
<span style="color:#00AA00">}</span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; (item=/mnt/Volume1/docker *(rw,async,no_root_squash,no_subtree_check)) =&gt; {</span>
<span style="color:#00AA00">    &quot;ansible_loop_var&quot;: &quot;item&quot;,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;gid&quot;: 1001,</span>
<span style="color:#00AA00">    &quot;group&quot;: &quot;ansible-nas&quot;,</span>
<span style="color:#00AA00">    &quot;item&quot;: &quot;/mnt/Volume1/docker *(rw,async,no_root_squash,no_subtree_check)&quot;,</span>
<span style="color:#00AA00">    &quot;mode&quot;: &quot;0777&quot;,</span>
<span style="color:#00AA00">    &quot;owner&quot;: &quot;1001&quot;,</span>
<span style="color:#00AA00">    &quot;path&quot;: &quot;/mnt/Volume1/docker&quot;,</span>
<span style="color:#00AA00">    &quot;size&quot;: 4096,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;directory&quot;,</span>
<span style="color:#00AA00">    &quot;uid&quot;: 1001</span>
<span style="color:#00AA00">}</span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; (item=/mnt/Volume1/local/Download *(rw,async,no_root_squash,no_subtree_check)) =&gt; {</span>
<span style="color:#00AA00">    &quot;ansible_loop_var&quot;: &quot;item&quot;,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;gid&quot;: 1001,</span>
<span style="color:#00AA00">    &quot;group&quot;: &quot;ansible-nas&quot;,</span>
<span style="color:#00AA00">    &quot;item&quot;: &quot;/mnt/Volume1/local/Download *(rw,async,no_root_squash,no_subtree_check)&quot;,</span>
<span style="color:#00AA00">    &quot;mode&quot;: &quot;0777&quot;,</span>
<span style="color:#00AA00">    &quot;owner&quot;: &quot;ansible-nas&quot;,</span>
<span style="color:#00AA00">    &quot;path&quot;: &quot;/mnt/Volume1/local/Download&quot;,</span>
<span style="color:#00AA00">    &quot;size&quot;: 4096,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;directory&quot;,</span>
<span style="color:#00AA00">    &quot;uid&quot;: 994</span>
<span style="color:#00AA00">}</span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; (item=/mnt/Volume1/local/Documents *(rw,async,no_root_squash,no_subtree_check)) =&gt; {</span>
<span style="color:#00AA00">    &quot;ansible_loop_var&quot;: &quot;item&quot;,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;gid&quot;: 1001,</span>
<span style="color:#00AA00">    &quot;group&quot;: &quot;ansible-nas&quot;,</span>
<span style="color:#00AA00">    &quot;item&quot;: &quot;/mnt/Volume1/local/Documents *(rw,async,no_root_squash,no_subtree_check)&quot;,</span>
<span style="color:#00AA00">    &quot;mode&quot;: &quot;0777&quot;,</span>
<span style="color:#00AA00">    &quot;owner&quot;: &quot;ansible-nas&quot;,</span>
<span style="color:#00AA00">    &quot;path&quot;: &quot;/mnt/Volume1/local/Documents&quot;,</span>
<span style="color:#00AA00">    &quot;size&quot;: 4096,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;directory&quot;,</span>
<span style="color:#00AA00">    &quot;uid&quot;: 994</span>
<span style="color:#00AA00">}</span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; (item=/mnt/Volume1/local/Ägyptologie *(rw,async,no_root_squash,no_subtree_check)) =&gt; {</span>
<span style="color:#00AA00">    &quot;ansible_loop_var&quot;: &quot;item&quot;,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;gid&quot;: 1001,</span>
<span style="color:#00AA00">    &quot;group&quot;: &quot;ansible-nas&quot;,</span>
<span style="color:#00AA00">    &quot;item&quot;: &quot;/mnt/Volume1/local/Ägyptologie *(rw,async,no_root_squash,no_subtree_check)&quot;,</span>
<span style="color:#00AA00">    &quot;mode&quot;: &quot;0777&quot;,</span>
<span style="color:#00AA00">    &quot;owner&quot;: &quot;ansible-nas&quot;,</span>
<span style="color:#00AA00">    &quot;path&quot;: &quot;/mnt/Volume1/local/Ägyptologie&quot;,</span>
<span style="color:#00AA00">    &quot;size&quot;: 4096,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;directory&quot;,</span>
<span style="color:#00AA00">    &quot;uid&quot;: 994</span>
<span style="color:#00AA00">}</span>
<span style="color:#AA5500">changed: [ansible-nas] =&gt; (item=/mnt/Volume1/local/EDV *(rw,async,no_root_squash,no_subtree_check)) =&gt; {</span>
<span style="color:#AA5500">    &quot;ansible_loop_var&quot;: &quot;item&quot;,</span>
<span style="color:#AA5500">    &quot;changed&quot;: true,</span>
<span style="color:#AA5500">    &quot;gid&quot;: 0,</span>
<span style="color:#AA5500">    &quot;group&quot;: &quot;root&quot;,</span>
<span style="color:#AA5500">    &quot;item&quot;: &quot;/mnt/Volume1/local/EDV *(rw,async,no_root_squash,no_subtree_check)&quot;,</span>
<span style="color:#AA5500">    &quot;mode&quot;: &quot;0755&quot;,</span>
<span style="color:#AA5500">    &quot;owner&quot;: &quot;root&quot;,</span>
<span style="color:#AA5500">    &quot;path&quot;: &quot;/mnt/Volume1/local/EDV&quot;,</span>
<span style="color:#AA5500">    &quot;size&quot;: 4096,</span>
<span style="color:#AA5500">    &quot;state&quot;: &quot;directory&quot;,</span>
<span style="color:#AA5500">    &quot;uid&quot;: 0</span>
<span style="color:#AA5500">}</span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; (item=/mnt/Volume1/local/Inventar *(rw,async,no_root_squash,no_subtree_check)) =&gt; {</span>
<span style="color:#00AA00">    &quot;ansible_loop_var&quot;: &quot;item&quot;,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;gid&quot;: 1001,</span>
<span style="color:#00AA00">    &quot;group&quot;: &quot;ansible-nas&quot;,</span>
<span style="color:#00AA00">    &quot;item&quot;: &quot;/mnt/Volume1/local/Inventar *(rw,async,no_root_squash,no_subtree_check)&quot;,</span>
<span style="color:#00AA00">    &quot;mode&quot;: &quot;0777&quot;,</span>
<span style="color:#00AA00">    &quot;owner&quot;: &quot;ansible-nas&quot;,</span>
<span style="color:#00AA00">    &quot;path&quot;: &quot;/mnt/Volume1/local/Inventar&quot;,</span>
<span style="color:#00AA00">    &quot;size&quot;: 4096,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;directory&quot;,</span>
<span style="color:#00AA00">    &quot;uid&quot;: 994</span>
<span style="color:#00AA00">}</span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; (item=/mnt/Volume1/local/Media *(rw,async,no_root_squash,no_subtree_check)) =&gt; {</span>
<span style="color:#00AA00">    &quot;ansible_loop_var&quot;: &quot;item&quot;,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;gid&quot;: 1001,</span>
<span style="color:#00AA00">    &quot;group&quot;: &quot;ansible-nas&quot;,</span>
<span style="color:#00AA00">    &quot;item&quot;: &quot;/mnt/Volume1/local/Media *(rw,async,no_root_squash,no_subtree_check)&quot;,</span>
<span style="color:#00AA00">    &quot;mode&quot;: &quot;0777&quot;,</span>
<span style="color:#00AA00">    &quot;owner&quot;: &quot;ansible-nas&quot;,</span>
<span style="color:#00AA00">    &quot;path&quot;: &quot;/mnt/Volume1/local/Media&quot;,</span>
<span style="color:#00AA00">    &quot;size&quot;: 4096,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;directory&quot;,</span>
<span style="color:#00AA00">    &quot;uid&quot;: 994</span>
<span style="color:#00AA00">}</span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; (item=/mnt/Volume1/local/Movies *(rw,async,no_root_squash,no_subtree_check)) =&gt; {</span>
<span style="color:#00AA00">    &quot;ansible_loop_var&quot;: &quot;item&quot;,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;gid&quot;: 1001,</span>
<span style="color:#00AA00">    &quot;group&quot;: &quot;ansible-nas&quot;,</span>
<span style="color:#00AA00">    &quot;item&quot;: &quot;/mnt/Volume1/local/Movies *(rw,async,no_root_squash,no_subtree_check)&quot;,</span>
<span style="color:#00AA00">    &quot;mode&quot;: &quot;0777&quot;,</span>
<span style="color:#00AA00">    &quot;owner&quot;: &quot;ansible-nas&quot;,</span>
<span style="color:#00AA00">    &quot;path&quot;: &quot;/mnt/Volume1/local/Movies&quot;,</span>
<span style="color:#00AA00">    &quot;size&quot;: 4096,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;directory&quot;,</span>
<span style="color:#00AA00">    &quot;uid&quot;: 994</span>
<span style="color:#00AA00">}</span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; (item=/mnt/Volume1/local/Music *(rw,async,no_root_squash,no_subtree_check)) =&gt; {</span>
<span style="color:#00AA00">    &quot;ansible_loop_var&quot;: &quot;item&quot;,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;gid&quot;: 1001,</span>
<span style="color:#00AA00">    &quot;group&quot;: &quot;ansible-nas&quot;,</span>
<span style="color:#00AA00">    &quot;item&quot;: &quot;/mnt/Volume1/local/Music *(rw,async,no_root_squash,no_subtree_check)&quot;,</span>
<span style="color:#00AA00">    &quot;mode&quot;: &quot;0777&quot;,</span>
<span style="color:#00AA00">    &quot;owner&quot;: &quot;ansible-nas&quot;,</span>
<span style="color:#00AA00">    &quot;path&quot;: &quot;/mnt/Volume1/local/Music&quot;,</span>
<span style="color:#00AA00">    &quot;size&quot;: 4096,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;directory&quot;,</span>
<span style="color:#00AA00">    &quot;uid&quot;: 994</span>
<span style="color:#00AA00">}</span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; (item=/mnt/Volume1/local/Organisation *(rw,async,no_root_squash,no_subtree_check)) =&gt; {</span>
<span style="color:#00AA00">    &quot;ansible_loop_var&quot;: &quot;item&quot;,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;gid&quot;: 1001,</span>
<span style="color:#00AA00">    &quot;group&quot;: &quot;ansible-nas&quot;,</span>
<span style="color:#00AA00">    &quot;item&quot;: &quot;/mnt/Volume1/local/Organisation *(rw,async,no_root_squash,no_subtree_check)&quot;,</span>
<span style="color:#00AA00">    &quot;mode&quot;: &quot;0777&quot;,</span>
<span style="color:#00AA00">    &quot;owner&quot;: &quot;ansible-nas&quot;,</span>
<span style="color:#00AA00">    &quot;path&quot;: &quot;/mnt/Volume1/local/Organisation&quot;,</span>
<span style="color:#00AA00">    &quot;size&quot;: 4096,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;directory&quot;,</span>
<span style="color:#00AA00">    &quot;uid&quot;: 994</span>
<span style="color:#00AA00">}</span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; (item=/mnt/Volume1/local/Persönliches *(rw,async,no_root_squash,no_subtree_check)) =&gt; {</span>
<span style="color:#00AA00">    &quot;ansible_loop_var&quot;: &quot;item&quot;,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;gid&quot;: 1001,</span>
<span style="color:#00AA00">    &quot;group&quot;: &quot;ansible-nas&quot;,</span>
<span style="color:#00AA00">    &quot;item&quot;: &quot;/mnt/Volume1/local/Persönliches *(rw,async,no_root_squash,no_subtree_check)&quot;,</span>
<span style="color:#00AA00">    &quot;mode&quot;: &quot;0777&quot;,</span>
<span style="color:#00AA00">    &quot;owner&quot;: &quot;ansible-nas&quot;,</span>
<span style="color:#00AA00">    &quot;path&quot;: &quot;/mnt/Volume1/local/Persönliches&quot;,</span>
<span style="color:#00AA00">    &quot;size&quot;: 4096,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;directory&quot;,</span>
<span style="color:#00AA00">    &quot;uid&quot;: 994</span>
<span style="color:#00AA00">}</span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; (item=/mnt/Volume1/local/Photos *(rw,async,no_root_squash,no_subtree_check)) =&gt; {</span>
<span style="color:#00AA00">    &quot;ansible_loop_var&quot;: &quot;item&quot;,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;gid&quot;: 1001,</span>
<span style="color:#00AA00">    &quot;group&quot;: &quot;ansible-nas&quot;,</span>
<span style="color:#00AA00">    &quot;item&quot;: &quot;/mnt/Volume1/local/Photos *(rw,async,no_root_squash,no_subtree_check)&quot;,</span>
<span style="color:#00AA00">    &quot;mode&quot;: &quot;0777&quot;,</span>
<span style="color:#00AA00">    &quot;owner&quot;: &quot;ansible-nas&quot;,</span>
<span style="color:#00AA00">    &quot;path&quot;: &quot;/mnt/Volume1/local/Photos&quot;,</span>
<span style="color:#00AA00">    &quot;size&quot;: 4096,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;directory&quot;,</span>
<span style="color:#00AA00">    &quot;uid&quot;: 994</span>
<span style="color:#00AA00">}</span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; (item=/mnt/Volume1/local/Podcasts *(rw,async,no_root_squash,no_subtree_check)) =&gt; {</span>
<span style="color:#00AA00">    &quot;ansible_loop_var&quot;: &quot;item&quot;,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;gid&quot;: 1001,</span>
<span style="color:#00AA00">    &quot;group&quot;: &quot;ansible-nas&quot;,</span>
<span style="color:#00AA00">    &quot;item&quot;: &quot;/mnt/Volume1/local/Podcasts *(rw,async,no_root_squash,no_subtree_check)&quot;,</span>
<span style="color:#00AA00">    &quot;mode&quot;: &quot;0777&quot;,</span>
<span style="color:#00AA00">    &quot;owner&quot;: &quot;ansible-nas&quot;,</span>
<span style="color:#00AA00">    &quot;path&quot;: &quot;/mnt/Volume1/local/Podcasts&quot;,</span>
<span style="color:#00AA00">    &quot;size&quot;: 4096,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;directory&quot;,</span>
<span style="color:#00AA00">    &quot;uid&quot;: 994</span>
<span style="color:#00AA00">}</span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; (item=/mnt/Volume1/local/Versorgung *(rw,async,no_root_squash,no_subtree_check)) =&gt; {</span>
<span style="color:#00AA00">    &quot;ansible_loop_var&quot;: &quot;item&quot;,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;gid&quot;: 1001,</span>
<span style="color:#00AA00">    &quot;group&quot;: &quot;ansible-nas&quot;,</span>
<span style="color:#00AA00">    &quot;item&quot;: &quot;/mnt/Volume1/local/Versorgung *(rw,async,no_root_squash,no_subtree_check)&quot;,</span>
<span style="color:#00AA00">    &quot;mode&quot;: &quot;0777&quot;,</span>
<span style="color:#00AA00">    &quot;owner&quot;: &quot;ansible-nas&quot;,</span>
<span style="color:#00AA00">    &quot;path&quot;: &quot;/mnt/Volume1/local/Versorgung&quot;,</span>
<span style="color:#00AA00">    &quot;size&quot;: 4096,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;directory&quot;,</span>
<span style="color:#00AA00">    &quot;uid&quot;: 994</span>
<span style="color:#00AA00">}</span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; (item=/mnt/Volume1/local/TV *(rw,async,no_root_squash,no_subtree_check)) =&gt; {</span>
<span style="color:#00AA00">    &quot;ansible_loop_var&quot;: &quot;item&quot;,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;gid&quot;: 1001,</span>
<span style="color:#00AA00">    &quot;group&quot;: &quot;ansible-nas&quot;,</span>
<span style="color:#00AA00">    &quot;item&quot;: &quot;/mnt/Volume1/local/TV *(rw,async,no_root_squash,no_subtree_check)&quot;,</span>
<span style="color:#00AA00">    &quot;mode&quot;: &quot;0777&quot;,</span>
<span style="color:#00AA00">    &quot;owner&quot;: &quot;ansible-nas&quot;,</span>
<span style="color:#00AA00">    &quot;path&quot;: &quot;/mnt/Volume1/local/TV&quot;,</span>
<span style="color:#00AA00">    &quot;size&quot;: 4096,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;directory&quot;,</span>
<span style="color:#00AA00">    &quot;uid&quot;: 994</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  00:12:13 +0200 (0:00:05.892)       0:00:33.569 ***** 
<span style="color:#0000AA">Notification for handler reload nfs has been saved.</span>

TASK [geerlingguy.nfs : Copy exports file.] ***********************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.nfs/tasks/main.yml:25</b></span>
<span style="color:#AA5500">changed: [ansible-nas] =&gt; {</span>
<span style="color:#AA5500">    &quot;changed&quot;: true,</span>
<span style="color:#AA5500">    &quot;checksum&quot;: &quot;8957f37805d918cbff27a51a8e07850a95e8fbde&quot;,</span>
<span style="color:#AA5500">    &quot;dest&quot;: &quot;/etc/exports&quot;,</span>
<span style="color:#AA5500">    &quot;gid&quot;: 0,</span>
<span style="color:#AA5500">    &quot;group&quot;: &quot;root&quot;,</span>
<span style="color:#AA5500">    &quot;md5sum&quot;: &quot;7de3caf72f3f255f7a51446f6b503938&quot;,</span>
<span style="color:#AA5500">    &quot;mode&quot;: &quot;0644&quot;,</span>
<span style="color:#AA5500">    &quot;owner&quot;: &quot;root&quot;,</span>
<span style="color:#AA5500">    &quot;size&quot;: 1670,</span>
<span style="color:#AA5500">    &quot;src&quot;: &quot;/home/dietmar/.ansible/tmp/ansible-tmp-1758406333.5906234-85231-34970933656444/source&quot;,</span>
<span style="color:#AA5500">    &quot;state&quot;: &quot;file&quot;,</span>
<span style="color:#AA5500">    &quot;uid&quot;: 0</span>
<span style="color:#AA5500">}</span>
Sonntag 21 September 2025  00:12:14 +0200 (0:00:00.705)       0:00:34.275 ***** 

TASK [geerlingguy.nfs : Ensure nfs is running.] *******************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.nfs/tasks/main.yml:34</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;enabled&quot;: true,</span>
<span style="color:#00AA00">    &quot;name&quot;: &quot;nfs-kernel-server&quot;,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;started&quot;,</span>
<span style="color:#00AA00">    &quot;status&quot;: {</span>
<span style="color:#00AA00">        &quot;ActiveEnterTimestamp&quot;: &quot;Sat 2025-09-13 03:47:24 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;ActiveEnterTimestampMonotonic&quot;: &quot;17934323&quot;,</span>
<span style="color:#00AA00">        &quot;ActiveExitTimestampMonotonic&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;ActiveState&quot;: &quot;active&quot;,</span>
<span style="color:#00AA00">        &quot;After&quot;: &quot;systemd-journald.socket network-online.target gssproxy.service nfs-mountd.service rpc-statd.service nfsdcld.service -.mount rpcbind.socket local-fs.target rpc-svcgssd.service mnt-Volume1.mount system.slice nfs-idmapd.service rpc-gssd.service proc-fs-nfsd.mount&quot;,</span>
<span style="color:#00AA00">        &quot;AllowIsolate&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;AssertResult&quot;: &quot;yes&quot;,</span>
<span style="color:#00AA00">        &quot;AssertTimestamp&quot;: &quot;Sat 2025-09-13 03:47:23 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;AssertTimestampMonotonic&quot;: &quot;17797807&quot;,</span>
<span style="color:#00AA00">        &quot;Before&quot;: &quot;media-web.mount media-Produktion.mount media-Dokumente.mount media-Medien.mount rpc-statd-notify.service&quot;,</span>
<span style="color:#00AA00">        &quot;BlockIOAccounting&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;BlockIOWeight&quot;: &quot;[not set]&quot;,</span>
<span style="color:#00AA00">        &quot;BoundBy&quot;: &quot;nfs-idmapd.service nfs-mountd.service&quot;,</span>
<span style="color:#00AA00">        &quot;CPUAccounting&quot;: &quot;yes&quot;,</span>
<span style="color:#00AA00">        &quot;CPUAffinityFromNUMA&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;CPUQuotaPerSecUSec&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;CPUQuotaPeriodUSec&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;CPUSchedulingPolicy&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;CPUSchedulingPriority&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;CPUSchedulingResetOnFork&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;CPUShares&quot;: &quot;[not set]&quot;,</span>
<span style="color:#00AA00">        &quot;CPUUsageNSec&quot;: &quot;4637000&quot;,</span>
<span style="color:#00AA00">        &quot;CPUWeight&quot;: &quot;[not set]&quot;,</span>
<span style="color:#00AA00">        &quot;CacheDirectoryMode&quot;: &quot;0755&quot;,</span>
<span style="color:#00AA00">        &quot;CanFreeze&quot;: &quot;yes&quot;,</span>
<span style="color:#00AA00">        &quot;CanIsolate&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;CanReload&quot;: &quot;yes&quot;,</span>
<span style="color:#00AA00">        &quot;CanStart&quot;: &quot;yes&quot;,</span>
<span style="color:#00AA00">        &quot;CanStop&quot;: &quot;yes&quot;,</span>
<span style="color:#00AA00">        &quot;CapabilityBoundingSet&quot;: &quot;cap_chown cap_dac_override cap_dac_read_search cap_fowner cap_fsetid cap_kill cap_setgid cap_setuid cap_setpcap cap_linux_immutable cap_net_bind_service cap_net_broadcast cap_net_admin cap_net_raw cap_ipc_lock cap_ipc_owner cap_sys_module cap_sys_rawio cap_sys_chroot cap_sys_ptrace cap_sys_pacct cap_sys_admin cap_sys_boot cap_sys_nice cap_sys_resource cap_sys_time cap_sys_tty_config cap_mknod cap_lease cap_audit_write cap_audit_control cap_setfcap cap_mac_override cap_mac_admin cap_syslog cap_wake_alarm cap_block_suspend cap_audit_read cap_perfmon cap_bpf cap_checkpoint_restore&quot;,</span>
<span style="color:#00AA00">        &quot;CleanResult&quot;: &quot;success&quot;,</span>
<span style="color:#00AA00">        &quot;CollectMode&quot;: &quot;inactive&quot;,</span>
<span style="color:#00AA00">        &quot;ConditionResult&quot;: &quot;yes&quot;,</span>
<span style="color:#00AA00">        &quot;ConditionTimestamp&quot;: &quot;Sat 2025-09-13 03:47:23 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;ConditionTimestampMonotonic&quot;: &quot;17797805&quot;,</span>
<span style="color:#00AA00">        &quot;ConfigurationDirectoryMode&quot;: &quot;0755&quot;,</span>
<span style="color:#00AA00">        &quot;ConsistsOf&quot;: &quot;rpc-svcgssd.service&quot;,</span>
<span style="color:#00AA00">        &quot;ControlGroupId&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;ControlPID&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;CoredumpFilter&quot;: &quot;0x33&quot;,</span>
<span style="color:#00AA00">        &quot;DefaultDependencies&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;DefaultMemoryLow&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;DefaultMemoryMin&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;Delegate&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;Description&quot;: &quot;NFS server and services&quot;,</span>
<span style="color:#00AA00">        &quot;DevicePolicy&quot;: &quot;auto&quot;,</span>
<span style="color:#00AA00">        &quot;DropInPaths&quot;: &quot;/run/systemd/generator/nfs-server.service.d/order-with-mounts.conf&quot;,</span>
<span style="color:#00AA00">        &quot;DynamicUser&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainCode&quot;: &quot;1&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainExitTimestamp&quot;: &quot;Sat 2025-09-13 03:47:24 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainExitTimestampMonotonic&quot;: &quot;17933634&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainPID&quot;: &quot;950&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainStartTimestamp&quot;: &quot;Sat 2025-09-13 03:47:24 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainStartTimestampMonotonic&quot;: &quot;17802500&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainStatus&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;ExecReload&quot;: &quot;{ path=/usr/sbin/exportfs ; argv[]=/usr/sbin/exportfs -r ; ignore_errors=yes ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }&quot;,</span>
<span style="color:#00AA00">        &quot;ExecReloadEx&quot;: &quot;{ path=/usr/sbin/exportfs ; argv[]=/usr/sbin/exportfs -r ; flags=ignore-failure ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }&quot;,</span>
<span style="color:#00AA00">        &quot;ExecStart&quot;: &quot;{ path=/usr/sbin/rpc.nfsd ; argv[]=/usr/sbin/rpc.nfsd ; ignore_errors=no ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }&quot;,</span>
<span style="color:#00AA00">        &quot;ExecStartEx&quot;: &quot;{ path=/usr/sbin/rpc.nfsd ; argv[]=/usr/sbin/rpc.nfsd ; flags= ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }&quot;,</span>
<span style="color:#00AA00">        &quot;ExecStartPre&quot;: &quot;{ path=/usr/sbin/exportfs ; argv[]=/usr/sbin/exportfs -r ; ignore_errors=yes ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }&quot;,</span>
<span style="color:#00AA00">        &quot;ExecStartPreEx&quot;: &quot;{ path=/usr/sbin/exportfs ; argv[]=/usr/sbin/exportfs -r ; flags=ignore-failure ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }&quot;,</span>
<span style="color:#00AA00">        &quot;ExecStop&quot;: &quot;{ path=/usr/sbin/rpc.nfsd ; argv[]=/usr/sbin/rpc.nfsd 0 ; ignore_errors=no ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }&quot;,</span>
<span style="color:#00AA00">        &quot;ExecStopEx&quot;: &quot;{ path=/usr/sbin/rpc.nfsd ; argv[]=/usr/sbin/rpc.nfsd 0 ; flags= ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }&quot;,</span>
<span style="color:#00AA00">        &quot;ExecStopPost&quot;: &quot;{ path=/usr/sbin/exportfs ; argv[]=/usr/sbin/exportfs -f ; ignore_errors=no ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }&quot;,</span>
<span style="color:#00AA00">        &quot;ExecStopPostEx&quot;: &quot;{ path=/usr/sbin/exportfs ; argv[]=/usr/sbin/exportfs -f ; flags= ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }&quot;,</span>
<span style="color:#00AA00">        &quot;ExitType&quot;: &quot;main&quot;,</span>
<span style="color:#00AA00">        &quot;FailureAction&quot;: &quot;none&quot;,</span>
<span style="color:#00AA00">        &quot;FileDescriptorStoreMax&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;FinalKillSignal&quot;: &quot;9&quot;,</span>
<span style="color:#00AA00">        &quot;FragmentPath&quot;: &quot;/lib/systemd/system/nfs-server.service&quot;,</span>
<span style="color:#00AA00">        &quot;FreezerState&quot;: &quot;running&quot;,</span>
<span style="color:#00AA00">        &quot;GID&quot;: &quot;[not set]&quot;,</span>
<span style="color:#00AA00">        &quot;GuessMainPID&quot;: &quot;yes&quot;,</span>
<span style="color:#00AA00">        &quot;IOAccounting&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;IOReadBytes&quot;: &quot;18446744073709551615&quot;,</span>
<span style="color:#00AA00">        &quot;IOReadOperations&quot;: &quot;18446744073709551615&quot;,</span>
<span style="color:#00AA00">        &quot;IOSchedulingClass&quot;: &quot;2&quot;,</span>
<span style="color:#00AA00">        &quot;IOSchedulingPriority&quot;: &quot;4&quot;,</span>
<span style="color:#00AA00">        &quot;IOWeight&quot;: &quot;[not set]&quot;,</span>
<span style="color:#00AA00">        &quot;IOWriteBytes&quot;: &quot;18446744073709551615&quot;,</span>
<span style="color:#00AA00">        &quot;IOWriteOperations&quot;: &quot;18446744073709551615&quot;,</span>
<span style="color:#00AA00">        &quot;IPAccounting&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;IPEgressBytes&quot;: &quot;[no data]&quot;,</span>
<span style="color:#00AA00">        &quot;IPEgressPackets&quot;: &quot;[no data]&quot;,</span>
<span style="color:#00AA00">        &quot;IPIngressBytes&quot;: &quot;[no data]&quot;,</span>
<span style="color:#00AA00">        &quot;IPIngressPackets&quot;: &quot;[no data]&quot;,</span>
<span style="color:#00AA00">        &quot;Id&quot;: &quot;nfs-server.service&quot;,</span>
<span style="color:#00AA00">        &quot;IgnoreOnIsolate&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;IgnoreSIGPIPE&quot;: &quot;yes&quot;,</span>
<span style="color:#00AA00">        &quot;InactiveEnterTimestampMonotonic&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;InactiveExitTimestamp&quot;: &quot;Sat 2025-09-13 03:47:23 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;InactiveExitTimestampMonotonic&quot;: &quot;17798935&quot;,</span>
<span style="color:#00AA00">        &quot;InvocationID&quot;: &quot;06a65896b98d46059df932268d8b563e&quot;,</span>
<span style="color:#00AA00">        &quot;JobRunningTimeoutUSec&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;JobTimeoutAction&quot;: &quot;none&quot;,</span>
<span style="color:#00AA00">        &quot;JobTimeoutUSec&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;KeyringMode&quot;: &quot;private&quot;,</span>
<span style="color:#00AA00">        &quot;KillMode&quot;: &quot;control-group&quot;,</span>
<span style="color:#00AA00">        &quot;KillSignal&quot;: &quot;15&quot;,</span>
<span style="color:#00AA00">        &quot;LimitAS&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;LimitASSoft&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;LimitCORE&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;LimitCORESoft&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;LimitCPU&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;LimitCPUSoft&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;LimitDATA&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;LimitDATASoft&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;LimitFSIZE&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;LimitFSIZESoft&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;LimitLOCKS&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;LimitLOCKSSoft&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;LimitMEMLOCK&quot;: &quot;8388608&quot;,</span>
<span style="color:#00AA00">        &quot;LimitMEMLOCKSoft&quot;: &quot;8388608&quot;,</span>
<span style="color:#00AA00">        &quot;LimitMSGQUEUE&quot;: &quot;819200&quot;,</span>
<span style="color:#00AA00">        &quot;LimitMSGQUEUESoft&quot;: &quot;819200&quot;,</span>
<span style="color:#00AA00">        &quot;LimitNICE&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;LimitNICESoft&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;LimitNOFILE&quot;: &quot;524288&quot;,</span>
<span style="color:#00AA00">        &quot;LimitNOFILESoft&quot;: &quot;1024&quot;,</span>
<span style="color:#00AA00">        &quot;LimitNPROC&quot;: &quot;31916&quot;,</span>
<span style="color:#00AA00">        &quot;LimitNPROCSoft&quot;: &quot;31916&quot;,</span>
<span style="color:#00AA00">        &quot;LimitRSS&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;LimitRSSSoft&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;LimitRTPRIO&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;LimitRTPRIOSoft&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;LimitRTTIME&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;LimitRTTIMESoft&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;LimitSIGPENDING&quot;: &quot;31916&quot;,</span>
<span style="color:#00AA00">        &quot;LimitSIGPENDINGSoft&quot;: &quot;31916&quot;,</span>
<span style="color:#00AA00">        &quot;LimitSTACK&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;LimitSTACKSoft&quot;: &quot;8388608&quot;,</span>
<span style="color:#00AA00">        &quot;LoadState&quot;: &quot;loaded&quot;,</span>
<span style="color:#00AA00">        &quot;LockPersonality&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;LogLevelMax&quot;: &quot;-1&quot;,</span>
<span style="color:#00AA00">        &quot;LogRateLimitBurst&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;LogRateLimitIntervalUSec&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;LogsDirectoryMode&quot;: &quot;0755&quot;,</span>
<span style="color:#00AA00">        &quot;MainPID&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;ManagedOOMMemoryPressure&quot;: &quot;auto&quot;,</span>
<span style="color:#00AA00">        &quot;ManagedOOMMemoryPressureLimit&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;ManagedOOMPreference&quot;: &quot;none&quot;,</span>
<span style="color:#00AA00">        &quot;ManagedOOMSwap&quot;: &quot;auto&quot;,</span>
<span style="color:#00AA00">        &quot;MemoryAccounting&quot;: &quot;yes&quot;,</span>
<span style="color:#00AA00">        &quot;MemoryAvailable&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;MemoryCurrent&quot;: &quot;[not set]&quot;,</span>
<span style="color:#00AA00">        &quot;MemoryDenyWriteExecute&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;MemoryHigh&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;MemoryLimit&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;MemoryLow&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;MemoryMax&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;MemoryMin&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;MemorySwapMax&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;MountAPIVFS&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;NFileDescriptorStore&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;NRestarts&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;NUMAPolicy&quot;: &quot;n/a&quot;,</span>
<span style="color:#00AA00">        &quot;Names&quot;: &quot;nfs-server.service nfs-kernel-server.service&quot;,</span>
<span style="color:#00AA00">        &quot;NeedDaemonReload&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;Nice&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;NoNewPrivileges&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;NonBlocking&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;NotifyAccess&quot;: &quot;none&quot;,</span>
<span style="color:#00AA00">        &quot;OOMPolicy&quot;: &quot;stop&quot;,</span>
<span style="color:#00AA00">        &quot;OOMScoreAdjust&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;OnFailureJobMode&quot;: &quot;replace&quot;,</span>
<span style="color:#00AA00">        &quot;OnSuccessJobMode&quot;: &quot;fail&quot;,</span>
<span style="color:#00AA00">        &quot;Perpetual&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;PrivateDevices&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;PrivateIPC&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;PrivateMounts&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;PrivateNetwork&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;PrivateTmp&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;PrivateUsers&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;ProcSubset&quot;: &quot;all&quot;,</span>
<span style="color:#00AA00">        &quot;ProtectClock&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;ProtectControlGroups&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;ProtectHome&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;ProtectHostname&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;ProtectKernelLogs&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;ProtectKernelModules&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;ProtectKernelTunables&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;ProtectProc&quot;: &quot;default&quot;,</span>
<span style="color:#00AA00">        &quot;ProtectSystem&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;RefuseManualStart&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;RefuseManualStop&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;ReloadResult&quot;: &quot;success&quot;,</span>
<span style="color:#00AA00">        &quot;RemainAfterExit&quot;: &quot;yes&quot;,</span>
<span style="color:#00AA00">        &quot;RemoveIPC&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;Requires&quot;: &quot;nfs-mountd.service network.target proc-fs-nfsd.mount system.slice mnt-Volume1.mount -.mount&quot;,</span>
<span style="color:#00AA00">        &quot;RequiresMountsFor&quot;: &quot;/mnt/Volume1&quot;,</span>
<span style="color:#00AA00">        &quot;Restart&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;RestartKillSignal&quot;: &quot;15&quot;,</span>
<span style="color:#00AA00">        &quot;RestartUSec&quot;: &quot;100ms&quot;,</span>
<span style="color:#00AA00">        &quot;RestrictNamespaces&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;RestrictRealtime&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;RestrictSUIDSGID&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;Result&quot;: &quot;success&quot;,</span>
<span style="color:#00AA00">        &quot;RootDirectoryStartOnly&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;RuntimeDirectoryMode&quot;: &quot;0755&quot;,</span>
<span style="color:#00AA00">        &quot;RuntimeDirectoryPreserve&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;RuntimeMaxUSec&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;RuntimeRandomizedExtraUSec&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;SameProcessGroup&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;SecureBits&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;SendSIGHUP&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;SendSIGKILL&quot;: &quot;yes&quot;,</span>
<span style="color:#00AA00">        &quot;Slice&quot;: &quot;system.slice&quot;,</span>
<span style="color:#00AA00">        &quot;StandardError&quot;: &quot;inherit&quot;,</span>
<span style="color:#00AA00">        &quot;StandardInput&quot;: &quot;null&quot;,</span>
<span style="color:#00AA00">        &quot;StandardOutput&quot;: &quot;journal&quot;,</span>
<span style="color:#00AA00">        &quot;StartLimitAction&quot;: &quot;none&quot;,</span>
<span style="color:#00AA00">        &quot;StartLimitBurst&quot;: &quot;5&quot;,</span>
<span style="color:#00AA00">        &quot;StartLimitIntervalUSec&quot;: &quot;10s&quot;,</span>
<span style="color:#00AA00">        &quot;StartupBlockIOWeight&quot;: &quot;[not set]&quot;,</span>
<span style="color:#00AA00">        &quot;StartupCPUShares&quot;: &quot;[not set]&quot;,</span>
<span style="color:#00AA00">        &quot;StartupCPUWeight&quot;: &quot;[not set]&quot;,</span>
<span style="color:#00AA00">        &quot;StartupIOWeight&quot;: &quot;[not set]&quot;,</span>
<span style="color:#00AA00">        &quot;StateChangeTimestamp&quot;: &quot;Sat 2025-09-13 03:47:24 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;StateChangeTimestampMonotonic&quot;: &quot;17934323&quot;,</span>
<span style="color:#00AA00">        &quot;StateDirectoryMode&quot;: &quot;0755&quot;,</span>
<span style="color:#00AA00">        &quot;StatusErrno&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;StopWhenUnneeded&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;SubState&quot;: &quot;exited&quot;,</span>
<span style="color:#00AA00">        &quot;SuccessAction&quot;: &quot;none&quot;,</span>
<span style="color:#00AA00">        &quot;SyslogFacility&quot;: &quot;3&quot;,</span>
<span style="color:#00AA00">        &quot;SyslogLevel&quot;: &quot;6&quot;,</span>
<span style="color:#00AA00">        &quot;SyslogLevelPrefix&quot;: &quot;yes&quot;,</span>
<span style="color:#00AA00">        &quot;SyslogPriority&quot;: &quot;30&quot;,</span>
<span style="color:#00AA00">        &quot;SystemCallErrorNumber&quot;: &quot;2147483646&quot;,</span>
<span style="color:#00AA00">        &quot;TTYReset&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;TTYVHangup&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;TTYVTDisallocate&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;TasksAccounting&quot;: &quot;yes&quot;,</span>
<span style="color:#00AA00">        &quot;TasksCurrent&quot;: &quot;[not set]&quot;,</span>
<span style="color:#00AA00">        &quot;TasksMax&quot;: &quot;9574&quot;,</span>
<span style="color:#00AA00">        &quot;TimeoutAbortUSec&quot;: &quot;1min 30s&quot;,</span>
<span style="color:#00AA00">        &quot;TimeoutCleanUSec&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;TimeoutStartFailureMode&quot;: &quot;terminate&quot;,</span>
<span style="color:#00AA00">        &quot;TimeoutStartUSec&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;TimeoutStopFailureMode&quot;: &quot;terminate&quot;,</span>
<span style="color:#00AA00">        &quot;TimeoutStopUSec&quot;: &quot;1min 30s&quot;,</span>
<span style="color:#00AA00">        &quot;TimerSlackNSec&quot;: &quot;50000&quot;,</span>
<span style="color:#00AA00">        &quot;Transient&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;Type&quot;: &quot;oneshot&quot;,</span>
<span style="color:#00AA00">        &quot;UID&quot;: &quot;[not set]&quot;,</span>
<span style="color:#00AA00">        &quot;UMask&quot;: &quot;0022&quot;,</span>
<span style="color:#00AA00">        &quot;UnitFilePreset&quot;: &quot;enabled&quot;,</span>
<span style="color:#00AA00">        &quot;UnitFileState&quot;: &quot;enabled&quot;,</span>
<span style="color:#00AA00">        &quot;UtmpMode&quot;: &quot;init&quot;,</span>
<span style="color:#00AA00">        &quot;WantedBy&quot;: &quot;multi-user.target&quot;,</span>
<span style="color:#00AA00">        &quot;Wants&quot;: &quot;rpcbind.socket nfsdcld.service nfs-idmapd.service rpc-svcgssd.service rpc-statd-notify.service auth-rpcgss-module.service rpc-statd.service network-online.target&quot;,</span>
<span style="color:#00AA00">        &quot;WatchdogSignal&quot;: &quot;6&quot;,</span>
<span style="color:#00AA00">        &quot;WatchdogTimestampMonotonic&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;WatchdogUSec&quot;: &quot;0&quot;</span>
<span style="color:#00AA00">    }</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  00:12:14 +0200 (0:00:00.581)       0:00:34.856 ***** 

TASK [geerlingguy.docker : Load OS-specific vars.] ****************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.docker/tasks/main.yml:2</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;ansible_facts&quot;: {},</span>
<span style="color:#00AA00">    &quot;ansible_included_var_files&quot;: [</span>
<span style="color:#00AA00">        &quot;/home/dietmar/.ansible/roles/geerlingguy.docker/vars/main.yml&quot;</span>
<span style="color:#00AA00">    ],</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  00:12:14 +0200 (0:00:00.041)       0:00:34.898 ***** 
Sonntag 21 September 2025  00:12:14 +0200 (0:00:00.033)       0:00:34.931 ***** 

TASK [geerlingguy.docker : include_tasks] *************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.docker/tasks/main.yml:16</b></span>
<span style="color:#00AAAA">included: /home/dietmar/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml for ansible-nas</span>
Sonntag 21 September 2025  00:12:14 +0200 (0:00:00.056)       0:00:34.988 ***** 

TASK [geerlingguy.docker : Ensure old versions of Docker are not installed.] **************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml:2</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  00:12:15 +0200 (0:00:00.964)       0:00:35.953 ***** 

TASK [geerlingguy.docker : Ensure dependencies are installed.] ****************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml:10</b></span>
<span style="color:#AA5500">changed: [ansible-nas] =&gt; {</span>
<span style="color:#AA5500">    &quot;cache_update_time&quot;: 1758331880,</span>
<span style="color:#AA5500">    &quot;cache_updated&quot;: false,</span>
<span style="color:#AA5500">    &quot;changed&quot;: true</span>
<span style="color:#AA5500">}</span>

<span style="color:#AA5500">STDOUT:</span>

<span style="color:#AA5500">Reading package lists...</span>
<span style="color:#AA5500">Building dependency tree...</span>
<span style="color:#AA5500">Reading state information...</span>
<span style="color:#AA5500">The following package was automatically installed and is no longer required:</span>
<span style="color:#AA5500">  rpicam-apps-lite</span>
<span style="color:#AA5500">Use &apos;sudo apt autoremove&apos; to remove it.</span>
<span style="color:#AA5500">The following NEW packages will be installed:</span>
<span style="color:#AA5500">  apt-transport-https</span>
<span style="color:#AA5500">0 upgraded, 1 newly installed, 0 to remove and 8 not upgraded.</span>
<span style="color:#AA5500">Need to get 25.2 kB of archives.</span>
<span style="color:#AA5500">After this operation, 35.8 kB of additional disk space will be used.</span>
<span style="color:#AA5500">Get:1 http://deb.debian.org/debian bookworm/main arm64 apt-transport-https all 2.6.1 [25.2 kB]</span>
<span style="color:#AA5500">Fetched 25.2 kB in 0s (521 kB/s)</span>
<span style="color:#AA5500">Selecting previously unselected package apt-transport-https.</span>
<span style="color:#AA5500">(Reading database ... 97762 files and directories currently installed.)</span>
<span style="color:#AA5500">Preparing to unpack .../apt-transport-https_2.6.1_all.deb ...</span>
<span style="color:#AA5500">Unpacking apt-transport-https (2.6.1) ...</span>
<span style="color:#AA5500">Setting up apt-transport-https (2.6.1) ...</span>

Sonntag 21 September 2025  00:12:19 +0200 (0:00:03.149)       0:00:39.102 ***** 

TASK [geerlingguy.docker : Ensure additional dependencies are installed (on Ubuntu &lt; 20.04 and any other systems).] ***********************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml:18</b></span>
<span style="color:#AA5500">changed: [ansible-nas] =&gt; {</span>
<span style="color:#AA5500">    &quot;cache_update_time&quot;: 1758331880,</span>
<span style="color:#AA5500">    &quot;cache_updated&quot;: false,</span>
<span style="color:#AA5500">    &quot;changed&quot;: true</span>
<span style="color:#AA5500">}</span>

<span style="color:#AA5500">STDOUT:</span>

<span style="color:#AA5500">Reading package lists...</span>
<span style="color:#AA5500">Building dependency tree...</span>
<span style="color:#AA5500">Reading state information...</span>
<span style="color:#AA5500">The following package was automatically installed and is no longer required:</span>
<span style="color:#AA5500">  rpicam-apps-lite</span>
<span style="color:#AA5500">Use &apos;sudo apt autoremove&apos; to remove it.</span>
<span style="color:#AA5500">The following NEW packages will be installed:</span>
<span style="color:#AA5500">  gnupg2</span>
<span style="color:#AA5500">0 upgraded, 1 newly installed, 0 to remove and 8 not upgraded.</span>
<span style="color:#AA5500">Need to get 446 kB of archives.</span>
<span style="color:#AA5500">After this operation, 464 kB of additional disk space will be used.</span>
<span style="color:#AA5500">Get:1 http://deb.debian.org/debian bookworm/main arm64 gnupg2 all 2.2.40-1.1+deb12u1 [446 kB]</span>
<span style="color:#AA5500">Fetched 446 kB in 0s (4521 kB/s)</span>
<span style="color:#AA5500">Selecting previously unselected package gnupg2.</span>
<span style="color:#AA5500">(Reading database ... 97766 files and directories currently installed.)</span>
<span style="color:#AA5500">Preparing to unpack .../gnupg2_2.2.40-1.1+deb12u1_all.deb ...</span>
<span style="color:#AA5500">Unpacking gnupg2 (2.2.40-1.1+deb12u1) ...</span>
<span style="color:#AA5500">Setting up gnupg2 (2.2.40-1.1+deb12u1) ...</span>
<span style="color:#AA5500">Processing triggers for man-db (2.11.2-2) ...</span>

Sonntag 21 September 2025  00:12:22 +0200 (0:00:03.595)       0:00:42.698 ***** 
Sonntag 21 September 2025  00:12:22 +0200 (0:00:00.042)       0:00:42.741 ***** 

TASK [geerlingguy.docker : Add Docker apt key.] *******************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml:30</b></span>
<span style="color:#AA5500">changed: [ansible-nas] =&gt; {</span>
<span style="color:#AA5500">    &quot;changed&quot;: true,</span>
<span style="color:#AA5500">    &quot;checksum_dest&quot;: null,</span>
<span style="color:#AA5500">    &quot;checksum_src&quot;: &quot;f5b5bd1487cefc0c53c947e11ca202e86b33dbad&quot;,</span>
<span style="color:#AA5500">    &quot;dest&quot;: &quot;/etc/apt/trusted.gpg.d/docker.asc&quot;,</span>
<span style="color:#AA5500">    &quot;elapsed&quot;: 0,</span>
<span style="color:#AA5500">    &quot;gid&quot;: 0,</span>
<span style="color:#AA5500">    &quot;group&quot;: &quot;root&quot;,</span>
<span style="color:#AA5500">    &quot;md5sum&quot;: &quot;1afae06b34a13c1b3d9cb61a26285a15&quot;,</span>
<span style="color:#AA5500">    &quot;mode&quot;: &quot;0644&quot;,</span>
<span style="color:#AA5500">    &quot;owner&quot;: &quot;root&quot;,</span>
<span style="color:#AA5500">    &quot;size&quot;: 3817,</span>
<span style="color:#AA5500">    &quot;src&quot;: &quot;/home/dietmar/.ansible/tmp/ansible-tmp-1758406342.801996-85425-158626313994763/tmp68prpba2&quot;,</span>
<span style="color:#AA5500">    &quot;state&quot;: &quot;file&quot;,</span>
<span style="color:#AA5500">    &quot;status_code&quot;: 200,</span>
<span style="color:#AA5500">    &quot;uid&quot;: 0,</span>
<span style="color:#AA5500">    &quot;url&quot;: &quot;https://download.docker.com/linux/debian/gpg&quot;</span>
<span style="color:#AA5500">}</span>

<span style="color:#AA5500">MSG:</span>

<span style="color:#AA5500">OK (3817 bytes)</span>
Sonntag 21 September 2025  00:12:23 +0200 (0:00:00.805)       0:00:43.547 ***** 
Sonntag 21 September 2025  00:12:23 +0200 (0:00:00.067)       0:00:43.614 ***** 
Sonntag 21 September 2025  00:12:23 +0200 (0:00:00.077)       0:00:43.691 ***** 

TASK [geerlingguy.docker : Add Docker repository.] ****************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml:50</b></span>
<span style="color:#AA5500">changed: [ansible-nas] =&gt; {</span>
<span style="color:#AA5500">    &quot;changed&quot;: true,</span>
<span style="color:#AA5500">    &quot;repo&quot;: &quot;deb [arch=arm64 signed-by=/etc/apt/trusted.gpg.d/docker.asc] https://download.docker.com/linux/debian bookworm stable&quot;,</span>
<span style="color:#AA5500">    &quot;sources_added&quot;: [</span>
<span style="color:#AA5500">        &quot;/etc/apt/sources.list.d/download_docker_com_linux_ubuntu.list&quot;</span>
<span style="color:#AA5500">    ],</span>
<span style="color:#AA5500">    &quot;sources_removed&quot;: [],</span>
<span style="color:#AA5500">    &quot;state&quot;: &quot;present&quot;</span>
<span style="color:#AA5500">}</span>
Sonntag 21 September 2025  00:12:28 +0200 (0:00:05.259)       0:00:48.950 ***** 
Sonntag 21 September 2025  00:12:28 +0200 (0:00:00.042)       0:00:48.993 ***** 
<span style="color:#0000AA">Notification for handler restart docker has been saved.</span>

TASK [geerlingguy.docker : Install Docker packages (with downgrade option).] **************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.docker/tasks/main.yml:27</b></span>
<span style="color:#AA5500">changed: [ansible-nas] =&gt; {</span>
<span style="color:#AA5500">    &quot;cache_update_time&quot;: 1758406347,</span>
<span style="color:#AA5500">    &quot;cache_updated&quot;: false,</span>
<span style="color:#AA5500">    &quot;changed&quot;: true</span>
<span style="color:#AA5500">}</span>

<span style="color:#AA5500">STDOUT:</span>

<span style="color:#AA5500">Reading package lists...</span>
<span style="color:#AA5500">Building dependency tree...</span>
<span style="color:#AA5500">Reading state information...</span>
<span style="color:#AA5500">The following package was automatically installed and is no longer required:</span>
<span style="color:#AA5500">  rpicam-apps-lite</span>
<span style="color:#AA5500">Use &apos;sudo apt autoremove&apos; to remove it.</span>
<span style="color:#AA5500">The following additional packages will be installed:</span>
<span style="color:#AA5500">  docker-compose-plugin git git-man liberror-perl pigz slirp4netns</span>
<span style="color:#AA5500">Suggested packages:</span>
<span style="color:#AA5500">  cgroupfs-mount | cgroup-lite docker-model-plugin git-daemon-run</span>
<span style="color:#AA5500">  | git-daemon-sysvinit git-doc git-email git-gui gitk gitweb git-cvs</span>
<span style="color:#AA5500">  git-mediawiki git-svn</span>
<span style="color:#AA5500">The following NEW packages will be installed:</span>
<span style="color:#AA5500">  containerd.io docker-buildx-plugin docker-ce docker-ce-cli</span>
<span style="color:#AA5500">  docker-ce-rootless-extras docker-compose-plugin git git-man liberror-perl</span>
<span style="color:#AA5500">  pigz slirp4netns</span>
<span style="color:#AA5500">0 upgraded, 11 newly installed, 0 to remove and 8 not upgraded.</span>
<span style="color:#AA5500">Need to get 95.9 MB of archives.</span>
<span style="color:#AA5500">After this operation, 442 MB of additional disk space will be used.</span>
<span style="color:#AA5500">Get:1 http://deb.debian.org/debian bookworm/main arm64 pigz arm64 2.6-1 [56.2 kB]</span>
<span style="color:#AA5500">Get:2 http://deb.debian.org/debian bookworm/main arm64 liberror-perl all 0.17029-2 [29.0 kB]</span>
<span style="color:#AA5500">Get:3 http://deb.debian.org/debian bookworm/main arm64 git-man all 1:2.39.5-0+deb12u2 [2053 kB]</span>
<span style="color:#AA5500">Get:4 https://download.docker.com/linux/debian bookworm/stable arm64 containerd.io arm64 1.7.27-1 [22.8 MB]</span>
<span style="color:#AA5500">Get:5 http://deb.debian.org/debian bookworm/main arm64 git arm64 1:2.39.5-0+deb12u2 [7148 kB]</span>
<span style="color:#AA5500">Get:6 https://download.docker.com/linux/debian bookworm/stable arm64 docker-ce-cli arm64 5:28.4.0-1~debian.12~bookworm [14.9 MB]</span>
<span style="color:#AA5500">Get:7 https://download.docker.com/linux/debian bookworm/stable arm64 docker-ce arm64 5:28.4.0-1~debian.12~bookworm [17.0 MB]</span>
<span style="color:#AA5500">Get:8 https://download.docker.com/linux/debian bookworm/stable arm64 docker-buildx-plugin arm64 0.28.0-0~debian.12~bookworm [13.9 MB]</span>
<span style="color:#AA5500">Get:9 https://download.docker.com/linux/debian bookworm/stable arm64 docker-ce-rootless-extras arm64 5:28.4.0-1~debian.12~bookworm [5819 kB]</span>
<span style="color:#AA5500">Get:10 https://download.docker.com/linux/debian bookworm/stable arm64 docker-compose-plugin arm64 2.39.4-0~debian.12~bookworm [12.3 MB]</span>
<span style="color:#AA5500">Get:11 http://deb.debian.org/debian bookworm/main arm64 slirp4netns arm64 1.2.0-1 [36.6 kB]</span>
<span style="color:#AA5500">Fetched 95.9 MB in 9s (10.5 MB/s)</span>
<span style="color:#AA5500">Selecting previously unselected package containerd.io.</span>
<span style="color:#AA5500">(Reading database ... 97773 files and directories currently installed.)</span>
<span style="color:#AA5500">Preparing to unpack .../00-containerd.io_1.7.27-1_arm64.deb ...</span>
<span style="color:#AA5500">Unpacking containerd.io (1.7.27-1) ...</span>
<span style="color:#AA5500">Selecting previously unselected package docker-ce-cli.</span>
<span style="color:#AA5500">Preparing to unpack .../01-docker-ce-cli_5%3a28.4.0-1~debian.12~bookworm_arm64.deb ...</span>
<span style="color:#AA5500">Unpacking docker-ce-cli (5:28.4.0-1~debian.12~bookworm) ...</span>
<span style="color:#AA5500">Selecting previously unselected package docker-ce.</span>
<span style="color:#AA5500">Preparing to unpack .../02-docker-ce_5%3a28.4.0-1~debian.12~bookworm_arm64.deb ...</span>
<span style="color:#AA5500">Unpacking docker-ce (5:28.4.0-1~debian.12~bookworm) ...</span>
<span style="color:#AA5500">Selecting previously unselected package pigz.</span>
<span style="color:#AA5500">Preparing to unpack .../03-pigz_2.6-1_arm64.deb ...</span>
<span style="color:#AA5500">Unpacking pigz (2.6-1) ...</span>
<span style="color:#AA5500">Selecting previously unselected package docker-buildx-plugin.</span>
<span style="color:#AA5500">Preparing to unpack .../04-docker-buildx-plugin_0.28.0-0~debian.12~bookworm_arm64.deb ...</span>
<span style="color:#AA5500">Unpacking docker-buildx-plugin (0.28.0-0~debian.12~bookworm) ...</span>
<span style="color:#AA5500">Selecting previously unselected package docker-ce-rootless-extras.</span>
<span style="color:#AA5500">Preparing to unpack .../05-docker-ce-rootless-extras_5%3a28.4.0-1~debian.12~bookworm_arm64.deb ...</span>
<span style="color:#AA5500">Unpacking docker-ce-rootless-extras (5:28.4.0-1~debian.12~bookworm) ...</span>
<span style="color:#AA5500">Selecting previously unselected package docker-compose-plugin.</span>
<span style="color:#AA5500">Preparing to unpack .../06-docker-compose-plugin_2.39.4-0~debian.12~bookworm_arm64.deb ...</span>
<span style="color:#AA5500">Unpacking docker-compose-plugin (2.39.4-0~debian.12~bookworm) ...</span>
<span style="color:#AA5500">Selecting previously unselected package liberror-perl.</span>
<span style="color:#AA5500">Preparing to unpack .../07-liberror-perl_0.17029-2_all.deb ...</span>
<span style="color:#AA5500">Unpacking liberror-perl (0.17029-2) ...</span>
<span style="color:#AA5500">Selecting previously unselected package git-man.</span>
<span style="color:#AA5500">Preparing to unpack .../08-git-man_1%3a2.39.5-0+deb12u2_all.deb ...</span>
<span style="color:#AA5500">Unpacking git-man (1:2.39.5-0+deb12u2) ...</span>
<span style="color:#AA5500">Selecting previously unselected package git.</span>
<span style="color:#AA5500">Preparing to unpack .../09-git_1%3a2.39.5-0+deb12u2_arm64.deb ...</span>
<span style="color:#AA5500">Unpacking git (1:2.39.5-0+deb12u2) ...</span>
<span style="color:#AA5500">Selecting previously unselected package slirp4netns.</span>
<span style="color:#AA5500">Preparing to unpack .../10-slirp4netns_1.2.0-1_arm64.deb ...</span>
<span style="color:#AA5500">Unpacking slirp4netns (1.2.0-1) ...</span>
<span style="color:#AA5500">Setting up slirp4netns (1.2.0-1) ...</span>
<span style="color:#AA5500">Setting up liberror-perl (0.17029-2) ...</span>
<span style="color:#AA5500">Setting up docker-buildx-plugin (0.28.0-0~debian.12~bookworm) ...</span>
<span style="color:#AA5500">Setting up containerd.io (1.7.27-1) ...</span>
<span style="color:#AA5500">Created symlink /etc/systemd/system/multi-user.target.wants/containerd.service → /lib/systemd/system/containerd.service.</span>
<span style="color:#AA5500">Setting up docker-compose-plugin (2.39.4-0~debian.12~bookworm) ...</span>
<span style="color:#AA5500">Setting up docker-ce-cli (5:28.4.0-1~debian.12~bookworm) ...</span>
<span style="color:#AA5500">Setting up pigz (2.6-1) ...</span>
<span style="color:#AA5500">Setting up git-man (1:2.39.5-0+deb12u2) ...</span>
<span style="color:#AA5500">Setting up docker-ce-rootless-extras (5:28.4.0-1~debian.12~bookworm) ...</span>
<span style="color:#AA5500">Setting up docker-ce (5:28.4.0-1~debian.12~bookworm) ...</span>
<span style="color:#AA5500">Created symlink /etc/systemd/system/multi-user.target.wants/docker.service → /lib/systemd/system/docker.service.</span>
<span style="color:#AA5500">Created symlink /etc/systemd/system/sockets.target.wants/docker.socket → /lib/systemd/system/docker.socket.</span>
<span style="color:#AA5500">Setting up git (1:2.39.5-0+deb12u2) ...</span>
<span style="color:#AA5500">Processing triggers for man-db (2.11.2-2) ...</span>

Sonntag 21 September 2025  00:12:50 +0200 (0:00:21.354)       0:01:10.347 ***** 
Sonntag 21 September 2025  00:12:50 +0200 (0:00:00.111)       0:01:10.459 ***** 

TASK [geerlingguy.docker : Install docker-compose-plugin (with downgrade option).] ********************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.docker/tasks/main.yml:44</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;cache_update_time&quot;: 1758406347,</span>
<span style="color:#00AA00">    &quot;cache_updated&quot;: false,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  00:12:51 +0200 (0:00:01.423)       0:01:11.883 ***** 
Sonntag 21 September 2025  00:12:51 +0200 (0:00:00.069)       0:01:11.952 ***** 
Sonntag 21 September 2025  00:12:51 +0200 (0:00:00.067)       0:01:12.019 ***** 

TASK [geerlingguy.docker : Ensure Docker is started and enabled at boot.] *****************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.docker/tasks/main.yml:68</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;enabled&quot;: true,</span>
<span style="color:#00AA00">    &quot;name&quot;: &quot;docker&quot;,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;started&quot;,</span>
<span style="color:#00AA00">    &quot;status&quot;: {</span>
<span style="color:#00AA00">        &quot;ActiveEnterTimestamp&quot;: &quot;Sun 2025-09-21 00:12:48 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;ActiveEnterTimestampMonotonic&quot;: &quot;678342761142&quot;,</span>
<span style="color:#00AA00">        &quot;ActiveExitTimestampMonotonic&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;ActiveState&quot;: &quot;active&quot;,</span>
<span style="color:#00AA00">        &quot;After&quot;: &quot;containerd.service network-online.target sysinit.target docker.socket time-set.target basic.target firewalld.service nss-lookup.target systemd-journald.socket system.slice&quot;,</span>
<span style="color:#00AA00">        &quot;AllowIsolate&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;AssertResult&quot;: &quot;yes&quot;,</span>
<span style="color:#00AA00">        &quot;AssertTimestamp&quot;: &quot;Sun 2025-09-21 00:12:48 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;AssertTimestampMonotonic&quot;: &quot;678342356876&quot;,</span>
<span style="color:#00AA00">        &quot;Before&quot;: &quot;multi-user.target shutdown.target&quot;,</span>
<span style="color:#00AA00">        &quot;BlockIOAccounting&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;BlockIOWeight&quot;: &quot;[not set]&quot;,</span>
<span style="color:#00AA00">        &quot;CPUAccounting&quot;: &quot;yes&quot;,</span>
<span style="color:#00AA00">        &quot;CPUAffinityFromNUMA&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;CPUQuotaPerSecUSec&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;CPUQuotaPeriodUSec&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;CPUSchedulingPolicy&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;CPUSchedulingPriority&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;CPUSchedulingResetOnFork&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;CPUShares&quot;: &quot;[not set]&quot;,</span>
<span style="color:#00AA00">        &quot;CPUUsageNSec&quot;: &quot;202774000&quot;,</span>
<span style="color:#00AA00">        &quot;CPUWeight&quot;: &quot;[not set]&quot;,</span>
<span style="color:#00AA00">        &quot;CacheDirectoryMode&quot;: &quot;0755&quot;,</span>
<span style="color:#00AA00">        &quot;CanFreeze&quot;: &quot;yes&quot;,</span>
<span style="color:#00AA00">        &quot;CanIsolate&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;CanReload&quot;: &quot;yes&quot;,</span>
<span style="color:#00AA00">        &quot;CanStart&quot;: &quot;yes&quot;,</span>
<span style="color:#00AA00">        &quot;CanStop&quot;: &quot;yes&quot;,</span>
<span style="color:#00AA00">        &quot;CapabilityBoundingSet&quot;: &quot;cap_chown cap_dac_override cap_dac_read_search cap_fowner cap_fsetid cap_kill cap_setgid cap_setuid cap_setpcap cap_linux_immutable cap_net_bind_service cap_net_broadcast cap_net_admin cap_net_raw cap_ipc_lock cap_ipc_owner cap_sys_module cap_sys_rawio cap_sys_chroot cap_sys_ptrace cap_sys_pacct cap_sys_admin cap_sys_boot cap_sys_nice cap_sys_resource cap_sys_time cap_sys_tty_config cap_mknod cap_lease cap_audit_write cap_audit_control cap_setfcap cap_mac_override cap_mac_admin cap_syslog cap_wake_alarm cap_block_suspend cap_audit_read cap_perfmon cap_bpf cap_checkpoint_restore&quot;,</span>
<span style="color:#00AA00">        &quot;CleanResult&quot;: &quot;success&quot;,</span>
<span style="color:#00AA00">        &quot;CollectMode&quot;: &quot;inactive&quot;,</span>
<span style="color:#00AA00">        &quot;ConditionResult&quot;: &quot;yes&quot;,</span>
<span style="color:#00AA00">        &quot;ConditionTimestamp&quot;: &quot;Sun 2025-09-21 00:12:48 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;ConditionTimestampMonotonic&quot;: &quot;678342356874&quot;,</span>
<span style="color:#00AA00">        &quot;ConfigurationDirectoryMode&quot;: &quot;0755&quot;,</span>
<span style="color:#00AA00">        &quot;Conflicts&quot;: &quot;shutdown.target&quot;,</span>
<span style="color:#00AA00">        &quot;ControlGroup&quot;: &quot;/system.slice/docker.service&quot;,</span>
<span style="color:#00AA00">        &quot;ControlGroupId&quot;: &quot;47271&quot;,</span>
<span style="color:#00AA00">        &quot;ControlPID&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;CoredumpFilter&quot;: &quot;0x33&quot;,</span>
<span style="color:#00AA00">        &quot;DefaultDependencies&quot;: &quot;yes&quot;,</span>
<span style="color:#00AA00">        &quot;DefaultMemoryLow&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;DefaultMemoryMin&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;Delegate&quot;: &quot;yes&quot;,</span>
<span style="color:#00AA00">        &quot;DelegateControllers&quot;: &quot;cpu cpuset io memory pids&quot;,</span>
<span style="color:#00AA00">        &quot;Description&quot;: &quot;Docker Application Container Engine&quot;,</span>
<span style="color:#00AA00">        &quot;DevicePolicy&quot;: &quot;auto&quot;,</span>
<span style="color:#00AA00">        &quot;Documentation&quot;: &quot;https://docs.docker.com&quot;,</span>
<span style="color:#00AA00">        &quot;DynamicUser&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;EffectiveCPUs&quot;: &quot;0-3&quot;,</span>
<span style="color:#00AA00">        &quot;EffectiveMemoryNodes&quot;: &quot;0-7&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainCode&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainExitTimestampMonotonic&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainPID&quot;: &quot;1371484&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainStartTimestamp&quot;: &quot;Sun 2025-09-21 00:12:48 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainStartTimestampMonotonic&quot;: &quot;678342357985&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainStatus&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;ExecReload&quot;: &quot;{ path=/bin/kill ; argv[]=/bin/kill -s HUP $MAINPID ; ignore_errors=no ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }&quot;,</span>
<span style="color:#00AA00">        &quot;ExecReloadEx&quot;: &quot;{ path=/bin/kill ; argv[]=/bin/kill -s HUP $MAINPID ; flags= ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }&quot;,</span>
<span style="color:#00AA00">        &quot;ExecStart&quot;: &quot;{ path=/usr/bin/dockerd ; argv[]=/usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock ; ignore_errors=no ; start_time=[Sun 2025-09-21 00:12:48 CEST] ; stop_time=[n/a] ; pid=1371484 ; code=(null) ; status=0/0 }&quot;,</span>
<span style="color:#00AA00">        &quot;ExecStartEx&quot;: &quot;{ path=/usr/bin/dockerd ; argv[]=/usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock ; flags= ; start_time=[Sun 2025-09-21 00:12:48 CEST] ; stop_time=[n/a] ; pid=1371484 ; code=(null) ; status=0/0 }&quot;,</span>
<span style="color:#00AA00">        &quot;ExitType&quot;: &quot;main&quot;,</span>
<span style="color:#00AA00">        &quot;FailureAction&quot;: &quot;none&quot;,</span>
<span style="color:#00AA00">        &quot;FileDescriptorStoreMax&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;FinalKillSignal&quot;: &quot;9&quot;,</span>
<span style="color:#00AA00">        &quot;FragmentPath&quot;: &quot;/lib/systemd/system/docker.service&quot;,</span>
<span style="color:#00AA00">        &quot;FreezerState&quot;: &quot;running&quot;,</span>
<span style="color:#00AA00">        &quot;GID&quot;: &quot;[not set]&quot;,</span>
<span style="color:#00AA00">        &quot;GuessMainPID&quot;: &quot;yes&quot;,</span>
<span style="color:#00AA00">        &quot;IOAccounting&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;IOReadBytes&quot;: &quot;18446744073709551615&quot;,</span>
<span style="color:#00AA00">        &quot;IOReadOperations&quot;: &quot;18446744073709551615&quot;,</span>
<span style="color:#00AA00">        &quot;IOSchedulingClass&quot;: &quot;2&quot;,</span>
<span style="color:#00AA00">        &quot;IOSchedulingPriority&quot;: &quot;4&quot;,</span>
<span style="color:#00AA00">        &quot;IOWeight&quot;: &quot;[not set]&quot;,</span>
<span style="color:#00AA00">        &quot;IOWriteBytes&quot;: &quot;18446744073709551615&quot;,</span>
<span style="color:#00AA00">        &quot;IOWriteOperations&quot;: &quot;18446744073709551615&quot;,</span>
<span style="color:#00AA00">        &quot;IPAccounting&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;IPEgressBytes&quot;: &quot;[no data]&quot;,</span>
<span style="color:#00AA00">        &quot;IPEgressPackets&quot;: &quot;[no data]&quot;,</span>
<span style="color:#00AA00">        &quot;IPIngressBytes&quot;: &quot;[no data]&quot;,</span>
<span style="color:#00AA00">        &quot;IPIngressPackets&quot;: &quot;[no data]&quot;,</span>
<span style="color:#00AA00">        &quot;Id&quot;: &quot;docker.service&quot;,</span>
<span style="color:#00AA00">        &quot;IgnoreOnIsolate&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;IgnoreSIGPIPE&quot;: &quot;yes&quot;,</span>
<span style="color:#00AA00">        &quot;InactiveEnterTimestampMonotonic&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;InactiveExitTimestamp&quot;: &quot;Sun 2025-09-21 00:12:48 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;InactiveExitTimestampMonotonic&quot;: &quot;678342358408&quot;,</span>
<span style="color:#00AA00">        &quot;InvocationID&quot;: &quot;f7cb2757e0c24167a1312789b269cfb6&quot;,</span>
<span style="color:#00AA00">        &quot;JobRunningTimeoutUSec&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;JobTimeoutAction&quot;: &quot;none&quot;,</span>
<span style="color:#00AA00">        &quot;JobTimeoutUSec&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;KeyringMode&quot;: &quot;private&quot;,</span>
<span style="color:#00AA00">        &quot;KillMode&quot;: &quot;process&quot;,</span>
<span style="color:#00AA00">        &quot;KillSignal&quot;: &quot;15&quot;,</span>
<span style="color:#00AA00">        &quot;LimitAS&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;LimitASSoft&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;LimitCORE&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;LimitCORESoft&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;LimitCPU&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;LimitCPUSoft&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;LimitDATA&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;LimitDATASoft&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;LimitFSIZE&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;LimitFSIZESoft&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;LimitLOCKS&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;LimitLOCKSSoft&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;LimitMEMLOCK&quot;: &quot;8388608&quot;,</span>
<span style="color:#00AA00">        &quot;LimitMEMLOCKSoft&quot;: &quot;8388608&quot;,</span>
<span style="color:#00AA00">        &quot;LimitMSGQUEUE&quot;: &quot;819200&quot;,</span>
<span style="color:#00AA00">        &quot;LimitMSGQUEUESoft&quot;: &quot;819200&quot;,</span>
<span style="color:#00AA00">        &quot;LimitNICE&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;LimitNICESoft&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;LimitNOFILE&quot;: &quot;524288&quot;,</span>
<span style="color:#00AA00">        &quot;LimitNOFILESoft&quot;: &quot;1024&quot;,</span>
<span style="color:#00AA00">        &quot;LimitNPROC&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;LimitNPROCSoft&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;LimitRSS&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;LimitRSSSoft&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;LimitRTPRIO&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;LimitRTPRIOSoft&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;LimitRTTIME&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;LimitRTTIMESoft&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;LimitSIGPENDING&quot;: &quot;31916&quot;,</span>
<span style="color:#00AA00">        &quot;LimitSIGPENDINGSoft&quot;: &quot;31916&quot;,</span>
<span style="color:#00AA00">        &quot;LimitSTACK&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;LimitSTACKSoft&quot;: &quot;8388608&quot;,</span>
<span style="color:#00AA00">        &quot;LoadState&quot;: &quot;loaded&quot;,</span>
<span style="color:#00AA00">        &quot;LockPersonality&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;LogLevelMax&quot;: &quot;-1&quot;,</span>
<span style="color:#00AA00">        &quot;LogRateLimitBurst&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;LogRateLimitIntervalUSec&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;LogsDirectoryMode&quot;: &quot;0755&quot;,</span>
<span style="color:#00AA00">        &quot;MainPID&quot;: &quot;1371484&quot;,</span>
<span style="color:#00AA00">        &quot;ManagedOOMMemoryPressure&quot;: &quot;auto&quot;,</span>
<span style="color:#00AA00">        &quot;ManagedOOMMemoryPressureLimit&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;ManagedOOMPreference&quot;: &quot;none&quot;,</span>
<span style="color:#00AA00">        &quot;ManagedOOMSwap&quot;: &quot;auto&quot;,</span>
<span style="color:#00AA00">        &quot;MemoryAccounting&quot;: &quot;yes&quot;,</span>
<span style="color:#00AA00">        &quot;MemoryAvailable&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;MemoryCurrent&quot;: &quot;[not set]&quot;,</span>
<span style="color:#00AA00">        &quot;MemoryDenyWriteExecute&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;MemoryHigh&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;MemoryLimit&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;MemoryLow&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;MemoryMax&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;MemoryMin&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;MemorySwapMax&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;MountAPIVFS&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;NFileDescriptorStore&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;NRestarts&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;NUMAPolicy&quot;: &quot;n/a&quot;,</span>
<span style="color:#00AA00">        &quot;Names&quot;: &quot;docker.service&quot;,</span>
<span style="color:#00AA00">        &quot;NeedDaemonReload&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;Nice&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;NoNewPrivileges&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;NonBlocking&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;NotifyAccess&quot;: &quot;main&quot;,</span>
<span style="color:#00AA00">        &quot;OOMPolicy&quot;: &quot;continue&quot;,</span>
<span style="color:#00AA00">        &quot;OOMScoreAdjust&quot;: &quot;-500&quot;,</span>
<span style="color:#00AA00">        &quot;OnFailureJobMode&quot;: &quot;replace&quot;,</span>
<span style="color:#00AA00">        &quot;OnSuccessJobMode&quot;: &quot;fail&quot;,</span>
<span style="color:#00AA00">        &quot;Perpetual&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;PrivateDevices&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;PrivateIPC&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;PrivateMounts&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;PrivateNetwork&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;PrivateTmp&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;PrivateUsers&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;ProcSubset&quot;: &quot;all&quot;,</span>
<span style="color:#00AA00">        &quot;ProtectClock&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;ProtectControlGroups&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;ProtectHome&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;ProtectHostname&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;ProtectKernelLogs&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;ProtectKernelModules&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;ProtectKernelTunables&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;ProtectProc&quot;: &quot;default&quot;,</span>
<span style="color:#00AA00">        &quot;ProtectSystem&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;RefuseManualStart&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;RefuseManualStop&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;ReloadResult&quot;: &quot;success&quot;,</span>
<span style="color:#00AA00">        &quot;RemainAfterExit&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;RemoveIPC&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;Requires&quot;: &quot;docker.socket sysinit.target system.slice&quot;,</span>
<span style="color:#00AA00">        &quot;Restart&quot;: &quot;always&quot;,</span>
<span style="color:#00AA00">        &quot;RestartKillSignal&quot;: &quot;15&quot;,</span>
<span style="color:#00AA00">        &quot;RestartUSec&quot;: &quot;2s&quot;,</span>
<span style="color:#00AA00">        &quot;RestrictNamespaces&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;RestrictRealtime&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;RestrictSUIDSGID&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;Result&quot;: &quot;success&quot;,</span>
<span style="color:#00AA00">        &quot;RootDirectoryStartOnly&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;RuntimeDirectoryMode&quot;: &quot;0755&quot;,</span>
<span style="color:#00AA00">        &quot;RuntimeDirectoryPreserve&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;RuntimeMaxUSec&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;RuntimeRandomizedExtraUSec&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;SameProcessGroup&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;SecureBits&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;SendSIGHUP&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;SendSIGKILL&quot;: &quot;yes&quot;,</span>
<span style="color:#00AA00">        &quot;Slice&quot;: &quot;system.slice&quot;,</span>
<span style="color:#00AA00">        &quot;StandardError&quot;: &quot;inherit&quot;,</span>
<span style="color:#00AA00">        &quot;StandardInput&quot;: &quot;null&quot;,</span>
<span style="color:#00AA00">        &quot;StandardOutput&quot;: &quot;journal&quot;,</span>
<span style="color:#00AA00">        &quot;StartLimitAction&quot;: &quot;none&quot;,</span>
<span style="color:#00AA00">        &quot;StartLimitBurst&quot;: &quot;3&quot;,</span>
<span style="color:#00AA00">        &quot;StartLimitIntervalUSec&quot;: &quot;1min&quot;,</span>
<span style="color:#00AA00">        &quot;StartupBlockIOWeight&quot;: &quot;[not set]&quot;,</span>
<span style="color:#00AA00">        &quot;StartupCPUShares&quot;: &quot;[not set]&quot;,</span>
<span style="color:#00AA00">        &quot;StartupCPUWeight&quot;: &quot;[not set]&quot;,</span>
<span style="color:#00AA00">        &quot;StartupIOWeight&quot;: &quot;[not set]&quot;,</span>
<span style="color:#00AA00">        &quot;StateChangeTimestamp&quot;: &quot;Sun 2025-09-21 00:12:48 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;StateChangeTimestampMonotonic&quot;: &quot;678342761142&quot;,</span>
<span style="color:#00AA00">        &quot;StateDirectoryMode&quot;: &quot;0755&quot;,</span>
<span style="color:#00AA00">        &quot;StatusErrno&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;StopWhenUnneeded&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;SubState&quot;: &quot;running&quot;,</span>
<span style="color:#00AA00">        &quot;SuccessAction&quot;: &quot;none&quot;,</span>
<span style="color:#00AA00">        &quot;SyslogFacility&quot;: &quot;3&quot;,</span>
<span style="color:#00AA00">        &quot;SyslogLevel&quot;: &quot;6&quot;,</span>
<span style="color:#00AA00">        &quot;SyslogLevelPrefix&quot;: &quot;yes&quot;,</span>
<span style="color:#00AA00">        &quot;SyslogPriority&quot;: &quot;30&quot;,</span>
<span style="color:#00AA00">        &quot;SystemCallErrorNumber&quot;: &quot;2147483646&quot;,</span>
<span style="color:#00AA00">        &quot;TTYReset&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;TTYVHangup&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;TTYVTDisallocate&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;TasksAccounting&quot;: &quot;yes&quot;,</span>
<span style="color:#00AA00">        &quot;TasksCurrent&quot;: &quot;11&quot;,</span>
<span style="color:#00AA00">        &quot;TasksMax&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;TimeoutAbortUSec&quot;: &quot;1min 30s&quot;,</span>
<span style="color:#00AA00">        &quot;TimeoutCleanUSec&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;TimeoutStartFailureMode&quot;: &quot;terminate&quot;,</span>
<span style="color:#00AA00">        &quot;TimeoutStartUSec&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;TimeoutStopFailureMode&quot;: &quot;terminate&quot;,</span>
<span style="color:#00AA00">        &quot;TimeoutStopUSec&quot;: &quot;1min 30s&quot;,</span>
<span style="color:#00AA00">        &quot;TimerSlackNSec&quot;: &quot;50000&quot;,</span>
<span style="color:#00AA00">        &quot;Transient&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;TriggeredBy&quot;: &quot;docker.socket&quot;,</span>
<span style="color:#00AA00">        &quot;Type&quot;: &quot;notify&quot;,</span>
<span style="color:#00AA00">        &quot;UID&quot;: &quot;[not set]&quot;,</span>
<span style="color:#00AA00">        &quot;UMask&quot;: &quot;0022&quot;,</span>
<span style="color:#00AA00">        &quot;UnitFilePreset&quot;: &quot;enabled&quot;,</span>
<span style="color:#00AA00">        &quot;UnitFileState&quot;: &quot;enabled&quot;,</span>
<span style="color:#00AA00">        &quot;UtmpMode&quot;: &quot;init&quot;,</span>
<span style="color:#00AA00">        &quot;WantedBy&quot;: &quot;multi-user.target&quot;,</span>
<span style="color:#00AA00">        &quot;Wants&quot;: &quot;network-online.target containerd.service&quot;,</span>
<span style="color:#00AA00">        &quot;WatchdogSignal&quot;: &quot;6&quot;,</span>
<span style="color:#00AA00">        &quot;WatchdogTimestampMonotonic&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;WatchdogUSec&quot;: &quot;0&quot;</span>
<span style="color:#00AA00">    }</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  00:12:52 +0200 (0:00:00.548)       0:01:12.568 ***** 
<span style="color:#0000AA">NOTIFIED HANDLER vladgh.samba.server : Restart SMB service for ansible-nas</span>
<span style="color:#0000AA">NOTIFIED HANDLER vladgh.samba.server : Restart NMB service for ansible-nas</span>
<span style="color:#0000AA">NOTIFIED HANDLER geerlingguy.nfs : reload nfs for ansible-nas</span>
<span style="color:#0000AA">NOTIFIED HANDLER geerlingguy.docker : restart docker for ansible-nas</span>
<span style="color:#0000AA">META: triggered running handlers for ansible-nas</span>
Sonntag 21 September 2025  00:12:52 +0200 (0:00:00.018)       0:01:12.587 ***** 

RUNNING HANDLER [vladgh.samba.server : Restart SMB service] *******************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/collections/ansible_collections/vladgh/samba/roles/server/handlers/main.yml:2</b></span>
<span style="color:#AA5500">changed: [ansible-nas] =&gt; {</span>
<span style="color:#AA5500">    &quot;changed&quot;: true,</span>
<span style="color:#AA5500">    &quot;name&quot;: &quot;smbd&quot;,</span>
<span style="color:#AA5500">    &quot;state&quot;: &quot;started&quot;,</span>
<span style="color:#AA5500">    &quot;status&quot;: {</span>
<span style="color:#AA5500">        &quot;ActiveEnterTimestamp&quot;: &quot;Sun 2025-09-21 00:11:59 CEST&quot;,</span>
<span style="color:#AA5500">        &quot;ActiveEnterTimestampMonotonic&quot;: &quot;678293390975&quot;,</span>
<span style="color:#AA5500">        &quot;ActiveExitTimestampMonotonic&quot;: &quot;0&quot;,</span>
<span style="color:#AA5500">        &quot;ActiveState&quot;: &quot;active&quot;,</span>
<span style="color:#AA5500">        &quot;After&quot;: &quot;nmbd.service network-online.target winbind.service sysinit.target system.slice basic.target network.target systemd-journald.socket&quot;,</span>
<span style="color:#AA5500">        &quot;AllowIsolate&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;AssertResult&quot;: &quot;yes&quot;,</span>
<span style="color:#AA5500">        &quot;AssertTimestamp&quot;: &quot;Sun 2025-09-21 00:11:59 CEST&quot;,</span>
<span style="color:#AA5500">        &quot;AssertTimestampMonotonic&quot;: &quot;678293262530&quot;,</span>
<span style="color:#AA5500">        &quot;Before&quot;: &quot;multi-user.target shutdown.target&quot;,</span>
<span style="color:#AA5500">        &quot;BlockIOAccounting&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;BlockIOWeight&quot;: &quot;[not set]&quot;,</span>
<span style="color:#AA5500">        &quot;CPUAccounting&quot;: &quot;yes&quot;,</span>
<span style="color:#AA5500">        &quot;CPUAffinityFromNUMA&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;CPUQuotaPerSecUSec&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;CPUQuotaPeriodUSec&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;CPUSchedulingPolicy&quot;: &quot;0&quot;,</span>
<span style="color:#AA5500">        &quot;CPUSchedulingPriority&quot;: &quot;0&quot;,</span>
<span style="color:#AA5500">        &quot;CPUSchedulingResetOnFork&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;CPUShares&quot;: &quot;[not set]&quot;,</span>
<span style="color:#AA5500">        &quot;CPUUsageNSec&quot;: &quot;80128000&quot;,</span>
<span style="color:#AA5500">        &quot;CPUWeight&quot;: &quot;[not set]&quot;,</span>
<span style="color:#AA5500">        &quot;CacheDirectoryMode&quot;: &quot;0755&quot;,</span>
<span style="color:#AA5500">        &quot;CanFreeze&quot;: &quot;yes&quot;,</span>
<span style="color:#AA5500">        &quot;CanIsolate&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;CanReload&quot;: &quot;yes&quot;,</span>
<span style="color:#AA5500">        &quot;CanStart&quot;: &quot;yes&quot;,</span>
<span style="color:#AA5500">        &quot;CanStop&quot;: &quot;yes&quot;,</span>
<span style="color:#AA5500">        &quot;CapabilityBoundingSet&quot;: &quot;cap_chown cap_dac_override cap_dac_read_search cap_fowner cap_fsetid cap_kill cap_setgid cap_setuid cap_setpcap cap_linux_immutable cap_net_bind_service cap_net_broadcast cap_net_admin cap_net_raw cap_ipc_lock cap_ipc_owner cap_sys_module cap_sys_rawio cap_sys_chroot cap_sys_ptrace cap_sys_pacct cap_sys_admin cap_sys_boot cap_sys_nice cap_sys_resource cap_sys_time cap_sys_tty_config cap_mknod cap_lease cap_audit_write cap_audit_control cap_setfcap cap_mac_override cap_mac_admin cap_syslog cap_wake_alarm cap_block_suspend cap_audit_read cap_perfmon cap_bpf cap_checkpoint_restore&quot;,</span>
<span style="color:#AA5500">        &quot;CleanResult&quot;: &quot;success&quot;,</span>
<span style="color:#AA5500">        &quot;CollectMode&quot;: &quot;inactive&quot;,</span>
<span style="color:#AA5500">        &quot;ConditionResult&quot;: &quot;yes&quot;,</span>
<span style="color:#AA5500">        &quot;ConditionTimestamp&quot;: &quot;Sun 2025-09-21 00:11:59 CEST&quot;,</span>
<span style="color:#AA5500">        &quot;ConditionTimestampMonotonic&quot;: &quot;678293262528&quot;,</span>
<span style="color:#AA5500">        &quot;ConfigurationDirectoryMode&quot;: &quot;0755&quot;,</span>
<span style="color:#AA5500">        &quot;Conflicts&quot;: &quot;shutdown.target&quot;,</span>
<span style="color:#AA5500">        &quot;ControlGroup&quot;: &quot;/system.slice/smbd.service&quot;,</span>
<span style="color:#AA5500">        &quot;ControlGroupId&quot;: &quot;46290&quot;,</span>
<span style="color:#AA5500">        &quot;ControlPID&quot;: &quot;0&quot;,</span>
<span style="color:#AA5500">        &quot;CoredumpFilter&quot;: &quot;0x33&quot;,</span>
<span style="color:#AA5500">        &quot;DefaultDependencies&quot;: &quot;yes&quot;,</span>
<span style="color:#AA5500">        &quot;DefaultMemoryLow&quot;: &quot;0&quot;,</span>
<span style="color:#AA5500">        &quot;DefaultMemoryMin&quot;: &quot;0&quot;,</span>
<span style="color:#AA5500">        &quot;Delegate&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;Description&quot;: &quot;Samba SMB Daemon&quot;,</span>
<span style="color:#AA5500">        &quot;DevicePolicy&quot;: &quot;auto&quot;,</span>
<span style="color:#AA5500">        &quot;Documentation&quot;: &quot;\&quot;man:smbd(8)\&quot; \&quot;man:samba(7)\&quot; \&quot;man:smb.conf(5)\&quot;&quot;,</span>
<span style="color:#AA5500">        &quot;DynamicUser&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;EffectiveCPUs&quot;: &quot;0-3&quot;,</span>
<span style="color:#AA5500">        &quot;EffectiveMemoryNodes&quot;: &quot;0-7&quot;,</span>
<span style="color:#AA5500">        &quot;EnvironmentFiles&quot;: &quot;/etc/default/samba (ignore_errors=yes)&quot;,</span>
<span style="color:#AA5500">        &quot;ExecCondition&quot;: &quot;{ path=/usr/share/samba/is-configured ; argv[]=/usr/share/samba/is-configured smb ; ignore_errors=no ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }&quot;,</span>
<span style="color:#AA5500">        &quot;ExecConditionEx&quot;: &quot;{ path=/usr/share/samba/is-configured ; argv[]=/usr/share/samba/is-configured smb ; flags= ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }&quot;,</span>
<span style="color:#AA5500">        &quot;ExecMainCode&quot;: &quot;0&quot;,</span>
<span style="color:#AA5500">        &quot;ExecMainExitTimestampMonotonic&quot;: &quot;0&quot;,</span>
<span style="color:#AA5500">        &quot;ExecMainPID&quot;: &quot;1369431&quot;,</span>
<span style="color:#AA5500">        &quot;ExecMainStartTimestamp&quot;: &quot;Sun 2025-09-21 00:11:59 CEST&quot;,</span>
<span style="color:#AA5500">        &quot;ExecMainStartTimestampMonotonic&quot;: &quot;678293322691&quot;,</span>
<span style="color:#AA5500">        &quot;ExecMainStatus&quot;: &quot;0&quot;,</span>
<span style="color:#AA5500">        &quot;ExecReload&quot;: &quot;{ path=/bin/kill ; argv[]=/bin/kill -HUP $MAINPID ; ignore_errors=no ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }&quot;,</span>
<span style="color:#AA5500">        &quot;ExecReloadEx&quot;: &quot;{ path=/bin/kill ; argv[]=/bin/kill -HUP $MAINPID ; flags= ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }&quot;,</span>
<span style="color:#AA5500">        &quot;ExecStart&quot;: &quot;{ path=/usr/sbin/smbd ; argv[]=/usr/sbin/smbd --foreground --no-process-group $SMBDOPTIONS ; ignore_errors=no ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }&quot;,</span>
<span style="color:#AA5500">        &quot;ExecStartEx&quot;: &quot;{ path=/usr/sbin/smbd ; argv[]=/usr/sbin/smbd --foreground --no-process-group $SMBDOPTIONS ; flags= ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }&quot;,</span>
<span style="color:#AA5500">        &quot;ExecStartPre&quot;: &quot;{ path=/usr/share/samba/update-apparmor-samba-profile ; argv[]=/usr/share/samba/update-apparmor-samba-profile ; ignore_errors=no ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }&quot;,</span>
<span style="color:#AA5500">        &quot;ExecStartPreEx&quot;: &quot;{ path=/usr/share/samba/update-apparmor-samba-profile ; argv[]=/usr/share/samba/update-apparmor-samba-profile ; flags= ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }&quot;,</span>
<span style="color:#AA5500">        &quot;ExitType&quot;: &quot;main&quot;,</span>
<span style="color:#AA5500">        &quot;FailureAction&quot;: &quot;none&quot;,</span>
<span style="color:#AA5500">        &quot;FileDescriptorStoreMax&quot;: &quot;0&quot;,</span>
<span style="color:#AA5500">        &quot;FinalKillSignal&quot;: &quot;9&quot;,</span>
<span style="color:#AA5500">        &quot;FragmentPath&quot;: &quot;/lib/systemd/system/smbd.service&quot;,</span>
<span style="color:#AA5500">        &quot;FreezerState&quot;: &quot;running&quot;,</span>
<span style="color:#AA5500">        &quot;GID&quot;: &quot;[not set]&quot;,</span>
<span style="color:#AA5500">        &quot;GuessMainPID&quot;: &quot;yes&quot;,</span>
<span style="color:#AA5500">        &quot;IOAccounting&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;IOReadBytes&quot;: &quot;18446744073709551615&quot;,</span>
<span style="color:#AA5500">        &quot;IOReadOperations&quot;: &quot;18446744073709551615&quot;,</span>
<span style="color:#AA5500">        &quot;IOSchedulingClass&quot;: &quot;2&quot;,</span>
<span style="color:#AA5500">        &quot;IOSchedulingPriority&quot;: &quot;4&quot;,</span>
<span style="color:#AA5500">        &quot;IOWeight&quot;: &quot;[not set]&quot;,</span>
<span style="color:#AA5500">        &quot;IOWriteBytes&quot;: &quot;18446744073709551615&quot;,</span>
<span style="color:#AA5500">        &quot;IOWriteOperations&quot;: &quot;18446744073709551615&quot;,</span>
<span style="color:#AA5500">        &quot;IPAccounting&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;IPEgressBytes&quot;: &quot;[no data]&quot;,</span>
<span style="color:#AA5500">        &quot;IPEgressPackets&quot;: &quot;[no data]&quot;,</span>
<span style="color:#AA5500">        &quot;IPIngressBytes&quot;: &quot;[no data]&quot;,</span>
<span style="color:#AA5500">        &quot;IPIngressPackets&quot;: &quot;[no data]&quot;,</span>
<span style="color:#AA5500">        &quot;Id&quot;: &quot;smbd.service&quot;,</span>
<span style="color:#AA5500">        &quot;IgnoreOnIsolate&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;IgnoreSIGPIPE&quot;: &quot;yes&quot;,</span>
<span style="color:#AA5500">        &quot;InactiveEnterTimestampMonotonic&quot;: &quot;0&quot;,</span>
<span style="color:#AA5500">        &quot;InactiveExitTimestamp&quot;: &quot;Sun 2025-09-21 00:11:59 CEST&quot;,</span>
<span style="color:#AA5500">        &quot;InactiveExitTimestampMonotonic&quot;: &quot;678293263998&quot;,</span>
<span style="color:#AA5500">        &quot;InvocationID&quot;: &quot;3f83abb020524418881b0a57a5fb672a&quot;,</span>
<span style="color:#AA5500">        &quot;JobRunningTimeoutUSec&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;JobTimeoutAction&quot;: &quot;none&quot;,</span>
<span style="color:#AA5500">        &quot;JobTimeoutUSec&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;KeyringMode&quot;: &quot;private&quot;,</span>
<span style="color:#AA5500">        &quot;KillMode&quot;: &quot;control-group&quot;,</span>
<span style="color:#AA5500">        &quot;KillSignal&quot;: &quot;15&quot;,</span>
<span style="color:#AA5500">        &quot;LimitAS&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;LimitASSoft&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;LimitCORE&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;LimitCORESoft&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;LimitCPU&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;LimitCPUSoft&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;LimitDATA&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;LimitDATASoft&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;LimitFSIZE&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;LimitFSIZESoft&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;LimitLOCKS&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;LimitLOCKSSoft&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;LimitMEMLOCK&quot;: &quot;8388608&quot;,</span>
<span style="color:#AA5500">        &quot;LimitMEMLOCKSoft&quot;: &quot;8388608&quot;,</span>
<span style="color:#AA5500">        &quot;LimitMSGQUEUE&quot;: &quot;819200&quot;,</span>
<span style="color:#AA5500">        &quot;LimitMSGQUEUESoft&quot;: &quot;819200&quot;,</span>
<span style="color:#AA5500">        &quot;LimitNICE&quot;: &quot;0&quot;,</span>
<span style="color:#AA5500">        &quot;LimitNICESoft&quot;: &quot;0&quot;,</span>
<span style="color:#AA5500">        &quot;LimitNOFILE&quot;: &quot;16384&quot;,</span>
<span style="color:#AA5500">        &quot;LimitNOFILESoft&quot;: &quot;16384&quot;,</span>
<span style="color:#AA5500">        &quot;LimitNPROC&quot;: &quot;31916&quot;,</span>
<span style="color:#AA5500">        &quot;LimitNPROCSoft&quot;: &quot;31916&quot;,</span>
<span style="color:#AA5500">        &quot;LimitRSS&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;LimitRSSSoft&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;LimitRTPRIO&quot;: &quot;0&quot;,</span>
<span style="color:#AA5500">        &quot;LimitRTPRIOSoft&quot;: &quot;0&quot;,</span>
<span style="color:#AA5500">        &quot;LimitRTTIME&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;LimitRTTIMESoft&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;LimitSIGPENDING&quot;: &quot;31916&quot;,</span>
<span style="color:#AA5500">        &quot;LimitSIGPENDINGSoft&quot;: &quot;31916&quot;,</span>
<span style="color:#AA5500">        &quot;LimitSTACK&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;LimitSTACKSoft&quot;: &quot;8388608&quot;,</span>
<span style="color:#AA5500">        &quot;LoadState&quot;: &quot;loaded&quot;,</span>
<span style="color:#AA5500">        &quot;LockPersonality&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;LogLevelMax&quot;: &quot;-1&quot;,</span>
<span style="color:#AA5500">        &quot;LogRateLimitBurst&quot;: &quot;0&quot;,</span>
<span style="color:#AA5500">        &quot;LogRateLimitIntervalUSec&quot;: &quot;0&quot;,</span>
<span style="color:#AA5500">        &quot;LogsDirectoryMode&quot;: &quot;0755&quot;,</span>
<span style="color:#AA5500">        &quot;MainPID&quot;: &quot;1369431&quot;,</span>
<span style="color:#AA5500">        &quot;ManagedOOMMemoryPressure&quot;: &quot;auto&quot;,</span>
<span style="color:#AA5500">        &quot;ManagedOOMMemoryPressureLimit&quot;: &quot;0&quot;,</span>
<span style="color:#AA5500">        &quot;ManagedOOMPreference&quot;: &quot;none&quot;,</span>
<span style="color:#AA5500">        &quot;ManagedOOMSwap&quot;: &quot;auto&quot;,</span>
<span style="color:#AA5500">        &quot;MemoryAccounting&quot;: &quot;yes&quot;,</span>
<span style="color:#AA5500">        &quot;MemoryAvailable&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;MemoryCurrent&quot;: &quot;[not set]&quot;,</span>
<span style="color:#AA5500">        &quot;MemoryDenyWriteExecute&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;MemoryHigh&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;MemoryLimit&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;MemoryLow&quot;: &quot;0&quot;,</span>
<span style="color:#AA5500">        &quot;MemoryMax&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;MemoryMin&quot;: &quot;0&quot;,</span>
<span style="color:#AA5500">        &quot;MemorySwapMax&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;MountAPIVFS&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;NFileDescriptorStore&quot;: &quot;0&quot;,</span>
<span style="color:#AA5500">        &quot;NRestarts&quot;: &quot;0&quot;,</span>
<span style="color:#AA5500">        &quot;NUMAPolicy&quot;: &quot;n/a&quot;,</span>
<span style="color:#AA5500">        &quot;Names&quot;: &quot;smbd.service smb.service&quot;,</span>
<span style="color:#AA5500">        &quot;NeedDaemonReload&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;Nice&quot;: &quot;0&quot;,</span>
<span style="color:#AA5500">        &quot;NoNewPrivileges&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;NonBlocking&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;NotifyAccess&quot;: &quot;main&quot;,</span>
<span style="color:#AA5500">        &quot;OOMPolicy&quot;: &quot;stop&quot;,</span>
<span style="color:#AA5500">        &quot;OOMScoreAdjust&quot;: &quot;0&quot;,</span>
<span style="color:#AA5500">        &quot;OnFailureJobMode&quot;: &quot;replace&quot;,</span>
<span style="color:#AA5500">        &quot;OnSuccessJobMode&quot;: &quot;fail&quot;,</span>
<span style="color:#AA5500">        &quot;PIDFile&quot;: &quot;/run/samba/smbd.pid&quot;,</span>
<span style="color:#AA5500">        &quot;Perpetual&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;PrivateDevices&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;PrivateIPC&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;PrivateMounts&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;PrivateNetwork&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;PrivateTmp&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;PrivateUsers&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;ProcSubset&quot;: &quot;all&quot;,</span>
<span style="color:#AA5500">        &quot;ProtectClock&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;ProtectControlGroups&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;ProtectHome&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;ProtectHostname&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;ProtectKernelLogs&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;ProtectKernelModules&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;ProtectKernelTunables&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;ProtectProc&quot;: &quot;default&quot;,</span>
<span style="color:#AA5500">        &quot;ProtectSystem&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;RefuseManualStart&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;RefuseManualStop&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;ReloadResult&quot;: &quot;success&quot;,</span>
<span style="color:#AA5500">        &quot;RemainAfterExit&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;RemoveIPC&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;Requires&quot;: &quot;sysinit.target system.slice&quot;,</span>
<span style="color:#AA5500">        &quot;Restart&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;RestartKillSignal&quot;: &quot;15&quot;,</span>
<span style="color:#AA5500">        &quot;RestartUSec&quot;: &quot;100ms&quot;,</span>
<span style="color:#AA5500">        &quot;RestrictNamespaces&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;RestrictRealtime&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;RestrictSUIDSGID&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;Result&quot;: &quot;success&quot;,</span>
<span style="color:#AA5500">        &quot;RootDirectoryStartOnly&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;RuntimeDirectoryMode&quot;: &quot;0755&quot;,</span>
<span style="color:#AA5500">        &quot;RuntimeDirectoryPreserve&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;RuntimeMaxUSec&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;RuntimeRandomizedExtraUSec&quot;: &quot;0&quot;,</span>
<span style="color:#AA5500">        &quot;SameProcessGroup&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;SecureBits&quot;: &quot;0&quot;,</span>
<span style="color:#AA5500">        &quot;SendSIGHUP&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;SendSIGKILL&quot;: &quot;yes&quot;,</span>
<span style="color:#AA5500">        &quot;Slice&quot;: &quot;system.slice&quot;,</span>
<span style="color:#AA5500">        &quot;StandardError&quot;: &quot;inherit&quot;,</span>
<span style="color:#AA5500">        &quot;StandardInput&quot;: &quot;null&quot;,</span>
<span style="color:#AA5500">        &quot;StandardOutput&quot;: &quot;journal&quot;,</span>
<span style="color:#AA5500">        &quot;StartLimitAction&quot;: &quot;none&quot;,</span>
<span style="color:#AA5500">        &quot;StartLimitBurst&quot;: &quot;5&quot;,</span>
<span style="color:#AA5500">        &quot;StartLimitIntervalUSec&quot;: &quot;10s&quot;,</span>
<span style="color:#AA5500">        &quot;StartupBlockIOWeight&quot;: &quot;[not set]&quot;,</span>
<span style="color:#AA5500">        &quot;StartupCPUShares&quot;: &quot;[not set]&quot;,</span>
<span style="color:#AA5500">        &quot;StartupCPUWeight&quot;: &quot;[not set]&quot;,</span>
<span style="color:#AA5500">        &quot;StartupIOWeight&quot;: &quot;[not set]&quot;,</span>
<span style="color:#AA5500">        &quot;StateChangeTimestamp&quot;: &quot;Sun 2025-09-21 00:11:59 CEST&quot;,</span>
<span style="color:#AA5500">        &quot;StateChangeTimestampMonotonic&quot;: &quot;678293390975&quot;,</span>
<span style="color:#AA5500">        &quot;StateDirectoryMode&quot;: &quot;0755&quot;,</span>
<span style="color:#AA5500">        &quot;StatusErrno&quot;: &quot;0&quot;,</span>
<span style="color:#AA5500">        &quot;StatusText&quot;: &quot;smbd: ready to serve connections...&quot;,</span>
<span style="color:#AA5500">        &quot;StopWhenUnneeded&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;SubState&quot;: &quot;running&quot;,</span>
<span style="color:#AA5500">        &quot;SuccessAction&quot;: &quot;none&quot;,</span>
<span style="color:#AA5500">        &quot;SyslogFacility&quot;: &quot;3&quot;,</span>
<span style="color:#AA5500">        &quot;SyslogLevel&quot;: &quot;6&quot;,</span>
<span style="color:#AA5500">        &quot;SyslogLevelPrefix&quot;: &quot;yes&quot;,</span>
<span style="color:#AA5500">        &quot;SyslogPriority&quot;: &quot;30&quot;,</span>
<span style="color:#AA5500">        &quot;SystemCallErrorNumber&quot;: &quot;2147483646&quot;,</span>
<span style="color:#AA5500">        &quot;TTYReset&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;TTYVHangup&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;TTYVTDisallocate&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;TasksAccounting&quot;: &quot;yes&quot;,</span>
<span style="color:#AA5500">        &quot;TasksCurrent&quot;: &quot;3&quot;,</span>
<span style="color:#AA5500">        &quot;TasksMax&quot;: &quot;9574&quot;,</span>
<span style="color:#AA5500">        &quot;TimeoutAbortUSec&quot;: &quot;1min 30s&quot;,</span>
<span style="color:#AA5500">        &quot;TimeoutCleanUSec&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;TimeoutStartFailureMode&quot;: &quot;terminate&quot;,</span>
<span style="color:#AA5500">        &quot;TimeoutStartUSec&quot;: &quot;1min 30s&quot;,</span>
<span style="color:#AA5500">        &quot;TimeoutStopFailureMode&quot;: &quot;terminate&quot;,</span>
<span style="color:#AA5500">        &quot;TimeoutStopUSec&quot;: &quot;1min 30s&quot;,</span>
<span style="color:#AA5500">        &quot;TimerSlackNSec&quot;: &quot;50000&quot;,</span>
<span style="color:#AA5500">        &quot;Transient&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;Type&quot;: &quot;notify&quot;,</span>
<span style="color:#AA5500">        &quot;UID&quot;: &quot;[not set]&quot;,</span>
<span style="color:#AA5500">        &quot;UMask&quot;: &quot;0022&quot;,</span>
<span style="color:#AA5500">        &quot;UnitFilePreset&quot;: &quot;enabled&quot;,</span>
<span style="color:#AA5500">        &quot;UnitFileState&quot;: &quot;enabled&quot;,</span>
<span style="color:#AA5500">        &quot;UtmpMode&quot;: &quot;init&quot;,</span>
<span style="color:#AA5500">        &quot;WantedBy&quot;: &quot;multi-user.target&quot;,</span>
<span style="color:#AA5500">        &quot;Wants&quot;: &quot;network-online.target&quot;,</span>
<span style="color:#AA5500">        &quot;WatchdogSignal&quot;: &quot;6&quot;,</span>
<span style="color:#AA5500">        &quot;WatchdogTimestampMonotonic&quot;: &quot;0&quot;,</span>
<span style="color:#AA5500">        &quot;WatchdogUSec&quot;: &quot;0&quot;</span>
<span style="color:#AA5500">    }</span>
<span style="color:#AA5500">}</span>
Sonntag 21 September 2025  00:12:53 +0200 (0:00:00.618)       0:01:13.205 ***** 

RUNNING HANDLER [vladgh.samba.server : Restart NMB service] *******************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/collections/ansible_collections/vladgh/samba/roles/server/handlers/main.yml:7</b></span>
<span style="color:#AA5500">changed: [ansible-nas] =&gt; {</span>
<span style="color:#AA5500">    &quot;changed&quot;: true,</span>
<span style="color:#AA5500">    &quot;name&quot;: &quot;nmbd&quot;,</span>
<span style="color:#AA5500">    &quot;state&quot;: &quot;started&quot;,</span>
<span style="color:#AA5500">    &quot;status&quot;: {</span>
<span style="color:#AA5500">        &quot;ActiveEnterTimestamp&quot;: &quot;Sun 2025-09-21 00:11:59 CEST&quot;,</span>
<span style="color:#AA5500">        &quot;ActiveEnterTimestampMonotonic&quot;: &quot;678293262184&quot;,</span>
<span style="color:#AA5500">        &quot;ActiveExitTimestampMonotonic&quot;: &quot;0&quot;,</span>
<span style="color:#AA5500">        &quot;ActiveState&quot;: &quot;active&quot;,</span>
<span style="color:#AA5500">        &quot;After&quot;: &quot;basic.target sysinit.target systemd-journald.socket network-online.target network.target system.slice&quot;,</span>
<span style="color:#AA5500">        &quot;AllowIsolate&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;AssertResult&quot;: &quot;yes&quot;,</span>
<span style="color:#AA5500">        &quot;AssertTimestamp&quot;: &quot;Sun 2025-09-21 00:11:58 CEST&quot;,</span>
<span style="color:#AA5500">        &quot;AssertTimestampMonotonic&quot;: &quot;678293122472&quot;,</span>
<span style="color:#AA5500">        &quot;Before&quot;: &quot;smbd.service shutdown.target multi-user.target&quot;,</span>
<span style="color:#AA5500">        &quot;BlockIOAccounting&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;BlockIOWeight&quot;: &quot;[not set]&quot;,</span>
<span style="color:#AA5500">        &quot;CPUAccounting&quot;: &quot;yes&quot;,</span>
<span style="color:#AA5500">        &quot;CPUAffinityFromNUMA&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;CPUQuotaPerSecUSec&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;CPUQuotaPeriodUSec&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;CPUSchedulingPolicy&quot;: &quot;0&quot;,</span>
<span style="color:#AA5500">        &quot;CPUSchedulingPriority&quot;: &quot;0&quot;,</span>
<span style="color:#AA5500">        &quot;CPUSchedulingResetOnFork&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;CPUShares&quot;: &quot;[not set]&quot;,</span>
<span style="color:#AA5500">        &quot;CPUUsageNSec&quot;: &quot;85178000&quot;,</span>
<span style="color:#AA5500">        &quot;CPUWeight&quot;: &quot;[not set]&quot;,</span>
<span style="color:#AA5500">        &quot;CacheDirectoryMode&quot;: &quot;0755&quot;,</span>
<span style="color:#AA5500">        &quot;CanFreeze&quot;: &quot;yes&quot;,</span>
<span style="color:#AA5500">        &quot;CanIsolate&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;CanReload&quot;: &quot;yes&quot;,</span>
<span style="color:#AA5500">        &quot;CanStart&quot;: &quot;yes&quot;,</span>
<span style="color:#AA5500">        &quot;CanStop&quot;: &quot;yes&quot;,</span>
<span style="color:#AA5500">        &quot;CapabilityBoundingSet&quot;: &quot;cap_chown cap_dac_override cap_dac_read_search cap_fowner cap_fsetid cap_kill cap_setgid cap_setuid cap_setpcap cap_linux_immutable cap_net_bind_service cap_net_broadcast cap_net_admin cap_net_raw cap_ipc_lock cap_ipc_owner cap_sys_module cap_sys_rawio cap_sys_chroot cap_sys_ptrace cap_sys_pacct cap_sys_admin cap_sys_boot cap_sys_nice cap_sys_resource cap_sys_time cap_sys_tty_config cap_mknod cap_lease cap_audit_write cap_audit_control cap_setfcap cap_mac_override cap_mac_admin cap_syslog cap_wake_alarm cap_block_suspend cap_audit_read cap_perfmon cap_bpf cap_checkpoint_restore&quot;,</span>
<span style="color:#AA5500">        &quot;CleanResult&quot;: &quot;success&quot;,</span>
<span style="color:#AA5500">        &quot;CollectMode&quot;: &quot;inactive&quot;,</span>
<span style="color:#AA5500">        &quot;ConditionResult&quot;: &quot;yes&quot;,</span>
<span style="color:#AA5500">        &quot;ConditionTimestamp&quot;: &quot;Sun 2025-09-21 00:11:58 CEST&quot;,</span>
<span style="color:#AA5500">        &quot;ConditionTimestampMonotonic&quot;: &quot;678293122470&quot;,</span>
<span style="color:#AA5500">        &quot;ConfigurationDirectoryMode&quot;: &quot;0755&quot;,</span>
<span style="color:#AA5500">        &quot;Conflicts&quot;: &quot;shutdown.target&quot;,</span>
<span style="color:#AA5500">        &quot;ControlGroup&quot;: &quot;/system.slice/nmbd.service&quot;,</span>
<span style="color:#AA5500">        &quot;ControlGroupId&quot;: &quot;46252&quot;,</span>
<span style="color:#AA5500">        &quot;ControlPID&quot;: &quot;0&quot;,</span>
<span style="color:#AA5500">        &quot;CoredumpFilter&quot;: &quot;0x33&quot;,</span>
<span style="color:#AA5500">        &quot;DefaultDependencies&quot;: &quot;yes&quot;,</span>
<span style="color:#AA5500">        &quot;DefaultMemoryLow&quot;: &quot;0&quot;,</span>
<span style="color:#AA5500">        &quot;DefaultMemoryMin&quot;: &quot;0&quot;,</span>
<span style="color:#AA5500">        &quot;Delegate&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;Description&quot;: &quot;Samba NMB Daemon&quot;,</span>
<span style="color:#AA5500">        &quot;DevicePolicy&quot;: &quot;auto&quot;,</span>
<span style="color:#AA5500">        &quot;Documentation&quot;: &quot;\&quot;man:nmbd(8)\&quot; \&quot;man:samba(7)\&quot; \&quot;man:smb.conf(5)\&quot;&quot;,</span>
<span style="color:#AA5500">        &quot;DynamicUser&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;EffectiveCPUs&quot;: &quot;0-3&quot;,</span>
<span style="color:#AA5500">        &quot;EffectiveMemoryNodes&quot;: &quot;0-7&quot;,</span>
<span style="color:#AA5500">        &quot;EnvironmentFiles&quot;: &quot;/etc/default/samba (ignore_errors=yes)&quot;,</span>
<span style="color:#AA5500">        &quot;ExecCondition&quot;: &quot;{ path=/usr/share/samba/is-configured ; argv[]=/usr/share/samba/is-configured nmb ; ignore_errors=no ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }&quot;,</span>
<span style="color:#AA5500">        &quot;ExecConditionEx&quot;: &quot;{ path=/usr/share/samba/is-configured ; argv[]=/usr/share/samba/is-configured nmb ; flags= ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }&quot;,</span>
<span style="color:#AA5500">        &quot;ExecMainCode&quot;: &quot;0&quot;,</span>
<span style="color:#AA5500">        &quot;ExecMainExitTimestampMonotonic&quot;: &quot;0&quot;,</span>
<span style="color:#AA5500">        &quot;ExecMainPID&quot;: &quot;1369426&quot;,</span>
<span style="color:#AA5500">        &quot;ExecMainStartTimestamp&quot;: &quot;Sun 2025-09-21 00:11:59 CEST&quot;,</span>
<span style="color:#AA5500">        &quot;ExecMainStartTimestampMonotonic&quot;: &quot;678293232166&quot;,</span>
<span style="color:#AA5500">        &quot;ExecMainStatus&quot;: &quot;0&quot;,</span>
<span style="color:#AA5500">        &quot;ExecReload&quot;: &quot;{ path=/bin/kill ; argv[]=/bin/kill -HUP $MAINPID ; ignore_errors=no ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }&quot;,</span>
<span style="color:#AA5500">        &quot;ExecReloadEx&quot;: &quot;{ path=/bin/kill ; argv[]=/bin/kill -HUP $MAINPID ; flags= ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }&quot;,</span>
<span style="color:#AA5500">        &quot;ExecStart&quot;: &quot;{ path=/usr/sbin/nmbd ; argv[]=/usr/sbin/nmbd --foreground --no-process-group $NMBDOPTIONS ; ignore_errors=no ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }&quot;,</span>
<span style="color:#AA5500">        &quot;ExecStartEx&quot;: &quot;{ path=/usr/sbin/nmbd ; argv[]=/usr/sbin/nmbd --foreground --no-process-group $NMBDOPTIONS ; flags= ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }&quot;,</span>
<span style="color:#AA5500">        &quot;ExitType&quot;: &quot;main&quot;,</span>
<span style="color:#AA5500">        &quot;FailureAction&quot;: &quot;none&quot;,</span>
<span style="color:#AA5500">        &quot;FileDescriptorStoreMax&quot;: &quot;0&quot;,</span>
<span style="color:#AA5500">        &quot;FinalKillSignal&quot;: &quot;9&quot;,</span>
<span style="color:#AA5500">        &quot;FragmentPath&quot;: &quot;/lib/systemd/system/nmbd.service&quot;,</span>
<span style="color:#AA5500">        &quot;FreezerState&quot;: &quot;running&quot;,</span>
<span style="color:#AA5500">        &quot;GID&quot;: &quot;[not set]&quot;,</span>
<span style="color:#AA5500">        &quot;GuessMainPID&quot;: &quot;yes&quot;,</span>
<span style="color:#AA5500">        &quot;IOAccounting&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;IOReadBytes&quot;: &quot;18446744073709551615&quot;,</span>
<span style="color:#AA5500">        &quot;IOReadOperations&quot;: &quot;18446744073709551615&quot;,</span>
<span style="color:#AA5500">        &quot;IOSchedulingClass&quot;: &quot;2&quot;,</span>
<span style="color:#AA5500">        &quot;IOSchedulingPriority&quot;: &quot;4&quot;,</span>
<span style="color:#AA5500">        &quot;IOWeight&quot;: &quot;[not set]&quot;,</span>
<span style="color:#AA5500">        &quot;IOWriteBytes&quot;: &quot;18446744073709551615&quot;,</span>
<span style="color:#AA5500">        &quot;IOWriteOperations&quot;: &quot;18446744073709551615&quot;,</span>
<span style="color:#AA5500">        &quot;IPAccounting&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;IPEgressBytes&quot;: &quot;[no data]&quot;,</span>
<span style="color:#AA5500">        &quot;IPEgressPackets&quot;: &quot;[no data]&quot;,</span>
<span style="color:#AA5500">        &quot;IPIngressBytes&quot;: &quot;[no data]&quot;,</span>
<span style="color:#AA5500">        &quot;IPIngressPackets&quot;: &quot;[no data]&quot;,</span>
<span style="color:#AA5500">        &quot;Id&quot;: &quot;nmbd.service&quot;,</span>
<span style="color:#AA5500">        &quot;IgnoreOnIsolate&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;IgnoreSIGPIPE&quot;: &quot;yes&quot;,</span>
<span style="color:#AA5500">        &quot;InactiveEnterTimestampMonotonic&quot;: &quot;0&quot;,</span>
<span style="color:#AA5500">        &quot;InactiveExitTimestamp&quot;: &quot;Sun 2025-09-21 00:11:58 CEST&quot;,</span>
<span style="color:#AA5500">        &quot;InactiveExitTimestampMonotonic&quot;: &quot;678293156547&quot;,</span>
<span style="color:#AA5500">        &quot;InvocationID&quot;: &quot;e76b6d580c874c1b8817b6abef8da1c0&quot;,</span>
<span style="color:#AA5500">        &quot;JobRunningTimeoutUSec&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;JobTimeoutAction&quot;: &quot;none&quot;,</span>
<span style="color:#AA5500">        &quot;JobTimeoutUSec&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;KeyringMode&quot;: &quot;private&quot;,</span>
<span style="color:#AA5500">        &quot;KillMode&quot;: &quot;control-group&quot;,</span>
<span style="color:#AA5500">        &quot;KillSignal&quot;: &quot;15&quot;,</span>
<span style="color:#AA5500">        &quot;LimitAS&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;LimitASSoft&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;LimitCORE&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;LimitCORESoft&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;LimitCPU&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;LimitCPUSoft&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;LimitDATA&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;LimitDATASoft&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;LimitFSIZE&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;LimitFSIZESoft&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;LimitLOCKS&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;LimitLOCKSSoft&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;LimitMEMLOCK&quot;: &quot;8388608&quot;,</span>
<span style="color:#AA5500">        &quot;LimitMEMLOCKSoft&quot;: &quot;8388608&quot;,</span>
<span style="color:#AA5500">        &quot;LimitMSGQUEUE&quot;: &quot;819200&quot;,</span>
<span style="color:#AA5500">        &quot;LimitMSGQUEUESoft&quot;: &quot;819200&quot;,</span>
<span style="color:#AA5500">        &quot;LimitNICE&quot;: &quot;0&quot;,</span>
<span style="color:#AA5500">        &quot;LimitNICESoft&quot;: &quot;0&quot;,</span>
<span style="color:#AA5500">        &quot;LimitNOFILE&quot;: &quot;524288&quot;,</span>
<span style="color:#AA5500">        &quot;LimitNOFILESoft&quot;: &quot;1024&quot;,</span>
<span style="color:#AA5500">        &quot;LimitNPROC&quot;: &quot;31916&quot;,</span>
<span style="color:#AA5500">        &quot;LimitNPROCSoft&quot;: &quot;31916&quot;,</span>
<span style="color:#AA5500">        &quot;LimitRSS&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;LimitRSSSoft&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;LimitRTPRIO&quot;: &quot;0&quot;,</span>
<span style="color:#AA5500">        &quot;LimitRTPRIOSoft&quot;: &quot;0&quot;,</span>
<span style="color:#AA5500">        &quot;LimitRTTIME&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;LimitRTTIMESoft&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;LimitSIGPENDING&quot;: &quot;31916&quot;,</span>
<span style="color:#AA5500">        &quot;LimitSIGPENDINGSoft&quot;: &quot;31916&quot;,</span>
<span style="color:#AA5500">        &quot;LimitSTACK&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;LimitSTACKSoft&quot;: &quot;8388608&quot;,</span>
<span style="color:#AA5500">        &quot;LoadState&quot;: &quot;loaded&quot;,</span>
<span style="color:#AA5500">        &quot;LockPersonality&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;LogLevelMax&quot;: &quot;-1&quot;,</span>
<span style="color:#AA5500">        &quot;LogRateLimitBurst&quot;: &quot;0&quot;,</span>
<span style="color:#AA5500">        &quot;LogRateLimitIntervalUSec&quot;: &quot;0&quot;,</span>
<span style="color:#AA5500">        &quot;LogsDirectoryMode&quot;: &quot;0755&quot;,</span>
<span style="color:#AA5500">        &quot;MainPID&quot;: &quot;1369426&quot;,</span>
<span style="color:#AA5500">        &quot;ManagedOOMMemoryPressure&quot;: &quot;auto&quot;,</span>
<span style="color:#AA5500">        &quot;ManagedOOMMemoryPressureLimit&quot;: &quot;0&quot;,</span>
<span style="color:#AA5500">        &quot;ManagedOOMPreference&quot;: &quot;none&quot;,</span>
<span style="color:#AA5500">        &quot;ManagedOOMSwap&quot;: &quot;auto&quot;,</span>
<span style="color:#AA5500">        &quot;MemoryAccounting&quot;: &quot;yes&quot;,</span>
<span style="color:#AA5500">        &quot;MemoryAvailable&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;MemoryCurrent&quot;: &quot;[not set]&quot;,</span>
<span style="color:#AA5500">        &quot;MemoryDenyWriteExecute&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;MemoryHigh&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;MemoryLimit&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;MemoryLow&quot;: &quot;0&quot;,</span>
<span style="color:#AA5500">        &quot;MemoryMax&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;MemoryMin&quot;: &quot;0&quot;,</span>
<span style="color:#AA5500">        &quot;MemorySwapMax&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;MountAPIVFS&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;NFileDescriptorStore&quot;: &quot;0&quot;,</span>
<span style="color:#AA5500">        &quot;NRestarts&quot;: &quot;0&quot;,</span>
<span style="color:#AA5500">        &quot;NUMAPolicy&quot;: &quot;n/a&quot;,</span>
<span style="color:#AA5500">        &quot;Names&quot;: &quot;nmbd.service nmb.service&quot;,</span>
<span style="color:#AA5500">        &quot;NeedDaemonReload&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;Nice&quot;: &quot;0&quot;,</span>
<span style="color:#AA5500">        &quot;NoNewPrivileges&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;NonBlocking&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;NotifyAccess&quot;: &quot;main&quot;,</span>
<span style="color:#AA5500">        &quot;OOMPolicy&quot;: &quot;stop&quot;,</span>
<span style="color:#AA5500">        &quot;OOMScoreAdjust&quot;: &quot;0&quot;,</span>
<span style="color:#AA5500">        &quot;OnFailureJobMode&quot;: &quot;replace&quot;,</span>
<span style="color:#AA5500">        &quot;OnSuccessJobMode&quot;: &quot;fail&quot;,</span>
<span style="color:#AA5500">        &quot;PIDFile&quot;: &quot;/run/samba/nmbd.pid&quot;,</span>
<span style="color:#AA5500">        &quot;Perpetual&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;PrivateDevices&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;PrivateIPC&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;PrivateMounts&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;PrivateNetwork&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;PrivateTmp&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;PrivateUsers&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;ProcSubset&quot;: &quot;all&quot;,</span>
<span style="color:#AA5500">        &quot;ProtectClock&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;ProtectControlGroups&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;ProtectHome&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;ProtectHostname&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;ProtectKernelLogs&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;ProtectKernelModules&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;ProtectKernelTunables&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;ProtectProc&quot;: &quot;default&quot;,</span>
<span style="color:#AA5500">        &quot;ProtectSystem&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;RefuseManualStart&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;RefuseManualStop&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;ReloadResult&quot;: &quot;success&quot;,</span>
<span style="color:#AA5500">        &quot;RemainAfterExit&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;RemoveIPC&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;Requires&quot;: &quot;sysinit.target system.slice&quot;,</span>
<span style="color:#AA5500">        &quot;Restart&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;RestartKillSignal&quot;: &quot;15&quot;,</span>
<span style="color:#AA5500">        &quot;RestartUSec&quot;: &quot;100ms&quot;,</span>
<span style="color:#AA5500">        &quot;RestrictNamespaces&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;RestrictRealtime&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;RestrictSUIDSGID&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;Result&quot;: &quot;success&quot;,</span>
<span style="color:#AA5500">        &quot;RootDirectoryStartOnly&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;RuntimeDirectoryMode&quot;: &quot;0755&quot;,</span>
<span style="color:#AA5500">        &quot;RuntimeDirectoryPreserve&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;RuntimeMaxUSec&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;RuntimeRandomizedExtraUSec&quot;: &quot;0&quot;,</span>
<span style="color:#AA5500">        &quot;SameProcessGroup&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;SecureBits&quot;: &quot;0&quot;,</span>
<span style="color:#AA5500">        &quot;SendSIGHUP&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;SendSIGKILL&quot;: &quot;yes&quot;,</span>
<span style="color:#AA5500">        &quot;Slice&quot;: &quot;system.slice&quot;,</span>
<span style="color:#AA5500">        &quot;StandardError&quot;: &quot;inherit&quot;,</span>
<span style="color:#AA5500">        &quot;StandardInput&quot;: &quot;null&quot;,</span>
<span style="color:#AA5500">        &quot;StandardOutput&quot;: &quot;journal&quot;,</span>
<span style="color:#AA5500">        &quot;StartLimitAction&quot;: &quot;none&quot;,</span>
<span style="color:#AA5500">        &quot;StartLimitBurst&quot;: &quot;5&quot;,</span>
<span style="color:#AA5500">        &quot;StartLimitIntervalUSec&quot;: &quot;10s&quot;,</span>
<span style="color:#AA5500">        &quot;StartupBlockIOWeight&quot;: &quot;[not set]&quot;,</span>
<span style="color:#AA5500">        &quot;StartupCPUShares&quot;: &quot;[not set]&quot;,</span>
<span style="color:#AA5500">        &quot;StartupCPUWeight&quot;: &quot;[not set]&quot;,</span>
<span style="color:#AA5500">        &quot;StartupIOWeight&quot;: &quot;[not set]&quot;,</span>
<span style="color:#AA5500">        &quot;StateChangeTimestamp&quot;: &quot;Sun 2025-09-21 00:11:59 CEST&quot;,</span>
<span style="color:#AA5500">        &quot;StateChangeTimestampMonotonic&quot;: &quot;678293262184&quot;,</span>
<span style="color:#AA5500">        &quot;StateDirectoryMode&quot;: &quot;0755&quot;,</span>
<span style="color:#AA5500">        &quot;StatusErrno&quot;: &quot;0&quot;,</span>
<span style="color:#AA5500">        &quot;StatusText&quot;: &quot;nmbd: ready to serve connections...&quot;,</span>
<span style="color:#AA5500">        &quot;StopWhenUnneeded&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;SubState&quot;: &quot;running&quot;,</span>
<span style="color:#AA5500">        &quot;SuccessAction&quot;: &quot;none&quot;,</span>
<span style="color:#AA5500">        &quot;SyslogFacility&quot;: &quot;3&quot;,</span>
<span style="color:#AA5500">        &quot;SyslogLevel&quot;: &quot;6&quot;,</span>
<span style="color:#AA5500">        &quot;SyslogLevelPrefix&quot;: &quot;yes&quot;,</span>
<span style="color:#AA5500">        &quot;SyslogPriority&quot;: &quot;30&quot;,</span>
<span style="color:#AA5500">        &quot;SystemCallErrorNumber&quot;: &quot;2147483646&quot;,</span>
<span style="color:#AA5500">        &quot;TTYReset&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;TTYVHangup&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;TTYVTDisallocate&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;TasksAccounting&quot;: &quot;yes&quot;,</span>
<span style="color:#AA5500">        &quot;TasksCurrent&quot;: &quot;1&quot;,</span>
<span style="color:#AA5500">        &quot;TasksMax&quot;: &quot;9574&quot;,</span>
<span style="color:#AA5500">        &quot;TimeoutAbortUSec&quot;: &quot;1min 30s&quot;,</span>
<span style="color:#AA5500">        &quot;TimeoutCleanUSec&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;TimeoutStartFailureMode&quot;: &quot;terminate&quot;,</span>
<span style="color:#AA5500">        &quot;TimeoutStartUSec&quot;: &quot;1min 30s&quot;,</span>
<span style="color:#AA5500">        &quot;TimeoutStopFailureMode&quot;: &quot;terminate&quot;,</span>
<span style="color:#AA5500">        &quot;TimeoutStopUSec&quot;: &quot;1min 30s&quot;,</span>
<span style="color:#AA5500">        &quot;TimerSlackNSec&quot;: &quot;50000&quot;,</span>
<span style="color:#AA5500">        &quot;Transient&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;Type&quot;: &quot;notify&quot;,</span>
<span style="color:#AA5500">        &quot;UID&quot;: &quot;[not set]&quot;,</span>
<span style="color:#AA5500">        &quot;UMask&quot;: &quot;0022&quot;,</span>
<span style="color:#AA5500">        &quot;UnitFilePreset&quot;: &quot;enabled&quot;,</span>
<span style="color:#AA5500">        &quot;UnitFileState&quot;: &quot;enabled&quot;,</span>
<span style="color:#AA5500">        &quot;UtmpMode&quot;: &quot;init&quot;,</span>
<span style="color:#AA5500">        &quot;WantedBy&quot;: &quot;multi-user.target&quot;,</span>
<span style="color:#AA5500">        &quot;Wants&quot;: &quot;network-online.target&quot;,</span>
<span style="color:#AA5500">        &quot;WatchdogSignal&quot;: &quot;6&quot;,</span>
<span style="color:#AA5500">        &quot;WatchdogTimestampMonotonic&quot;: &quot;0&quot;,</span>
<span style="color:#AA5500">        &quot;WatchdogUSec&quot;: &quot;0&quot;</span>
<span style="color:#AA5500">    }</span>
<span style="color:#AA5500">}</span>
Sonntag 21 September 2025  00:12:53 +0200 (0:00:00.682)       0:01:13.887 ***** 

RUNNING HANDLER [geerlingguy.nfs : reload nfs] ********************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.nfs/handlers/main.yml:2</b></span>
<span style="color:#AA5500">changed: [ansible-nas] =&gt; {</span>
<span style="color:#AA5500">    &quot;changed&quot;: true,</span>
<span style="color:#AA5500">    &quot;cmd&quot;: [</span>
<span style="color:#AA5500">        &quot;exportfs&quot;,</span>
<span style="color:#AA5500">        &quot;-ra&quot;</span>
<span style="color:#AA5500">    ],</span>
<span style="color:#AA5500">    &quot;delta&quot;: &quot;0:00:00.003663&quot;,</span>
<span style="color:#AA5500">    &quot;end&quot;: &quot;2025-09-21 00:12:54.170009&quot;,</span>
<span style="color:#AA5500">    &quot;rc&quot;: 0,</span>
<span style="color:#AA5500">    &quot;start&quot;: &quot;2025-09-21 00:12:54.166346&quot;</span>
<span style="color:#AA5500">}</span>
Sonntag 21 September 2025  00:12:54 +0200 (0:00:00.362)       0:01:14.250 ***** 

RUNNING HANDLER [geerlingguy.docker : restart docker] *************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.docker/handlers/main.yml:2</b></span>
<span style="color:#AA5500">changed: [ansible-nas] =&gt; {</span>
<span style="color:#AA5500">    &quot;changed&quot;: true,</span>
<span style="color:#AA5500">    &quot;name&quot;: &quot;docker&quot;,</span>
<span style="color:#AA5500">    &quot;state&quot;: &quot;started&quot;,</span>
<span style="color:#AA5500">    &quot;status&quot;: {</span>
<span style="color:#AA5500">        &quot;ActiveEnterTimestamp&quot;: &quot;Sun 2025-09-21 00:12:48 CEST&quot;,</span>
<span style="color:#AA5500">        &quot;ActiveEnterTimestampMonotonic&quot;: &quot;678342761142&quot;,</span>
<span style="color:#AA5500">        &quot;ActiveExitTimestampMonotonic&quot;: &quot;0&quot;,</span>
<span style="color:#AA5500">        &quot;ActiveState&quot;: &quot;active&quot;,</span>
<span style="color:#AA5500">        &quot;After&quot;: &quot;containerd.service network-online.target sysinit.target docker.socket time-set.target basic.target firewalld.service nss-lookup.target systemd-journald.socket system.slice&quot;,</span>
<span style="color:#AA5500">        &quot;AllowIsolate&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;AssertResult&quot;: &quot;yes&quot;,</span>
<span style="color:#AA5500">        &quot;AssertTimestamp&quot;: &quot;Sun 2025-09-21 00:12:48 CEST&quot;,</span>
<span style="color:#AA5500">        &quot;AssertTimestampMonotonic&quot;: &quot;678342356876&quot;,</span>
<span style="color:#AA5500">        &quot;Before&quot;: &quot;multi-user.target shutdown.target&quot;,</span>
<span style="color:#AA5500">        &quot;BlockIOAccounting&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;BlockIOWeight&quot;: &quot;[not set]&quot;,</span>
<span style="color:#AA5500">        &quot;CPUAccounting&quot;: &quot;yes&quot;,</span>
<span style="color:#AA5500">        &quot;CPUAffinityFromNUMA&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;CPUQuotaPerSecUSec&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;CPUQuotaPeriodUSec&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;CPUSchedulingPolicy&quot;: &quot;0&quot;,</span>
<span style="color:#AA5500">        &quot;CPUSchedulingPriority&quot;: &quot;0&quot;,</span>
<span style="color:#AA5500">        &quot;CPUSchedulingResetOnFork&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;CPUShares&quot;: &quot;[not set]&quot;,</span>
<span style="color:#AA5500">        &quot;CPUUsageNSec&quot;: &quot;202884000&quot;,</span>
<span style="color:#AA5500">        &quot;CPUWeight&quot;: &quot;[not set]&quot;,</span>
<span style="color:#AA5500">        &quot;CacheDirectoryMode&quot;: &quot;0755&quot;,</span>
<span style="color:#AA5500">        &quot;CanFreeze&quot;: &quot;yes&quot;,</span>
<span style="color:#AA5500">        &quot;CanIsolate&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;CanReload&quot;: &quot;yes&quot;,</span>
<span style="color:#AA5500">        &quot;CanStart&quot;: &quot;yes&quot;,</span>
<span style="color:#AA5500">        &quot;CanStop&quot;: &quot;yes&quot;,</span>
<span style="color:#AA5500">        &quot;CapabilityBoundingSet&quot;: &quot;cap_chown cap_dac_override cap_dac_read_search cap_fowner cap_fsetid cap_kill cap_setgid cap_setuid cap_setpcap cap_linux_immutable cap_net_bind_service cap_net_broadcast cap_net_admin cap_net_raw cap_ipc_lock cap_ipc_owner cap_sys_module cap_sys_rawio cap_sys_chroot cap_sys_ptrace cap_sys_pacct cap_sys_admin cap_sys_boot cap_sys_nice cap_sys_resource cap_sys_time cap_sys_tty_config cap_mknod cap_lease cap_audit_write cap_audit_control cap_setfcap cap_mac_override cap_mac_admin cap_syslog cap_wake_alarm cap_block_suspend cap_audit_read cap_perfmon cap_bpf cap_checkpoint_restore&quot;,</span>
<span style="color:#AA5500">        &quot;CleanResult&quot;: &quot;success&quot;,</span>
<span style="color:#AA5500">        &quot;CollectMode&quot;: &quot;inactive&quot;,</span>
<span style="color:#AA5500">        &quot;ConditionResult&quot;: &quot;yes&quot;,</span>
<span style="color:#AA5500">        &quot;ConditionTimestamp&quot;: &quot;Sun 2025-09-21 00:12:48 CEST&quot;,</span>
<span style="color:#AA5500">        &quot;ConditionTimestampMonotonic&quot;: &quot;678342356874&quot;,</span>
<span style="color:#AA5500">        &quot;ConfigurationDirectoryMode&quot;: &quot;0755&quot;,</span>
<span style="color:#AA5500">        &quot;Conflicts&quot;: &quot;shutdown.target&quot;,</span>
<span style="color:#AA5500">        &quot;ControlGroup&quot;: &quot;/system.slice/docker.service&quot;,</span>
<span style="color:#AA5500">        &quot;ControlGroupId&quot;: &quot;47271&quot;,</span>
<span style="color:#AA5500">        &quot;ControlPID&quot;: &quot;0&quot;,</span>
<span style="color:#AA5500">        &quot;CoredumpFilter&quot;: &quot;0x33&quot;,</span>
<span style="color:#AA5500">        &quot;DefaultDependencies&quot;: &quot;yes&quot;,</span>
<span style="color:#AA5500">        &quot;DefaultMemoryLow&quot;: &quot;0&quot;,</span>
<span style="color:#AA5500">        &quot;DefaultMemoryMin&quot;: &quot;0&quot;,</span>
<span style="color:#AA5500">        &quot;Delegate&quot;: &quot;yes&quot;,</span>
<span style="color:#AA5500">        &quot;DelegateControllers&quot;: &quot;cpu cpuset io memory pids&quot;,</span>
<span style="color:#AA5500">        &quot;Description&quot;: &quot;Docker Application Container Engine&quot;,</span>
<span style="color:#AA5500">        &quot;DevicePolicy&quot;: &quot;auto&quot;,</span>
<span style="color:#AA5500">        &quot;Documentation&quot;: &quot;https://docs.docker.com&quot;,</span>
<span style="color:#AA5500">        &quot;DynamicUser&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;EffectiveCPUs&quot;: &quot;0-3&quot;,</span>
<span style="color:#AA5500">        &quot;EffectiveMemoryNodes&quot;: &quot;0-7&quot;,</span>
<span style="color:#AA5500">        &quot;ExecMainCode&quot;: &quot;0&quot;,</span>
<span style="color:#AA5500">        &quot;ExecMainExitTimestampMonotonic&quot;: &quot;0&quot;,</span>
<span style="color:#AA5500">        &quot;ExecMainPID&quot;: &quot;1371484&quot;,</span>
<span style="color:#AA5500">        &quot;ExecMainStartTimestamp&quot;: &quot;Sun 2025-09-21 00:12:48 CEST&quot;,</span>
<span style="color:#AA5500">        &quot;ExecMainStartTimestampMonotonic&quot;: &quot;678342357985&quot;,</span>
<span style="color:#AA5500">        &quot;ExecMainStatus&quot;: &quot;0&quot;,</span>
<span style="color:#AA5500">        &quot;ExecReload&quot;: &quot;{ path=/bin/kill ; argv[]=/bin/kill -s HUP $MAINPID ; ignore_errors=no ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }&quot;,</span>
<span style="color:#AA5500">        &quot;ExecReloadEx&quot;: &quot;{ path=/bin/kill ; argv[]=/bin/kill -s HUP $MAINPID ; flags= ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }&quot;,</span>
<span style="color:#AA5500">        &quot;ExecStart&quot;: &quot;{ path=/usr/bin/dockerd ; argv[]=/usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock ; ignore_errors=no ; start_time=[Sun 2025-09-21 00:12:48 CEST] ; stop_time=[n/a] ; pid=1371484 ; code=(null) ; status=0/0 }&quot;,</span>
<span style="color:#AA5500">        &quot;ExecStartEx&quot;: &quot;{ path=/usr/bin/dockerd ; argv[]=/usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock ; flags= ; start_time=[Sun 2025-09-21 00:12:48 CEST] ; stop_time=[n/a] ; pid=1371484 ; code=(null) ; status=0/0 }&quot;,</span>
<span style="color:#AA5500">        &quot;ExitType&quot;: &quot;main&quot;,</span>
<span style="color:#AA5500">        &quot;FailureAction&quot;: &quot;none&quot;,</span>
<span style="color:#AA5500">        &quot;FileDescriptorStoreMax&quot;: &quot;0&quot;,</span>
<span style="color:#AA5500">        &quot;FinalKillSignal&quot;: &quot;9&quot;,</span>
<span style="color:#AA5500">        &quot;FragmentPath&quot;: &quot;/lib/systemd/system/docker.service&quot;,</span>
<span style="color:#AA5500">        &quot;FreezerState&quot;: &quot;running&quot;,</span>
<span style="color:#AA5500">        &quot;GID&quot;: &quot;[not set]&quot;,</span>
<span style="color:#AA5500">        &quot;GuessMainPID&quot;: &quot;yes&quot;,</span>
<span style="color:#AA5500">        &quot;IOAccounting&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;IOReadBytes&quot;: &quot;18446744073709551615&quot;,</span>
<span style="color:#AA5500">        &quot;IOReadOperations&quot;: &quot;18446744073709551615&quot;,</span>
<span style="color:#AA5500">        &quot;IOSchedulingClass&quot;: &quot;2&quot;,</span>
<span style="color:#AA5500">        &quot;IOSchedulingPriority&quot;: &quot;4&quot;,</span>
<span style="color:#AA5500">        &quot;IOWeight&quot;: &quot;[not set]&quot;,</span>
<span style="color:#AA5500">        &quot;IOWriteBytes&quot;: &quot;18446744073709551615&quot;,</span>
<span style="color:#AA5500">        &quot;IOWriteOperations&quot;: &quot;18446744073709551615&quot;,</span>
<span style="color:#AA5500">        &quot;IPAccounting&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;IPEgressBytes&quot;: &quot;[no data]&quot;,</span>
<span style="color:#AA5500">        &quot;IPEgressPackets&quot;: &quot;[no data]&quot;,</span>
<span style="color:#AA5500">        &quot;IPIngressBytes&quot;: &quot;[no data]&quot;,</span>
<span style="color:#AA5500">        &quot;IPIngressPackets&quot;: &quot;[no data]&quot;,</span>
<span style="color:#AA5500">        &quot;Id&quot;: &quot;docker.service&quot;,</span>
<span style="color:#AA5500">        &quot;IgnoreOnIsolate&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;IgnoreSIGPIPE&quot;: &quot;yes&quot;,</span>
<span style="color:#AA5500">        &quot;InactiveEnterTimestampMonotonic&quot;: &quot;0&quot;,</span>
<span style="color:#AA5500">        &quot;InactiveExitTimestamp&quot;: &quot;Sun 2025-09-21 00:12:48 CEST&quot;,</span>
<span style="color:#AA5500">        &quot;InactiveExitTimestampMonotonic&quot;: &quot;678342358408&quot;,</span>
<span style="color:#AA5500">        &quot;InvocationID&quot;: &quot;f7cb2757e0c24167a1312789b269cfb6&quot;,</span>
<span style="color:#AA5500">        &quot;JobRunningTimeoutUSec&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;JobTimeoutAction&quot;: &quot;none&quot;,</span>
<span style="color:#AA5500">        &quot;JobTimeoutUSec&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;KeyringMode&quot;: &quot;private&quot;,</span>
<span style="color:#AA5500">        &quot;KillMode&quot;: &quot;process&quot;,</span>
<span style="color:#AA5500">        &quot;KillSignal&quot;: &quot;15&quot;,</span>
<span style="color:#AA5500">        &quot;LimitAS&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;LimitASSoft&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;LimitCORE&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;LimitCORESoft&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;LimitCPU&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;LimitCPUSoft&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;LimitDATA&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;LimitDATASoft&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;LimitFSIZE&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;LimitFSIZESoft&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;LimitLOCKS&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;LimitLOCKSSoft&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;LimitMEMLOCK&quot;: &quot;8388608&quot;,</span>
<span style="color:#AA5500">        &quot;LimitMEMLOCKSoft&quot;: &quot;8388608&quot;,</span>
<span style="color:#AA5500">        &quot;LimitMSGQUEUE&quot;: &quot;819200&quot;,</span>
<span style="color:#AA5500">        &quot;LimitMSGQUEUESoft&quot;: &quot;819200&quot;,</span>
<span style="color:#AA5500">        &quot;LimitNICE&quot;: &quot;0&quot;,</span>
<span style="color:#AA5500">        &quot;LimitNICESoft&quot;: &quot;0&quot;,</span>
<span style="color:#AA5500">        &quot;LimitNOFILE&quot;: &quot;524288&quot;,</span>
<span style="color:#AA5500">        &quot;LimitNOFILESoft&quot;: &quot;1024&quot;,</span>
<span style="color:#AA5500">        &quot;LimitNPROC&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;LimitNPROCSoft&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;LimitRSS&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;LimitRSSSoft&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;LimitRTPRIO&quot;: &quot;0&quot;,</span>
<span style="color:#AA5500">        &quot;LimitRTPRIOSoft&quot;: &quot;0&quot;,</span>
<span style="color:#AA5500">        &quot;LimitRTTIME&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;LimitRTTIMESoft&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;LimitSIGPENDING&quot;: &quot;31916&quot;,</span>
<span style="color:#AA5500">        &quot;LimitSIGPENDINGSoft&quot;: &quot;31916&quot;,</span>
<span style="color:#AA5500">        &quot;LimitSTACK&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;LimitSTACKSoft&quot;: &quot;8388608&quot;,</span>
<span style="color:#AA5500">        &quot;LoadState&quot;: &quot;loaded&quot;,</span>
<span style="color:#AA5500">        &quot;LockPersonality&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;LogLevelMax&quot;: &quot;-1&quot;,</span>
<span style="color:#AA5500">        &quot;LogRateLimitBurst&quot;: &quot;0&quot;,</span>
<span style="color:#AA5500">        &quot;LogRateLimitIntervalUSec&quot;: &quot;0&quot;,</span>
<span style="color:#AA5500">        &quot;LogsDirectoryMode&quot;: &quot;0755&quot;,</span>
<span style="color:#AA5500">        &quot;MainPID&quot;: &quot;1371484&quot;,</span>
<span style="color:#AA5500">        &quot;ManagedOOMMemoryPressure&quot;: &quot;auto&quot;,</span>
<span style="color:#AA5500">        &quot;ManagedOOMMemoryPressureLimit&quot;: &quot;0&quot;,</span>
<span style="color:#AA5500">        &quot;ManagedOOMPreference&quot;: &quot;none&quot;,</span>
<span style="color:#AA5500">        &quot;ManagedOOMSwap&quot;: &quot;auto&quot;,</span>
<span style="color:#AA5500">        &quot;MemoryAccounting&quot;: &quot;yes&quot;,</span>
<span style="color:#AA5500">        &quot;MemoryAvailable&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;MemoryCurrent&quot;: &quot;[not set]&quot;,</span>
<span style="color:#AA5500">        &quot;MemoryDenyWriteExecute&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;MemoryHigh&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;MemoryLimit&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;MemoryLow&quot;: &quot;0&quot;,</span>
<span style="color:#AA5500">        &quot;MemoryMax&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;MemoryMin&quot;: &quot;0&quot;,</span>
<span style="color:#AA5500">        &quot;MemorySwapMax&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;MountAPIVFS&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;NFileDescriptorStore&quot;: &quot;0&quot;,</span>
<span style="color:#AA5500">        &quot;NRestarts&quot;: &quot;0&quot;,</span>
<span style="color:#AA5500">        &quot;NUMAPolicy&quot;: &quot;n/a&quot;,</span>
<span style="color:#AA5500">        &quot;Names&quot;: &quot;docker.service&quot;,</span>
<span style="color:#AA5500">        &quot;NeedDaemonReload&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;Nice&quot;: &quot;0&quot;,</span>
<span style="color:#AA5500">        &quot;NoNewPrivileges&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;NonBlocking&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;NotifyAccess&quot;: &quot;main&quot;,</span>
<span style="color:#AA5500">        &quot;OOMPolicy&quot;: &quot;continue&quot;,</span>
<span style="color:#AA5500">        &quot;OOMScoreAdjust&quot;: &quot;-500&quot;,</span>
<span style="color:#AA5500">        &quot;OnFailureJobMode&quot;: &quot;replace&quot;,</span>
<span style="color:#AA5500">        &quot;OnSuccessJobMode&quot;: &quot;fail&quot;,</span>
<span style="color:#AA5500">        &quot;Perpetual&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;PrivateDevices&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;PrivateIPC&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;PrivateMounts&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;PrivateNetwork&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;PrivateTmp&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;PrivateUsers&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;ProcSubset&quot;: &quot;all&quot;,</span>
<span style="color:#AA5500">        &quot;ProtectClock&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;ProtectControlGroups&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;ProtectHome&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;ProtectHostname&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;ProtectKernelLogs&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;ProtectKernelModules&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;ProtectKernelTunables&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;ProtectProc&quot;: &quot;default&quot;,</span>
<span style="color:#AA5500">        &quot;ProtectSystem&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;RefuseManualStart&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;RefuseManualStop&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;ReloadResult&quot;: &quot;success&quot;,</span>
<span style="color:#AA5500">        &quot;RemainAfterExit&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;RemoveIPC&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;Requires&quot;: &quot;docker.socket sysinit.target system.slice&quot;,</span>
<span style="color:#AA5500">        &quot;Restart&quot;: &quot;always&quot;,</span>
<span style="color:#AA5500">        &quot;RestartKillSignal&quot;: &quot;15&quot;,</span>
<span style="color:#AA5500">        &quot;RestartUSec&quot;: &quot;2s&quot;,</span>
<span style="color:#AA5500">        &quot;RestrictNamespaces&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;RestrictRealtime&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;RestrictSUIDSGID&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;Result&quot;: &quot;success&quot;,</span>
<span style="color:#AA5500">        &quot;RootDirectoryStartOnly&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;RuntimeDirectoryMode&quot;: &quot;0755&quot;,</span>
<span style="color:#AA5500">        &quot;RuntimeDirectoryPreserve&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;RuntimeMaxUSec&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;RuntimeRandomizedExtraUSec&quot;: &quot;0&quot;,</span>
<span style="color:#AA5500">        &quot;SameProcessGroup&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;SecureBits&quot;: &quot;0&quot;,</span>
<span style="color:#AA5500">        &quot;SendSIGHUP&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;SendSIGKILL&quot;: &quot;yes&quot;,</span>
<span style="color:#AA5500">        &quot;Slice&quot;: &quot;system.slice&quot;,</span>
<span style="color:#AA5500">        &quot;StandardError&quot;: &quot;inherit&quot;,</span>
<span style="color:#AA5500">        &quot;StandardInput&quot;: &quot;null&quot;,</span>
<span style="color:#AA5500">        &quot;StandardOutput&quot;: &quot;journal&quot;,</span>
<span style="color:#AA5500">        &quot;StartLimitAction&quot;: &quot;none&quot;,</span>
<span style="color:#AA5500">        &quot;StartLimitBurst&quot;: &quot;3&quot;,</span>
<span style="color:#AA5500">        &quot;StartLimitIntervalUSec&quot;: &quot;1min&quot;,</span>
<span style="color:#AA5500">        &quot;StartupBlockIOWeight&quot;: &quot;[not set]&quot;,</span>
<span style="color:#AA5500">        &quot;StartupCPUShares&quot;: &quot;[not set]&quot;,</span>
<span style="color:#AA5500">        &quot;StartupCPUWeight&quot;: &quot;[not set]&quot;,</span>
<span style="color:#AA5500">        &quot;StartupIOWeight&quot;: &quot;[not set]&quot;,</span>
<span style="color:#AA5500">        &quot;StateChangeTimestamp&quot;: &quot;Sun 2025-09-21 00:12:48 CEST&quot;,</span>
<span style="color:#AA5500">        &quot;StateChangeTimestampMonotonic&quot;: &quot;678342761142&quot;,</span>
<span style="color:#AA5500">        &quot;StateDirectoryMode&quot;: &quot;0755&quot;,</span>
<span style="color:#AA5500">        &quot;StatusErrno&quot;: &quot;0&quot;,</span>
<span style="color:#AA5500">        &quot;StopWhenUnneeded&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;SubState&quot;: &quot;running&quot;,</span>
<span style="color:#AA5500">        &quot;SuccessAction&quot;: &quot;none&quot;,</span>
<span style="color:#AA5500">        &quot;SyslogFacility&quot;: &quot;3&quot;,</span>
<span style="color:#AA5500">        &quot;SyslogLevel&quot;: &quot;6&quot;,</span>
<span style="color:#AA5500">        &quot;SyslogLevelPrefix&quot;: &quot;yes&quot;,</span>
<span style="color:#AA5500">        &quot;SyslogPriority&quot;: &quot;30&quot;,</span>
<span style="color:#AA5500">        &quot;SystemCallErrorNumber&quot;: &quot;2147483646&quot;,</span>
<span style="color:#AA5500">        &quot;TTYReset&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;TTYVHangup&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;TTYVTDisallocate&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;TasksAccounting&quot;: &quot;yes&quot;,</span>
<span style="color:#AA5500">        &quot;TasksCurrent&quot;: &quot;11&quot;,</span>
<span style="color:#AA5500">        &quot;TasksMax&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;TimeoutAbortUSec&quot;: &quot;1min 30s&quot;,</span>
<span style="color:#AA5500">        &quot;TimeoutCleanUSec&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;TimeoutStartFailureMode&quot;: &quot;terminate&quot;,</span>
<span style="color:#AA5500">        &quot;TimeoutStartUSec&quot;: &quot;infinity&quot;,</span>
<span style="color:#AA5500">        &quot;TimeoutStopFailureMode&quot;: &quot;terminate&quot;,</span>
<span style="color:#AA5500">        &quot;TimeoutStopUSec&quot;: &quot;1min 30s&quot;,</span>
<span style="color:#AA5500">        &quot;TimerSlackNSec&quot;: &quot;50000&quot;,</span>
<span style="color:#AA5500">        &quot;Transient&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;TriggeredBy&quot;: &quot;docker.socket&quot;,</span>
<span style="color:#AA5500">        &quot;Type&quot;: &quot;notify&quot;,</span>
<span style="color:#AA5500">        &quot;UID&quot;: &quot;[not set]&quot;,</span>
<span style="color:#AA5500">        &quot;UMask&quot;: &quot;0022&quot;,</span>
<span style="color:#AA5500">        &quot;UnitFilePreset&quot;: &quot;enabled&quot;,</span>
<span style="color:#AA5500">        &quot;UnitFileState&quot;: &quot;enabled&quot;,</span>
<span style="color:#AA5500">        &quot;UtmpMode&quot;: &quot;init&quot;,</span>
<span style="color:#AA5500">        &quot;WantedBy&quot;: &quot;multi-user.target&quot;,</span>
<span style="color:#AA5500">        &quot;Wants&quot;: &quot;network-online.target containerd.service&quot;,</span>
<span style="color:#AA5500">        &quot;WatchdogSignal&quot;: &quot;6&quot;,</span>
<span style="color:#AA5500">        &quot;WatchdogTimestampMonotonic&quot;: &quot;0&quot;,</span>
<span style="color:#AA5500">        &quot;WatchdogUSec&quot;: &quot;0&quot;</span>
<span style="color:#AA5500">    }</span>
<span style="color:#AA5500">}</span>
Sonntag 21 September 2025  00:12:55 +0200 (0:00:01.759)       0:01:16.010 ***** 
Sonntag 21 September 2025  00:12:56 +0200 (0:00:00.080)       0:01:16.090 ***** 
Sonntag 21 September 2025  00:12:56 +0200 (0:00:00.096)       0:01:16.187 ***** 
Sonntag 21 September 2025  00:12:56 +0200 (0:00:00.028)       0:01:16.215 ***** 
Sonntag 21 September 2025  00:12:56 +0200 (0:00:00.063)       0:01:16.279 ***** 

TASK [ansible-nas-general : Set login banner] *********************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-general/tasks/main.yml:2</b></span>
<span style="color:#AA0000">An exception occurred during task execution. To see the full traceback, use -vvv. The error was: If you are using a module and expect the file to exist on the remote, see the remote_src option</span>
<span style="color:#AA0000">fatal: [ansible-nas]: FAILED! =&gt; {</span>
<span style="color:#AA0000">    &quot;changed&quot;: false</span>
<span style="color:#AA0000">}</span>

<span style="color:#AA0000">MSG:</span>

<span style="color:#AA0000">Could not find or access &apos;motd.txt&apos;</span>
<span style="color:#AA0000">Searched in:</span>
	<span style="color:#AA0000">/media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-general/files/motd.txt</span>
	<span style="color:#AA0000">/media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-general/motd.txt</span>
	<span style="color:#AA0000">/media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-general/tasks/files/motd.txt</span>
	<span style="color:#AA0000">/media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-general/tasks/motd.txt</span>
	<span style="color:#AA0000">/media/IT/repos/github/forked/ansible-nas/files/motd.txt</span>
	<span style="color:#AA0000">/media/IT/repos/github/forked/ansible-nas/motd.txt on the Ansible Controller.</span>
<span style="color:#AA0000">If you are using a module and expect the file to exist on the remote, see the remote_src option</span>

PLAY RECAP ********************************************************************************************************************************************************************************************************
<span style="color:#AA0000">ansible-nas</span>                : <span style="color:#00AA00">ok=30  </span> <span style="color:#AA5500">changed=15  </span> unreachable=0    <span style="color:#AA0000">failed=1   </span> <span style="color:#00AAAA">skipped=23  </span> rescued=0    ignored=0   

Sonntag 21 September 2025  00:12:56 +0200 (0:00:00.151)       0:01:16.430 ***** 
=============================================================================== 
geerlingguy.docker : Install Docker packages (with downgrade option). ------------------------------------------------------------------------------------------------------------------------------------- 21.35s
/home/dietmar/.ansible/roles/geerlingguy.docker/tasks/main.yml:27 ------------------------------------------------------------------------------------------------------------------------------------------------
vladgh.samba.server : Install Samba packages -------------------------------------------------------------------------------------------------------------------------------------------------------------- 17.12s
/home/dietmar/.ansible/collections/ansible_collections/vladgh/samba/roles/server/tasks/main.yml:12 ---------------------------------------------------------------------------------------------------------------
geerlingguy.nfs : Ensure directories to export exist ------------------------------------------------------------------------------------------------------------------------------------------------------- 5.89s
/home/dietmar/.ansible/roles/geerlingguy.nfs/tasks/main.yml:19 ---------------------------------------------------------------------------------------------------------------------------------------------------
geerlingguy.docker : Add Docker repository. ---------------------------------------------------------------------------------------------------------------------------------------------------------------- 5.26s
/home/dietmar/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml:50 ----------------------------------------------------------------------------------------------------------------------------------------
geerlingguy.docker : Ensure additional dependencies are installed (on Ubuntu &lt; 20.04 and any other systems). ----------------------------------------------------------------------------------------------- 3.60s
/home/dietmar/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml:18 ----------------------------------------------------------------------------------------------------------------------------------------
geerlingguy.docker : Ensure dependencies are installed. ---------------------------------------------------------------------------------------------------------------------------------------------------- 3.15s
/home/dietmar/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml:10 ----------------------------------------------------------------------------------------------------------------------------------------
Gathering Facts -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 2.08s
/media/IT/repos/github/forked/ansible-nas/nas.yml:2 --------------------------------------------------------------------------------------------------------------------------------------------------------------
geerlingguy.docker : restart docker ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 1.76s
/home/dietmar/.ansible/roles/geerlingguy.docker/handlers/main.yml:2 ----------------------------------------------------------------------------------------------------------------------------------------------
vladgh.samba.server : Install Samba VFS extensions packages ------------------------------------------------------------------------------------------------------------------------------------------------ 1.44s
/home/dietmar/.ansible/collections/ansible_collections/vladgh/samba/roles/server/tasks/main.yml:19 ---------------------------------------------------------------------------------------------------------------
geerlingguy.docker : Install docker-compose-plugin (with downgrade option). -------------------------------------------------------------------------------------------------------------------------------- 1.42s
/home/dietmar/.ansible/roles/geerlingguy.docker/tasks/main.yml:44 ------------------------------------------------------------------------------------------------------------------------------------------------
geerlingguy.nfs : Ensure NFS utilities are installed. ------------------------------------------------------------------------------------------------------------------------------------------------------ 1.36s
/home/dietmar/.ansible/roles/geerlingguy.nfs/tasks/setup-Debian.yml:2 --------------------------------------------------------------------------------------------------------------------------------------------
vladgh.samba.server : Samba configuration ------------------------------------------------------------------------------------------------------------------------------------------------------------------ 1.29s
/home/dietmar/.ansible/collections/ansible_collections/vladgh/samba/roles/server/tasks/main.yml:80 ---------------------------------------------------------------------------------------------------------------
vladgh.samba.server : Start SMB service -------------------------------------------------------------------------------------------------------------------------------------------------------------------- 1.05s
/home/dietmar/.ansible/collections/ansible_collections/vladgh/samba/roles/server/tasks/main.yml:141 --------------------------------------------------------------------------------------------------------------
geerlingguy.docker : Ensure old versions of Docker are not installed. -------------------------------------------------------------------------------------------------------------------------------------- 0.96s
/home/dietmar/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml:2 -----------------------------------------------------------------------------------------------------------------------------------------
geerlingguy.docker : Add Docker apt key. ------------------------------------------------------------------------------------------------------------------------------------------------------------------- 0.81s
/home/dietmar/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml:30 ----------------------------------------------------------------------------------------------------------------------------------------
ansible-nas-users : Create ansible-nas user ---------------------------------------------------------------------------------------------------------------------------------------------------------------- 0.73s
/media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-users/tasks/main.yml:7 -------------------------------------------------------------------------------------------------------------------------------
geerlingguy.nfs : Copy exports file. ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- 0.71s
/home/dietmar/.ansible/roles/geerlingguy.nfs/tasks/main.yml:25 ---------------------------------------------------------------------------------------------------------------------------------------------------
vladgh.samba.server : Restart NMB service ------------------------------------------------------------------------------------------------------------------------------------------------------------------ 0.68s
/home/dietmar/.ansible/collections/ansible_collections/vladgh/samba/roles/server/handlers/main.yml:7 -------------------------------------------------------------------------------------------------------------
vladgh.samba.server : Register Samba version --------------------------------------------------------------------------------------------------------------------------------------------------------------- 0.64s
/home/dietmar/.ansible/collections/ansible_collections/vladgh/samba/roles/server/tasks/main.yml:26 ---------------------------------------------------------------------------------------------------------------
vladgh.samba.server : Restart SMB service ------------------------------------------------------------------------------------------------------------------------------------------------------------------ 0.62s
/home/dietmar/.ansible/collections/ansible_collections/vladgh/samba/roles/server/handlers/main.yml:2 -------------------------------------------------------------------------------------------------------------
[<span style="color:#00AA00">2025-09-21 00:12:56</span>] (venv) [<span style="color:#55FF55"><b>dietmar@MiraPi</b></span>] [<span style="color:#5555FF"><b>.../forked/ansible-nas</b></span>] $ 
</pre>
