<pre><span style="color:#00AA00">2025-09-21 01:32:55</span>] (venv) [<span style="color:#55FF55"><b>dietmar@MiraPi</b></span>] [<span style="color:#5555FF"><b>.../forked/ansible-nas</b></span>] $ ansible-playbook -i inventories/RaspiNAS/inventory nas.yml -b 
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
Sonntag 21 September 2025  01:33:02 +0200 (0:00:00.186)       0:00:00.186 ***** 

TASK [ansible-nas-users : Create ansible-nas group] ***************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-users/tasks/main.yml:2</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;gid&quot;: 1001,</span>
<span style="color:#00AA00">    &quot;name&quot;: &quot;ansible-nas&quot;,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;present&quot;,</span>
<span style="color:#00AA00">    &quot;system&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:33:03 +0200 (0:00:00.971)       0:00:01.157 ***** 

TASK [ansible-nas-users : Create ansible-nas user] ****************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-users/tasks/main.yml:7</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;append&quot;: false,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;comment&quot;: &quot;&quot;,</span>
<span style="color:#00AA00">    &quot;group&quot;: 1001,</span>
<span style="color:#00AA00">    &quot;home&quot;: &quot;/home/ansible-nas&quot;,</span>
<span style="color:#00AA00">    &quot;move_home&quot;: false,</span>
<span style="color:#00AA00">    &quot;name&quot;: &quot;ansible-nas&quot;,</span>
<span style="color:#00AA00">    &quot;shell&quot;: &quot;/usr/sbin/nologin&quot;,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;present&quot;,</span>
<span style="color:#00AA00">    &quot;uid&quot;: 994</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:33:04 +0200 (0:00:00.701)       0:00:01.859 ***** 

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
Sonntag 21 September 2025  01:33:04 +0200 (0:00:00.052)       0:00:01.912 ***** 

TASK [vladgh.samba.server : Install Samba packages] ***************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/collections/ansible_collections/vladgh/samba/roles/server/tasks/main.yml:12</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;cache_update_time&quot;: 1758406347,</span>
<span style="color:#00AA00">    &quot;cache_updated&quot;: false,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:33:06 +0200 (0:00:01.733)       0:00:03.646 ***** 

TASK [vladgh.samba.server : Install Samba VFS extensions packages] ************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/collections/ansible_collections/vladgh/samba/roles/server/tasks/main.yml:19</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;cache_update_time&quot;: 1758406347,</span>
<span style="color:#00AA00">    &quot;cache_updated&quot;: false,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:33:07 +0200 (0:00:01.408)       0:00:05.054 ***** 

TASK [vladgh.samba.server : Register Samba version] ***************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/collections/ansible_collections/vladgh/samba/roles/server/tasks/main.yml:26</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;cmd&quot;: &quot;set -o nounset -o pipefail -o errexit &amp;&amp; smbd --version | sed &apos;s/Version //&apos;\n&quot;,</span>
<span style="color:#00AA00">    &quot;delta&quot;: &quot;0:00:00.043587&quot;,</span>
<span style="color:#00AA00">    &quot;end&quot;: &quot;2025-09-21 01:33:08.052020&quot;,</span>
<span style="color:#00AA00">    &quot;rc&quot;: 0,</span>
<span style="color:#00AA00">    &quot;start&quot;: &quot;2025-09-21 01:33:08.008433&quot;</span>
<span style="color:#00AA00">}</span>

<span style="color:#00AA00">STDOUT:</span>

<span style="color:#00AA00">4.17.12-Debian</span>
Sonntag 21 September 2025  01:33:08 +0200 (0:00:00.624)       0:00:05.679 ***** 
Sonntag 21 September 2025  01:33:08 +0200 (0:00:00.078)       0:00:05.758 ***** 
Sonntag 21 September 2025  01:33:08 +0200 (0:00:00.028)       0:00:05.787 ***** 
Sonntag 21 September 2025  01:33:08 +0200 (0:00:00.072)       0:00:05.859 ***** 
Sonntag 21 September 2025  01:33:08 +0200 (0:00:00.031)       0:00:05.891 ***** 

TASK [vladgh.samba.server : Samba configuration] ******************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/collections/ansible_collections/vladgh/samba/roles/server/tasks/main.yml:80</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;checksum&quot;: &quot;353157b186814dd24425adcce53a023a2361a2e5&quot;,</span>
<span style="color:#00AA00">    &quot;dest&quot;: &quot;/etc/samba/smb.conf&quot;,</span>
<span style="color:#00AA00">    &quot;gid&quot;: 0,</span>
<span style="color:#00AA00">    &quot;group&quot;: &quot;root&quot;,</span>
<span style="color:#00AA00">    &quot;mode&quot;: &quot;0644&quot;,</span>
<span style="color:#00AA00">    &quot;owner&quot;: &quot;root&quot;,</span>
<span style="color:#00AA00">    &quot;path&quot;: &quot;/etc/samba/smb.conf&quot;,</span>
<span style="color:#00AA00">    &quot;size&quot;: 509,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;file&quot;,</span>
<span style="color:#00AA00">    &quot;uid&quot;: 0</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:33:09 +0200 (0:00:01.314)       0:00:07.206 ***** 
Sonntag 21 September 2025  01:33:09 +0200 (0:00:00.043)       0:00:07.249 ***** 
Sonntag 21 September 2025  01:33:09 +0200 (0:00:00.062)       0:00:07.311 ***** 
Sonntag 21 September 2025  01:33:09 +0200 (0:00:00.027)       0:00:07.339 ***** 
Sonntag 21 September 2025  01:33:09 +0200 (0:00:00.047)       0:00:07.387 ***** 

TASK [vladgh.samba.server : Start SMB service] ********************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/collections/ansible_collections/vladgh/samba/roles/server/tasks/main.yml:141</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;enabled&quot;: true,</span>
<span style="color:#00AA00">    &quot;name&quot;: &quot;smbd&quot;,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;started&quot;,</span>
<span style="color:#00AA00">    &quot;status&quot;: {</span>
<span style="color:#00AA00">        &quot;ActiveEnterTimestamp&quot;: &quot;Sun 2025-09-21 00:12:53 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;ActiveEnterTimestampMonotonic&quot;: &quot;678347313550&quot;,</span>
<span style="color:#00AA00">        &quot;ActiveExitTimestamp&quot;: &quot;Sun 2025-09-21 00:12:53 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;ActiveExitTimestampMonotonic&quot;: &quot;678347213001&quot;,</span>
<span style="color:#00AA00">        &quot;ActiveState&quot;: &quot;active&quot;,</span>
<span style="color:#00AA00">        &quot;After&quot;: &quot;network-online.target system.slice winbind.service sysinit.target nmbd.service basic.target systemd-journald.socket network.target&quot;,</span>
<span style="color:#00AA00">        &quot;AllowIsolate&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;AssertResult&quot;: &quot;yes&quot;,</span>
<span style="color:#00AA00">        &quot;AssertTimestamp&quot;: &quot;Sun 2025-09-21 00:12:53 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;AssertTimestampMonotonic&quot;: &quot;678347215605&quot;,</span>
<span style="color:#00AA00">        &quot;Before&quot;: &quot;zfs-share.service shutdown.target multi-user.target&quot;,</span>
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
<span style="color:#00AA00">        &quot;CPUUsageNSec&quot;: &quot;116335000&quot;,</span>
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
<span style="color:#00AA00">        &quot;ConditionTimestamp&quot;: &quot;Sun 2025-09-21 00:12:53 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;ConditionTimestampMonotonic&quot;: &quot;678347215603&quot;,</span>
<span style="color:#00AA00">        &quot;ConfigurationDirectoryMode&quot;: &quot;0755&quot;,</span>
<span style="color:#00AA00">        &quot;Conflicts&quot;: &quot;shutdown.target&quot;,</span>
<span style="color:#00AA00">        &quot;ConsistsOf&quot;: &quot;zfs-share.service&quot;,</span>
<span style="color:#00AA00">        &quot;ControlGroup&quot;: &quot;/system.slice/smbd.service&quot;,</span>
<span style="color:#00AA00">        &quot;ControlGroupId&quot;: &quot;47339&quot;,</span>
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
<span style="color:#00AA00">        &quot;EffectiveCPUs&quot;: &quot;0-3&quot;,</span>
<span style="color:#00AA00">        &quot;EffectiveMemoryNodes&quot;: &quot;0-7&quot;,</span>
<span style="color:#00AA00">        &quot;EnvironmentFiles&quot;: &quot;/etc/default/samba (ignore_errors=yes)&quot;,</span>
<span style="color:#00AA00">        &quot;ExecCondition&quot;: &quot;{ path=/usr/share/samba/is-configured ; argv[]=/usr/share/samba/is-configured smb ; ignore_errors=no ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }&quot;,</span>
<span style="color:#00AA00">        &quot;ExecConditionEx&quot;: &quot;{ path=/usr/share/samba/is-configured ; argv[]=/usr/share/samba/is-configured smb ; flags= ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainCode&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainExitTimestampMonotonic&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainPID&quot;: &quot;1371841&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainStartTimestamp&quot;: &quot;Sun 2025-09-21 00:12:53 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainStartTimestampMonotonic&quot;: &quot;678347263654&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainStatus&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;ExecReload&quot;: &quot;{ path=/bin/kill ; argv[]=/bin/kill -HUP $MAINPID ; ignore_errors=no ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }&quot;,</span>
<span style="color:#00AA00">        &quot;ExecReloadEx&quot;: &quot;{ path=/bin/kill ; argv[]=/bin/kill -HUP $MAINPID ; flags= ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }&quot;,</span>
<span style="color:#00AA00">        &quot;ExecStart&quot;: &quot;{ path=/usr/sbin/smbd ; argv[]=/usr/sbin/smbd --foreground --no-process-group $SMBDOPTIONS ; ignore_errors=no ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }&quot;,</span>
<span style="color:#00AA00">        &quot;ExecStartEx&quot;: &quot;{ path=/usr/sbin/smbd ; argv[]=/usr/sbin/smbd --foreground --no-process-group $SMBDOPTIONS ; flags= ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }&quot;,</span>
<span style="color:#00AA00">        &quot;ExecStartPre&quot;: &quot;{ path=/usr/share/samba/update-apparmor-samba-profile ; argv[]=/usr/share/samba/update-apparmor-samba-profile ; ignore_errors=no ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }&quot;,</span>
<span style="color:#00AA00">        &quot;ExecStartPreEx&quot;: &quot;{ path=/usr/share/samba/update-apparmor-samba-profile ; argv[]=/usr/share/samba/update-apparmor-samba-profile ; flags= ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }&quot;,</span>
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
<span style="color:#00AA00">        &quot;InactiveEnterTimestamp&quot;: &quot;Sun 2025-09-21 00:12:53 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;InactiveEnterTimestampMonotonic&quot;: &quot;678347214977&quot;,</span>
<span style="color:#00AA00">        &quot;InactiveExitTimestamp&quot;: &quot;Sun 2025-09-21 00:12:53 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;InactiveExitTimestampMonotonic&quot;: &quot;678347236449&quot;,</span>
<span style="color:#00AA00">        &quot;InvocationID&quot;: &quot;81169d50bea849678ca9dde5f74c8369&quot;,</span>
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
<span style="color:#00AA00">        &quot;MainPID&quot;: &quot;1371841&quot;,</span>
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
<span style="color:#00AA00">        &quot;Requires&quot;: &quot;system.slice sysinit.target&quot;,</span>
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
<span style="color:#00AA00">        &quot;StateChangeTimestamp&quot;: &quot;Sun 2025-09-21 00:12:53 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;StateChangeTimestampMonotonic&quot;: &quot;678347313550&quot;,</span>
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
Sonntag 21 September 2025  01:33:10 +0200 (0:00:01.060)       0:00:08.447 ***** 

TASK [vladgh.samba.server : Start NMB service] ********************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/collections/ansible_collections/vladgh/samba/roles/server/tasks/main.yml:148</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;enabled&quot;: true,</span>
<span style="color:#00AA00">    &quot;name&quot;: &quot;nmbd&quot;,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;started&quot;,</span>
<span style="color:#00AA00">    &quot;status&quot;: {</span>
<span style="color:#00AA00">        &quot;ActiveEnterTimestamp&quot;: &quot;Sun 2025-09-21 00:12:53 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;ActiveEnterTimestampMonotonic&quot;: &quot;678347998447&quot;,</span>
<span style="color:#00AA00">        &quot;ActiveExitTimestamp&quot;: &quot;Sun 2025-09-21 00:12:53 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;ActiveExitTimestampMonotonic&quot;: &quot;678347854364&quot;,</span>
<span style="color:#00AA00">        &quot;ActiveState&quot;: &quot;active&quot;,</span>
<span style="color:#00AA00">        &quot;After&quot;: &quot;network.target sysinit.target system.slice network-online.target systemd-journald.socket basic.target&quot;,</span>
<span style="color:#00AA00">        &quot;AllowIsolate&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;AssertResult&quot;: &quot;yes&quot;,</span>
<span style="color:#00AA00">        &quot;AssertTimestamp&quot;: &quot;Sun 2025-09-21 00:12:53 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;AssertTimestampMonotonic&quot;: &quot;678347856528&quot;,</span>
<span style="color:#00AA00">        &quot;Before&quot;: &quot;shutdown.target smbd.service multi-user.target&quot;,</span>
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
<span style="color:#00AA00">        &quot;CPUUsageNSec&quot;: &quot;666246000&quot;,</span>
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
<span style="color:#00AA00">        &quot;ConditionTimestamp&quot;: &quot;Sun 2025-09-21 00:12:53 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;ConditionTimestampMonotonic&quot;: &quot;678347856524&quot;,</span>
<span style="color:#00AA00">        &quot;ConfigurationDirectoryMode&quot;: &quot;0755&quot;,</span>
<span style="color:#00AA00">        &quot;Conflicts&quot;: &quot;shutdown.target&quot;,</span>
<span style="color:#00AA00">        &quot;ControlGroup&quot;: &quot;/system.slice/nmbd.service&quot;,</span>
<span style="color:#00AA00">        &quot;ControlGroupId&quot;: &quot;47373&quot;,</span>
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
<span style="color:#00AA00">        &quot;EffectiveCPUs&quot;: &quot;0-3&quot;,</span>
<span style="color:#00AA00">        &quot;EffectiveMemoryNodes&quot;: &quot;0-7&quot;,</span>
<span style="color:#00AA00">        &quot;EnvironmentFiles&quot;: &quot;/etc/default/samba (ignore_errors=yes)&quot;,</span>
<span style="color:#00AA00">        &quot;ExecCondition&quot;: &quot;{ path=/usr/share/samba/is-configured ; argv[]=/usr/share/samba/is-configured nmb ; ignore_errors=no ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }&quot;,</span>
<span style="color:#00AA00">        &quot;ExecConditionEx&quot;: &quot;{ path=/usr/share/samba/is-configured ; argv[]=/usr/share/samba/is-configured nmb ; flags= ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainCode&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainExitTimestampMonotonic&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainPID&quot;: &quot;1371899&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainStartTimestamp&quot;: &quot;Sun 2025-09-21 00:12:53 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainStartTimestampMonotonic&quot;: &quot;678347968158&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainStatus&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;ExecReload&quot;: &quot;{ path=/bin/kill ; argv[]=/bin/kill -HUP $MAINPID ; ignore_errors=no ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }&quot;,</span>
<span style="color:#00AA00">        &quot;ExecReloadEx&quot;: &quot;{ path=/bin/kill ; argv[]=/bin/kill -HUP $MAINPID ; flags= ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }&quot;,</span>
<span style="color:#00AA00">        &quot;ExecStart&quot;: &quot;{ path=/usr/sbin/nmbd ; argv[]=/usr/sbin/nmbd --foreground --no-process-group $NMBDOPTIONS ; ignore_errors=no ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }&quot;,</span>
<span style="color:#00AA00">        &quot;ExecStartEx&quot;: &quot;{ path=/usr/sbin/nmbd ; argv[]=/usr/sbin/nmbd --foreground --no-process-group $NMBDOPTIONS ; flags= ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }&quot;,</span>
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
<span style="color:#00AA00">        &quot;InactiveEnterTimestamp&quot;: &quot;Sun 2025-09-21 00:12:53 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;InactiveEnterTimestampMonotonic&quot;: &quot;678347855894&quot;,</span>
<span style="color:#00AA00">        &quot;InactiveExitTimestamp&quot;: &quot;Sun 2025-09-21 00:12:53 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;InactiveExitTimestampMonotonic&quot;: &quot;678347896856&quot;,</span>
<span style="color:#00AA00">        &quot;InvocationID&quot;: &quot;f2d0ebab30ec4b6ea44ff35ac088ecd4&quot;,</span>
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
<span style="color:#00AA00">        &quot;MainPID&quot;: &quot;1371899&quot;,</span>
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
<span style="color:#00AA00">        &quot;Requires&quot;: &quot;system.slice sysinit.target&quot;,</span>
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
<span style="color:#00AA00">        &quot;StateChangeTimestamp&quot;: &quot;Sun 2025-09-21 00:12:53 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;StateChangeTimestampMonotonic&quot;: &quot;678347998447&quot;,</span>
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
<span style="color:#00AA00">        &quot;TasksCurrent&quot;: &quot;2&quot;,</span>
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
Sonntag 21 September 2025  01:33:11 +0200 (0:00:00.548)       0:00:08.995 ***** 
Sonntag 21 September 2025  01:33:11 +0200 (0:00:00.060)       0:00:09.056 ***** 

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
Sonntag 21 September 2025  01:33:11 +0200 (0:00:00.047)       0:00:09.103 ***** 
Sonntag 21 September 2025  01:33:11 +0200 (0:00:00.031)       0:00:09.135 ***** 
Sonntag 21 September 2025  01:33:11 +0200 (0:00:00.037)       0:00:09.172 ***** 

TASK [geerlingguy.nfs : include_tasks] ****************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.nfs/tasks/main.yml:16</b></span>
<span style="color:#00AAAA">included: /home/dietmar/.ansible/roles/geerlingguy.nfs/tasks/setup-Debian.yml for ansible-nas</span>
Sonntag 21 September 2025  01:33:11 +0200 (0:00:00.056)       0:00:09.228 ***** 

TASK [geerlingguy.nfs : Ensure NFS utilities are installed.] ******************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.nfs/tasks/setup-Debian.yml:2</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;cache_update_time&quot;: 1758406347,</span>
<span style="color:#00AA00">    &quot;cache_updated&quot;: false,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:33:13 +0200 (0:00:01.341)       0:00:10.569 ***** 

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
<span style="color:#00AA00">    &quot;mode&quot;: &quot;0755&quot;,</span>
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
<span style="color:#00AA00">ok: [ansible-nas] =&gt; (item=/mnt/Volume1/local/IT *(rw,async,no_root_squash,no_subtree_check)) =&gt; {</span>
<span style="color:#00AA00">    &quot;ansible_loop_var&quot;: &quot;item&quot;,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;gid&quot;: 1001,</span>
<span style="color:#00AA00">    &quot;group&quot;: &quot;ansible-nas&quot;,</span>
<span style="color:#00AA00">    &quot;item&quot;: &quot;/mnt/Volume1/local/IT *(rw,async,no_root_squash,no_subtree_check)&quot;,</span>
<span style="color:#00AA00">    &quot;mode&quot;: &quot;0777&quot;,</span>
<span style="color:#00AA00">    &quot;owner&quot;: &quot;ansible-nas&quot;,</span>
<span style="color:#00AA00">    &quot;path&quot;: &quot;/mnt/Volume1/local/IT&quot;,</span>
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
Sonntag 21 September 2025  01:33:18 +0200 (0:00:05.964)       0:00:16.534 ***** 

TASK [geerlingguy.nfs : Copy exports file.] ***********************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.nfs/tasks/main.yml:25</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;checksum&quot;: &quot;524aa4b4f1584667de00f8fe8d327c22b1f27f70&quot;,</span>
<span style="color:#00AA00">    &quot;dest&quot;: &quot;/etc/exports&quot;,</span>
<span style="color:#00AA00">    &quot;gid&quot;: 0,</span>
<span style="color:#00AA00">    &quot;group&quot;: &quot;root&quot;,</span>
<span style="color:#00AA00">    &quot;mode&quot;: &quot;0644&quot;,</span>
<span style="color:#00AA00">    &quot;owner&quot;: &quot;root&quot;,</span>
<span style="color:#00AA00">    &quot;path&quot;: &quot;/etc/exports&quot;,</span>
<span style="color:#00AA00">    &quot;size&quot;: 1669,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;file&quot;,</span>
<span style="color:#00AA00">    &quot;uid&quot;: 0</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:33:19 +0200 (0:00:00.647)       0:00:17.182 ***** 

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
<span style="color:#00AA00">        &quot;After&quot;: &quot;local-fs.target rpc-gssd.service zfs-share.service nfs-mountd.service gssproxy.service nfsdcld.service mnt-Volume1.mount rpc-svcgssd.service nfs-idmapd.service network-online.target rpc-statd.service systemd-journald.socket rpcbind.socket proc-fs-nfsd.mount system.slice -.mount&quot;,</span>
<span style="color:#00AA00">        &quot;AllowIsolate&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;AssertResult&quot;: &quot;yes&quot;,</span>
<span style="color:#00AA00">        &quot;AssertTimestamp&quot;: &quot;Sat 2025-09-13 03:47:23 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;AssertTimestampMonotonic&quot;: &quot;17797807&quot;,</span>
<span style="color:#00AA00">        &quot;Before&quot;: &quot;media-Produktion.mount media-Medien.mount media-web.mount media-Dokumente.mount rpc-statd-notify.service&quot;,</span>
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
<span style="color:#00AA00">        &quot;ConsistsOf&quot;: &quot;rpc-svcgssd.service zfs-share.service&quot;,</span>
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
<span style="color:#00AA00">        &quot;Requires&quot;: &quot;system.slice mnt-Volume1.mount proc-fs-nfsd.mount -.mount network.target nfs-mountd.service&quot;,</span>
<span style="color:#00AA00">        &quot;RequiresMountsFor&quot;: &quot;/mnt/Volume1/local/Ägyptologie /mnt/Volume1/local/Podcasts /mnt/Volume1/docker /mnt/Volume1/local/Media /mnt/Volume1/local/Comics /mnt/Volume1/local/Persönliches /mnt/Volume1/local/TV /mnt/Volume1/local/Organisation /mnt/Volume1/local/Documents /mnt/Volume1/local/Books /mnt/Volume1/local/Movies /mnt/Volume1/local/Download /mnt/Volume1/local/Versorgung /mnt/Volume1/local/Inventar /mnt/Volume1/local/Music /mnt/Volume1/local/Audiobooks /mnt/Volume1/local/Photos /mnt/Volume1/local/IT&quot;,</span>
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
<span style="color:#00AA00">        &quot;Wants&quot;: &quot;auth-rpcgss-module.service rpcbind.socket network-online.target rpc-statd-notify.service nfs-idmapd.service rpc-statd.service rpc-svcgssd.service nfsdcld.service&quot;,</span>
<span style="color:#00AA00">        &quot;WatchdogSignal&quot;: &quot;6&quot;,</span>
<span style="color:#00AA00">        &quot;WatchdogTimestampMonotonic&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;WatchdogUSec&quot;: &quot;0&quot;</span>
<span style="color:#00AA00">    }</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:33:20 +0200 (0:00:00.580)       0:00:17.762 ***** 

TASK [geerlingguy.docker : Load OS-specific vars.] ****************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.docker/tasks/main.yml:2</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;ansible_facts&quot;: {},</span>
<span style="color:#00AA00">    &quot;ansible_included_var_files&quot;: [</span>
<span style="color:#00AA00">        &quot;/home/dietmar/.ansible/roles/geerlingguy.docker/vars/main.yml&quot;</span>
<span style="color:#00AA00">    ],</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:33:20 +0200 (0:00:00.040)       0:00:17.803 ***** 
Sonntag 21 September 2025  01:33:20 +0200 (0:00:00.041)       0:00:17.844 ***** 

TASK [geerlingguy.docker : include_tasks] *************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.docker/tasks/main.yml:16</b></span>
<span style="color:#00AAAA">included: /home/dietmar/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml for ansible-nas</span>
Sonntag 21 September 2025  01:33:20 +0200 (0:00:00.061)       0:00:17.905 ***** 

TASK [geerlingguy.docker : Ensure old versions of Docker are not installed.] **************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml:2</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:33:21 +0200 (0:00:00.973)       0:00:18.879 ***** 

TASK [geerlingguy.docker : Ensure dependencies are installed.] ****************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml:10</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;cache_update_time&quot;: 1758406347,</span>
<span style="color:#00AA00">    &quot;cache_updated&quot;: false,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:33:22 +0200 (0:00:01.468)       0:00:20.348 ***** 

TASK [geerlingguy.docker : Ensure additional dependencies are installed (on Ubuntu &lt; 20.04 and any other systems).] ***********************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml:18</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;cache_update_time&quot;: 1758406347,</span>
<span style="color:#00AA00">    &quot;cache_updated&quot;: false,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:33:24 +0200 (0:00:01.396)       0:00:21.745 ***** 
Sonntag 21 September 2025  01:33:24 +0200 (0:00:00.058)       0:00:21.804 ***** 

TASK [geerlingguy.docker : Add Docker apt key.] *******************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml:30</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;checksum_dest&quot;: null,</span>
<span style="color:#00AA00">    &quot;checksum_src&quot;: null,</span>
<span style="color:#00AA00">    &quot;dest&quot;: &quot;/etc/apt/trusted.gpg.d/docker.asc&quot;,</span>
<span style="color:#00AA00">    &quot;elapsed&quot;: 0,</span>
<span style="color:#00AA00">    &quot;gid&quot;: 0,</span>
<span style="color:#00AA00">    &quot;group&quot;: &quot;root&quot;,</span>
<span style="color:#00AA00">    &quot;mode&quot;: &quot;0644&quot;,</span>
<span style="color:#00AA00">    &quot;owner&quot;: &quot;root&quot;,</span>
<span style="color:#00AA00">    &quot;size&quot;: 3817,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;file&quot;,</span>
<span style="color:#00AA00">    &quot;uid&quot;: 0,</span>
<span style="color:#00AA00">    &quot;url&quot;: &quot;https://download.docker.com/linux/debian/gpg&quot;</span>
<span style="color:#00AA00">}</span>

<span style="color:#00AA00">MSG:</span>

<span style="color:#00AA00">file already exists</span>
Sonntag 21 September 2025  01:33:24 +0200 (0:00:00.720)       0:00:22.524 ***** 
Sonntag 21 September 2025  01:33:25 +0200 (0:00:00.080)       0:00:22.605 ***** 
Sonntag 21 September 2025  01:33:25 +0200 (0:00:00.075)       0:00:22.681 ***** 

TASK [geerlingguy.docker : Add Docker repository.] ****************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml:50</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;repo&quot;: &quot;deb [arch=arm64 signed-by=/etc/apt/trusted.gpg.d/docker.asc] https://download.docker.com/linux/debian bookworm stable&quot;,</span>
<span style="color:#00AA00">    &quot;sources_added&quot;: [],</span>
<span style="color:#00AA00">    &quot;sources_removed&quot;: [],</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;present&quot;</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:33:25 +0200 (0:00:00.826)       0:00:23.507 ***** 
Sonntag 21 September 2025  01:33:25 +0200 (0:00:00.042)       0:00:23.550 ***** 

TASK [geerlingguy.docker : Install Docker packages (with downgrade option).] **************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.docker/tasks/main.yml:27</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;cache_update_time&quot;: 1758406347,</span>
<span style="color:#00AA00">    &quot;cache_updated&quot;: false,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:33:27 +0200 (0:00:01.392)       0:00:24.942 ***** 
Sonntag 21 September 2025  01:33:27 +0200 (0:00:00.076)       0:00:25.019 ***** 

TASK [geerlingguy.docker : Install docker-compose-plugin (with downgrade option).] ********************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.docker/tasks/main.yml:44</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;cache_update_time&quot;: 1758406347,</span>
<span style="color:#00AA00">    &quot;cache_updated&quot;: false,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:33:28 +0200 (0:00:01.402)       0:00:26.422 ***** 
Sonntag 21 September 2025  01:33:28 +0200 (0:00:00.066)       0:00:26.489 ***** 
Sonntag 21 September 2025  01:33:29 +0200 (0:00:00.095)       0:00:26.584 ***** 

TASK [geerlingguy.docker : Ensure Docker is started and enabled at boot.] *****************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.docker/tasks/main.yml:68</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;enabled&quot;: true,</span>
<span style="color:#00AA00">    &quot;name&quot;: &quot;docker&quot;,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;started&quot;,</span>
<span style="color:#00AA00">    &quot;status&quot;: {</span>
<span style="color:#00AA00">        &quot;ActiveEnterTimestamp&quot;: &quot;Sun 2025-09-21 01:17:18 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;ActiveEnterTimestampMonotonic&quot;: &quot;682212838471&quot;,</span>
<span style="color:#00AA00">        &quot;ActiveExitTimestamp&quot;: &quot;Sun 2025-09-21 01:17:17 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;ActiveExitTimestampMonotonic&quot;: &quot;682211738319&quot;,</span>
<span style="color:#00AA00">        &quot;ActiveState&quot;: &quot;active&quot;,</span>
<span style="color:#00AA00">        &quot;After&quot;: &quot;basic.target network-online.target systemd-journald.socket firewalld.service sysinit.target system.slice docker.socket time-set.target containerd.service nss-lookup.target&quot;,</span>
<span style="color:#00AA00">        &quot;AllowIsolate&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;AssertResult&quot;: &quot;yes&quot;,</span>
<span style="color:#00AA00">        &quot;AssertTimestamp&quot;: &quot;Sun 2025-09-21 01:17:17 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;AssertTimestampMonotonic&quot;: &quot;682211744363&quot;,</span>
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
<span style="color:#00AA00">        &quot;CPUUsageNSec&quot;: &quot;6816023000&quot;,</span>
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
<span style="color:#00AA00">        &quot;ConditionTimestamp&quot;: &quot;Sun 2025-09-21 01:17:17 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;ConditionTimestampMonotonic&quot;: &quot;682211744361&quot;,</span>
<span style="color:#00AA00">        &quot;ConfigurationDirectoryMode&quot;: &quot;0755&quot;,</span>
<span style="color:#00AA00">        &quot;Conflicts&quot;: &quot;shutdown.target&quot;,</span>
<span style="color:#00AA00">        &quot;ControlGroup&quot;: &quot;/system.slice/docker.service&quot;,</span>
<span style="color:#00AA00">        &quot;ControlGroupId&quot;: &quot;48501&quot;,</span>
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
<span style="color:#00AA00">        &quot;ExecMainPID&quot;: &quot;1438392&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainStartTimestamp&quot;: &quot;Sun 2025-09-21 01:17:17 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainStartTimestampMonotonic&quot;: &quot;682211772140&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainStatus&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;ExecReload&quot;: &quot;{ path=/bin/kill ; argv[]=/bin/kill -s HUP $MAINPID ; ignore_errors=no ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }&quot;,</span>
<span style="color:#00AA00">        &quot;ExecReloadEx&quot;: &quot;{ path=/bin/kill ; argv[]=/bin/kill -s HUP $MAINPID ; flags= ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }&quot;,</span>
<span style="color:#00AA00">        &quot;ExecStart&quot;: &quot;{ path=/usr/bin/dockerd ; argv[]=/usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock ; ignore_errors=no ; start_time=[Sun 2025-09-21 01:17:17 CEST] ; stop_time=[n/a] ; pid=1438392 ; code=(null) ; status=0/0 }&quot;,</span>
<span style="color:#00AA00">        &quot;ExecStartEx&quot;: &quot;{ path=/usr/bin/dockerd ; argv[]=/usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock ; flags= ; start_time=[Sun 2025-09-21 01:17:17 CEST] ; stop_time=[n/a] ; pid=1438392 ; code=(null) ; status=0/0 }&quot;,</span>
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
<span style="color:#00AA00">        &quot;InactiveEnterTimestamp&quot;: &quot;Sun 2025-09-21 01:17:17 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;InactiveEnterTimestampMonotonic&quot;: &quot;682211741982&quot;,</span>
<span style="color:#00AA00">        &quot;InactiveExitTimestamp&quot;: &quot;Sun 2025-09-21 01:17:17 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;InactiveExitTimestampMonotonic&quot;: &quot;682211772532&quot;,</span>
<span style="color:#00AA00">        &quot;InvocationID&quot;: &quot;de2456bc0f404954bbc6dfebcf18bbb2&quot;,</span>
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
<span style="color:#00AA00">        &quot;MainPID&quot;: &quot;1438392&quot;,</span>
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
<span style="color:#00AA00">        &quot;StateChangeTimestamp&quot;: &quot;Sun 2025-09-21 01:17:18 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;StateChangeTimestampMonotonic&quot;: &quot;682212838471&quot;,</span>
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
<span style="color:#00AA00">        &quot;TasksCurrent&quot;: &quot;21&quot;,</span>
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
Sonntag 21 September 2025  01:33:29 +0200 (0:00:00.564)       0:00:27.148 ***** 
<span style="color:#0000AA">META: triggered running handlers for ansible-nas</span>
Sonntag 21 September 2025  01:33:29 +0200 (0:00:00.020)       0:00:27.169 ***** 
Sonntag 21 September 2025  01:33:29 +0200 (0:00:00.071)       0:00:27.240 ***** 
Sonntag 21 September 2025  01:33:29 +0200 (0:00:00.072)       0:00:27.312 ***** 
Sonntag 21 September 2025  01:33:29 +0200 (0:00:00.029)       0:00:27.342 ***** 
Sonntag 21 September 2025  01:33:29 +0200 (0:00:00.058)       0:00:27.401 ***** 

TASK [ansible-nas-general : Set login banner] *********************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-general/tasks/main.yml:2</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;checksum&quot;: &quot;cafe32892b670cb14dcc5f348fbb0b38062e90da&quot;,</span>
<span style="color:#00AA00">    &quot;dest&quot;: &quot;/etc/motd&quot;,</span>
<span style="color:#00AA00">    &quot;gid&quot;: 0,</span>
<span style="color:#00AA00">    &quot;group&quot;: &quot;root&quot;,</span>
<span style="color:#00AA00">    &quot;mode&quot;: &quot;0644&quot;,</span>
<span style="color:#00AA00">    &quot;owner&quot;: &quot;root&quot;,</span>
<span style="color:#00AA00">    &quot;path&quot;: &quot;/etc/motd&quot;,</span>
<span style="color:#00AA00">    &quot;size&quot;: 488,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;file&quot;,</span>
<span style="color:#00AA00">    &quot;uid&quot;: 0</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:33:30 +0200 (0:00:00.624)       0:00:28.026 ***** 

TASK [ansible-nas-general : Update apt-cache] *********************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-general/tasks/main.yml:7</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;attempts&quot;: 1,</span>
<span style="color:#00AA00">    &quot;cache_update_time&quot;: 1758406347,</span>
<span style="color:#00AA00">    &quot;cache_updated&quot;: false,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:33:32 +0200 (0:00:02.073)       0:00:30.099 ***** 
Sonntag 21 September 2025  01:33:32 +0200 (0:00:00.034)       0:00:30.134 ***** 

TASK [ansible-nas-general : Install some packages] ****************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-general/tasks/main.yml:22</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;attempts&quot;: 1,</span>
<span style="color:#00AA00">    &quot;cache_update_time&quot;: 1758406347,</span>
<span style="color:#00AA00">    &quot;cache_updated&quot;: false,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:33:33 +0200 (0:00:01.375)       0:00:31.510 ***** 

TASK [ansible-nas-general : Set hostname to RaspiNAS] *************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-general/tasks/main.yml:29</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;ansible_facts&quot;: {</span>
<span style="color:#00AA00">        &quot;ansible_domain&quot;: &quot;schneider.nbg&quot;,</span>
<span style="color:#00AA00">        &quot;ansible_fqdn&quot;: &quot;raspinas.schneider.nbg&quot;,</span>
<span style="color:#00AA00">        &quot;ansible_hostname&quot;: &quot;RaspiNAS&quot;,</span>
<span style="color:#00AA00">        &quot;ansible_nodename&quot;: &quot;RaspiNAS&quot;</span>
<span style="color:#00AA00">    },</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;name&quot;: &quot;RaspiNAS&quot;</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:33:35 +0200 (0:00:01.249)       0:00:32.759 ***** 

TASK [ansible-nas-general : Set timezone to Europe/Berlin] ********************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-general/tasks/main.yml:33</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:33:36 +0200 (0:00:00.862)       0:00:33.621 ***** 
Sonntag 21 September 2025  01:33:36 +0200 (0:00:00.043)       0:00:33.665 ***** 

TASK [ansible-nas-docker : Install python3-pip] *******************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-docker/tasks/main.yml:2</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;attempts&quot;: 1,</span>
<span style="color:#00AA00">    &quot;cache_update_time&quot;: 1758406347,</span>
<span style="color:#00AA00">    &quot;cache_updated&quot;: false,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:33:37 +0200 (0:00:01.378)       0:00:35.044 ***** 

TASK [ansible-nas-docker : Copy &quot;ext-managed&quot;] ********************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-docker/tasks/main.yml:9</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;checksum&quot;: &quot;654cca365a9351054dd5f8f8d0f27bdc330c0489&quot;,</span>
<span style="color:#00AA00">    &quot;dest&quot;: &quot;/usr/lib/python3.11/EXTERNALLY-MANAGED_bak&quot;,</span>
<span style="color:#00AA00">    &quot;gid&quot;: 0,</span>
<span style="color:#00AA00">    &quot;group&quot;: &quot;root&quot;,</span>
<span style="color:#00AA00">    &quot;mode&quot;: &quot;0644&quot;,</span>
<span style="color:#00AA00">    &quot;owner&quot;: &quot;root&quot;,</span>
<span style="color:#00AA00">    &quot;path&quot;: &quot;/usr/lib/python3.11/EXTERNALLY-MANAGED_bak&quot;,</span>
<span style="color:#00AA00">    &quot;size&quot;: 432,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;file&quot;,</span>
<span style="color:#00AA00">    &quot;uid&quot;: 0</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:33:38 +0200 (0:00:00.600)       0:00:35.644 ***** 

TASK [ansible-nas-docker : Remove &quot;ext-managed&quot;] ******************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-docker/tasks/main.yml:14</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;path&quot;: &quot;/usr/lib/python3.11/EXTERNALLY-MANAGED&quot;,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;absent&quot;</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:33:38 +0200 (0:00:00.356)       0:00:36.000 ***** 

TASK [ansible-nas-docker : Remove docker-py python module] ********************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-docker/tasks/main.yml:19</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;attempts&quot;: 1,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;cmd&quot;: [</span>
<span style="color:#00AA00">        &quot;/usr/bin/python3&quot;,</span>
<span style="color:#00AA00">        &quot;-m&quot;,</span>
<span style="color:#00AA00">        &quot;pip.__main__&quot;,</span>
<span style="color:#00AA00">        &quot;uninstall&quot;,</span>
<span style="color:#00AA00">        &quot;-y&quot;,</span>
<span style="color:#00AA00">        &quot;docker-py&quot;</span>
<span style="color:#00AA00">    ],</span>
<span style="color:#00AA00">    &quot;name&quot;: [</span>
<span style="color:#00AA00">        &quot;docker-py&quot;</span>
<span style="color:#00AA00">    ],</span>
<span style="color:#00AA00">    &quot;requirements&quot;: null,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;absent&quot;,</span>
<span style="color:#00AA00">    &quot;version&quot;: null,</span>
<span style="color:#00AA00">    &quot;virtualenv&quot;: null</span>
<span style="color:#00AA00">}</span>

<span style="color:#00AA00">STDERR:</span>

<span style="color:#00AA00">WARNING: Skipping docker-py as it is not installed.</span>
<span style="color:#00AA00">WARNING: Running pip as the &apos;root&apos; user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv</span>

Sonntag 21 September 2025  01:33:39 +0200 (0:00:01.118)       0:00:37.119 ***** 

TASK [ansible-nas-docker : Install docker python module] **********************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-docker/tasks/main.yml:26</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;attempts&quot;: 1,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;cmd&quot;: [</span>
<span style="color:#00AA00">        &quot;/usr/bin/python3&quot;,</span>
<span style="color:#00AA00">        &quot;-m&quot;,</span>
<span style="color:#00AA00">        &quot;pip.__main__&quot;,</span>
<span style="color:#00AA00">        &quot;install&quot;,</span>
<span style="color:#00AA00">        &quot;docker&quot;</span>
<span style="color:#00AA00">    ],</span>
<span style="color:#00AA00">    &quot;name&quot;: [</span>
<span style="color:#00AA00">        &quot;docker&quot;</span>
<span style="color:#00AA00">    ],</span>
<span style="color:#00AA00">    &quot;requirements&quot;: null,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;present&quot;,</span>
<span style="color:#00AA00">    &quot;version&quot;: null,</span>
<span style="color:#00AA00">    &quot;virtualenv&quot;: null</span>
<span style="color:#00AA00">}</span>

<span style="color:#00AA00">STDOUT:</span>

<span style="color:#00AA00">Looking in indexes: https://pypi.org/simple, https://www.piwheels.org/simple</span>
<span style="color:#00AA00">Requirement already satisfied: docker in /usr/local/lib/python3.11/dist-packages (7.1.0)</span>
<span style="color:#00AA00">Requirement already satisfied: requests&gt;=2.26.0 in /usr/lib/python3/dist-packages (from docker) (2.28.1)</span>
<span style="color:#00AA00">Requirement already satisfied: urllib3&gt;=1.26.0 in /usr/lib/python3/dist-packages (from docker) (1.26.12)</span>



<span style="color:#00AA00">STDERR:</span>

<span style="color:#00AA00">WARNING: Running pip as the &apos;root&apos; user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv</span>

Sonntag 21 September 2025  01:33:40 +0200 (0:00:01.226)       0:00:38.345 ***** 

TASK [ansible-nas-docker : Create Docker home directory] **********************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-docker/tasks/main.yml:33</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;gid&quot;: 1001,</span>
<span style="color:#00AA00">    &quot;group&quot;: &quot;ansible-nas&quot;,</span>
<span style="color:#00AA00">    &quot;mode&quot;: &quot;0755&quot;,</span>
<span style="color:#00AA00">    &quot;owner&quot;: &quot;1001&quot;,</span>
<span style="color:#00AA00">    &quot;path&quot;: &quot;/mnt/Volume1/docker&quot;,</span>
<span style="color:#00AA00">    &quot;size&quot;: 4096,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;directory&quot;,</span>
<span style="color:#00AA00">    &quot;uid&quot;: 1001</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:33:41 +0200 (0:00:00.400)       0:00:38.746 ***** 

TASK [ansible-nas-docker : Add user account to Docker group] ******************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-docker/tasks/main.yml:39</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;append&quot;: true,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;comment&quot;: &quot;,,,&quot;,</span>
<span style="color:#00AA00">    &quot;group&quot;: 1000,</span>
<span style="color:#00AA00">    &quot;groups&quot;: &quot;docker&quot;,</span>
<span style="color:#00AA00">    &quot;home&quot;: &quot;/home/dietmar&quot;,</span>
<span style="color:#00AA00">    &quot;move_home&quot;: false,</span>
<span style="color:#00AA00">    &quot;name&quot;: &quot;dietmar&quot;,</span>
<span style="color:#00AA00">    &quot;shell&quot;: &quot;/bin/bash&quot;,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;present&quot;,</span>
<span style="color:#00AA00">    &quot;uid&quot;: 1000</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:33:41 +0200 (0:00:00.420)       0:00:39.166 ***** 

TASK [ansible-nas-docker : Generate Docker daemon.json] ***********************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-docker/tasks/main.yml:45</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;checksum&quot;: &quot;b49ff4beca73d8e8ac8315d97b6f6fa38d02f720&quot;,</span>
<span style="color:#00AA00">    &quot;dest&quot;: &quot;/etc/docker/daemon.json&quot;,</span>
<span style="color:#00AA00">    &quot;gid&quot;: 0,</span>
<span style="color:#00AA00">    &quot;group&quot;: &quot;root&quot;,</span>
<span style="color:#00AA00">    &quot;mode&quot;: &quot;0644&quot;,</span>
<span style="color:#00AA00">    &quot;owner&quot;: &quot;root&quot;,</span>
<span style="color:#00AA00">    &quot;path&quot;: &quot;/etc/docker/daemon.json&quot;,</span>
<span style="color:#00AA00">    &quot;size&quot;: 72,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;file&quot;,</span>
<span style="color:#00AA00">    &quot;uid&quot;: 0</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:33:42 +0200 (0:00:00.646)       0:00:39.813 ***** 
Sonntag 21 September 2025  01:33:42 +0200 (0:00:00.065)       0:00:39.878 ***** 
Sonntag 21 September 2025  01:33:42 +0200 (0:00:00.060)       0:00:39.939 ***** 

TASK [logging : Disable logging roles] ****************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/logging/tasks/main.yml:19</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;ansible_facts&quot;: {</span>
<span style="color:#00AA00">        &quot;grafana_enabled&quot;: false,</span>
<span style="color:#00AA00">        &quot;loki_enabled&quot;: false,</span>
<span style="color:#00AA00">        &quot;minio_enabled&quot;: false,</span>
<span style="color:#00AA00">        &quot;promtail_enabled&quot;: false</span>
<span style="color:#00AA00">    },</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:33:42 +0200 (0:00:00.135)       0:00:40.075 ***** 
Sonntag 21 September 2025  01:33:42 +0200 (0:00:00.071)       0:00:40.146 ***** 
Sonntag 21 September 2025  01:33:42 +0200 (0:00:00.056)       0:00:40.203 ***** 

TASK [airsonic : Stop Airsonic] ***********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/airsonic/tasks/main.yml:37</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:33:43 +0200 (0:00:01.341)       0:00:41.545 ***** 
Sonntag 21 September 2025  01:33:44 +0200 (0:00:00.044)       0:00:41.590 ***** 
Sonntag 21 September 2025  01:33:44 +0200 (0:00:00.048)       0:00:41.639 ***** 
Sonntag 21 September 2025  01:33:44 +0200 (0:00:00.044)       0:00:41.683 ***** 
Sonntag 21 September 2025  01:33:44 +0200 (0:00:00.041)       0:00:41.725 ***** 

TASK [apcupsd : Stop Apcupsd] *************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/apcupsd/tasks/main.yml:44</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:33:44 +0200 (0:00:00.584)       0:00:42.309 ***** 
Sonntag 21 September 2025  01:33:44 +0200 (0:00:00.132)       0:00:42.442 ***** 
Sonntag 21 September 2025  01:33:44 +0200 (0:00:00.042)       0:00:42.485 ***** 

TASK [bazarr : Stop Bazarr] ***************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/bazarr/tasks/main.yml:46</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:33:45 +0200 (0:00:00.594)       0:00:43.079 ***** 
Sonntag 21 September 2025  01:33:45 +0200 (0:00:00.056)       0:00:43.135 ***** 
Sonntag 21 September 2025  01:33:45 +0200 (0:00:00.046)       0:00:43.181 ***** 
Sonntag 21 September 2025  01:33:45 +0200 (0:00:00.046)       0:00:43.227 ***** 
Sonntag 21 September 2025  01:33:45 +0200 (0:00:00.045)       0:00:43.273 ***** 

TASK [bitwarden : Stop Bitwarden] *********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/bitwarden/tasks/main.yml:64</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:33:46 +0200 (0:00:00.588)       0:00:43.861 ***** 

TASK [bitwarden : Stop Bitwarden Backup] **************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/bitwarden/tasks/main.yml:69</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:33:46 +0200 (0:00:00.604)       0:00:44.466 ***** 
Sonntag 21 September 2025  01:33:46 +0200 (0:00:00.066)       0:00:44.533 ***** 
Sonntag 21 September 2025  01:33:47 +0200 (0:00:00.041)       0:00:44.574 ***** 

TASK [booksonic : Stop Booksonic] *********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/booksonic/tasks/main.yml:42</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:33:47 +0200 (0:00:00.593)       0:00:45.168 ***** 
Sonntag 21 September 2025  01:33:47 +0200 (0:00:00.045)       0:00:45.213 ***** 
Sonntag 21 September 2025  01:33:47 +0200 (0:00:00.048)       0:00:45.262 ***** 

TASK [calibre : Stop Calibre] *************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/calibre/tasks/main.yml:44</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:33:48 +0200 (0:00:00.580)       0:00:45.843 ***** 
Sonntag 21 September 2025  01:33:48 +0200 (0:00:00.050)       0:00:45.893 ***** 
Sonntag 21 September 2025  01:33:48 +0200 (0:00:00.044)       0:00:45.938 ***** 

TASK [calibreweb : Stop Calibre-web] ******************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/calibreweb/tasks/main.yml:41</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:33:48 +0200 (0:00:00.584)       0:00:46.522 ***** 
Sonntag 21 September 2025  01:33:49 +0200 (0:00:00.048)       0:00:46.571 ***** 
Sonntag 21 September 2025  01:33:49 +0200 (0:00:00.046)       0:00:46.617 ***** 

TASK [cloudcmd : Stop Cloudcmd] ***********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/cloudcmd/tasks/main.yml:38</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:33:49 +0200 (0:00:00.685)       0:00:47.303 ***** 
Sonntag 21 September 2025  01:33:49 +0200 (0:00:00.046)       0:00:47.349 ***** 
Sonntag 21 September 2025  01:33:49 +0200 (0:00:00.040)       0:00:47.389 ***** 
Sonntag 21 September 2025  01:33:49 +0200 (0:00:00.047)       0:00:47.437 ***** 
Sonntag 21 September 2025  01:33:49 +0200 (0:00:00.044)       0:00:47.481 ***** 

TASK [cloudflare_ddns : Stop Cloudflare DDNS] *********************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/cloudflare_ddns/tasks/main.yml:34</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:33:50 +0200 (0:00:00.574)       0:00:48.055 ***** 
Sonntag 21 September 2025  01:33:50 +0200 (0:00:00.054)       0:00:48.109 ***** 
Sonntag 21 September 2025  01:33:50 +0200 (0:00:00.065)       0:00:48.175 ***** 

TASK [couchdb : Stop CouchDB] *************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/couchdb/tasks/main.yml:38</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:33:51 +0200 (0:00:00.610)       0:00:48.785 ***** 
Sonntag 21 September 2025  01:33:51 +0200 (0:00:00.041)       0:00:48.827 ***** 

TASK [code-server : Stop Code Server] *****************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/code-server/tasks/main.yml:32</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:33:51 +0200 (0:00:00.585)       0:00:49.412 ***** 
Sonntag 21 September 2025  01:33:51 +0200 (0:00:00.047)       0:00:49.459 ***** 
Sonntag 21 September 2025  01:33:51 +0200 (0:00:00.045)       0:00:49.505 ***** 

TASK [couchpotato : Stop Couchpotato] *****************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/couchpotato/tasks/main.yml:41</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:33:52 +0200 (0:00:00.622)       0:00:50.127 ***** 
Sonntag 21 September 2025  01:33:52 +0200 (0:00:00.060)       0:00:50.187 ***** 
Sonntag 21 September 2025  01:33:52 +0200 (0:00:00.045)       0:00:50.232 ***** 
Sonntag 21 September 2025  01:33:52 +0200 (0:00:00.072)       0:00:50.305 ***** 

TASK [dashy : Stop Dashy] *****************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/dashy/tasks/main.yml:39</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:33:53 +0200 (0:00:00.605)       0:00:50.910 ***** 
Sonntag 21 September 2025  01:33:53 +0200 (0:00:00.039)       0:00:50.949 ***** 
Sonntag 21 September 2025  01:33:53 +0200 (0:00:00.047)       0:00:50.997 ***** 
Sonntag 21 September 2025  01:33:53 +0200 (0:00:00.128)       0:00:51.125 ***** 
Sonntag 21 September 2025  01:33:53 +0200 (0:00:00.042)       0:00:51.168 ***** 

TASK [ddns_updater : Stop DDNS Updater] ***************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/ddns_updater/tasks/main.yml:54</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:33:54 +0200 (0:00:00.584)       0:00:51.752 ***** 
Sonntag 21 September 2025  01:33:54 +0200 (0:00:00.045)       0:00:51.798 ***** 
Sonntag 21 September 2025  01:33:54 +0200 (0:00:00.046)       0:00:51.845 ***** 

TASK [deluge : Stop Deluge] ***************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/deluge/tasks/main.yml:46</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:33:54 +0200 (0:00:00.600)       0:00:52.445 ***** 
Sonntag 21 September 2025  01:33:54 +0200 (0:00:00.047)       0:00:52.492 ***** 
Sonntag 21 September 2025  01:33:54 +0200 (0:00:00.046)       0:00:52.538 ***** 

TASK [dokuwiki : Stop Dokuwiki] ***********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/dokuwiki/tasks/main.yml:37</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:33:55 +0200 (0:00:00.594)       0:00:53.133 ***** 
Sonntag 21 September 2025  01:33:55 +0200 (0:00:00.040)       0:00:53.174 ***** 
Sonntag 21 September 2025  01:33:55 +0200 (0:00:00.048)       0:00:53.222 ***** 
Sonntag 21 September 2025  01:33:55 +0200 (0:00:00.052)       0:00:53.275 ***** 
Sonntag 21 September 2025  01:33:55 +0200 (0:00:00.047)       0:00:53.323 ***** 
Sonntag 21 September 2025  01:33:55 +0200 (0:00:00.046)       0:00:53.370 ***** 
Sonntag 21 September 2025  01:33:55 +0200 (0:00:00.062)       0:00:53.433 ***** 

TASK [drone-ci : Stop Drone-CI] ***********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/drone-ci/tasks/main.yml:79</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:33:56 +0200 (0:00:00.608)       0:00:54.041 ***** 

TASK [drone-ci : Stop Drone-CI Runner] ****************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/drone-ci/tasks/main.yml:84</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:33:57 +0200 (0:00:00.585)       0:00:54.627 ***** 
Sonntag 21 September 2025  01:33:57 +0200 (0:00:00.055)       0:00:54.683 ***** 
Sonntag 21 September 2025  01:33:57 +0200 (0:00:00.048)       0:00:54.731 ***** 

TASK [duplicacy : Stop Duplicacy] *********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/duplicacy/tasks/main.yml:44</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:33:57 +0200 (0:00:00.604)       0:00:55.336 ***** 
Sonntag 21 September 2025  01:33:57 +0200 (0:00:00.139)       0:00:55.475 ***** 
Sonntag 21 September 2025  01:33:57 +0200 (0:00:00.053)       0:00:55.529 ***** 

TASK [duplicati : Stop Duplicati] *********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/duplicati/tasks/main.yml:40</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:33:58 +0200 (0:00:00.591)       0:00:56.121 ***** 
Sonntag 21 September 2025  01:33:58 +0200 (0:00:00.045)       0:00:56.167 ***** 
Sonntag 21 September 2025  01:33:58 +0200 (0:00:00.048)       0:00:56.216 ***** 

TASK [emby : Stop Emby] *******************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/emby/tasks/main.yml:41</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:33:59 +0200 (0:00:00.595)       0:00:56.812 ***** 
Sonntag 21 September 2025  01:33:59 +0200 (0:00:00.049)       0:00:56.861 ***** 
Sonntag 21 September 2025  01:33:59 +0200 (0:00:00.047)       0:00:56.909 ***** 

TASK [esphome : Stop EspHome] *************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/esphome/tasks/main.yml:38</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:33:59 +0200 (0:00:00.583)       0:00:57.493 ***** 
Sonntag 21 September 2025  01:34:00 +0200 (0:00:00.070)       0:00:57.563 ***** 
Sonntag 21 September 2025  01:34:00 +0200 (0:00:00.071)       0:00:57.635 ***** 
Sonntag 21 September 2025  01:34:00 +0200 (0:00:00.043)       0:00:57.678 ***** 
Sonntag 21 September 2025  01:34:00 +0200 (0:00:00.051)       0:00:57.729 ***** 

TASK [firefly : Stop Firefly] *************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/firefly/tasks/main.yml:68</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:34:00 +0200 (0:00:00.574)       0:00:58.304 ***** 

TASK [firefly : Stop Firefly MySQL] *******************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/firefly/tasks/main.yml:73</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:34:01 +0200 (0:00:00.598)       0:00:58.903 ***** 
Sonntag 21 September 2025  01:34:01 +0200 (0:00:00.053)       0:00:58.956 ***** 
Sonntag 21 September 2025  01:34:01 +0200 (0:00:00.046)       0:00:59.003 ***** 

TASK [flaresolverr : Stop FlareSolverr] ***************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/flaresolverr/tasks/main.yml:35</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:34:02 +0200 (0:00:00.619)       0:00:59.623 ***** 
Sonntag 21 September 2025  01:34:02 +0200 (0:00:00.086)       0:00:59.709 ***** 
Sonntag 21 September 2025  01:34:02 +0200 (0:00:00.045)       0:00:59.755 ***** 

TASK [freshrss : Stop FreshRSS] ***********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/freshrss/tasks/main.yml:38</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:34:02 +0200 (0:00:00.690)       0:01:00.445 ***** 
Sonntag 21 September 2025  01:34:02 +0200 (0:00:00.067)       0:01:00.513 ***** 
Sonntag 21 September 2025  01:34:03 +0200 (0:00:00.051)       0:01:00.565 ***** 

TASK [get_iplayer : Stop get_iplayer] *****************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/get_iplayer/tasks/main.yml:28</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:34:03 +0200 (0:00:00.599)       0:01:01.164 ***** 
Sonntag 21 September 2025  01:34:03 +0200 (0:00:00.050)       0:01:01.214 ***** 
Sonntag 21 September 2025  01:34:03 +0200 (0:00:00.050)       0:01:01.264 ***** 
Sonntag 21 September 2025  01:34:03 +0200 (0:00:00.045)       0:01:01.309 ***** 

TASK [gitea : Stop Gitea] *****************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/gitea/tasks/main.yml:65</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:34:04 +0200 (0:00:00.570)       0:01:01.880 ***** 

TASK [gitea : Stop Gitea Mysql] ***********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/gitea/tasks/main.yml:70</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:34:04 +0200 (0:00:00.585)       0:01:02.465 ***** 
Sonntag 21 September 2025  01:34:04 +0200 (0:00:00.059)       0:01:02.524 ***** 
Sonntag 21 September 2025  01:34:05 +0200 (0:00:00.042)       0:01:02.567 ***** 
Sonntag 21 September 2025  01:34:05 +0200 (0:00:00.060)       0:01:02.627 ***** 
Sonntag 21 September 2025  01:34:05 +0200 (0:00:00.051)       0:01:02.678 ***** 

TASK [gitlab : Stop Gitlab] ***************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/gitlab/tasks/main.yml:64</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:34:05 +0200 (0:00:00.601)       0:01:03.280 ***** 
Sonntag 21 September 2025  01:34:05 +0200 (0:00:00.040)       0:01:03.321 ***** 

TASK [glances : Stop Glances] *************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/glances/tasks/main.yml:32</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:34:06 +0200 (0:00:00.587)       0:01:03.909 ***** 
Sonntag 21 September 2025  01:34:06 +0200 (0:00:00.047)       0:01:03.956 ***** 
Sonntag 21 September 2025  01:34:06 +0200 (0:00:00.047)       0:01:04.004 ***** 

TASK [gotify : Stop Gotify] ***************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/gotify/tasks/main.yml:38</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:34:07 +0200 (0:00:00.608)       0:01:04.613 ***** 
Sonntag 21 September 2025  01:34:07 +0200 (0:00:00.045)       0:01:04.659 ***** 
Sonntag 21 September 2025  01:34:07 +0200 (0:00:00.142)       0:01:04.801 ***** 
Sonntag 21 September 2025  01:34:07 +0200 (0:00:00.066)       0:01:04.867 ***** 
Sonntag 21 September 2025  01:34:07 +0200 (0:00:00.054)       0:01:04.922 ***** 
Sonntag 21 September 2025  01:34:07 +0200 (0:00:00.041)       0:01:04.964 ***** 
Sonntag 21 September 2025  01:34:07 +0200 (0:00:00.042)       0:01:05.006 ***** 

TASK [guacamole : Stop Guacamole] *********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/guacamole/tasks/main.yml:59</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:34:08 +0200 (0:00:00.606)       0:01:05.613 ***** 
Sonntag 21 September 2025  01:34:08 +0200 (0:00:00.051)       0:01:05.664 ***** 

TASK [healthchecks.io : Remove healthchecks.io cronjob] ***********************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/healthchecks.io/tasks/main.yml:14</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;envs&quot;: [],</span>
<span style="color:#00AA00">    &quot;jobs&quot;: []</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:34:08 +0200 (0:00:00.585)       0:01:06.250 ***** 
Sonntag 21 September 2025  01:34:08 +0200 (0:00:00.046)       0:01:06.296 ***** 
Sonntag 21 September 2025  01:34:08 +0200 (0:00:00.046)       0:01:06.343 ***** 

TASK [heimdall : Stop Heimdall] ***********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/heimdall/tasks/main.yml:36</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:34:09 +0200 (0:00:00.608)       0:01:06.952 ***** 
Sonntag 21 September 2025  01:34:09 +0200 (0:00:00.051)       0:01:07.004 ***** 
Sonntag 21 September 2025  01:34:09 +0200 (0:00:00.041)       0:01:07.045 ***** 

TASK [hello_world : Stop Hello World] *****************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/hello_world/tasks/main.yml:33</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:34:10 +0200 (0:00:00.594)       0:01:07.639 ***** 
Sonntag 21 September 2025  01:34:10 +0200 (0:00:00.046)       0:01:07.686 ***** 
Sonntag 21 September 2025  01:34:10 +0200 (0:00:00.051)       0:01:07.737 ***** 

TASK [homeassistant : Stop homeassistant] *************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/homeassistant/tasks/main.yml:34</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:34:10 +0200 (0:00:00.603)       0:01:08.341 ***** 
Sonntag 21 September 2025  01:34:10 +0200 (0:00:00.046)       0:01:08.387 ***** 
Sonntag 21 September 2025  01:34:10 +0200 (0:00:00.061)       0:01:08.449 ***** 

TASK [homebridge : Stop Homebridge] *******************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/homebridge/tasks/main.yml:39</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:34:11 +0200 (0:00:00.577)       0:01:09.026 ***** 

TASK [homepage : Create Homepage Directories] *********************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/homepage/tasks/main.yml:4</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; (item=/mnt/Volume1/docker/homepage) =&gt; {</span>
<span style="color:#00AA00">    &quot;ansible_loop_var&quot;: &quot;item&quot;,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;gid&quot;: 0,</span>
<span style="color:#00AA00">    &quot;group&quot;: &quot;root&quot;,</span>
<span style="color:#00AA00">    &quot;item&quot;: &quot;/mnt/Volume1/docker/homepage&quot;,</span>
<span style="color:#00AA00">    &quot;mode&quot;: &quot;0777&quot;,</span>
<span style="color:#00AA00">    &quot;owner&quot;: &quot;root&quot;,</span>
<span style="color:#00AA00">    &quot;path&quot;: &quot;/mnt/Volume1/docker/homepage&quot;,</span>
<span style="color:#00AA00">    &quot;size&quot;: 4096,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;directory&quot;,</span>
<span style="color:#00AA00">    &quot;uid&quot;: 0</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:34:11 +0200 (0:00:00.455)       0:01:09.481 ***** 

TASK [homepage : Template config files] ***************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/homepage/tasks/main.yml:11</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; (item=bookmarks.yaml) =&gt; {</span>
<span style="color:#00AA00">    &quot;ansible_loop_var&quot;: &quot;item&quot;,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;checksum&quot;: &quot;a2783fdfb95c4d6e0f77924c506c26b968ae6dc6&quot;,</span>
<span style="color:#00AA00">    &quot;dest&quot;: &quot;/mnt/Volume1/docker/homepage/bookmarks.yaml&quot;,</span>
<span style="color:#00AA00">    &quot;gid&quot;: 0,</span>
<span style="color:#00AA00">    &quot;group&quot;: &quot;root&quot;,</span>
<span style="color:#00AA00">    &quot;item&quot;: &quot;bookmarks.yaml&quot;,</span>
<span style="color:#00AA00">    &quot;mode&quot;: &quot;0777&quot;,</span>
<span style="color:#00AA00">    &quot;owner&quot;: &quot;root&quot;,</span>
<span style="color:#00AA00">    &quot;path&quot;: &quot;/mnt/Volume1/docker/homepage/bookmarks.yaml&quot;,</span>
<span style="color:#00AA00">    &quot;size&quot;: 527,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;file&quot;,</span>
<span style="color:#00AA00">    &quot;uid&quot;: 0</span>
<span style="color:#00AA00">}</span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; (item=docker.yaml) =&gt; {</span>
<span style="color:#00AA00">    &quot;ansible_loop_var&quot;: &quot;item&quot;,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;checksum&quot;: &quot;c9c9f5d43dab59e638c885b21bba46d28f5c0509&quot;,</span>
<span style="color:#00AA00">    &quot;dest&quot;: &quot;/mnt/Volume1/docker/homepage/docker.yaml&quot;,</span>
<span style="color:#00AA00">    &quot;gid&quot;: 0,</span>
<span style="color:#00AA00">    &quot;group&quot;: &quot;root&quot;,</span>
<span style="color:#00AA00">    &quot;item&quot;: &quot;docker.yaml&quot;,</span>
<span style="color:#00AA00">    &quot;mode&quot;: &quot;0777&quot;,</span>
<span style="color:#00AA00">    &quot;owner&quot;: &quot;root&quot;,</span>
<span style="color:#00AA00">    &quot;path&quot;: &quot;/mnt/Volume1/docker/homepage/docker.yaml&quot;,</span>
<span style="color:#00AA00">    &quot;size&quot;: 45,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;file&quot;,</span>
<span style="color:#00AA00">    &quot;uid&quot;: 0</span>
<span style="color:#00AA00">}</span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; (item=settings.yaml) =&gt; {</span>
<span style="color:#00AA00">    &quot;ansible_loop_var&quot;: &quot;item&quot;,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;checksum&quot;: &quot;12ad15433ee55e9f49b4346cb3d5765ecac6dd08&quot;,</span>
<span style="color:#00AA00">    &quot;dest&quot;: &quot;/mnt/Volume1/docker/homepage/settings.yaml&quot;,</span>
<span style="color:#00AA00">    &quot;gid&quot;: 0,</span>
<span style="color:#00AA00">    &quot;group&quot;: &quot;root&quot;,</span>
<span style="color:#00AA00">    &quot;item&quot;: &quot;settings.yaml&quot;,</span>
<span style="color:#00AA00">    &quot;mode&quot;: &quot;0777&quot;,</span>
<span style="color:#00AA00">    &quot;owner&quot;: &quot;root&quot;,</span>
<span style="color:#00AA00">    &quot;path&quot;: &quot;/mnt/Volume1/docker/homepage/settings.yaml&quot;,</span>
<span style="color:#00AA00">    &quot;size&quot;: 64,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;file&quot;,</span>
<span style="color:#00AA00">    &quot;uid&quot;: 0</span>
<span style="color:#00AA00">}</span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; (item=services.yaml) =&gt; {</span>
<span style="color:#00AA00">    &quot;ansible_loop_var&quot;: &quot;item&quot;,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;checksum&quot;: &quot;701d82d2ab4f38f259110d140d1c66bfdd9ef2ba&quot;,</span>
<span style="color:#00AA00">    &quot;dest&quot;: &quot;/mnt/Volume1/docker/homepage/services.yaml&quot;,</span>
<span style="color:#00AA00">    &quot;gid&quot;: 0,</span>
<span style="color:#00AA00">    &quot;group&quot;: &quot;root&quot;,</span>
<span style="color:#00AA00">    &quot;item&quot;: &quot;services.yaml&quot;,</span>
<span style="color:#00AA00">    &quot;mode&quot;: &quot;0777&quot;,</span>
<span style="color:#00AA00">    &quot;owner&quot;: &quot;root&quot;,</span>
<span style="color:#00AA00">    &quot;path&quot;: &quot;/mnt/Volume1/docker/homepage/services.yaml&quot;,</span>
<span style="color:#00AA00">    &quot;size&quot;: 141,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;file&quot;,</span>
<span style="color:#00AA00">    &quot;uid&quot;: 0</span>
<span style="color:#00AA00">}</span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; (item=widgets.yaml) =&gt; {</span>
<span style="color:#00AA00">    &quot;ansible_loop_var&quot;: &quot;item&quot;,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;checksum&quot;: &quot;7c716bdbcc8065135fbe8f1a314a3dae569cedb2&quot;,</span>
<span style="color:#00AA00">    &quot;dest&quot;: &quot;/mnt/Volume1/docker/homepage/widgets.yaml&quot;,</span>
<span style="color:#00AA00">    &quot;gid&quot;: 0,</span>
<span style="color:#00AA00">    &quot;group&quot;: &quot;root&quot;,</span>
<span style="color:#00AA00">    &quot;item&quot;: &quot;widgets.yaml&quot;,</span>
<span style="color:#00AA00">    &quot;mode&quot;: &quot;0777&quot;,</span>
<span style="color:#00AA00">    &quot;owner&quot;: &quot;root&quot;,</span>
<span style="color:#00AA00">    &quot;path&quot;: &quot;/mnt/Volume1/docker/homepage/widgets.yaml&quot;,</span>
<span style="color:#00AA00">    &quot;size&quot;: 288,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;file&quot;,</span>
<span style="color:#00AA00">    &quot;uid&quot;: 0</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:34:14 +0200 (0:00:03.015)       0:01:12.497 ***** 

TASK [homepage : Create Homepage Docker Container] ****************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/homepage/tasks/main.yml:23</b></span>
<span style="color:#FF55FF"><b>[WARNING]: Docker warning: Your kernel does not support memory limit capabilities or the cgroup is not mounted. Limitation discarded.</b></span>
<span style="color:#AA5500">changed: [ansible-nas] =&gt; {</span>
<span style="color:#AA5500">    &quot;changed&quot;: true,</span>
<span style="color:#AA5500">    &quot;container&quot;: {</span>
<span style="color:#AA5500">        &quot;AppArmorProfile&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">        &quot;Args&quot;: [</span>
<span style="color:#AA5500">            &quot;node&quot;,</span>
<span style="color:#AA5500">            &quot;server.js&quot;</span>
<span style="color:#AA5500">        ],</span>
<span style="color:#AA5500">        &quot;Config&quot;: {</span>
<span style="color:#AA5500">            &quot;AttachStderr&quot;: true,</span>
<span style="color:#AA5500">            &quot;AttachStdin&quot;: false,</span>
<span style="color:#AA5500">            &quot;AttachStdout&quot;: true,</span>
<span style="color:#AA5500">            &quot;Cmd&quot;: [</span>
<span style="color:#AA5500">                &quot;node&quot;,</span>
<span style="color:#AA5500">                &quot;server.js&quot;</span>
<span style="color:#AA5500">            ],</span>
<span style="color:#AA5500">            &quot;Domainname&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;Entrypoint&quot;: [</span>
<span style="color:#AA5500">                &quot;docker-entrypoint.sh&quot;</span>
<span style="color:#AA5500">            ],</span>
<span style="color:#AA5500">            &quot;Env&quot;: [</span>
<span style="color:#AA5500">                &quot;TZ=Europe/Berlin&quot;,</span>
<span style="color:#AA5500">                &quot;HOMEPAGE_ALLOWED_HOSTS=*&quot;,</span>
<span style="color:#AA5500">                &quot;PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin&quot;,</span>
<span style="color:#AA5500">                &quot;NODE_VERSION=22.18.0&quot;,</span>
<span style="color:#AA5500">                &quot;YARN_VERSION=1.22.22&quot;,</span>
<span style="color:#AA5500">                &quot;NODE_ENV=production&quot;,</span>
<span style="color:#AA5500">                &quot;HOSTNAME=0.0.0.0&quot;,</span>
<span style="color:#AA5500">                &quot;PORT=3000&quot;</span>
<span style="color:#AA5500">            ],</span>
<span style="color:#AA5500">            &quot;ExposedPorts&quot;: {</span>
<span style="color:#AA5500">                &quot;3000/tcp&quot;: {}</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            &quot;Healthcheck&quot;: {</span>
<span style="color:#AA5500">                &quot;Interval&quot;: 10000000000,</span>
<span style="color:#AA5500">                &quot;StartPeriod&quot;: 20000000000,</span>
<span style="color:#AA5500">                &quot;Test&quot;: [</span>
<span style="color:#AA5500">                    &quot;CMD-SHELL&quot;,</span>
<span style="color:#AA5500">                    &quot;wget --no-verbose --tries=1 --spider http://127.0.0.1:$PORT/api/healthcheck || exit 1&quot;</span>
<span style="color:#AA5500">                ],</span>
<span style="color:#AA5500">                &quot;Timeout&quot;: 3000000000</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            &quot;Hostname&quot;: &quot;9fcef53a88a2&quot;,</span>
<span style="color:#AA5500">            &quot;Image&quot;: &quot;ghcr.io/gethomepage/homepage:latest&quot;,</span>
<span style="color:#AA5500">            &quot;Labels&quot;: {</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.created&quot;: &quot;2025-08-21T14:02:17.125Z&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.description&quot;: &quot;A highly customizable homepage (or startpage / application dashboard) with Docker and service API integrations.&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.documentation&quot;: &quot;https://github.com/gethomepage/homepage/wiki&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.licenses&quot;: &quot;GPL-3.0&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.revision&quot;: &quot;c6ad937619ddb6b3c26946f087898a76654f0caf&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.source&quot;: &quot;https://github.com/gethomepage/homepage&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.title&quot;: &quot;homepage&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.url&quot;: &quot;https://github.com/gethomepage/homepage&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.version&quot;: &quot;v1.4.6&quot;,</span>
<span style="color:#AA5500">                &quot;traefik.enable&quot;: &quot;False&quot;,</span>
<span style="color:#AA5500">                &quot;traefik.http.routers.homepage.rule&quot;: &quot;Host(`homepage.Schneider.nbg`)&quot;,</span>
<span style="color:#AA5500">                &quot;traefik.http.routers.homepage.tls.certresolver&quot;: &quot;letsencrypt&quot;,</span>
<span style="color:#AA5500">                &quot;traefik.http.routers.homepage.tls.domains[0].main&quot;: &quot;Schneider.nbg&quot;,</span>
<span style="color:#AA5500">                &quot;traefik.http.routers.homepage.tls.domains[0].sans&quot;: &quot;*.Schneider.nbg&quot;,</span>
<span style="color:#AA5500">                &quot;traefik.http.services.homepage.loadbalancer.server.port&quot;: &quot;3000&quot;</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            &quot;OnBuild&quot;: null,</span>
<span style="color:#AA5500">            &quot;OpenStdin&quot;: false,</span>
<span style="color:#AA5500">            &quot;StdinOnce&quot;: false,</span>
<span style="color:#AA5500">            &quot;Tty&quot;: false,</span>
<span style="color:#AA5500">            &quot;User&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;Volumes&quot;: null,</span>
<span style="color:#AA5500">            &quot;WorkingDir&quot;: &quot;/app&quot;</span>
<span style="color:#AA5500">        },</span>
<span style="color:#AA5500">        &quot;Created&quot;: &quot;2025-09-20T23:18:04.546031012Z&quot;,</span>
<span style="color:#AA5500">        &quot;Driver&quot;: &quot;overlay2&quot;,</span>
<span style="color:#AA5500">        &quot;ExecIDs&quot;: null,</span>
<span style="color:#AA5500">        &quot;GraphDriver&quot;: {</span>
<span style="color:#AA5500">            &quot;Data&quot;: {</span>
<span style="color:#AA5500">                &quot;ID&quot;: &quot;9fcef53a88a2a24e9f3da2b2b9a50e83665556427acf611d08aa1cdea9f20673&quot;,</span>
<span style="color:#AA5500">                &quot;LowerDir&quot;: &quot;/var/lib/docker/overlay2/d6b995d0a3017ccfb42d1cc1c3e57d5fdb7ccfaee7531a37f05531a2aab53a13-init/diff:/var/lib/docker/overlay2/00b48dd4a08ccb48ce765670a9eb9c7248ebbc66a9a4409883bf28955fbc0604/diff:/var/lib/docker/overlay2/48f841643aa7fecff28cbb812c8e1275a88cb53641ca28bbd16f7d004b383191/diff:/var/lib/docker/overlay2/f5d43d8c70328639f5580f9bd073cb15bcfe87b3f34d821e03b900a13b5367a8/diff:/var/lib/docker/overlay2/d6afb5a1d8d71476a59213281c3bd2698f3566f1a0ad0342c710145dacd595ee/diff:/var/lib/docker/overlay2/239bc8dc5c8330f47cd0f7c1046b6c21b370966f165439761e3fcaa8245a30a4/diff:/var/lib/docker/overlay2/96999b94e79bd3461383e9c83e305941b226fd431c26c01931eb105dce2fb3e9/diff:/var/lib/docker/overlay2/f53a5694931566f7ff7428ad57ddeb1c77472b1710965b0e8f391a678d0fdfc4/diff:/var/lib/docker/overlay2/83b8da72adac92245748a000527482dc430b7d31e2220166cd7304b2ac0795b3/diff:/var/lib/docker/overlay2/496b8e709bb6fbc31076cbb210e4f06f70a34b2bd88e605d93bf44c96779554b/diff:/var/lib/docker/overlay2/502c7107094a5bb68299bb6f3d8d9b644daf0a27a5836740ac357984351c9297/diff&quot;,</span>
<span style="color:#AA5500">                &quot;MergedDir&quot;: &quot;/var/lib/docker/overlay2/d6b995d0a3017ccfb42d1cc1c3e57d5fdb7ccfaee7531a37f05531a2aab53a13/merged&quot;,</span>
<span style="color:#AA5500">                &quot;UpperDir&quot;: &quot;/var/lib/docker/overlay2/d6b995d0a3017ccfb42d1cc1c3e57d5fdb7ccfaee7531a37f05531a2aab53a13/diff&quot;,</span>
<span style="color:#AA5500">                &quot;WorkDir&quot;: &quot;/var/lib/docker/overlay2/d6b995d0a3017ccfb42d1cc1c3e57d5fdb7ccfaee7531a37f05531a2aab53a13/work&quot;</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            &quot;Name&quot;: &quot;overlay2&quot;</span>
<span style="color:#AA5500">        },</span>
<span style="color:#AA5500">        &quot;HostConfig&quot;: {</span>
<span style="color:#AA5500">            &quot;AutoRemove&quot;: false,</span>
<span style="color:#AA5500">            &quot;Binds&quot;: [</span>
<span style="color:#AA5500">                &quot;/mnt/Volume1/docker/homepage:/app/config:rw&quot;,</span>
<span style="color:#AA5500">                &quot;/var/run/docker.sock:/var/run/docker.sock:rw&quot;</span>
<span style="color:#AA5500">            ],</span>
<span style="color:#AA5500">            &quot;BlkioDeviceReadBps&quot;: null,</span>
<span style="color:#AA5500">            &quot;BlkioDeviceReadIOps&quot;: null,</span>
<span style="color:#AA5500">            &quot;BlkioDeviceWriteBps&quot;: null,</span>
<span style="color:#AA5500">            &quot;BlkioDeviceWriteIOps&quot;: null,</span>
<span style="color:#AA5500">            &quot;BlkioWeight&quot;: 0,</span>
<span style="color:#AA5500">            &quot;BlkioWeightDevice&quot;: null,</span>
<span style="color:#AA5500">            &quot;CapAdd&quot;: null,</span>
<span style="color:#AA5500">            &quot;CapDrop&quot;: null,</span>
<span style="color:#AA5500">            &quot;Cgroup&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;CgroupParent&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;CgroupnsMode&quot;: &quot;private&quot;,</span>
<span style="color:#AA5500">            &quot;ConsoleSize&quot;: [</span>
<span style="color:#AA5500">                0,</span>
<span style="color:#AA5500">                0</span>
<span style="color:#AA5500">            ],</span>
<span style="color:#AA5500">            &quot;ContainerIDFile&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;CpuCount&quot;: 0,</span>
<span style="color:#AA5500">            &quot;CpuPercent&quot;: 0,</span>
<span style="color:#AA5500">            &quot;CpuPeriod&quot;: 0,</span>
<span style="color:#AA5500">            &quot;CpuQuota&quot;: 0,</span>
<span style="color:#AA5500">            &quot;CpuRealtimePeriod&quot;: 0,</span>
<span style="color:#AA5500">            &quot;CpuRealtimeRuntime&quot;: 0,</span>
<span style="color:#AA5500">            &quot;CpuShares&quot;: 0,</span>
<span style="color:#AA5500">            &quot;CpusetCpus&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;CpusetMems&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;DeviceCgroupRules&quot;: null,</span>
<span style="color:#AA5500">            &quot;DeviceRequests&quot;: null,</span>
<span style="color:#AA5500">            &quot;Devices&quot;: null,</span>
<span style="color:#AA5500">            &quot;Dns&quot;: null,</span>
<span style="color:#AA5500">            &quot;DnsOptions&quot;: null,</span>
<span style="color:#AA5500">            &quot;DnsSearch&quot;: null,</span>
<span style="color:#AA5500">            &quot;ExtraHosts&quot;: null,</span>
<span style="color:#AA5500">            &quot;GroupAdd&quot;: null,</span>
<span style="color:#AA5500">            &quot;IOMaximumBandwidth&quot;: 0,</span>
<span style="color:#AA5500">            &quot;IOMaximumIOps&quot;: 0,</span>
<span style="color:#AA5500">            &quot;IpcMode&quot;: &quot;private&quot;,</span>
<span style="color:#AA5500">            &quot;Isolation&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;Links&quot;: null,</span>
<span style="color:#AA5500">            &quot;LogConfig&quot;: {</span>
<span style="color:#AA5500">                &quot;Config&quot;: {},</span>
<span style="color:#AA5500">                &quot;Type&quot;: &quot;json-file&quot;</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            &quot;MaskedPaths&quot;: [</span>
<span style="color:#AA5500">                &quot;/proc/asound&quot;,</span>
<span style="color:#AA5500">                &quot;/proc/acpi&quot;,</span>
<span style="color:#AA5500">                &quot;/proc/interrupts&quot;,</span>
<span style="color:#AA5500">                &quot;/proc/kcore&quot;,</span>
<span style="color:#AA5500">                &quot;/proc/keys&quot;,</span>
<span style="color:#AA5500">                &quot;/proc/latency_stats&quot;,</span>
<span style="color:#AA5500">                &quot;/proc/timer_list&quot;,</span>
<span style="color:#AA5500">                &quot;/proc/timer_stats&quot;,</span>
<span style="color:#AA5500">                &quot;/proc/sched_debug&quot;,</span>
<span style="color:#AA5500">                &quot;/proc/scsi&quot;,</span>
<span style="color:#AA5500">                &quot;/sys/firmware&quot;,</span>
<span style="color:#AA5500">                &quot;/sys/devices/virtual/powercap&quot;</span>
<span style="color:#AA5500">            ],</span>
<span style="color:#AA5500">            &quot;Memory&quot;: 0,</span>
<span style="color:#AA5500">            &quot;MemoryReservation&quot;: 0,</span>
<span style="color:#AA5500">            &quot;MemorySwap&quot;: -1,</span>
<span style="color:#AA5500">            &quot;MemorySwappiness&quot;: null,</span>
<span style="color:#AA5500">            &quot;NanoCpus&quot;: 0,</span>
<span style="color:#AA5500">            &quot;NetworkMode&quot;: &quot;bridge&quot;,</span>
<span style="color:#AA5500">            &quot;OomKillDisable&quot;: null,</span>
<span style="color:#AA5500">            &quot;OomScoreAdj&quot;: 0,</span>
<span style="color:#AA5500">            &quot;PidMode&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;PidsLimit&quot;: null,</span>
<span style="color:#AA5500">            &quot;PortBindings&quot;: {</span>
<span style="color:#AA5500">                &quot;3000/tcp&quot;: [</span>
<span style="color:#AA5500">                    {</span>
<span style="color:#AA5500">                        &quot;HostIp&quot;: &quot;0.0.0.0&quot;,</span>
<span style="color:#AA5500">                        &quot;HostPort&quot;: &quot;11111&quot;</span>
<span style="color:#AA5500">                    }</span>
<span style="color:#AA5500">                ]</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            &quot;Privileged&quot;: false,</span>
<span style="color:#AA5500">            &quot;PublishAllPorts&quot;: false,</span>
<span style="color:#AA5500">            &quot;ReadonlyPaths&quot;: [</span>
<span style="color:#AA5500">                &quot;/proc/bus&quot;,</span>
<span style="color:#AA5500">                &quot;/proc/fs&quot;,</span>
<span style="color:#AA5500">                &quot;/proc/irq&quot;,</span>
<span style="color:#AA5500">                &quot;/proc/sys&quot;,</span>
<span style="color:#AA5500">                &quot;/proc/sysrq-trigger&quot;</span>
<span style="color:#AA5500">            ],</span>
<span style="color:#AA5500">            &quot;ReadonlyRootfs&quot;: false,</span>
<span style="color:#AA5500">            &quot;RestartPolicy&quot;: {</span>
<span style="color:#AA5500">                &quot;MaximumRetryCount&quot;: 0,</span>
<span style="color:#AA5500">                &quot;Name&quot;: &quot;unless-stopped&quot;</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            &quot;Runtime&quot;: &quot;runc&quot;,</span>
<span style="color:#AA5500">            &quot;SecurityOpt&quot;: null,</span>
<span style="color:#AA5500">            &quot;ShmSize&quot;: 67108864,</span>
<span style="color:#AA5500">            &quot;UTSMode&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;Ulimits&quot;: null,</span>
<span style="color:#AA5500">            &quot;UsernsMode&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;VolumeDriver&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;VolumesFrom&quot;: null</span>
<span style="color:#AA5500">        },</span>
<span style="color:#AA5500">        &quot;HostnamePath&quot;: &quot;/var/lib/docker/containers/9fcef53a88a2a24e9f3da2b2b9a50e83665556427acf611d08aa1cdea9f20673/hostname&quot;,</span>
<span style="color:#AA5500">        &quot;HostsPath&quot;: &quot;/var/lib/docker/containers/9fcef53a88a2a24e9f3da2b2b9a50e83665556427acf611d08aa1cdea9f20673/hosts&quot;,</span>
<span style="color:#AA5500">        &quot;Id&quot;: &quot;9fcef53a88a2a24e9f3da2b2b9a50e83665556427acf611d08aa1cdea9f20673&quot;,</span>
<span style="color:#AA5500">        &quot;Image&quot;: &quot;sha256:d26b13682ea197d5ed456a59d72d8782d4ccc40b172ddff301a6d1e45c79a3bd&quot;,</span>
<span style="color:#AA5500">        &quot;LogPath&quot;: &quot;/var/lib/docker/containers/9fcef53a88a2a24e9f3da2b2b9a50e83665556427acf611d08aa1cdea9f20673/9fcef53a88a2a24e9f3da2b2b9a50e83665556427acf611d08aa1cdea9f20673-json.log&quot;,</span>
<span style="color:#AA5500">        &quot;MountLabel&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">        &quot;Mounts&quot;: [</span>
<span style="color:#AA5500">            {</span>
<span style="color:#AA5500">                &quot;Destination&quot;: &quot;/app/config&quot;,</span>
<span style="color:#AA5500">                &quot;Mode&quot;: &quot;rw&quot;,</span>
<span style="color:#AA5500">                &quot;Propagation&quot;: &quot;rprivate&quot;,</span>
<span style="color:#AA5500">                &quot;RW&quot;: true,</span>
<span style="color:#AA5500">                &quot;Source&quot;: &quot;/mnt/Volume1/docker/homepage&quot;,</span>
<span style="color:#AA5500">                &quot;Type&quot;: &quot;bind&quot;</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            {</span>
<span style="color:#AA5500">                &quot;Destination&quot;: &quot;/var/run/docker.sock&quot;,</span>
<span style="color:#AA5500">                &quot;Mode&quot;: &quot;rw&quot;,</span>
<span style="color:#AA5500">                &quot;Propagation&quot;: &quot;rprivate&quot;,</span>
<span style="color:#AA5500">                &quot;RW&quot;: true,</span>
<span style="color:#AA5500">                &quot;Source&quot;: &quot;/var/run/docker.sock&quot;,</span>
<span style="color:#AA5500">                &quot;Type&quot;: &quot;bind&quot;</span>
<span style="color:#AA5500">            }</span>
<span style="color:#AA5500">        ],</span>
<span style="color:#AA5500">        &quot;Name&quot;: &quot;/homepage&quot;,</span>
<span style="color:#AA5500">        &quot;NetworkSettings&quot;: {</span>
<span style="color:#AA5500">            &quot;Bridge&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;EndpointID&quot;: &quot;28fb8a3b0349edbe781b7a88756d59ace401507ddc169aebf182fdd9196afff9&quot;,</span>
<span style="color:#AA5500">            &quot;Gateway&quot;: &quot;172.17.0.1&quot;,</span>
<span style="color:#AA5500">            &quot;GlobalIPv6Address&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;GlobalIPv6PrefixLen&quot;: 0,</span>
<span style="color:#AA5500">            &quot;HairpinMode&quot;: false,</span>
<span style="color:#AA5500">            &quot;IPAddress&quot;: &quot;172.17.0.2&quot;,</span>
<span style="color:#AA5500">            &quot;IPPrefixLen&quot;: 16,</span>
<span style="color:#AA5500">            &quot;IPv6Gateway&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;LinkLocalIPv6Address&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;LinkLocalIPv6PrefixLen&quot;: 0,</span>
<span style="color:#AA5500">            &quot;MacAddress&quot;: &quot;42:49:2e:4f:74:83&quot;,</span>
<span style="color:#AA5500">            &quot;Networks&quot;: {</span>
<span style="color:#AA5500">                &quot;bridge&quot;: {</span>
<span style="color:#AA5500">                    &quot;Aliases&quot;: null,</span>
<span style="color:#AA5500">                    &quot;DNSNames&quot;: null,</span>
<span style="color:#AA5500">                    &quot;DriverOpts&quot;: null,</span>
<span style="color:#AA5500">                    &quot;EndpointID&quot;: &quot;28fb8a3b0349edbe781b7a88756d59ace401507ddc169aebf182fdd9196afff9&quot;,</span>
<span style="color:#AA5500">                    &quot;Gateway&quot;: &quot;172.17.0.1&quot;,</span>
<span style="color:#AA5500">                    &quot;GlobalIPv6Address&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">                    &quot;GlobalIPv6PrefixLen&quot;: 0,</span>
<span style="color:#AA5500">                    &quot;GwPriority&quot;: 0,</span>
<span style="color:#AA5500">                    &quot;IPAMConfig&quot;: null,</span>
<span style="color:#AA5500">                    &quot;IPAddress&quot;: &quot;172.17.0.2&quot;,</span>
<span style="color:#AA5500">                    &quot;IPPrefixLen&quot;: 16,</span>
<span style="color:#AA5500">                    &quot;IPv6Gateway&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">                    &quot;Links&quot;: null,</span>
<span style="color:#AA5500">                    &quot;MacAddress&quot;: &quot;42:49:2e:4f:74:83&quot;,</span>
<span style="color:#AA5500">                    &quot;NetworkID&quot;: &quot;530cbb1798f0794e4f2b90b938da8fc514f2b64ec3877ec5766a5eaf257ffb34&quot;</span>
<span style="color:#AA5500">                }</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            &quot;Ports&quot;: {</span>
<span style="color:#AA5500">                &quot;3000/tcp&quot;: [</span>
<span style="color:#AA5500">                    {</span>
<span style="color:#AA5500">                        &quot;HostIp&quot;: &quot;0.0.0.0&quot;,</span>
<span style="color:#AA5500">                        &quot;HostPort&quot;: &quot;11111&quot;</span>
<span style="color:#AA5500">                    }</span>
<span style="color:#AA5500">                ]</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            &quot;SandboxID&quot;: &quot;9762f613590d0ae1156fdf2ebdf5581a203c51024b8eac6babe8a0e288e90768&quot;,</span>
<span style="color:#AA5500">            &quot;SandboxKey&quot;: &quot;/var/run/docker/netns/9762f613590d&quot;,</span>
<span style="color:#AA5500">            &quot;SecondaryIPAddresses&quot;: null,</span>
<span style="color:#AA5500">            &quot;SecondaryIPv6Addresses&quot;: null</span>
<span style="color:#AA5500">        },</span>
<span style="color:#AA5500">        &quot;Path&quot;: &quot;docker-entrypoint.sh&quot;,</span>
<span style="color:#AA5500">        &quot;Platform&quot;: &quot;linux&quot;,</span>
<span style="color:#AA5500">        &quot;ProcessLabel&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">        &quot;ResolvConfPath&quot;: &quot;/var/lib/docker/containers/9fcef53a88a2a24e9f3da2b2b9a50e83665556427acf611d08aa1cdea9f20673/resolv.conf&quot;,</span>
<span style="color:#AA5500">        &quot;RestartCount&quot;: 0,</span>
<span style="color:#AA5500">        &quot;State&quot;: {</span>
<span style="color:#AA5500">            &quot;Dead&quot;: false,</span>
<span style="color:#AA5500">            &quot;Error&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;ExitCode&quot;: 0,</span>
<span style="color:#AA5500">            &quot;FinishedAt&quot;: &quot;0001-01-01T00:00:00Z&quot;,</span>
<span style="color:#AA5500">            &quot;Health&quot;: {</span>
<span style="color:#AA5500">                &quot;FailingStreak&quot;: 0,</span>
<span style="color:#AA5500">                &quot;Log&quot;: [</span>
<span style="color:#AA5500">                    {</span>
<span style="color:#AA5500">                        &quot;End&quot;: &quot;2025-09-21T01:33:26.544256554+02:00&quot;,</span>
<span style="color:#AA5500">                        &quot;ExitCode&quot;: 0,</span>
<span style="color:#AA5500">                        &quot;Output&quot;: &quot;Connecting to 127.0.0.1:3000 (127.0.0.1:3000)\nremote file exists\n&quot;,</span>
<span style="color:#AA5500">                        &quot;Start&quot;: &quot;2025-09-21T01:33:26.49415177+02:00&quot;</span>
<span style="color:#AA5500">                    },</span>
<span style="color:#AA5500">                    {</span>
<span style="color:#AA5500">                        &quot;End&quot;: &quot;2025-09-21T01:33:36.612706288+02:00&quot;,</span>
<span style="color:#AA5500">                        &quot;ExitCode&quot;: 0,</span>
<span style="color:#AA5500">                        &quot;Output&quot;: &quot;Connecting to 127.0.0.1:3000 (127.0.0.1:3000)\nremote file exists\n&quot;,</span>
<span style="color:#AA5500">                        &quot;Start&quot;: &quot;2025-09-21T01:33:36.547033598+02:00&quot;</span>
<span style="color:#AA5500">                    },</span>
<span style="color:#AA5500">                    {</span>
<span style="color:#AA5500">                        &quot;End&quot;: &quot;2025-09-21T01:33:46.670755235+02:00&quot;,</span>
<span style="color:#AA5500">                        &quot;ExitCode&quot;: 0,</span>
<span style="color:#AA5500">                        &quot;Output&quot;: &quot;Connecting to 127.0.0.1:3000 (127.0.0.1:3000)\nremote file exists\n&quot;,</span>
<span style="color:#AA5500">                        &quot;Start&quot;: &quot;2025-09-21T01:33:46.613271766+02:00&quot;</span>
<span style="color:#AA5500">                    },</span>
<span style="color:#AA5500">                    {</span>
<span style="color:#AA5500">                        &quot;End&quot;: &quot;2025-09-21T01:33:56.734665263+02:00&quot;,</span>
<span style="color:#AA5500">                        &quot;ExitCode&quot;: 0,</span>
<span style="color:#AA5500">                        &quot;Output&quot;: &quot;Connecting to 127.0.0.1:3000 (127.0.0.1:3000)\nremote file exists\n&quot;,</span>
<span style="color:#AA5500">                        &quot;Start&quot;: &quot;2025-09-21T01:33:56.671790522+02:00&quot;</span>
<span style="color:#AA5500">                    },</span>
<span style="color:#AA5500">                    {</span>
<span style="color:#AA5500">                        &quot;End&quot;: &quot;2025-09-21T01:34:06.801857142+02:00&quot;,</span>
<span style="color:#AA5500">                        &quot;ExitCode&quot;: 0,</span>
<span style="color:#AA5500">                        &quot;Output&quot;: &quot;Connecting to 127.0.0.1:3000 (127.0.0.1:3000)\nremote file exists\n&quot;,</span>
<span style="color:#AA5500">                        &quot;Start&quot;: &quot;2025-09-21T01:34:06.736083987+02:00&quot;</span>
<span style="color:#AA5500">                    }</span>
<span style="color:#AA5500">                ],</span>
<span style="color:#AA5500">                &quot;Status&quot;: &quot;healthy&quot;</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            &quot;OOMKilled&quot;: false,</span>
<span style="color:#AA5500">            &quot;Paused&quot;: false,</span>
<span style="color:#AA5500">            &quot;Pid&quot;: 1440693,</span>
<span style="color:#AA5500">            &quot;Restarting&quot;: false,</span>
<span style="color:#AA5500">            &quot;Running&quot;: true,</span>
<span style="color:#AA5500">            &quot;StartedAt&quot;: &quot;2025-09-20T23:18:05.325619608Z&quot;,</span>
<span style="color:#AA5500">            &quot;Status&quot;: &quot;running&quot;</span>
<span style="color:#AA5500">        }</span>
<span style="color:#AA5500">    }</span>
<span style="color:#AA5500">}</span>
Sonntag 21 September 2025  01:34:16 +0200 (0:00:01.273)       0:01:13.770 ***** 
Sonntag 21 September 2025  01:34:16 +0200 (0:00:00.058)       0:01:13.828 ***** 
Sonntag 21 September 2025  01:34:16 +0200 (0:00:00.052)       0:01:13.881 ***** 
Sonntag 21 September 2025  01:34:16 +0200 (0:00:00.047)       0:01:13.929 ***** 

TASK [ispyagentdvr : Stop iSpyAgentDVR] ***************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/ispyagentdvr/tasks/main.yml:50</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:34:16 +0200 (0:00:00.584)       0:01:14.513 ***** 
Sonntag 21 September 2025  01:34:17 +0200 (0:00:00.048)       0:01:14.561 ***** 
Sonntag 21 September 2025  01:34:17 +0200 (0:00:00.045)       0:01:14.606 ***** 

TASK [jackett : Stop Jackett] *************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/jackett/tasks/main.yml:41</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:34:17 +0200 (0:00:00.602)       0:01:15.209 ***** 
Sonntag 21 September 2025  01:34:17 +0200 (0:00:00.047)       0:01:15.257 ***** 
Sonntag 21 September 2025  01:34:17 +0200 (0:00:00.046)       0:01:15.303 ***** 

TASK [jellyfin : Stop jellyfin] ***********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/jellyfin/tasks/main.yml:52</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:34:18 +0200 (0:00:00.577)       0:01:15.881 ***** 
Sonntag 21 September 2025  01:34:18 +0200 (0:00:00.054)       0:01:15.936 ***** 
Sonntag 21 September 2025  01:34:18 +0200 (0:00:00.044)       0:01:15.981 ***** 
Sonntag 21 September 2025  01:34:18 +0200 (0:00:00.041)       0:01:16.022 ***** 
Sonntag 21 September 2025  01:34:18 +0200 (0:00:00.048)       0:01:16.070 ***** 

TASK [joomla : Stop Joomla] ***************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/joomla/tasks/main.yml:62</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:34:19 +0200 (0:00:00.575)       0:01:16.646 ***** 

TASK [joomla : Stop Joomla DB] ************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/joomla/tasks/main.yml:66</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:34:19 +0200 (0:00:00.612)       0:01:17.258 ***** 
Sonntag 21 September 2025  01:34:19 +0200 (0:00:00.053)       0:01:17.311 ***** 
Sonntag 21 September 2025  01:34:19 +0200 (0:00:00.133)       0:01:17.445 ***** 

TASK [komga : Stop Komga] *****************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/komga/tasks/main.yml:42</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:34:20 +0200 (0:00:00.586)       0:01:18.031 ***** 
Sonntag 21 September 2025  01:34:20 +0200 (0:00:00.046)       0:01:18.078 ***** 
Sonntag 21 September 2025  01:34:20 +0200 (0:00:00.049)       0:01:18.128 ***** 

TASK [krusader : Stop Krusader] ***********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/krusader/tasks/main.yml:43</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:34:21 +0200 (0:00:00.602)       0:01:18.731 ***** 
Sonntag 21 September 2025  01:34:21 +0200 (0:00:00.042)       0:01:18.773 ***** 
Sonntag 21 September 2025  01:34:21 +0200 (0:00:00.048)       0:01:18.822 ***** 

TASK [lidarr : Stop Lidarr] ***************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/lidarr/tasks/main.yml:37</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:34:21 +0200 (0:00:00.582)       0:01:19.405 ***** 
Sonntag 21 September 2025  01:34:21 +0200 (0:00:00.042)       0:01:19.447 ***** 
Sonntag 21 September 2025  01:34:21 +0200 (0:00:00.053)       0:01:19.501 ***** 
Sonntag 21 September 2025  01:34:21 +0200 (0:00:00.047)       0:01:19.548 ***** 
Sonntag 21 September 2025  01:34:22 +0200 (0:00:00.048)       0:01:19.596 ***** 
Sonntag 21 September 2025  01:34:22 +0200 (0:00:00.054)       0:01:19.651 ***** 
Sonntag 21 September 2025  01:34:22 +0200 (0:00:00.049)       0:01:19.701 ***** 
Sonntag 21 September 2025  01:34:22 +0200 (0:00:00.047)       0:01:19.748 ***** 
Sonntag 21 September 2025  01:34:22 +0200 (0:00:00.046)       0:01:19.795 ***** 

TASK [loki : Stop loki] *******************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/loki/tasks/main.yml:74</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:34:22 +0200 (0:00:00.620)       0:01:20.415 ***** 
Sonntag 21 September 2025  01:34:22 +0200 (0:00:00.048)       0:01:20.463 ***** 
Sonntag 21 September 2025  01:34:22 +0200 (0:00:00.050)       0:01:20.514 ***** 

TASK [mealie : Stop Mealie] ***************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/mealie/tasks/main.yml:44</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:34:23 +0200 (0:00:00.603)       0:01:21.118 ***** 
Sonntag 21 September 2025  01:34:23 +0200 (0:00:00.047)       0:01:21.166 ***** 
Sonntag 21 September 2025  01:34:23 +0200 (0:00:00.255)       0:01:21.421 ***** 

TASK [minecraft-bedrock-server : Stop Minecraft Bedrock Server] ***************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/minecraft-bedrock-server/tasks/main.yml:34</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:34:24 +0200 (0:00:00.586)       0:01:22.007 ***** 
Sonntag 21 September 2025  01:34:24 +0200 (0:00:00.047)       0:01:22.055 ***** 
Sonntag 21 September 2025  01:34:24 +0200 (0:00:00.046)       0:01:22.102 ***** 

TASK [minecraft-server : Stop Minecraft Server] *******************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/minecraft-server/tasks/main.yml:27</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:34:25 +0200 (0:00:00.597)       0:01:22.699 ***** 
Sonntag 21 September 2025  01:34:25 +0200 (0:00:00.058)       0:01:22.757 ***** 

TASK [minidlna : Stop MiniDLNA] ***********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/minidlna/tasks/main.yml:24</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:34:25 +0200 (0:00:00.611)       0:01:23.369 ***** 
Sonntag 21 September 2025  01:34:25 +0200 (0:00:00.082)       0:01:23.451 ***** 
Sonntag 21 September 2025  01:34:25 +0200 (0:00:00.049)       0:01:23.500 ***** 
Sonntag 21 September 2025  01:34:25 +0200 (0:00:00.046)       0:01:23.547 ***** 
Sonntag 21 September 2025  01:34:26 +0200 (0:00:00.050)       0:01:23.598 ***** 

TASK [miniflux : Stop Miniflux] ***********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/miniflux/tasks/main.yml:60</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:34:26 +0200 (0:00:00.576)       0:01:24.175 ***** 
Sonntag 21 September 2025  01:34:26 +0200 (0:00:00.046)       0:01:24.221 ***** 
Sonntag 21 September 2025  01:34:26 +0200 (0:00:00.048)       0:01:24.270 ***** 

TASK [minio : Stop minio] *****************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/minio/tasks/main.yml:40</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:34:27 +0200 (0:00:00.591)       0:01:24.862 ***** 
Sonntag 21 September 2025  01:34:27 +0200 (0:00:00.064)       0:01:24.926 ***** 
Sonntag 21 September 2025  01:34:27 +0200 (0:00:00.040)       0:01:24.966 ***** 
Sonntag 21 September 2025  01:34:27 +0200 (0:00:00.050)       0:01:25.017 ***** 

TASK [mosquitto : Stop Mosquitto] *********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/mosquitto/tasks/main.yml:38</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:34:28 +0200 (0:00:00.606)       0:01:25.623 ***** 
Sonntag 21 September 2025  01:34:28 +0200 (0:00:00.146)       0:01:25.770 ***** 
Sonntag 21 September 2025  01:34:28 +0200 (0:00:00.043)       0:01:25.814 ***** 

TASK [mumble : Stop Mumble] ***************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/mumble/tasks/main.yml:39</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:34:28 +0200 (0:00:00.576)       0:01:26.390 ***** 
Sonntag 21 September 2025  01:34:28 +0200 (0:00:00.049)       0:01:26.440 ***** 
Sonntag 21 September 2025  01:34:28 +0200 (0:00:00.055)       0:01:26.495 ***** 

TASK [mylar : Stop Mylar] *****************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/mylar/tasks/main.yml:41</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:34:29 +0200 (0:00:00.596)       0:01:27.092 ***** 
Sonntag 21 September 2025  01:34:29 +0200 (0:00:00.050)       0:01:27.142 ***** 
Sonntag 21 September 2025  01:34:29 +0200 (0:00:00.049)       0:01:27.192 ***** 

TASK [mymediaforalexa : Stop Mymediaforalexa] *********************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/mymediaforalexa/tasks/main.yml:27</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:34:30 +0200 (0:00:00.582)       0:01:27.774 ***** 
Sonntag 21 September 2025  01:34:30 +0200 (0:00:00.047)       0:01:27.821 ***** 
Sonntag 21 September 2025  01:34:30 +0200 (0:00:00.048)       0:01:27.870 ***** 

TASK [n8n : Stop n8n] *********************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/n8n/tasks/main.yml:40</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:34:30 +0200 (0:00:00.583)       0:01:28.454 ***** 
Sonntag 21 September 2025  01:34:30 +0200 (0:00:00.077)       0:01:28.531 ***** 
Sonntag 21 September 2025  01:34:31 +0200 (0:00:00.086)       0:01:28.617 ***** 

TASK [navidrome : Stop Navidrome] *********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/navidrome/tasks/main.yml:42</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:34:31 +0200 (0:00:00.593)       0:01:29.211 ***** 
Sonntag 21 September 2025  01:34:31 +0200 (0:00:00.054)       0:01:29.265 ***** 
Sonntag 21 September 2025  01:34:31 +0200 (0:00:00.045)       0:01:29.311 ***** 

TASK [netbootxyz : Stop Netbootxyz] *******************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/netbootxyz/tasks/main.yml:41</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:34:32 +0200 (0:00:00.577)       0:01:29.888 ***** 
Sonntag 21 September 2025  01:34:32 +0200 (0:00:00.046)       0:01:29.935 ***** 
Sonntag 21 September 2025  01:34:32 +0200 (0:00:00.134)       0:01:30.070 ***** 

TASK [netdata : Stop Netdata] *************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/netdata/tasks/main.yml:41</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:34:33 +0200 (0:00:00.609)       0:01:30.679 ***** 
Sonntag 21 September 2025  01:34:33 +0200 (0:00:00.062)       0:01:30.742 ***** 
Sonntag 21 September 2025  01:34:33 +0200 (0:00:00.042)       0:01:30.784 ***** 
Sonntag 21 September 2025  01:34:33 +0200 (0:00:00.057)       0:01:30.841 ***** 
Sonntag 21 September 2025  01:34:33 +0200 (0:00:00.044)       0:01:30.886 ***** 

TASK [nextcloud : Stop Nextcloud] *********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/nextcloud/tasks/main.yml:72</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:34:33 +0200 (0:00:00.577)       0:01:31.463 ***** 

TASK [nextcloud : Stop Nextcloud DB] ******************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/nextcloud/tasks/main.yml:76</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:34:34 +0200 (0:00:00.582)       0:01:32.045 ***** 
Sonntag 21 September 2025  01:34:34 +0200 (0:00:00.041)       0:01:32.087 ***** 
Sonntag 21 September 2025  01:34:34 +0200 (0:00:00.047)       0:01:32.134 ***** 
Sonntag 21 September 2025  01:34:34 +0200 (0:00:00.047)       0:01:32.181 ***** 
Sonntag 21 September 2025  01:34:34 +0200 (0:00:00.040)       0:01:32.222 ***** 
Sonntag 21 September 2025  01:34:34 +0200 (0:00:00.048)       0:01:32.270 ***** 

TASK [nomad : Check if Nomad is installed] ************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/nomad/tasks/main.yml:37</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;stat&quot;: {</span>
<span style="color:#00AA00">        &quot;exists&quot;: false</span>
<span style="color:#00AA00">    }</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:34:35 +0200 (0:00:00.342)       0:01:32.613 ***** 
Sonntag 21 September 2025  01:34:35 +0200 (0:00:00.063)       0:01:32.676 ***** 
Sonntag 21 September 2025  01:34:35 +0200 (0:00:00.087)       0:01:32.764 ***** 
Sonntag 21 September 2025  01:34:35 +0200 (0:00:00.049)       0:01:32.813 ***** 
Sonntag 21 September 2025  01:34:35 +0200 (0:00:00.050)       0:01:32.864 ***** 

TASK [nzbget : Stop NZBget] ***************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/nzbget/tasks/main.yml:38</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:34:35 +0200 (0:00:00.577)       0:01:33.442 ***** 
Sonntag 21 September 2025  01:34:35 +0200 (0:00:00.048)       0:01:33.490 ***** 
Sonntag 21 September 2025  01:34:35 +0200 (0:00:00.050)       0:01:33.541 ***** 

TASK [octoprint : Stop Octoprint] *********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/octoprint/tasks/main.yml:40</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:34:36 +0200 (0:00:00.727)       0:01:34.268 ***** 
Sonntag 21 September 2025  01:34:36 +0200 (0:00:00.048)       0:01:34.316 ***** 
Sonntag 21 September 2025  01:34:36 +0200 (0:00:00.043)       0:01:34.360 ***** 

TASK [ombi : Stop Ombi] *******************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/ombi/tasks/main.yml:35</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:34:37 +0200 (0:00:00.589)       0:01:34.950 ***** 
Sonntag 21 September 2025  01:34:37 +0200 (0:00:00.050)       0:01:35.001 ***** 
Sonntag 21 September 2025  01:34:37 +0200 (0:00:00.041)       0:01:35.043 ***** 
Sonntag 21 September 2025  01:34:37 +0200 (0:00:00.068)       0:01:35.111 ***** 
Sonntag 21 September 2025  01:34:37 +0200 (0:00:00.046)       0:01:35.157 ***** 

TASK [openhab : Stop openHAB] *************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/openhab/tasks/main.yml:60</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:34:38 +0200 (0:00:00.624)       0:01:35.781 ***** 
Sonntag 21 September 2025  01:34:38 +0200 (0:00:00.048)       0:01:35.830 ***** 
Sonntag 21 September 2025  01:34:38 +0200 (0:00:00.046)       0:01:35.877 ***** 

TASK [organizr : Stop Organizr] ***********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/organizr/tasks/main.yml:38</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:34:38 +0200 (0:00:00.580)       0:01:36.457 ***** 
Sonntag 21 September 2025  01:34:38 +0200 (0:00:00.053)       0:01:36.510 ***** 
Sonntag 21 September 2025  01:34:38 +0200 (0:00:00.047)       0:01:36.557 ***** 

TASK [overseerr : Stop Overseerr] *********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/overseerr/tasks/main.yml:43</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:34:39 +0200 (0:00:00.612)       0:01:37.170 ***** 
Sonntag 21 September 2025  01:34:39 +0200 (0:00:00.083)       0:01:37.254 ***** 
Sonntag 21 September 2025  01:34:39 +0200 (0:00:00.042)       0:01:37.297 ***** 
Sonntag 21 September 2025  01:34:39 +0200 (0:00:00.047)       0:01:37.344 ***** 
Sonntag 21 September 2025  01:34:39 +0200 (0:00:00.046)       0:01:37.391 ***** 
Sonntag 21 September 2025  01:34:39 +0200 (0:00:00.041)       0:01:37.432 ***** 

TASK [paperless_ng : Stop paperless_ng] ***************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/paperless_ng/tasks/main.yml:83</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:34:40 +0200 (0:00:00.573)       0:01:38.005 ***** 

TASK [paperless_ng : Stop paperless_ng redis] *********************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/paperless_ng/tasks/main.yml:87</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:34:41 +0200 (0:00:00.559)       0:01:38.565 ***** 

TASK [paperless_ng : Stop paperless_ng db] ************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/paperless_ng/tasks/main.yml:91</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:34:41 +0200 (0:00:00.700)       0:01:39.265 ***** 
Sonntag 21 September 2025  01:34:41 +0200 (0:00:00.062)       0:01:39.328 ***** 
Sonntag 21 September 2025  01:34:41 +0200 (0:00:00.047)       0:01:39.376 ***** 
Sonntag 21 September 2025  01:34:41 +0200 (0:00:00.042)       0:01:39.418 ***** 
Sonntag 21 September 2025  01:34:41 +0200 (0:00:00.046)       0:01:39.465 ***** 

TASK [piwigo : Stop Piwigo] ***************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/piwigo/tasks/main.yml:71</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:34:42 +0200 (0:00:00.589)       0:01:40.054 ***** 

TASK [piwigo : Stop Piwigo Db] ************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/piwigo/tasks/main.yml:75</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:34:43 +0200 (0:00:00.637)       0:01:40.691 ***** 
Sonntag 21 September 2025  01:34:43 +0200 (0:00:00.064)       0:01:40.756 ***** 
Sonntag 21 September 2025  01:34:43 +0200 (0:00:00.053)       0:01:40.809 ***** 

TASK [plex : Stop Plex] *******************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/plex/tasks/main.yml:51</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:34:43 +0200 (0:00:00.600)       0:01:41.410 ***** 
Sonntag 21 September 2025  01:34:43 +0200 (0:00:00.040)       0:01:41.450 ***** 
Sonntag 21 September 2025  01:34:43 +0200 (0:00:00.054)       0:01:41.505 ***** 
Sonntag 21 September 2025  01:34:43 +0200 (0:00:00.046)       0:01:41.551 ***** 

TASK [portainer : Stop Portainer] *********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/portainer/tasks/main.yml:49</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:34:44 +0200 (0:00:00.573)       0:01:42.125 ***** 
Sonntag 21 September 2025  01:34:44 +0200 (0:00:00.046)       0:01:42.171 ***** 
Sonntag 21 September 2025  01:34:44 +0200 (0:00:00.055)       0:01:42.227 ***** 

TASK [prowlarr : Stop Prowlarr] ***********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/prowlarr/tasks/main.yml:43</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:34:45 +0200 (0:00:00.592)       0:01:42.820 ***** 
Sonntag 21 September 2025  01:34:45 +0200 (0:00:00.040)       0:01:42.860 ***** 
Sonntag 21 September 2025  01:34:45 +0200 (0:00:00.053)       0:01:42.914 ***** 
Sonntag 21 September 2025  01:34:45 +0200 (0:00:00.086)       0:01:43.000 ***** 
Sonntag 21 September 2025  01:34:45 +0200 (0:00:00.047)       0:01:43.048 ***** 
Sonntag 21 September 2025  01:34:45 +0200 (0:00:00.135)       0:01:43.184 ***** 

TASK [promtail : Stop promtail] ***********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/promtail/tasks/main.yml:50</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:34:46 +0200 (0:00:00.593)       0:01:43.777 ***** 
Sonntag 21 September 2025  01:34:46 +0200 (0:00:00.044)       0:01:43.821 ***** 
Sonntag 21 September 2025  01:34:46 +0200 (0:00:00.053)       0:01:43.874 ***** 

TASK [pyload : Stop pyLoad] ***************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/pyload/tasks/main.yml:45</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:34:46 +0200 (0:00:00.620)       0:01:44.495 ***** 
Sonntag 21 September 2025  01:34:46 +0200 (0:00:00.062)       0:01:44.557 ***** 
Sonntag 21 September 2025  01:34:47 +0200 (0:00:00.042)       0:01:44.600 ***** 

TASK [pytivo : Stop Pytivo] ***************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/pytivo/tasks/main.yml:45</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:34:47 +0200 (0:00:00.596)       0:01:45.196 ***** 
Sonntag 21 September 2025  01:34:47 +0200 (0:00:00.045)       0:01:45.242 ***** 
Sonntag 21 September 2025  01:34:47 +0200 (0:00:00.057)       0:01:45.299 ***** 

TASK [radarr : Stop Radarr] ***************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/radarr/tasks/main.yml:44</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:34:48 +0200 (0:00:00.608)       0:01:45.908 ***** 
Sonntag 21 September 2025  01:34:48 +0200 (0:00:00.054)       0:01:45.963 ***** 
Sonntag 21 September 2025  01:34:48 +0200 (0:00:00.043)       0:01:46.006 ***** 
Sonntag 21 September 2025  01:34:48 +0200 (0:00:00.056)       0:01:46.063 ***** 
Sonntag 21 September 2025  01:34:48 +0200 (0:00:00.061)       0:01:46.124 ***** 

TASK [romm : Stop Romm] *******************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/romm/tasks/main.yml:84</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:34:49 +0200 (0:00:00.564)       0:01:46.689 ***** 

TASK [romm : Stop Romm DB] ****************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/romm/tasks/main.yml:89</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:34:49 +0200 (0:00:00.608)       0:01:47.298 ***** 
Sonntag 21 September 2025  01:34:49 +0200 (0:00:00.040)       0:01:47.339 ***** 
Sonntag 21 September 2025  01:34:49 +0200 (0:00:00.049)       0:01:47.388 ***** 
Sonntag 21 September 2025  01:34:49 +0200 (0:00:00.043)       0:01:47.432 ***** 
Sonntag 21 September 2025  01:34:50 +0200 (0:00:00.149)       0:01:47.581 ***** 
Sonntag 21 September 2025  01:34:50 +0200 (0:00:00.052)       0:01:47.634 ***** 
Sonntag 21 September 2025  01:34:50 +0200 (0:00:00.046)       0:01:47.680 ***** 

TASK [rssbridge : Stop RSSBridge] *********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/rssbridge/tasks/main.yml:34</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:34:50 +0200 (0:00:00.599)       0:01:48.280 ***** 
Sonntag 21 September 2025  01:34:50 +0200 (0:00:00.046)       0:01:48.326 ***** 
Sonntag 21 September 2025  01:34:50 +0200 (0:00:00.048)       0:01:48.374 ***** 

TASK [sabnzbd : Stop Sabnzbd] *************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/sabnzbd/tasks/main.yml:38</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:34:51 +0200 (0:00:00.596)       0:01:48.971 ***** 
Sonntag 21 September 2025  01:34:51 +0200 (0:00:00.049)       0:01:49.020 ***** 
Sonntag 21 September 2025  01:34:51 +0200 (0:00:00.044)       0:01:49.064 ***** 

TASK [sickchill : Stop Sickchill] *********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/sickchill/tasks/main.yml:40</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:34:52 +0200 (0:00:00.624)       0:01:49.689 ***** 
Sonntag 21 September 2025  01:34:52 +0200 (0:00:00.069)       0:01:49.758 ***** 
Sonntag 21 September 2025  01:34:52 +0200 (0:00:00.048)       0:01:49.807 ***** 

TASK [silverbullet : Stop silverbullet] ***************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/silverbullet/tasks/main.yml:40</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:34:52 +0200 (0:00:00.597)       0:01:50.405 ***** 
Sonntag 21 September 2025  01:34:52 +0200 (0:00:00.047)       0:01:50.452 ***** 
Sonntag 21 September 2025  01:34:52 +0200 (0:00:00.050)       0:01:50.503 ***** 

TASK [sonarr : Stop Sonarr] ***************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/sonarr/tasks/main.yml:39</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:34:53 +0200 (0:00:00.598)       0:01:51.102 ***** 
Sonntag 21 September 2025  01:34:53 +0200 (0:00:00.053)       0:01:51.155 ***** 
Sonntag 21 September 2025  01:34:53 +0200 (0:00:00.046)       0:01:51.202 ***** 
Sonntag 21 September 2025  01:34:53 +0200 (0:00:00.060)       0:01:51.262 ***** 
Sonntag 21 September 2025  01:34:53 +0200 (0:00:00.066)       0:01:51.329 ***** 
Sonntag 21 September 2025  01:34:54 +0200 (0:00:00.251)       0:01:51.580 ***** 
Sonntag 21 September 2025  01:34:54 +0200 (0:00:00.053)       0:01:51.634 ***** 
Sonntag 21 September 2025  01:34:54 +0200 (0:00:00.048)       0:01:51.683 ***** 
Sonntag 21 September 2025  01:34:54 +0200 (0:00:00.045)       0:01:51.728 ***** 

TASK [stats : Stop Prometheus] ************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/stats/tasks/prometheus.yml:60</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:34:54 +0200 (0:00:00.590)       0:01:52.319 ***** 
Sonntag 21 September 2025  01:34:54 +0200 (0:00:00.050)       0:01:52.370 ***** 
Sonntag 21 September 2025  01:34:54 +0200 (0:00:00.062)       0:01:52.433 ***** 
Sonntag 21 September 2025  01:34:54 +0200 (0:00:00.074)       0:01:52.507 ***** 
Sonntag 21 September 2025  01:34:54 +0200 (0:00:00.043)       0:01:52.550 ***** 

TASK [stats : Stop stats_telegraf] ********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/stats/tasks/telegraf.yml:56</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:34:55 +0200 (0:00:00.575)       0:01:53.126 ***** 
Sonntag 21 September 2025  01:34:55 +0200 (0:00:00.043)       0:01:53.169 ***** 
Sonntag 21 September 2025  01:34:55 +0200 (0:00:00.054)       0:01:53.224 ***** 
Sonntag 21 September 2025  01:34:55 +0200 (0:00:00.067)       0:01:53.291 ***** 

TASK [stats : Stop Smartctl Exporter] *****************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/stats/tasks/exporters.yml:45</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:34:56 +0200 (0:00:00.575)       0:01:53.866 ***** 

TASK [stats : Stop Speedtest Exporter] ****************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/stats/tasks/exporters.yml:49</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:34:56 +0200 (0:00:00.571)       0:01:54.438 ***** 
Sonntag 21 September 2025  01:34:56 +0200 (0:00:00.074)       0:01:54.513 ***** 
Sonntag 21 September 2025  01:34:57 +0200 (0:00:00.049)       0:01:54.562 ***** 
Sonntag 21 September 2025  01:34:57 +0200 (0:00:00.048)       0:01:54.611 ***** 
Sonntag 21 September 2025  01:34:57 +0200 (0:00:00.049)       0:01:54.660 ***** 
Sonntag 21 September 2025  01:34:57 +0200 (0:00:00.048)       0:01:54.708 ***** 

TASK [stats : Stop Grafana] ***************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/stats/tasks/grafana.yml:65</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:34:57 +0200 (0:00:00.642)       0:01:55.351 ***** 
Sonntag 21 September 2025  01:34:57 +0200 (0:00:00.059)       0:01:55.411 ***** 
Sonntag 21 September 2025  01:34:57 +0200 (0:00:00.043)       0:01:55.454 ***** 

TASK [syncthing : Stop Syncthing] *********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/syncthing/tasks/main.yml:38</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:34:58 +0200 (0:00:00.703)       0:01:56.158 ***** 
Sonntag 21 September 2025  01:34:58 +0200 (0:00:00.054)       0:01:56.212 ***** 
Sonntag 21 September 2025  01:34:58 +0200 (0:00:00.046)       0:01:56.259 ***** 

TASK [tautulli : Stop Tautulli] ***********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/tautulli/tasks/main.yml:40</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:34:59 +0200 (0:00:00.593)       0:01:56.852 ***** 
Sonntag 21 September 2025  01:34:59 +0200 (0:00:00.051)       0:01:56.904 ***** 
Sonntag 21 September 2025  01:34:59 +0200 (0:00:00.050)       0:01:56.954 ***** 
Sonntag 21 September 2025  01:34:59 +0200 (0:00:00.042)       0:01:56.997 ***** 

TASK [thelounge : Stop The Lounge] ********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/thelounge/tasks/main.yml:42</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:35:00 +0200 (0:00:00.597)       0:01:57.595 ***** 
Sonntag 21 September 2025  01:35:00 +0200 (0:00:00.069)       0:01:57.664 ***** 
Sonntag 21 September 2025  01:35:00 +0200 (0:00:00.059)       0:01:57.724 ***** 

TASK [threadfin : Stop Threadfin] *********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/threadfin/tasks/main.yml:34</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:35:00 +0200 (0:00:00.603)       0:01:58.327 ***** 
Sonntag 21 September 2025  01:35:00 +0200 (0:00:00.043)       0:01:58.370 ***** 
Sonntag 21 September 2025  01:35:00 +0200 (0:00:00.059)       0:01:58.430 ***** 

TASK [tiddlywiki : Stop Tiddlywiki] *******************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/tiddlywiki/tasks/main.yml:36</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:35:01 +0200 (0:00:00.604)       0:01:59.035 ***** 
Sonntag 21 September 2025  01:35:01 +0200 (0:00:00.044)       0:01:59.079 ***** 
Sonntag 21 September 2025  01:35:01 +0200 (0:00:00.048)       0:01:59.127 ***** 
Sonntag 21 September 2025  01:35:01 +0200 (0:00:00.048)       0:01:59.176 ***** 
Sonntag 21 September 2025  01:35:01 +0200 (0:00:00.041)       0:01:59.217 ***** 

TASK [timemachine : Stop Time Machine] ****************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/timemachine/tasks/main.yml:45</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:35:02 +0200 (0:00:00.600)       0:01:59.817 ***** 
Sonntag 21 September 2025  01:35:02 +0200 (0:00:00.055)       0:01:59.873 ***** 
Sonntag 21 September 2025  01:35:02 +0200 (0:00:00.145)       0:02:00.019 ***** 
Sonntag 21 September 2025  01:35:02 +0200 (0:00:00.043)       0:02:00.063 ***** 

TASK [traefik : Stop Traefik] *************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/traefik/tasks/main.yml:44</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:35:03 +0200 (0:00:00.594)       0:02:00.658 ***** 
Sonntag 21 September 2025  01:35:03 +0200 (0:00:00.072)       0:02:00.730 ***** 
Sonntag 21 September 2025  01:35:03 +0200 (0:00:00.045)       0:02:00.775 ***** 

TASK [transmission : Stop Transmission] ***************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/transmission/tasks/main.yml:44</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:35:03 +0200 (0:00:00.611)       0:02:01.387 ***** 
Sonntag 21 September 2025  01:35:03 +0200 (0:00:00.045)       0:02:01.432 ***** 
Sonntag 21 September 2025  01:35:03 +0200 (0:00:00.052)       0:02:01.484 ***** 

TASK [transmission-with-openvpn : Stop Transmission with OpenVPM] *************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/transmission-with-openvpn/tasks/main.yml:64</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:35:04 +0200 (0:00:00.600)       0:02:02.085 ***** 
Sonntag 21 September 2025  01:35:04 +0200 (0:00:00.047)       0:02:02.132 ***** 
Sonntag 21 September 2025  01:35:04 +0200 (0:00:00.051)       0:02:02.184 ***** 

TASK [ubooquity : Stop Ubooquity] *********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/ubooquity/tasks/main.yml:42</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:35:05 +0200 (0:00:00.604)       0:02:02.788 ***** 
Sonntag 21 September 2025  01:35:05 +0200 (0:00:00.075)       0:02:02.863 ***** 
Sonntag 21 September 2025  01:35:05 +0200 (0:00:00.041)       0:02:02.905 ***** 

TASK [utorrent : Stop uTorrent] ***********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/utorrent/tasks/main.yml:46</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:35:05 +0200 (0:00:00.595)       0:02:03.500 ***** 
Sonntag 21 September 2025  01:35:06 +0200 (0:00:00.060)       0:02:03.560 ***** 
Sonntag 21 September 2025  01:35:06 +0200 (0:00:00.048)       0:02:03.608 ***** 

TASK [valheim : Stop Valheim] *************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/valheim/tasks/main.yml:44</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:35:06 +0200 (0:00:00.622)       0:02:04.231 ***** 
Sonntag 21 September 2025  01:35:06 +0200 (0:00:00.054)       0:02:04.286 ***** 
Sonntag 21 September 2025  01:35:06 +0200 (0:00:00.140)       0:02:04.427 ***** 
Sonntag 21 September 2025  01:35:06 +0200 (0:00:00.043)       0:02:04.471 ***** 

TASK [virtual_desktop : Stop Virtual Desktop] *********************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/virtual_desktop/tasks/main.yml:37</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:35:07 +0200 (0:00:00.595)       0:02:05.066 ***** 
Sonntag 21 September 2025  01:35:07 +0200 (0:00:00.056)       0:02:05.122 ***** 
Sonntag 21 September 2025  01:35:07 +0200 (0:00:00.052)       0:02:05.175 ***** 

TASK [wallabag : Stop Wallabag] ***********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/wallabag/tasks/main.yml:40</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:35:08 +0200 (0:00:00.600)       0:02:05.776 ***** 
Sonntag 21 September 2025  01:35:08 +0200 (0:00:00.068)       0:02:05.844 ***** 

TASK [watchtower : Stop Watchtower] *******************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/watchtower/tasks/main.yml:20</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:35:08 +0200 (0:00:00.617)       0:02:06.462 ***** 
Sonntag 21 September 2025  01:35:08 +0200 (0:00:00.054)       0:02:06.516 ***** 
Sonntag 21 September 2025  01:35:09 +0200 (0:00:00.044)       0:02:06.561 ***** 

TASK [wireshark : Stop Wireshark] *********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/wireshark/tasks/main.yml:39</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:35:09 +0200 (0:00:00.607)       0:02:07.168 ***** 
Sonntag 21 September 2025  01:35:09 +0200 (0:00:00.041)       0:02:07.210 ***** 
Sonntag 21 September 2025  01:35:09 +0200 (0:00:00.052)       0:02:07.262 ***** 
Sonntag 21 September 2025  01:35:09 +0200 (0:00:00.055)       0:02:07.317 ***** 
Sonntag 21 September 2025  01:35:09 +0200 (0:00:00.046)       0:02:07.364 ***** 
Sonntag 21 September 2025  01:35:09 +0200 (0:00:00.046)       0:02:07.410 ***** 
Sonntag 21 September 2025  01:35:09 +0200 (0:00:00.045)       0:02:07.456 ***** 

TASK [woodpecker-ci : Stop Woodpecker-CI] *************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/woodpecker-ci/tasks/main.yml:78</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:35:10 +0200 (0:00:00.594)       0:02:08.050 ***** 
Sonntag 21 September 2025  01:35:10 +0200 (0:00:00.049)       0:02:08.100 ***** 
Sonntag 21 September 2025  01:35:10 +0200 (0:00:00.048)       0:02:08.148 ***** 

TASK [youtubedlmaterial : Stop Youtubedlmaterial] *****************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/youtubedlmaterial/tasks/main.yml:52</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:35:11 +0200 (0:00:00.692)       0:02:08.841 ***** 
Sonntag 21 September 2025  01:35:11 +0200 (0:00:00.058)       0:02:08.899 ***** 
Sonntag 21 September 2025  01:35:11 +0200 (0:00:00.060)       0:02:08.960 ***** 
Sonntag 21 September 2025  01:35:11 +0200 (0:00:00.040)       0:02:09.001 ***** 

TASK [znc : Stop ZNC] *********************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/znc/tasks/main.yml:45</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>

PLAY RECAP ********************************************************************************************************************************************************************************************************
<span style="color:#AA5500">ansible-nas</span>                : <span style="color:#00AA00">ok=156 </span> <span style="color:#AA5500">changed=1   </span> unreachable=0    failed=0    <span style="color:#00AAAA">skipped=308 </span> rescued=0    ignored=0   

Sonntag 21 September 2025  01:35:12 +0200 (0:00:00.572)       0:02:09.574 ***** 
=============================================================================== 
geerlingguy.nfs : Ensure directories to export exist ------------------------------------------------------------------------------------------------------------------------------------------------------- 5.96s
/home/dietmar/.ansible/roles/geerlingguy.nfs/tasks/main.yml:19 ---------------------------------------------------------------------------------------------------------------------------------------------------
homepage : Template config files --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 3.02s
/media/IT/repos/github/forked/ansible-nas/roles/homepage/tasks/main.yml:11 ---------------------------------------------------------------------------------------------------------------------------------------
ansible-nas-general : Update apt-cache --------------------------------------------------------------------------------------------------------------------------------------------------------------------- 2.07s
/media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-general/tasks/main.yml:7 -----------------------------------------------------------------------------------------------------------------------------
vladgh.samba.server : Install Samba packages --------------------------------------------------------------------------------------------------------------------------------------------------------------- 1.73s
/home/dietmar/.ansible/collections/ansible_collections/vladgh/samba/roles/server/tasks/main.yml:12 ---------------------------------------------------------------------------------------------------------------
geerlingguy.docker : Ensure dependencies are installed. ---------------------------------------------------------------------------------------------------------------------------------------------------- 1.47s
/home/dietmar/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml:10 ----------------------------------------------------------------------------------------------------------------------------------------
vladgh.samba.server : Install Samba VFS extensions packages ------------------------------------------------------------------------------------------------------------------------------------------------ 1.41s
/home/dietmar/.ansible/collections/ansible_collections/vladgh/samba/roles/server/tasks/main.yml:19 ---------------------------------------------------------------------------------------------------------------
geerlingguy.docker : Install docker-compose-plugin (with downgrade option). -------------------------------------------------------------------------------------------------------------------------------- 1.40s
/home/dietmar/.ansible/roles/geerlingguy.docker/tasks/main.yml:44 ------------------------------------------------------------------------------------------------------------------------------------------------
geerlingguy.docker : Ensure additional dependencies are installed (on Ubuntu &lt; 20.04 and any other systems). ----------------------------------------------------------------------------------------------- 1.40s
/home/dietmar/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml:18 ----------------------------------------------------------------------------------------------------------------------------------------
geerlingguy.docker : Install Docker packages (with downgrade option). -------------------------------------------------------------------------------------------------------------------------------------- 1.39s
/home/dietmar/.ansible/roles/geerlingguy.docker/tasks/main.yml:27 ------------------------------------------------------------------------------------------------------------------------------------------------
ansible-nas-docker : Install python3-pip ------------------------------------------------------------------------------------------------------------------------------------------------------------------- 1.38s
/media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-docker/tasks/main.yml:2 ------------------------------------------------------------------------------------------------------------------------------
ansible-nas-general : Install some packages ---------------------------------------------------------------------------------------------------------------------------------------------------------------- 1.38s
/media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-general/tasks/main.yml:22 ----------------------------------------------------------------------------------------------------------------------------
airsonic : Stop Airsonic ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 1.34s
/media/IT/repos/github/forked/ansible-nas/roles/airsonic/tasks/main.yml:37 ---------------------------------------------------------------------------------------------------------------------------------------
geerlingguy.nfs : Ensure NFS utilities are installed. ------------------------------------------------------------------------------------------------------------------------------------------------------ 1.34s
/home/dietmar/.ansible/roles/geerlingguy.nfs/tasks/setup-Debian.yml:2 --------------------------------------------------------------------------------------------------------------------------------------------
vladgh.samba.server : Samba configuration ------------------------------------------------------------------------------------------------------------------------------------------------------------------ 1.31s
/home/dietmar/.ansible/collections/ansible_collections/vladgh/samba/roles/server/tasks/main.yml:80 ---------------------------------------------------------------------------------------------------------------
homepage : Create Homepage Docker Container ---------------------------------------------------------------------------------------------------------------------------------------------------------------- 1.27s
/media/IT/repos/github/forked/ansible-nas/roles/homepage/tasks/main.yml:23 ---------------------------------------------------------------------------------------------------------------------------------------
ansible-nas-general : Set hostname to RaspiNAS ------------------------------------------------------------------------------------------------------------------------------------------------------------- 1.25s
/media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-general/tasks/main.yml:29 ----------------------------------------------------------------------------------------------------------------------------
ansible-nas-docker : Install docker python module ---------------------------------------------------------------------------------------------------------------------------------------------------------- 1.23s
/media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-docker/tasks/main.yml:26 -----------------------------------------------------------------------------------------------------------------------------
ansible-nas-docker : Remove docker-py python module -------------------------------------------------------------------------------------------------------------------------------------------------------- 1.12s
/media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-docker/tasks/main.yml:19 -----------------------------------------------------------------------------------------------------------------------------
vladgh.samba.server : Start SMB service -------------------------------------------------------------------------------------------------------------------------------------------------------------------- 1.06s
/home/dietmar/.ansible/collections/ansible_collections/vladgh/samba/roles/server/tasks/main.yml:141 --------------------------------------------------------------------------------------------------------------
geerlingguy.docker : Ensure old versions of Docker are not installed. -------------------------------------------------------------------------------------------------------------------------------------- 0.97s
/home/dietmar/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml:2 -----------------------------------------------------------------------------------------------------------------------------------------
[<span style="color:#00AA00">2025-09-21 01:35:12</span>] (venv) [<span style="color:#55FF55"><b>dietmar@MiraPi</b></span>] [<span style="color:#5555FF"><b>.../forked/ansible-nas</b></span>] $ 
</pre>
