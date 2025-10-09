<pre>[<span style="color:#00AA00">2025-09-21 01:16:27</span>] (venv) [<span style="color:#55FF55"><b>dietmar@MiraPi</b></span>] [<span style="color:#5555FF"><b>.../forked/ansible-nas</b></span>] $ ansible-playbook -i inventories/RaspiNAS/inventory nas.yml -b 
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
Sonntag 21 September 2025  01:16:33 +0200 (0:00:00.162)       0:00:00.162 ***** 

TASK [ansible-nas-users : Create ansible-nas group] ***************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-users/tasks/main.yml:2</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;gid&quot;: 1001,</span>
<span style="color:#00AA00">    &quot;name&quot;: &quot;ansible-nas&quot;,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;present&quot;,</span>
<span style="color:#00AA00">    &quot;system&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:16:35 +0200 (0:00:01.228)       0:00:01.391 ***** 

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
Sonntag 21 September 2025  01:16:36 +0200 (0:00:01.030)       0:00:02.422 ***** 

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
Sonntag 21 September 2025  01:16:36 +0200 (0:00:00.080)       0:00:02.503 ***** 

TASK [vladgh.samba.server : Install Samba packages] ***************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/collections/ansible_collections/vladgh/samba/roles/server/tasks/main.yml:12</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;cache_update_time&quot;: 1758406347,</span>
<span style="color:#00AA00">    &quot;cache_updated&quot;: false,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:16:38 +0200 (0:00:02.236)       0:00:04.739 ***** 

TASK [vladgh.samba.server : Install Samba VFS extensions packages] ************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/collections/ansible_collections/vladgh/samba/roles/server/tasks/main.yml:19</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;cache_update_time&quot;: 1758406347,</span>
<span style="color:#00AA00">    &quot;cache_updated&quot;: false,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:16:40 +0200 (0:00:01.550)       0:00:06.289 ***** 

TASK [vladgh.samba.server : Register Samba version] ***************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/collections/ansible_collections/vladgh/samba/roles/server/tasks/main.yml:26</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;cmd&quot;: &quot;set -o nounset -o pipefail -o errexit &amp;&amp; smbd --version | sed &apos;s/Version //&apos;\n&quot;,</span>
<span style="color:#00AA00">    &quot;delta&quot;: &quot;0:00:00.044235&quot;,</span>
<span style="color:#00AA00">    &quot;end&quot;: &quot;2025-09-21 01:16:41.047441&quot;,</span>
<span style="color:#00AA00">    &quot;rc&quot;: 0,</span>
<span style="color:#00AA00">    &quot;start&quot;: &quot;2025-09-21 01:16:41.003206&quot;</span>
<span style="color:#00AA00">}</span>

<span style="color:#00AA00">STDOUT:</span>

<span style="color:#00AA00">4.17.12-Debian</span>
Sonntag 21 September 2025  01:16:41 +0200 (0:00:01.045)       0:00:07.334 ***** 
Sonntag 21 September 2025  01:16:41 +0200 (0:00:00.203)       0:00:07.538 ***** 
Sonntag 21 September 2025  01:16:41 +0200 (0:00:00.053)       0:00:07.591 ***** 
Sonntag 21 September 2025  01:16:41 +0200 (0:00:00.157)       0:00:07.749 ***** 
Sonntag 21 September 2025  01:16:41 +0200 (0:00:00.063)       0:00:07.812 ***** 

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
Sonntag 21 September 2025  01:16:43 +0200 (0:00:02.317)       0:00:10.130 ***** 
Sonntag 21 September 2025  01:16:43 +0200 (0:00:00.046)       0:00:10.176 ***** 
Sonntag 21 September 2025  01:16:44 +0200 (0:00:00.044)       0:00:10.221 ***** 
Sonntag 21 September 2025  01:16:44 +0200 (0:00:00.031)       0:00:10.252 ***** 
Sonntag 21 September 2025  01:16:44 +0200 (0:00:00.043)       0:00:10.295 ***** 

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
<span style="color:#00AA00">        &quot;CPUUsageNSec&quot;: &quot;110524000&quot;,</span>
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
Sonntag 21 September 2025  01:16:45 +0200 (0:00:01.064)       0:00:11.360 ***** 

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
<span style="color:#00AA00">        &quot;CPUUsageNSec&quot;: &quot;554515000&quot;,</span>
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
Sonntag 21 September 2025  01:16:45 +0200 (0:00:00.549)       0:00:11.909 ***** 
Sonntag 21 September 2025  01:16:45 +0200 (0:00:00.046)       0:00:11.956 ***** 

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
Sonntag 21 September 2025  01:16:45 +0200 (0:00:00.047)       0:00:12.004 ***** 
Sonntag 21 September 2025  01:16:45 +0200 (0:00:00.029)       0:00:12.033 ***** 
Sonntag 21 September 2025  01:16:45 +0200 (0:00:00.035)       0:00:12.069 ***** 

TASK [geerlingguy.nfs : include_tasks] ****************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.nfs/tasks/main.yml:16</b></span>
<span style="color:#00AAAA">included: /home/dietmar/.ansible/roles/geerlingguy.nfs/tasks/setup-Debian.yml for ansible-nas</span>
Sonntag 21 September 2025  01:16:45 +0200 (0:00:00.052)       0:00:12.121 ***** 

TASK [geerlingguy.nfs : Ensure NFS utilities are installed.] ******************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.nfs/tasks/setup-Debian.yml:2</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;cache_update_time&quot;: 1758406347,</span>
<span style="color:#00AA00">    &quot;cache_updated&quot;: false,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:16:47 +0200 (0:00:01.378)       0:00:13.500 ***** 

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
Sonntag 21 September 2025  01:16:53 +0200 (0:00:05.765)       0:00:19.265 ***** 

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
Sonntag 21 September 2025  01:16:53 +0200 (0:00:00.612)       0:00:19.878 ***** 

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
Sonntag 21 September 2025  01:16:54 +0200 (0:00:00.599)       0:00:20.478 ***** 

TASK [geerlingguy.docker : Load OS-specific vars.] ****************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.docker/tasks/main.yml:2</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;ansible_facts&quot;: {},</span>
<span style="color:#00AA00">    &quot;ansible_included_var_files&quot;: [</span>
<span style="color:#00AA00">        &quot;/home/dietmar/.ansible/roles/geerlingguy.docker/vars/main.yml&quot;</span>
<span style="color:#00AA00">    ],</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:16:54 +0200 (0:00:00.039)       0:00:20.517 ***** 
Sonntag 21 September 2025  01:16:54 +0200 (0:00:00.040)       0:00:20.558 ***** 

TASK [geerlingguy.docker : include_tasks] *************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.docker/tasks/main.yml:16</b></span>
<span style="color:#00AAAA">included: /home/dietmar/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml for ansible-nas</span>
Sonntag 21 September 2025  01:16:54 +0200 (0:00:00.064)       0:00:20.623 ***** 

TASK [geerlingguy.docker : Ensure old versions of Docker are not installed.] **************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml:2</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:16:55 +0200 (0:00:00.975)       0:00:21.598 ***** 

TASK [geerlingguy.docker : Ensure dependencies are installed.] ****************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml:10</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;cache_update_time&quot;: 1758406347,</span>
<span style="color:#00AA00">    &quot;cache_updated&quot;: false,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:16:56 +0200 (0:00:01.474)       0:00:23.072 ***** 

TASK [geerlingguy.docker : Ensure additional dependencies are installed (on Ubuntu &lt; 20.04 and any other systems).] ***********************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml:18</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;cache_update_time&quot;: 1758406347,</span>
<span style="color:#00AA00">    &quot;cache_updated&quot;: false,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:16:58 +0200 (0:00:01.369)       0:00:24.442 ***** 
Sonntag 21 September 2025  01:16:58 +0200 (0:00:00.049)       0:00:24.492 ***** 

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
Sonntag 21 September 2025  01:16:58 +0200 (0:00:00.703)       0:00:25.196 ***** 
Sonntag 21 September 2025  01:16:59 +0200 (0:00:00.069)       0:00:25.265 ***** 
Sonntag 21 September 2025  01:16:59 +0200 (0:00:00.076)       0:00:25.341 ***** 

TASK [geerlingguy.docker : Add Docker repository.] ****************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml:50</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;repo&quot;: &quot;deb [arch=arm64 signed-by=/etc/apt/trusted.gpg.d/docker.asc] https://download.docker.com/linux/debian bookworm stable&quot;,</span>
<span style="color:#00AA00">    &quot;sources_added&quot;: [],</span>
<span style="color:#00AA00">    &quot;sources_removed&quot;: [],</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;present&quot;</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:16:59 +0200 (0:00:00.805)       0:00:26.147 ***** 
Sonntag 21 September 2025  01:16:59 +0200 (0:00:00.042)       0:00:26.189 ***** 

TASK [geerlingguy.docker : Install Docker packages (with downgrade option).] **************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.docker/tasks/main.yml:27</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;cache_update_time&quot;: 1758406347,</span>
<span style="color:#00AA00">    &quot;cache_updated&quot;: false,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:17:01 +0200 (0:00:01.365)       0:00:27.555 ***** 
Sonntag 21 September 2025  01:17:01 +0200 (0:00:00.081)       0:00:27.637 ***** 

TASK [geerlingguy.docker : Install docker-compose-plugin (with downgrade option).] ********************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.docker/tasks/main.yml:44</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;cache_update_time&quot;: 1758406347,</span>
<span style="color:#00AA00">    &quot;cache_updated&quot;: false,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:17:02 +0200 (0:00:01.430)       0:00:29.068 ***** 
Sonntag 21 September 2025  01:17:02 +0200 (0:00:00.068)       0:00:29.136 ***** 
Sonntag 21 September 2025  01:17:03 +0200 (0:00:00.092)       0:00:29.229 ***** 

TASK [geerlingguy.docker : Ensure Docker is started and enabled at boot.] *****************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.docker/tasks/main.yml:68</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;enabled&quot;: true,</span>
<span style="color:#00AA00">    &quot;name&quot;: &quot;docker&quot;,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;started&quot;,</span>
<span style="color:#00AA00">    &quot;status&quot;: {</span>
<span style="color:#00AA00">        &quot;ActiveEnterTimestamp&quot;: &quot;Sun 2025-09-21 00:12:55 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;ActiveEnterTimestampMonotonic&quot;: &quot;678350106808&quot;,</span>
<span style="color:#00AA00">        &quot;ActiveExitTimestamp&quot;: &quot;Sun 2025-09-21 00:12:54 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;ActiveExitTimestampMonotonic&quot;: &quot;678348896500&quot;,</span>
<span style="color:#00AA00">        &quot;ActiveState&quot;: &quot;active&quot;,</span>
<span style="color:#00AA00">        &quot;After&quot;: &quot;basic.target network-online.target systemd-journald.socket firewalld.service sysinit.target system.slice docker.socket time-set.target containerd.service nss-lookup.target&quot;,</span>
<span style="color:#00AA00">        &quot;AllowIsolate&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;AssertResult&quot;: &quot;yes&quot;,</span>
<span style="color:#00AA00">        &quot;AssertTimestamp&quot;: &quot;Sun 2025-09-21 00:12:54 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;AssertTimestampMonotonic&quot;: &quot;678348900844&quot;,</span>
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
<span style="color:#00AA00">        &quot;CPUUsageNSec&quot;: &quot;566614000&quot;,</span>
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
<span style="color:#00AA00">        &quot;ConditionTimestamp&quot;: &quot;Sun 2025-09-21 00:12:54 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;ConditionTimestampMonotonic&quot;: &quot;678348900842&quot;,</span>
<span style="color:#00AA00">        &quot;ConfigurationDirectoryMode&quot;: &quot;0755&quot;,</span>
<span style="color:#00AA00">        &quot;Conflicts&quot;: &quot;shutdown.target&quot;,</span>
<span style="color:#00AA00">        &quot;ControlGroup&quot;: &quot;/system.slice/docker.service&quot;,</span>
<span style="color:#00AA00">        &quot;ControlGroupId&quot;: &quot;47407&quot;,</span>
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
<span style="color:#00AA00">        &quot;ExecMainPID&quot;: &quot;1371972&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainStartTimestamp&quot;: &quot;Sun 2025-09-21 00:12:54 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainStartTimestampMonotonic&quot;: &quot;678348932159&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainStatus&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;ExecReload&quot;: &quot;{ path=/bin/kill ; argv[]=/bin/kill -s HUP $MAINPID ; ignore_errors=no ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }&quot;,</span>
<span style="color:#00AA00">        &quot;ExecReloadEx&quot;: &quot;{ path=/bin/kill ; argv[]=/bin/kill -s HUP $MAINPID ; flags= ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }&quot;,</span>
<span style="color:#00AA00">        &quot;ExecStart&quot;: &quot;{ path=/usr/bin/dockerd ; argv[]=/usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock ; ignore_errors=no ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }&quot;,</span>
<span style="color:#00AA00">        &quot;ExecStartEx&quot;: &quot;{ path=/usr/bin/dockerd ; argv[]=/usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock ; flags= ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }&quot;,</span>
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
<span style="color:#00AA00">        &quot;InactiveEnterTimestamp&quot;: &quot;Sun 2025-09-21 00:12:54 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;InactiveEnterTimestampMonotonic&quot;: &quot;678348900407&quot;,</span>
<span style="color:#00AA00">        &quot;InactiveExitTimestamp&quot;: &quot;Sun 2025-09-21 00:12:54 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;InactiveExitTimestampMonotonic&quot;: &quot;678348932564&quot;,</span>
<span style="color:#00AA00">        &quot;InvocationID&quot;: &quot;a02f08afccc34e5ea50f0eaefebab828&quot;,</span>
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
<span style="color:#00AA00">        &quot;MainPID&quot;: &quot;1371972&quot;,</span>
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
<span style="color:#00AA00">        &quot;StateChangeTimestamp&quot;: &quot;Sun 2025-09-21 00:12:55 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;StateChangeTimestampMonotonic&quot;: &quot;678350106808&quot;,</span>
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
Sonntag 21 September 2025  01:17:03 +0200 (0:00:00.556)       0:00:29.786 ***** 
<span style="color:#0000AA">META: triggered running handlers for ansible-nas</span>
Sonntag 21 September 2025  01:17:03 +0200 (0:00:00.022)       0:00:29.808 ***** 
Sonntag 21 September 2025  01:17:03 +0200 (0:00:00.074)       0:00:29.882 ***** 
Sonntag 21 September 2025  01:17:03 +0200 (0:00:00.094)       0:00:29.977 ***** 
Sonntag 21 September 2025  01:17:03 +0200 (0:00:00.032)       0:00:30.009 ***** 
Sonntag 21 September 2025  01:17:03 +0200 (0:00:00.057)       0:00:30.066 ***** 

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
Sonntag 21 September 2025  01:17:04 +0200 (0:00:00.609)       0:00:30.676 ***** 

TASK [ansible-nas-general : Update apt-cache] *********************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-general/tasks/main.yml:7</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;attempts&quot;: 1,</span>
<span style="color:#00AA00">    &quot;cache_update_time&quot;: 1758406347,</span>
<span style="color:#00AA00">    &quot;cache_updated&quot;: false,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:17:06 +0200 (0:00:02.058)       0:00:32.735 ***** 
Sonntag 21 September 2025  01:17:06 +0200 (0:00:00.034)       0:00:32.769 ***** 

TASK [ansible-nas-general : Install some packages] ****************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-general/tasks/main.yml:22</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;attempts&quot;: 1,</span>
<span style="color:#00AA00">    &quot;cache_update_time&quot;: 1758406347,</span>
<span style="color:#00AA00">    &quot;cache_updated&quot;: false,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:17:07 +0200 (0:00:01.394)       0:00:34.163 ***** 

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
Sonntag 21 September 2025  01:17:09 +0200 (0:00:01.232)       0:00:35.396 ***** 

TASK [ansible-nas-general : Set timezone to Europe/Berlin] ********************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-general/tasks/main.yml:33</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:17:09 +0200 (0:00:00.814)       0:00:36.210 ***** 
Sonntag 21 September 2025  01:17:10 +0200 (0:00:00.044)       0:00:36.254 ***** 

TASK [ansible-nas-docker : Install python3-pip] *******************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-docker/tasks/main.yml:2</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;attempts&quot;: 1,</span>
<span style="color:#00AA00">    &quot;cache_update_time&quot;: 1758406347,</span>
<span style="color:#00AA00">    &quot;cache_updated&quot;: false,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:17:11 +0200 (0:00:01.402)       0:00:37.656 ***** 

TASK [ansible-nas-docker : Copy &quot;ext-managed&quot;] ********************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-docker/tasks/main.yml:9</b></span>
<span style="color:#AA5500">changed: [ansible-nas] =&gt; {</span>
<span style="color:#AA5500">    &quot;changed&quot;: true,</span>
<span style="color:#AA5500">    &quot;checksum&quot;: &quot;654cca365a9351054dd5f8f8d0f27bdc330c0489&quot;,</span>
<span style="color:#AA5500">    &quot;dest&quot;: &quot;/usr/lib/python3.11/EXTERNALLY-MANAGED_bak&quot;,</span>
<span style="color:#AA5500">    &quot;gid&quot;: 0,</span>
<span style="color:#AA5500">    &quot;group&quot;: &quot;root&quot;,</span>
<span style="color:#AA5500">    &quot;md5sum&quot;: &quot;12215eeffd7532bcd25f2817facafdf9&quot;,</span>
<span style="color:#AA5500">    &quot;mode&quot;: &quot;0644&quot;,</span>
<span style="color:#AA5500">    &quot;owner&quot;: &quot;root&quot;,</span>
<span style="color:#AA5500">    &quot;size&quot;: 432,</span>
<span style="color:#AA5500">    &quot;src&quot;: &quot;/home/dietmar/.ansible/tmp/ansible-tmp-1758410231.4865222-39430-189702383803147/source&quot;,</span>
<span style="color:#AA5500">    &quot;state&quot;: &quot;file&quot;,</span>
<span style="color:#AA5500">    &quot;uid&quot;: 0</span>
<span style="color:#AA5500">}</span>
Sonntag 21 September 2025  01:17:12 +0200 (0:00:00.823)       0:00:38.480 ***** 

TASK [ansible-nas-docker : Remove &quot;ext-managed&quot;] ******************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-docker/tasks/main.yml:14</b></span>
<span style="color:#AA5500">changed: [ansible-nas] =&gt; {</span>
<span style="color:#AA5500">    &quot;changed&quot;: true,</span>
<span style="color:#AA5500">    &quot;path&quot;: &quot;/usr/lib/python3.11/EXTERNALLY-MANAGED&quot;,</span>
<span style="color:#AA5500">    &quot;state&quot;: &quot;absent&quot;</span>
<span style="color:#AA5500">}</span>
Sonntag 21 September 2025  01:17:12 +0200 (0:00:00.352)       0:00:38.833 ***** 

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

Sonntag 21 September 2025  01:17:13 +0200 (0:00:01.119)       0:00:39.952 ***** 

TASK [ansible-nas-docker : Install docker python module] **********************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-docker/tasks/main.yml:26</b></span>
<span style="color:#AA5500">changed: [ansible-nas] =&gt; {</span>
<span style="color:#AA5500">    &quot;attempts&quot;: 1,</span>
<span style="color:#AA5500">    &quot;changed&quot;: true,</span>
<span style="color:#AA5500">    &quot;cmd&quot;: [</span>
<span style="color:#AA5500">        &quot;/usr/bin/python3&quot;,</span>
<span style="color:#AA5500">        &quot;-m&quot;,</span>
<span style="color:#AA5500">        &quot;pip.__main__&quot;,</span>
<span style="color:#AA5500">        &quot;install&quot;,</span>
<span style="color:#AA5500">        &quot;docker&quot;</span>
<span style="color:#AA5500">    ],</span>
<span style="color:#AA5500">    &quot;name&quot;: [</span>
<span style="color:#AA5500">        &quot;docker&quot;</span>
<span style="color:#AA5500">    ],</span>
<span style="color:#AA5500">    &quot;requirements&quot;: null,</span>
<span style="color:#AA5500">    &quot;state&quot;: &quot;present&quot;,</span>
<span style="color:#AA5500">    &quot;version&quot;: null,</span>
<span style="color:#AA5500">    &quot;virtualenv&quot;: null</span>
<span style="color:#AA5500">}</span>

<span style="color:#AA5500">STDOUT:</span>

<span style="color:#AA5500">Looking in indexes: https://pypi.org/simple, https://www.piwheels.org/simple</span>
<span style="color:#AA5500">Collecting docker</span>
<span style="color:#AA5500">  Downloading https://www.piwheels.org/simple/docker/docker-7.1.0-py3-none-any.whl (147 kB)</span>
<span style="color:#AA5500">     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 147.8/147.8 kB 2.1 MB/s eta 0:00:00</span>
<span style="color:#AA5500">Requirement already satisfied: requests&gt;=2.26.0 in /usr/lib/python3/dist-packages (from docker) (2.28.1)</span>
<span style="color:#AA5500">Requirement already satisfied: urllib3&gt;=1.26.0 in /usr/lib/python3/dist-packages (from docker) (1.26.12)</span>
<span style="color:#AA5500">Installing collected packages: docker</span>
<span style="color:#AA5500">Successfully installed docker-7.1.0</span>



<span style="color:#AA5500">STDERR:</span>

<span style="color:#AA5500">WARNING: Running pip as the &apos;root&apos; user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv</span>

Sonntag 21 September 2025  01:17:15 +0200 (0:00:01.864)       0:00:41.816 ***** 

TASK [ansible-nas-docker : Create Docker home directory] **********************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-docker/tasks/main.yml:33</b></span>
<span style="color:#AA5500">changed: [ansible-nas] =&gt; {</span>
<span style="color:#AA5500">    &quot;changed&quot;: true,</span>
<span style="color:#AA5500">    &quot;gid&quot;: 1001,</span>
<span style="color:#AA5500">    &quot;group&quot;: &quot;ansible-nas&quot;,</span>
<span style="color:#AA5500">    &quot;mode&quot;: &quot;0755&quot;,</span>
<span style="color:#AA5500">    &quot;owner&quot;: &quot;1001&quot;,</span>
<span style="color:#AA5500">    &quot;path&quot;: &quot;/mnt/Volume1/docker&quot;,</span>
<span style="color:#AA5500">    &quot;size&quot;: 4096,</span>
<span style="color:#AA5500">    &quot;state&quot;: &quot;directory&quot;,</span>
<span style="color:#AA5500">    &quot;uid&quot;: 1001</span>
<span style="color:#AA5500">}</span>
Sonntag 21 September 2025  01:17:15 +0200 (0:00:00.378)       0:00:42.195 ***** 

TASK [ansible-nas-docker : Add user account to Docker group] ******************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-docker/tasks/main.yml:39</b></span>
<span style="color:#AA5500">changed: [ansible-nas] =&gt; {</span>
<span style="color:#AA5500">    &quot;append&quot;: true,</span>
<span style="color:#AA5500">    &quot;changed&quot;: true,</span>
<span style="color:#AA5500">    &quot;comment&quot;: &quot;,,,&quot;,</span>
<span style="color:#AA5500">    &quot;group&quot;: 1000,</span>
<span style="color:#AA5500">    &quot;groups&quot;: &quot;docker&quot;,</span>
<span style="color:#AA5500">    &quot;home&quot;: &quot;/home/dietmar&quot;,</span>
<span style="color:#AA5500">    &quot;move_home&quot;: false,</span>
<span style="color:#AA5500">    &quot;name&quot;: &quot;dietmar&quot;,</span>
<span style="color:#AA5500">    &quot;shell&quot;: &quot;/bin/bash&quot;,</span>
<span style="color:#AA5500">    &quot;state&quot;: &quot;present&quot;,</span>
<span style="color:#AA5500">    &quot;uid&quot;: 1000</span>
<span style="color:#AA5500">}</span>
Sonntag 21 September 2025  01:17:16 +0200 (0:00:00.438)       0:00:42.633 ***** 

TASK [ansible-nas-docker : Generate Docker daemon.json] ***********************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-docker/tasks/main.yml:45</b></span>
<span style="color:#AA5500">changed: [ansible-nas] =&gt; {</span>
<span style="color:#AA5500">    &quot;changed&quot;: true,</span>
<span style="color:#AA5500">    &quot;checksum&quot;: &quot;b49ff4beca73d8e8ac8315d97b6f6fa38d02f720&quot;,</span>
<span style="color:#AA5500">    &quot;dest&quot;: &quot;/etc/docker/daemon.json&quot;,</span>
<span style="color:#AA5500">    &quot;gid&quot;: 0,</span>
<span style="color:#AA5500">    &quot;group&quot;: &quot;root&quot;,</span>
<span style="color:#AA5500">    &quot;md5sum&quot;: &quot;667edd16b98b80403c27170329a10bb3&quot;,</span>
<span style="color:#AA5500">    &quot;mode&quot;: &quot;0644&quot;,</span>
<span style="color:#AA5500">    &quot;owner&quot;: &quot;root&quot;,</span>
<span style="color:#AA5500">    &quot;size&quot;: 72,</span>
<span style="color:#AA5500">    &quot;src&quot;: &quot;/home/dietmar/.ansible/tmp/ansible-tmp-1758410236.5069573-39599-58340601230823/source&quot;,</span>
<span style="color:#AA5500">    &quot;state&quot;: &quot;file&quot;,</span>
<span style="color:#AA5500">    &quot;uid&quot;: 0</span>
<span style="color:#AA5500">}</span>
Sonntag 21 September 2025  01:17:17 +0200 (0:00:00.642)       0:00:43.276 ***** 

TASK [ansible-nas-docker : Restart Docker] ************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-docker/tasks/main.yml:51</b></span>
<span style="color:#AA5500">changed: [ansible-nas] =&gt; {</span>
<span style="color:#AA5500">    &quot;changed&quot;: true,</span>
<span style="color:#AA5500">    &quot;name&quot;: &quot;docker&quot;,</span>
<span style="color:#AA5500">    &quot;state&quot;: &quot;started&quot;,</span>
<span style="color:#AA5500">    &quot;status&quot;: {</span>
<span style="color:#AA5500">        &quot;ActiveEnterTimestamp&quot;: &quot;Sun 2025-09-21 00:12:55 CEST&quot;,</span>
<span style="color:#AA5500">        &quot;ActiveEnterTimestampMonotonic&quot;: &quot;678350106808&quot;,</span>
<span style="color:#AA5500">        &quot;ActiveExitTimestamp&quot;: &quot;Sun 2025-09-21 00:12:54 CEST&quot;,</span>
<span style="color:#AA5500">        &quot;ActiveExitTimestampMonotonic&quot;: &quot;678348896500&quot;,</span>
<span style="color:#AA5500">        &quot;ActiveState&quot;: &quot;active&quot;,</span>
<span style="color:#AA5500">        &quot;After&quot;: &quot;basic.target network-online.target systemd-journald.socket firewalld.service sysinit.target system.slice docker.socket time-set.target containerd.service nss-lookup.target&quot;,</span>
<span style="color:#AA5500">        &quot;AllowIsolate&quot;: &quot;no&quot;,</span>
<span style="color:#AA5500">        &quot;AssertResult&quot;: &quot;yes&quot;,</span>
<span style="color:#AA5500">        &quot;AssertTimestamp&quot;: &quot;Sun 2025-09-21 00:12:54 CEST&quot;,</span>
<span style="color:#AA5500">        &quot;AssertTimestampMonotonic&quot;: &quot;678348900844&quot;,</span>
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
<span style="color:#AA5500">        &quot;CPUUsageNSec&quot;: &quot;566973000&quot;,</span>
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
<span style="color:#AA5500">        &quot;ConditionTimestamp&quot;: &quot;Sun 2025-09-21 00:12:54 CEST&quot;,</span>
<span style="color:#AA5500">        &quot;ConditionTimestampMonotonic&quot;: &quot;678348900842&quot;,</span>
<span style="color:#AA5500">        &quot;ConfigurationDirectoryMode&quot;: &quot;0755&quot;,</span>
<span style="color:#AA5500">        &quot;Conflicts&quot;: &quot;shutdown.target&quot;,</span>
<span style="color:#AA5500">        &quot;ControlGroup&quot;: &quot;/system.slice/docker.service&quot;,</span>
<span style="color:#AA5500">        &quot;ControlGroupId&quot;: &quot;47407&quot;,</span>
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
<span style="color:#AA5500">        &quot;ExecMainPID&quot;: &quot;1371972&quot;,</span>
<span style="color:#AA5500">        &quot;ExecMainStartTimestamp&quot;: &quot;Sun 2025-09-21 00:12:54 CEST&quot;,</span>
<span style="color:#AA5500">        &quot;ExecMainStartTimestampMonotonic&quot;: &quot;678348932159&quot;,</span>
<span style="color:#AA5500">        &quot;ExecMainStatus&quot;: &quot;0&quot;,</span>
<span style="color:#AA5500">        &quot;ExecReload&quot;: &quot;{ path=/bin/kill ; argv[]=/bin/kill -s HUP $MAINPID ; ignore_errors=no ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }&quot;,</span>
<span style="color:#AA5500">        &quot;ExecReloadEx&quot;: &quot;{ path=/bin/kill ; argv[]=/bin/kill -s HUP $MAINPID ; flags= ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }&quot;,</span>
<span style="color:#AA5500">        &quot;ExecStart&quot;: &quot;{ path=/usr/bin/dockerd ; argv[]=/usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock ; ignore_errors=no ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }&quot;,</span>
<span style="color:#AA5500">        &quot;ExecStartEx&quot;: &quot;{ path=/usr/bin/dockerd ; argv[]=/usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock ; flags= ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }&quot;,</span>
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
<span style="color:#AA5500">        &quot;InactiveEnterTimestamp&quot;: &quot;Sun 2025-09-21 00:12:54 CEST&quot;,</span>
<span style="color:#AA5500">        &quot;InactiveEnterTimestampMonotonic&quot;: &quot;678348900407&quot;,</span>
<span style="color:#AA5500">        &quot;InactiveExitTimestamp&quot;: &quot;Sun 2025-09-21 00:12:54 CEST&quot;,</span>
<span style="color:#AA5500">        &quot;InactiveExitTimestampMonotonic&quot;: &quot;678348932564&quot;,</span>
<span style="color:#AA5500">        &quot;InvocationID&quot;: &quot;a02f08afccc34e5ea50f0eaefebab828&quot;,</span>
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
<span style="color:#AA5500">        &quot;MainPID&quot;: &quot;1371972&quot;,</span>
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
<span style="color:#AA5500">        &quot;StateChangeTimestamp&quot;: &quot;Sun 2025-09-21 00:12:55 CEST&quot;,</span>
<span style="color:#AA5500">        &quot;StateChangeTimestampMonotonic&quot;: &quot;678350106808&quot;,</span>
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
Sonntag 21 September 2025  01:17:18 +0200 (0:00:01.666)       0:00:44.942 ***** 
Sonntag 21 September 2025  01:17:18 +0200 (0:00:00.039)       0:00:44.982 ***** 

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
Sonntag 21 September 2025  01:17:18 +0200 (0:00:00.068)       0:00:45.050 ***** 
Sonntag 21 September 2025  01:17:18 +0200 (0:00:00.058)       0:00:45.108 ***** 
Sonntag 21 September 2025  01:17:18 +0200 (0:00:00.041)       0:00:45.150 ***** 

TASK [airsonic : Stop Airsonic] ***********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/airsonic/tasks/main.yml:37</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:17:20 +0200 (0:00:01.302)       0:00:46.452 ***** 
Sonntag 21 September 2025  01:17:20 +0200 (0:00:00.044)       0:00:46.497 ***** 
Sonntag 21 September 2025  01:17:20 +0200 (0:00:00.056)       0:00:46.554 ***** 
Sonntag 21 September 2025  01:17:20 +0200 (0:00:00.046)       0:00:46.600 ***** 
Sonntag 21 September 2025  01:17:20 +0200 (0:00:00.059)       0:00:46.659 ***** 

TASK [apcupsd : Stop Apcupsd] *************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/apcupsd/tasks/main.yml:44</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:17:21 +0200 (0:00:00.574)       0:00:47.233 ***** 
Sonntag 21 September 2025  01:17:21 +0200 (0:00:00.141)       0:00:47.375 ***** 
Sonntag 21 September 2025  01:17:21 +0200 (0:00:00.045)       0:00:47.420 ***** 

TASK [bazarr : Stop Bazarr] ***************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/bazarr/tasks/main.yml:46</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:17:21 +0200 (0:00:00.615)       0:00:48.036 ***** 
Sonntag 21 September 2025  01:17:21 +0200 (0:00:00.056)       0:00:48.092 ***** 
Sonntag 21 September 2025  01:17:21 +0200 (0:00:00.044)       0:00:48.136 ***** 
Sonntag 21 September 2025  01:17:21 +0200 (0:00:00.049)       0:00:48.185 ***** 
Sonntag 21 September 2025  01:17:22 +0200 (0:00:00.042)       0:00:48.228 ***** 

TASK [bitwarden : Stop Bitwarden] *********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/bitwarden/tasks/main.yml:64</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:17:22 +0200 (0:00:00.615)       0:00:48.844 ***** 

TASK [bitwarden : Stop Bitwarden Backup] **************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/bitwarden/tasks/main.yml:69</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:17:23 +0200 (0:00:00.580)       0:00:49.424 ***** 
Sonntag 21 September 2025  01:17:23 +0200 (0:00:00.053)       0:00:49.477 ***** 
Sonntag 21 September 2025  01:17:23 +0200 (0:00:00.046)       0:00:49.524 ***** 

TASK [booksonic : Stop Booksonic] *********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/booksonic/tasks/main.yml:42</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:17:23 +0200 (0:00:00.597)       0:00:50.121 ***** 
Sonntag 21 September 2025  01:17:23 +0200 (0:00:00.045)       0:00:50.166 ***** 
Sonntag 21 September 2025  01:17:24 +0200 (0:00:00.050)       0:00:50.217 ***** 

TASK [calibre : Stop Calibre] *************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/calibre/tasks/main.yml:44</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:17:24 +0200 (0:00:00.594)       0:00:50.811 ***** 
Sonntag 21 September 2025  01:17:24 +0200 (0:00:00.051)       0:00:50.863 ***** 
Sonntag 21 September 2025  01:17:24 +0200 (0:00:00.043)       0:00:50.906 ***** 

TASK [calibreweb : Stop Calibre-web] ******************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/calibreweb/tasks/main.yml:41</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:17:25 +0200 (0:00:00.588)       0:00:51.495 ***** 
Sonntag 21 September 2025  01:17:25 +0200 (0:00:00.047)       0:00:51.542 ***** 
Sonntag 21 September 2025  01:17:25 +0200 (0:00:00.049)       0:00:51.591 ***** 

TASK [cloudcmd : Stop Cloudcmd] ***********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/cloudcmd/tasks/main.yml:38</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:17:26 +0200 (0:00:00.673)       0:00:52.265 ***** 
Sonntag 21 September 2025  01:17:26 +0200 (0:00:00.042)       0:00:52.307 ***** 
Sonntag 21 September 2025  01:17:26 +0200 (0:00:00.051)       0:00:52.359 ***** 
Sonntag 21 September 2025  01:17:26 +0200 (0:00:00.053)       0:00:52.413 ***** 
Sonntag 21 September 2025  01:17:26 +0200 (0:00:00.044)       0:00:52.458 ***** 

TASK [cloudflare_ddns : Stop Cloudflare DDNS] *********************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/cloudflare_ddns/tasks/main.yml:34</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:17:26 +0200 (0:00:00.582)       0:00:53.040 ***** 
Sonntag 21 September 2025  01:17:26 +0200 (0:00:00.051)       0:00:53.092 ***** 
Sonntag 21 September 2025  01:17:26 +0200 (0:00:00.054)       0:00:53.146 ***** 

TASK [couchdb : Stop CouchDB] *************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/couchdb/tasks/main.yml:38</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:17:27 +0200 (0:00:00.584)       0:00:53.731 ***** 
Sonntag 21 September 2025  01:17:27 +0200 (0:00:00.041)       0:00:53.772 ***** 

TASK [code-server : Stop Code Server] *****************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/code-server/tasks/main.yml:32</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:17:28 +0200 (0:00:00.640)       0:00:54.413 ***** 
Sonntag 21 September 2025  01:17:28 +0200 (0:00:00.047)       0:00:54.460 ***** 
Sonntag 21 September 2025  01:17:28 +0200 (0:00:00.042)       0:00:54.503 ***** 

TASK [couchpotato : Stop Couchpotato] *****************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/couchpotato/tasks/main.yml:41</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:17:28 +0200 (0:00:00.588)       0:00:55.091 ***** 
Sonntag 21 September 2025  01:17:28 +0200 (0:00:00.050)       0:00:55.141 ***** 
Sonntag 21 September 2025  01:17:28 +0200 (0:00:00.042)       0:00:55.184 ***** 
Sonntag 21 September 2025  01:17:29 +0200 (0:00:00.047)       0:00:55.232 ***** 

TASK [dashy : Stop Dashy] *****************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/dashy/tasks/main.yml:39</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:17:29 +0200 (0:00:00.572)       0:00:55.804 ***** 
Sonntag 21 September 2025  01:17:29 +0200 (0:00:00.038)       0:00:55.843 ***** 
Sonntag 21 September 2025  01:17:29 +0200 (0:00:00.058)       0:00:55.901 ***** 
Sonntag 21 September 2025  01:17:29 +0200 (0:00:00.132)       0:00:56.034 ***** 
Sonntag 21 September 2025  01:17:29 +0200 (0:00:00.042)       0:00:56.076 ***** 

TASK [ddns_updater : Stop DDNS Updater] ***************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/ddns_updater/tasks/main.yml:54</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:17:30 +0200 (0:00:00.574)       0:00:56.651 ***** 
Sonntag 21 September 2025  01:17:30 +0200 (0:00:00.053)       0:00:56.704 ***** 
Sonntag 21 September 2025  01:17:30 +0200 (0:00:00.042)       0:00:56.747 ***** 

TASK [deluge : Stop Deluge] ***************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/deluge/tasks/main.yml:46</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:17:31 +0200 (0:00:00.578)       0:00:57.326 ***** 
Sonntag 21 September 2025  01:17:31 +0200 (0:00:00.045)       0:00:57.371 ***** 
Sonntag 21 September 2025  01:17:31 +0200 (0:00:00.054)       0:00:57.426 ***** 

TASK [dokuwiki : Stop Dokuwiki] ***********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/dokuwiki/tasks/main.yml:37</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:17:31 +0200 (0:00:00.596)       0:00:58.022 ***** 
Sonntag 21 September 2025  01:17:31 +0200 (0:00:00.038)       0:00:58.061 ***** 
Sonntag 21 September 2025  01:17:31 +0200 (0:00:00.047)       0:00:58.109 ***** 
Sonntag 21 September 2025  01:17:31 +0200 (0:00:00.048)       0:00:58.157 ***** 
Sonntag 21 September 2025  01:17:31 +0200 (0:00:00.041)       0:00:58.198 ***** 
Sonntag 21 September 2025  01:17:32 +0200 (0:00:00.057)       0:00:58.256 ***** 
Sonntag 21 September 2025  01:17:32 +0200 (0:00:00.048)       0:00:58.304 ***** 

TASK [drone-ci : Stop Drone-CI] ***********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/drone-ci/tasks/main.yml:79</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:17:32 +0200 (0:00:00.577)       0:00:58.881 ***** 

TASK [drone-ci : Stop Drone-CI Runner] ****************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/drone-ci/tasks/main.yml:84</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:17:33 +0200 (0:00:00.610)       0:00:59.492 ***** 
Sonntag 21 September 2025  01:17:33 +0200 (0:00:00.068)       0:00:59.560 ***** 
Sonntag 21 September 2025  01:17:33 +0200 (0:00:00.040)       0:00:59.601 ***** 

TASK [duplicacy : Stop Duplicacy] *********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/duplicacy/tasks/main.yml:44</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:17:33 +0200 (0:00:00.591)       0:01:00.192 ***** 
Sonntag 21 September 2025  01:17:34 +0200 (0:00:00.133)       0:01:00.326 ***** 
Sonntag 21 September 2025  01:17:34 +0200 (0:00:00.046)       0:01:00.372 ***** 

TASK [duplicati : Stop Duplicati] *********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/duplicati/tasks/main.yml:40</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:17:34 +0200 (0:00:00.596)       0:01:00.968 ***** 
Sonntag 21 September 2025  01:17:34 +0200 (0:00:00.046)       0:01:01.015 ***** 
Sonntag 21 September 2025  01:17:34 +0200 (0:00:00.063)       0:01:01.079 ***** 

TASK [emby : Stop Emby] *******************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/emby/tasks/main.yml:41</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:17:35 +0200 (0:00:00.580)       0:01:01.659 ***** 
Sonntag 21 September 2025  01:17:35 +0200 (0:00:00.047)       0:01:01.707 ***** 
Sonntag 21 September 2025  01:17:35 +0200 (0:00:00.054)       0:01:01.761 ***** 

TASK [esphome : Stop EspHome] *************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/esphome/tasks/main.yml:38</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:17:36 +0200 (0:00:00.581)       0:01:02.342 ***** 
Sonntag 21 September 2025  01:17:36 +0200 (0:00:00.069)       0:01:02.411 ***** 
Sonntag 21 September 2025  01:17:36 +0200 (0:00:00.063)       0:01:02.475 ***** 
Sonntag 21 September 2025  01:17:36 +0200 (0:00:00.052)       0:01:02.527 ***** 
Sonntag 21 September 2025  01:17:36 +0200 (0:00:00.052)       0:01:02.580 ***** 

TASK [firefly : Stop Firefly] *************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/firefly/tasks/main.yml:68</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:17:36 +0200 (0:00:00.581)       0:01:03.161 ***** 

TASK [firefly : Stop Firefly MySQL] *******************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/firefly/tasks/main.yml:73</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:17:37 +0200 (0:00:00.595)       0:01:03.757 ***** 
Sonntag 21 September 2025  01:17:37 +0200 (0:00:00.073)       0:01:03.830 ***** 
Sonntag 21 September 2025  01:17:37 +0200 (0:00:00.046)       0:01:03.876 ***** 

TASK [flaresolverr : Stop FlareSolverr] ***************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/flaresolverr/tasks/main.yml:35</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:17:38 +0200 (0:00:00.611)       0:01:04.488 ***** 
Sonntag 21 September 2025  01:17:38 +0200 (0:00:00.065)       0:01:04.554 ***** 
Sonntag 21 September 2025  01:17:38 +0200 (0:00:00.045)       0:01:04.600 ***** 

TASK [freshrss : Stop FreshRSS] ***********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/freshrss/tasks/main.yml:38</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:17:39 +0200 (0:00:00.694)       0:01:05.295 ***** 
Sonntag 21 September 2025  01:17:39 +0200 (0:00:00.054)       0:01:05.349 ***** 
Sonntag 21 September 2025  01:17:39 +0200 (0:00:00.054)       0:01:05.404 ***** 

TASK [get_iplayer : Stop get_iplayer] *****************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/get_iplayer/tasks/main.yml:28</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:17:39 +0200 (0:00:00.603)       0:01:06.008 ***** 
Sonntag 21 September 2025  01:17:39 +0200 (0:00:00.053)       0:01:06.061 ***** 
Sonntag 21 September 2025  01:17:39 +0200 (0:00:00.047)       0:01:06.109 ***** 
Sonntag 21 September 2025  01:17:39 +0200 (0:00:00.047)       0:01:06.157 ***** 

TASK [gitea : Stop Gitea] *****************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/gitea/tasks/main.yml:65</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:17:40 +0200 (0:00:00.571)       0:01:06.729 ***** 

TASK [gitea : Stop Gitea Mysql] ***********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/gitea/tasks/main.yml:70</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:17:41 +0200 (0:00:00.629)       0:01:07.359 ***** 
Sonntag 21 September 2025  01:17:41 +0200 (0:00:00.051)       0:01:07.410 ***** 
Sonntag 21 September 2025  01:17:41 +0200 (0:00:00.040)       0:01:07.451 ***** 
Sonntag 21 September 2025  01:17:41 +0200 (0:00:00.063)       0:01:07.514 ***** 
Sonntag 21 September 2025  01:17:41 +0200 (0:00:00.059)       0:01:07.573 ***** 

TASK [gitlab : Stop Gitlab] ***************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/gitlab/tasks/main.yml:64</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:17:41 +0200 (0:00:00.584)       0:01:08.157 ***** 
Sonntag 21 September 2025  01:17:41 +0200 (0:00:00.042)       0:01:08.200 ***** 

TASK [glances : Stop Glances] *************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/glances/tasks/main.yml:32</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:17:42 +0200 (0:00:00.590)       0:01:08.790 ***** 
Sonntag 21 September 2025  01:17:42 +0200 (0:00:00.054)       0:01:08.844 ***** 
Sonntag 21 September 2025  01:17:42 +0200 (0:00:00.042)       0:01:08.887 ***** 

TASK [gotify : Stop Gotify] ***************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/gotify/tasks/main.yml:38</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:17:43 +0200 (0:00:00.642)       0:01:09.530 ***** 
Sonntag 21 September 2025  01:17:43 +0200 (0:00:00.061)       0:01:09.592 ***** 
Sonntag 21 September 2025  01:17:43 +0200 (0:00:00.131)       0:01:09.724 ***** 
Sonntag 21 September 2025  01:17:43 +0200 (0:00:00.042)       0:01:09.766 ***** 
Sonntag 21 September 2025  01:17:43 +0200 (0:00:00.056)       0:01:09.823 ***** 
Sonntag 21 September 2025  01:17:43 +0200 (0:00:00.042)       0:01:09.865 ***** 
Sonntag 21 September 2025  01:17:43 +0200 (0:00:00.046)       0:01:09.911 ***** 

TASK [guacamole : Stop Guacamole] *********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/guacamole/tasks/main.yml:59</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:17:44 +0200 (0:00:00.578)       0:01:10.490 ***** 
Sonntag 21 September 2025  01:17:44 +0200 (0:00:00.056)       0:01:10.546 ***** 

TASK [healthchecks.io : Remove healthchecks.io cronjob] ***********************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/healthchecks.io/tasks/main.yml:14</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;envs&quot;: [],</span>
<span style="color:#00AA00">    &quot;jobs&quot;: []</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:17:44 +0200 (0:00:00.589)       0:01:11.136 ***** 
Sonntag 21 September 2025  01:17:44 +0200 (0:00:00.045)       0:01:11.181 ***** 
Sonntag 21 September 2025  01:17:45 +0200 (0:00:00.047)       0:01:11.229 ***** 

TASK [heimdall : Stop Heimdall] ***********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/heimdall/tasks/main.yml:36</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:17:45 +0200 (0:00:00.595)       0:01:11.824 ***** 
Sonntag 21 September 2025  01:17:45 +0200 (0:00:00.049)       0:01:11.874 ***** 
Sonntag 21 September 2025  01:17:45 +0200 (0:00:00.044)       0:01:11.919 ***** 

TASK [hello_world : Stop Hello World] *****************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/hello_world/tasks/main.yml:33</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:17:46 +0200 (0:00:00.579)       0:01:12.498 ***** 
Sonntag 21 September 2025  01:17:46 +0200 (0:00:00.054)       0:01:12.552 ***** 
Sonntag 21 September 2025  01:17:46 +0200 (0:00:00.048)       0:01:12.600 ***** 

TASK [homeassistant : Stop homeassistant] *************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/homeassistant/tasks/main.yml:34</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:17:46 +0200 (0:00:00.581)       0:01:13.182 ***** 
Sonntag 21 September 2025  01:17:47 +0200 (0:00:00.046)       0:01:13.229 ***** 
Sonntag 21 September 2025  01:17:47 +0200 (0:00:00.049)       0:01:13.278 ***** 

TASK [homebridge : Stop Homebridge] *******************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/homebridge/tasks/main.yml:39</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:17:47 +0200 (0:00:00.587)       0:01:13.866 ***** 

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
Sonntag 21 September 2025  01:17:48 +0200 (0:00:00.449)       0:01:14.315 ***** 

TASK [homepage : Template config files] ***************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/homepage/tasks/main.yml:11</b></span>
<span style="color:#AA5500">changed: [ansible-nas] =&gt; (item=bookmarks.yaml) =&gt; {</span>
<span style="color:#AA5500">    &quot;ansible_loop_var&quot;: &quot;item&quot;,</span>
<span style="color:#AA5500">    &quot;changed&quot;: true,</span>
<span style="color:#AA5500">    &quot;checksum&quot;: &quot;a2783fdfb95c4d6e0f77924c506c26b968ae6dc6&quot;,</span>
<span style="color:#AA5500">    &quot;dest&quot;: &quot;/mnt/Volume1/docker/homepage/bookmarks.yaml&quot;,</span>
<span style="color:#AA5500">    &quot;gid&quot;: 0,</span>
<span style="color:#AA5500">    &quot;group&quot;: &quot;root&quot;,</span>
<span style="color:#AA5500">    &quot;item&quot;: &quot;bookmarks.yaml&quot;,</span>
<span style="color:#AA5500">    &quot;md5sum&quot;: &quot;eead3de3d8ef96379652275209c5610a&quot;,</span>
<span style="color:#AA5500">    &quot;mode&quot;: &quot;0777&quot;,</span>
<span style="color:#AA5500">    &quot;owner&quot;: &quot;root&quot;,</span>
<span style="color:#AA5500">    &quot;size&quot;: 527,</span>
<span style="color:#AA5500">    &quot;src&quot;: &quot;/home/dietmar/.ansible/tmp/ansible-tmp-1758410268.1596546-40768-278472229691602/source&quot;,</span>
<span style="color:#AA5500">    &quot;state&quot;: &quot;file&quot;,</span>
<span style="color:#AA5500">    &quot;uid&quot;: 0</span>
<span style="color:#AA5500">}</span>
<span style="color:#AA5500">changed: [ansible-nas] =&gt; (item=docker.yaml) =&gt; {</span>
<span style="color:#AA5500">    &quot;ansible_loop_var&quot;: &quot;item&quot;,</span>
<span style="color:#AA5500">    &quot;changed&quot;: true,</span>
<span style="color:#AA5500">    &quot;checksum&quot;: &quot;c9c9f5d43dab59e638c885b21bba46d28f5c0509&quot;,</span>
<span style="color:#AA5500">    &quot;dest&quot;: &quot;/mnt/Volume1/docker/homepage/docker.yaml&quot;,</span>
<span style="color:#AA5500">    &quot;gid&quot;: 0,</span>
<span style="color:#AA5500">    &quot;group&quot;: &quot;root&quot;,</span>
<span style="color:#AA5500">    &quot;item&quot;: &quot;docker.yaml&quot;,</span>
<span style="color:#AA5500">    &quot;md5sum&quot;: &quot;76fb8ae78268d0ef057a633d5479d266&quot;,</span>
<span style="color:#AA5500">    &quot;mode&quot;: &quot;0777&quot;,</span>
<span style="color:#AA5500">    &quot;owner&quot;: &quot;root&quot;,</span>
<span style="color:#AA5500">    &quot;size&quot;: 45,</span>
<span style="color:#AA5500">    &quot;src&quot;: &quot;/home/dietmar/.ansible/tmp/ansible-tmp-1758410268.8536518-40768-257766301075153/source&quot;,</span>
<span style="color:#AA5500">    &quot;state&quot;: &quot;file&quot;,</span>
<span style="color:#AA5500">    &quot;uid&quot;: 0</span>
<span style="color:#AA5500">}</span>
<span style="color:#AA5500">changed: [ansible-nas] =&gt; (item=settings.yaml) =&gt; {</span>
<span style="color:#AA5500">    &quot;ansible_loop_var&quot;: &quot;item&quot;,</span>
<span style="color:#AA5500">    &quot;changed&quot;: true,</span>
<span style="color:#AA5500">    &quot;checksum&quot;: &quot;12ad15433ee55e9f49b4346cb3d5765ecac6dd08&quot;,</span>
<span style="color:#AA5500">    &quot;dest&quot;: &quot;/mnt/Volume1/docker/homepage/settings.yaml&quot;,</span>
<span style="color:#AA5500">    &quot;gid&quot;: 0,</span>
<span style="color:#AA5500">    &quot;group&quot;: &quot;root&quot;,</span>
<span style="color:#AA5500">    &quot;item&quot;: &quot;settings.yaml&quot;,</span>
<span style="color:#AA5500">    &quot;md5sum&quot;: &quot;e296ee9fde92b3a6b6ac061820783b71&quot;,</span>
<span style="color:#AA5500">    &quot;mode&quot;: &quot;0777&quot;,</span>
<span style="color:#AA5500">    &quot;owner&quot;: &quot;root&quot;,</span>
<span style="color:#AA5500">    &quot;size&quot;: 64,</span>
<span style="color:#AA5500">    &quot;src&quot;: &quot;/home/dietmar/.ansible/tmp/ansible-tmp-1758410269.4486747-40768-76921977859853/source&quot;,</span>
<span style="color:#AA5500">    &quot;state&quot;: &quot;file&quot;,</span>
<span style="color:#AA5500">    &quot;uid&quot;: 0</span>
<span style="color:#AA5500">}</span>
<span style="color:#AA5500">changed: [ansible-nas] =&gt; (item=services.yaml) =&gt; {</span>
<span style="color:#AA5500">    &quot;ansible_loop_var&quot;: &quot;item&quot;,</span>
<span style="color:#AA5500">    &quot;changed&quot;: true,</span>
<span style="color:#AA5500">    &quot;checksum&quot;: &quot;701d82d2ab4f38f259110d140d1c66bfdd9ef2ba&quot;,</span>
<span style="color:#AA5500">    &quot;dest&quot;: &quot;/mnt/Volume1/docker/homepage/services.yaml&quot;,</span>
<span style="color:#AA5500">    &quot;gid&quot;: 0,</span>
<span style="color:#AA5500">    &quot;group&quot;: &quot;root&quot;,</span>
<span style="color:#AA5500">    &quot;item&quot;: &quot;services.yaml&quot;,</span>
<span style="color:#AA5500">    &quot;md5sum&quot;: &quot;0985e58bf8c899f4f81d89715ad15595&quot;,</span>
<span style="color:#AA5500">    &quot;mode&quot;: &quot;0777&quot;,</span>
<span style="color:#AA5500">    &quot;owner&quot;: &quot;root&quot;,</span>
<span style="color:#AA5500">    &quot;size&quot;: 141,</span>
<span style="color:#AA5500">    &quot;src&quot;: &quot;/home/dietmar/.ansible/tmp/ansible-tmp-1758410270.0361912-40768-239021321124491/source&quot;,</span>
<span style="color:#AA5500">    &quot;state&quot;: &quot;file&quot;,</span>
<span style="color:#AA5500">    &quot;uid&quot;: 0</span>
<span style="color:#AA5500">}</span>
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
Sonntag 21 September 2025  01:17:51 +0200 (0:00:03.093)       0:01:17.409 ***** 

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
<span style="color:#AA5500">                &quot;Log&quot;: [],</span>
<span style="color:#AA5500">                &quot;Status&quot;: &quot;starting&quot;</span>
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
Sonntag 21 September 2025  01:18:05 +0200 (0:00:14.395)       0:01:31.805 ***** 
Sonntag 21 September 2025  01:18:05 +0200 (0:00:00.064)       0:01:31.869 ***** 
Sonntag 21 September 2025  01:18:05 +0200 (0:00:00.058)       0:01:31.928 ***** 
Sonntag 21 September 2025  01:18:05 +0200 (0:00:00.049)       0:01:31.978 ***** 

TASK [ispyagentdvr : Stop iSpyAgentDVR] ***************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/ispyagentdvr/tasks/main.yml:50</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:18:06 +0200 (0:00:00.734)       0:01:32.712 ***** 
Sonntag 21 September 2025  01:18:06 +0200 (0:00:00.059)       0:01:32.772 ***** 
Sonntag 21 September 2025  01:18:06 +0200 (0:00:00.039)       0:01:32.811 ***** 

TASK [jackett : Stop Jackett] *************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/jackett/tasks/main.yml:41</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:18:07 +0200 (0:00:00.668)       0:01:33.480 ***** 
Sonntag 21 September 2025  01:18:07 +0200 (0:00:00.048)       0:01:33.529 ***** 
Sonntag 21 September 2025  01:18:07 +0200 (0:00:00.050)       0:01:33.579 ***** 

TASK [jellyfin : Stop jellyfin] ***********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/jellyfin/tasks/main.yml:52</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:18:07 +0200 (0:00:00.635)       0:01:34.214 ***** 
Sonntag 21 September 2025  01:18:08 +0200 (0:00:00.055)       0:01:34.270 ***** 
Sonntag 21 September 2025  01:18:08 +0200 (0:00:00.044)       0:01:34.315 ***** 
Sonntag 21 September 2025  01:18:08 +0200 (0:00:00.050)       0:01:34.365 ***** 
Sonntag 21 September 2025  01:18:08 +0200 (0:00:00.048)       0:01:34.413 ***** 

TASK [joomla : Stop Joomla] ***************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/joomla/tasks/main.yml:62</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:18:08 +0200 (0:00:00.578)       0:01:34.992 ***** 

TASK [joomla : Stop Joomla DB] ************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/joomla/tasks/main.yml:66</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:18:09 +0200 (0:00:00.576)       0:01:35.568 ***** 
Sonntag 21 September 2025  01:18:09 +0200 (0:00:00.054)       0:01:35.623 ***** 
Sonntag 21 September 2025  01:18:09 +0200 (0:00:00.130)       0:01:35.753 ***** 

TASK [komga : Stop Komga] *****************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/komga/tasks/main.yml:42</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:18:10 +0200 (0:00:00.596)       0:01:36.350 ***** 
Sonntag 21 September 2025  01:18:10 +0200 (0:00:00.052)       0:01:36.403 ***** 
Sonntag 21 September 2025  01:18:10 +0200 (0:00:00.043)       0:01:36.447 ***** 

TASK [krusader : Stop Krusader] ***********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/krusader/tasks/main.yml:43</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:18:10 +0200 (0:00:00.631)       0:01:37.078 ***** 
Sonntag 21 September 2025  01:18:10 +0200 (0:00:00.045)       0:01:37.123 ***** 
Sonntag 21 September 2025  01:18:10 +0200 (0:00:00.049)       0:01:37.173 ***** 

TASK [lidarr : Stop Lidarr] ***************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/lidarr/tasks/main.yml:37</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:18:11 +0200 (0:00:00.616)       0:01:37.790 ***** 
Sonntag 21 September 2025  01:18:11 +0200 (0:00:00.049)       0:01:37.840 ***** 
Sonntag 21 September 2025  01:18:11 +0200 (0:00:00.051)       0:01:37.891 ***** 
Sonntag 21 September 2025  01:18:11 +0200 (0:00:00.050)       0:01:37.942 ***** 
Sonntag 21 September 2025  01:18:11 +0200 (0:00:00.051)       0:01:37.994 ***** 
Sonntag 21 September 2025  01:18:11 +0200 (0:00:00.051)       0:01:38.045 ***** 
Sonntag 21 September 2025  01:18:11 +0200 (0:00:00.047)       0:01:38.093 ***** 
Sonntag 21 September 2025  01:18:11 +0200 (0:00:00.054)       0:01:38.147 ***** 
Sonntag 21 September 2025  01:18:11 +0200 (0:00:00.040)       0:01:38.188 ***** 

TASK [loki : Stop loki] *******************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/loki/tasks/main.yml:74</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:18:12 +0200 (0:00:00.657)       0:01:38.845 ***** 
Sonntag 21 September 2025  01:18:12 +0200 (0:00:00.055)       0:01:38.901 ***** 
Sonntag 21 September 2025  01:18:12 +0200 (0:00:00.045)       0:01:38.946 ***** 

TASK [mealie : Stop Mealie] ***************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/mealie/tasks/main.yml:44</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:18:13 +0200 (0:00:00.593)       0:01:39.540 ***** 
Sonntag 21 September 2025  01:18:13 +0200 (0:00:00.053)       0:01:39.593 ***** 
Sonntag 21 September 2025  01:18:13 +0200 (0:00:00.130)       0:01:39.724 ***** 

TASK [minecraft-bedrock-server : Stop Minecraft Bedrock Server] ***************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/minecraft-bedrock-server/tasks/main.yml:34</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:18:14 +0200 (0:00:00.577)       0:01:40.301 ***** 
Sonntag 21 September 2025  01:18:14 +0200 (0:00:00.087)       0:01:40.389 ***** 
Sonntag 21 September 2025  01:18:14 +0200 (0:00:00.047)       0:01:40.437 ***** 

TASK [minecraft-server : Stop Minecraft Server] *******************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/minecraft-server/tasks/main.yml:27</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:18:14 +0200 (0:00:00.586)       0:01:41.024 ***** 
Sonntag 21 September 2025  01:18:14 +0200 (0:00:00.051)       0:01:41.075 ***** 

TASK [minidlna : Stop MiniDLNA] ***********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/minidlna/tasks/main.yml:24</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:18:15 +0200 (0:00:00.580)       0:01:41.655 ***** 
Sonntag 21 September 2025  01:18:15 +0200 (0:00:00.048)       0:01:41.704 ***** 
Sonntag 21 September 2025  01:18:15 +0200 (0:00:00.049)       0:01:41.754 ***** 
Sonntag 21 September 2025  01:18:15 +0200 (0:00:00.048)       0:01:41.802 ***** 
Sonntag 21 September 2025  01:18:15 +0200 (0:00:00.040)       0:01:41.843 ***** 

TASK [miniflux : Stop Miniflux] ***********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/miniflux/tasks/main.yml:60</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:18:16 +0200 (0:00:00.606)       0:01:42.449 ***** 
Sonntag 21 September 2025  01:18:16 +0200 (0:00:00.052)       0:01:42.502 ***** 
Sonntag 21 September 2025  01:18:16 +0200 (0:00:00.048)       0:01:42.551 ***** 

TASK [minio : Stop minio] *****************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/minio/tasks/main.yml:40</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:18:16 +0200 (0:00:00.613)       0:01:43.164 ***** 
Sonntag 21 September 2025  01:18:17 +0200 (0:00:00.071)       0:01:43.235 ***** 
Sonntag 21 September 2025  01:18:17 +0200 (0:00:00.047)       0:01:43.282 ***** 
Sonntag 21 September 2025  01:18:17 +0200 (0:00:00.043)       0:01:43.325 ***** 

TASK [mosquitto : Stop Mosquitto] *********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/mosquitto/tasks/main.yml:38</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:18:17 +0200 (0:00:00.636)       0:01:43.962 ***** 
Sonntag 21 September 2025  01:18:17 +0200 (0:00:00.056)       0:01:44.019 ***** 
Sonntag 21 September 2025  01:18:18 +0200 (0:00:00.250)       0:01:44.269 ***** 

TASK [mumble : Stop Mumble] ***************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/mumble/tasks/main.yml:39</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:18:18 +0200 (0:00:00.603)       0:01:44.873 ***** 
Sonntag 21 September 2025  01:18:18 +0200 (0:00:00.056)       0:01:44.930 ***** 
Sonntag 21 September 2025  01:18:18 +0200 (0:00:00.058)       0:01:44.988 ***** 

TASK [mylar : Stop Mylar] *****************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/mylar/tasks/main.yml:41</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:18:19 +0200 (0:00:00.595)       0:01:45.583 ***** 
Sonntag 21 September 2025  01:18:19 +0200 (0:00:00.057)       0:01:45.641 ***** 
Sonntag 21 September 2025  01:18:19 +0200 (0:00:00.042)       0:01:45.684 ***** 

TASK [mymediaforalexa : Stop Mymediaforalexa] *********************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/mymediaforalexa/tasks/main.yml:27</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:18:20 +0200 (0:00:00.600)       0:01:46.284 ***** 
Sonntag 21 September 2025  01:18:20 +0200 (0:00:00.055)       0:01:46.340 ***** 
Sonntag 21 September 2025  01:18:20 +0200 (0:00:00.047)       0:01:46.388 ***** 

TASK [n8n : Stop n8n] *********************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/n8n/tasks/main.yml:40</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:18:20 +0200 (0:00:00.638)       0:01:47.026 ***** 
Sonntag 21 September 2025  01:18:20 +0200 (0:00:00.055)       0:01:47.082 ***** 
Sonntag 21 September 2025  01:18:20 +0200 (0:00:00.043)       0:01:47.126 ***** 

TASK [navidrome : Stop Navidrome] *********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/navidrome/tasks/main.yml:42</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:18:21 +0200 (0:00:00.582)       0:01:47.708 ***** 
Sonntag 21 September 2025  01:18:21 +0200 (0:00:00.054)       0:01:47.763 ***** 
Sonntag 21 September 2025  01:18:21 +0200 (0:00:00.046)       0:01:47.809 ***** 

TASK [netbootxyz : Stop Netbootxyz] *******************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/netbootxyz/tasks/main.yml:41</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:18:22 +0200 (0:00:00.636)       0:01:48.446 ***** 
Sonntag 21 September 2025  01:18:22 +0200 (0:00:00.052)       0:01:48.499 ***** 
Sonntag 21 September 2025  01:18:22 +0200 (0:00:00.077)       0:01:48.576 ***** 

TASK [netdata : Stop Netdata] *************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/netdata/tasks/main.yml:41</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:18:23 +0200 (0:00:00.850)       0:01:49.427 ***** 
Sonntag 21 September 2025  01:18:23 +0200 (0:00:00.061)       0:01:49.488 ***** 
Sonntag 21 September 2025  01:18:23 +0200 (0:00:00.053)       0:01:49.542 ***** 
Sonntag 21 September 2025  01:18:23 +0200 (0:00:00.075)       0:01:49.617 ***** 
Sonntag 21 September 2025  01:18:23 +0200 (0:00:00.055)       0:01:49.673 ***** 

TASK [nextcloud : Stop Nextcloud] *********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/nextcloud/tasks/main.yml:72</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:18:24 +0200 (0:00:00.578)       0:01:50.251 ***** 

TASK [nextcloud : Stop Nextcloud DB] ******************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/nextcloud/tasks/main.yml:76</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:18:24 +0200 (0:00:00.598)       0:01:50.850 ***** 
Sonntag 21 September 2025  01:18:24 +0200 (0:00:00.055)       0:01:50.905 ***** 
Sonntag 21 September 2025  01:18:24 +0200 (0:00:00.047)       0:01:50.953 ***** 
Sonntag 21 September 2025  01:18:24 +0200 (0:00:00.053)       0:01:51.006 ***** 
Sonntag 21 September 2025  01:18:24 +0200 (0:00:00.045)       0:01:51.052 ***** 
Sonntag 21 September 2025  01:18:24 +0200 (0:00:00.045)       0:01:51.097 ***** 

TASK [nomad : Check if Nomad is installed] ************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/nomad/tasks/main.yml:37</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;stat&quot;: {</span>
<span style="color:#00AA00">        &quot;exists&quot;: false</span>
<span style="color:#00AA00">    }</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:18:25 +0200 (0:00:00.378)       0:01:51.475 ***** 
Sonntag 21 September 2025  01:18:25 +0200 (0:00:00.049)       0:01:51.525 ***** 
Sonntag 21 September 2025  01:18:25 +0200 (0:00:00.070)       0:01:51.596 ***** 
Sonntag 21 September 2025  01:18:25 +0200 (0:00:00.073)       0:01:51.670 ***** 
Sonntag 21 September 2025  01:18:25 +0200 (0:00:00.072)       0:01:51.743 ***** 

TASK [nzbget : Stop NZBget] ***************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/nzbget/tasks/main.yml:38</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:18:26 +0200 (0:00:00.592)       0:01:52.335 ***** 
Sonntag 21 September 2025  01:18:26 +0200 (0:00:00.055)       0:01:52.391 ***** 
Sonntag 21 September 2025  01:18:26 +0200 (0:00:00.052)       0:01:52.443 ***** 

TASK [octoprint : Stop Octoprint] *********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/octoprint/tasks/main.yml:40</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:18:26 +0200 (0:00:00.682)       0:01:53.126 ***** 
Sonntag 21 September 2025  01:18:26 +0200 (0:00:00.049)       0:01:53.175 ***** 
Sonntag 21 September 2025  01:18:27 +0200 (0:00:00.044)       0:01:53.220 ***** 

TASK [ombi : Stop Ombi] *******************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/ombi/tasks/main.yml:35</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:18:27 +0200 (0:00:00.621)       0:01:53.841 ***** 
Sonntag 21 September 2025  01:18:27 +0200 (0:00:00.046)       0:01:53.887 ***** 
Sonntag 21 September 2025  01:18:27 +0200 (0:00:00.051)       0:01:53.939 ***** 
Sonntag 21 September 2025  01:18:27 +0200 (0:00:00.088)       0:01:54.028 ***** 
Sonntag 21 September 2025  01:18:27 +0200 (0:00:00.048)       0:01:54.077 ***** 

TASK [openhab : Stop openHAB] *************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/openhab/tasks/main.yml:60</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:18:28 +0200 (0:00:00.621)       0:01:54.699 ***** 
Sonntag 21 September 2025  01:18:28 +0200 (0:00:00.052)       0:01:54.751 ***** 
Sonntag 21 September 2025  01:18:28 +0200 (0:00:00.078)       0:01:54.829 ***** 

TASK [organizr : Stop Organizr] ***********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/organizr/tasks/main.yml:38</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:18:29 +0200 (0:00:00.595)       0:01:55.425 ***** 
Sonntag 21 September 2025  01:18:29 +0200 (0:00:00.061)       0:01:55.487 ***** 
Sonntag 21 September 2025  01:18:29 +0200 (0:00:00.049)       0:01:55.536 ***** 

TASK [overseerr : Stop Overseerr] *********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/overseerr/tasks/main.yml:43</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:18:29 +0200 (0:00:00.589)       0:01:56.126 ***** 
Sonntag 21 September 2025  01:18:29 +0200 (0:00:00.088)       0:01:56.214 ***** 
Sonntag 21 September 2025  01:18:30 +0200 (0:00:00.045)       0:01:56.260 ***** 
Sonntag 21 September 2025  01:18:30 +0200 (0:00:00.047)       0:01:56.308 ***** 
Sonntag 21 September 2025  01:18:30 +0200 (0:00:00.050)       0:01:56.359 ***** 
Sonntag 21 September 2025  01:18:30 +0200 (0:00:00.053)       0:01:56.412 ***** 

TASK [paperless_ng : Stop paperless_ng] ***************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/paperless_ng/tasks/main.yml:83</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:18:30 +0200 (0:00:00.583)       0:01:56.995 ***** 

TASK [paperless_ng : Stop paperless_ng redis] *********************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/paperless_ng/tasks/main.yml:87</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:18:31 +0200 (0:00:00.576)       0:01:57.571 ***** 

TASK [paperless_ng : Stop paperless_ng db] ************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/paperless_ng/tasks/main.yml:91</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:18:32 +0200 (0:00:00.687)       0:01:58.259 ***** 
Sonntag 21 September 2025  01:18:32 +0200 (0:00:00.068)       0:01:58.328 ***** 
Sonntag 21 September 2025  01:18:32 +0200 (0:00:00.056)       0:01:58.384 ***** 
Sonntag 21 September 2025  01:18:32 +0200 (0:00:00.047)       0:01:58.432 ***** 
Sonntag 21 September 2025  01:18:32 +0200 (0:00:00.052)       0:01:58.484 ***** 

TASK [piwigo : Stop Piwigo] ***************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/piwigo/tasks/main.yml:71</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:18:32 +0200 (0:00:00.577)       0:01:59.061 ***** 

TASK [piwigo : Stop Piwigo Db] ************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/piwigo/tasks/main.yml:75</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:18:33 +0200 (0:00:00.655)       0:01:59.717 ***** 
Sonntag 21 September 2025  01:18:33 +0200 (0:00:00.068)       0:01:59.786 ***** 
Sonntag 21 September 2025  01:18:33 +0200 (0:00:00.053)       0:01:59.839 ***** 

TASK [plex : Stop Plex] *******************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/plex/tasks/main.yml:51</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:18:34 +0200 (0:00:00.606)       0:02:00.446 ***** 
Sonntag 21 September 2025  01:18:34 +0200 (0:00:00.045)       0:02:00.491 ***** 
Sonntag 21 September 2025  01:18:34 +0200 (0:00:00.058)       0:02:00.550 ***** 
Sonntag 21 September 2025  01:18:34 +0200 (0:00:00.048)       0:02:00.598 ***** 

TASK [portainer : Stop Portainer] *********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/portainer/tasks/main.yml:49</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:18:34 +0200 (0:00:00.594)       0:02:01.192 ***** 
Sonntag 21 September 2025  01:18:35 +0200 (0:00:00.053)       0:02:01.246 ***** 
Sonntag 21 September 2025  01:18:35 +0200 (0:00:00.055)       0:02:01.302 ***** 

TASK [prowlarr : Stop Prowlarr] ***********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/prowlarr/tasks/main.yml:43</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:18:35 +0200 (0:00:00.605)       0:02:01.907 ***** 
Sonntag 21 September 2025  01:18:35 +0200 (0:00:00.070)       0:02:01.978 ***** 
Sonntag 21 September 2025  01:18:35 +0200 (0:00:00.053)       0:02:02.031 ***** 
Sonntag 21 September 2025  01:18:35 +0200 (0:00:00.061)       0:02:02.093 ***** 
Sonntag 21 September 2025  01:18:35 +0200 (0:00:00.047)       0:02:02.140 ***** 
Sonntag 21 September 2025  01:18:36 +0200 (0:00:00.142)       0:02:02.283 ***** 

TASK [promtail : Stop promtail] ***********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/promtail/tasks/main.yml:50</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:18:36 +0200 (0:00:00.590)       0:02:02.873 ***** 
Sonntag 21 September 2025  01:18:36 +0200 (0:00:00.083)       0:02:02.956 ***** 
Sonntag 21 September 2025  01:18:36 +0200 (0:00:00.071)       0:02:03.028 ***** 

TASK [pyload : Stop pyLoad] ***************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/pyload/tasks/main.yml:45</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:18:37 +0200 (0:00:00.590)       0:02:03.618 ***** 
Sonntag 21 September 2025  01:18:37 +0200 (0:00:00.062)       0:02:03.681 ***** 
Sonntag 21 September 2025  01:18:37 +0200 (0:00:00.045)       0:02:03.726 ***** 

TASK [pytivo : Stop Pytivo] ***************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/pytivo/tasks/main.yml:45</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:18:38 +0200 (0:00:00.585)       0:02:04.312 ***** 
Sonntag 21 September 2025  01:18:38 +0200 (0:00:00.052)       0:02:04.365 ***** 
Sonntag 21 September 2025  01:18:38 +0200 (0:00:00.063)       0:02:04.428 ***** 

TASK [radarr : Stop Radarr] ***************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/radarr/tasks/main.yml:44</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:18:38 +0200 (0:00:00.652)       0:02:05.080 ***** 
Sonntag 21 September 2025  01:18:38 +0200 (0:00:00.069)       0:02:05.150 ***** 
Sonntag 21 September 2025  01:18:38 +0200 (0:00:00.049)       0:02:05.199 ***** 
Sonntag 21 September 2025  01:18:39 +0200 (0:00:00.050)       0:02:05.250 ***** 
Sonntag 21 September 2025  01:18:39 +0200 (0:00:00.052)       0:02:05.302 ***** 

TASK [romm : Stop Romm] *******************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/romm/tasks/main.yml:84</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:18:39 +0200 (0:00:00.580)       0:02:05.882 ***** 

TASK [romm : Stop Romm DB] ****************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/romm/tasks/main.yml:89</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:18:40 +0200 (0:00:00.628)       0:02:06.510 ***** 
Sonntag 21 September 2025  01:18:40 +0200 (0:00:00.049)       0:02:06.559 ***** 
Sonntag 21 September 2025  01:18:40 +0200 (0:00:00.048)       0:02:06.608 ***** 
Sonntag 21 September 2025  01:18:40 +0200 (0:00:00.052)       0:02:06.661 ***** 
Sonntag 21 September 2025  01:18:40 +0200 (0:00:00.155)       0:02:06.816 ***** 
Sonntag 21 September 2025  01:18:40 +0200 (0:00:00.051)       0:02:06.868 ***** 
Sonntag 21 September 2025  01:18:40 +0200 (0:00:00.055)       0:02:06.923 ***** 

TASK [rssbridge : Stop RSSBridge] *********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/rssbridge/tasks/main.yml:34</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:18:41 +0200 (0:00:00.626)       0:02:07.550 ***** 
Sonntag 21 September 2025  01:18:41 +0200 (0:00:00.055)       0:02:07.605 ***** 
Sonntag 21 September 2025  01:18:41 +0200 (0:00:00.051)       0:02:07.657 ***** 

TASK [sabnzbd : Stop Sabnzbd] *************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/sabnzbd/tasks/main.yml:38</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:18:42 +0200 (0:00:00.582)       0:02:08.239 ***** 
Sonntag 21 September 2025  01:18:42 +0200 (0:00:00.054)       0:02:08.293 ***** 
Sonntag 21 September 2025  01:18:42 +0200 (0:00:00.048)       0:02:08.342 ***** 

TASK [sickchill : Stop Sickchill] *********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/sickchill/tasks/main.yml:40</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:18:42 +0200 (0:00:00.605)       0:02:08.947 ***** 
Sonntag 21 September 2025  01:18:42 +0200 (0:00:00.053)       0:02:09.001 ***** 
Sonntag 21 September 2025  01:18:42 +0200 (0:00:00.077)       0:02:09.079 ***** 

TASK [silverbullet : Stop silverbullet] ***************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/silverbullet/tasks/main.yml:40</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:18:43 +0200 (0:00:00.592)       0:02:09.671 ***** 
Sonntag 21 September 2025  01:18:43 +0200 (0:00:00.055)       0:02:09.727 ***** 
Sonntag 21 September 2025  01:18:43 +0200 (0:00:00.049)       0:02:09.776 ***** 

TASK [sonarr : Stop Sonarr] ***************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/sonarr/tasks/main.yml:39</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:18:44 +0200 (0:00:00.632)       0:02:10.409 ***** 
Sonntag 21 September 2025  01:18:44 +0200 (0:00:00.058)       0:02:10.468 ***** 
Sonntag 21 September 2025  01:18:44 +0200 (0:00:00.043)       0:02:10.512 ***** 
Sonntag 21 September 2025  01:18:44 +0200 (0:00:00.053)       0:02:10.565 ***** 
Sonntag 21 September 2025  01:18:44 +0200 (0:00:00.063)       0:02:10.629 ***** 
Sonntag 21 September 2025  01:18:44 +0200 (0:00:00.261)       0:02:10.890 ***** 
Sonntag 21 September 2025  01:18:44 +0200 (0:00:00.054)       0:02:10.944 ***** 
Sonntag 21 September 2025  01:18:44 +0200 (0:00:00.047)       0:02:10.992 ***** 
Sonntag 21 September 2025  01:18:44 +0200 (0:00:00.039)       0:02:11.032 ***** 

TASK [stats : Stop Prometheus] ************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/stats/tasks/prometheus.yml:60</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:18:45 +0200 (0:00:00.599)       0:02:11.631 ***** 
Sonntag 21 September 2025  01:18:45 +0200 (0:00:00.049)       0:02:11.681 ***** 
Sonntag 21 September 2025  01:18:45 +0200 (0:00:00.051)       0:02:11.733 ***** 
Sonntag 21 September 2025  01:18:45 +0200 (0:00:00.046)       0:02:11.779 ***** 
Sonntag 21 September 2025  01:18:45 +0200 (0:00:00.043)       0:02:11.822 ***** 

TASK [stats : Stop stats_telegraf] ********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/stats/tasks/telegraf.yml:56</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:18:46 +0200 (0:00:00.583)       0:02:12.406 ***** 
Sonntag 21 September 2025  01:18:46 +0200 (0:00:00.044)       0:02:12.450 ***** 
Sonntag 21 September 2025  01:18:46 +0200 (0:00:00.056)       0:02:12.507 ***** 
Sonntag 21 September 2025  01:18:46 +0200 (0:00:00.042)       0:02:12.550 ***** 

TASK [stats : Stop Smartctl Exporter] *****************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/stats/tasks/exporters.yml:45</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:18:46 +0200 (0:00:00.564)       0:02:13.114 ***** 

TASK [stats : Stop Speedtest Exporter] ****************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/stats/tasks/exporters.yml:49</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:18:47 +0200 (0:00:00.590)       0:02:13.705 ***** 
Sonntag 21 September 2025  01:18:47 +0200 (0:00:00.072)       0:02:13.777 ***** 
Sonntag 21 September 2025  01:18:47 +0200 (0:00:00.040)       0:02:13.818 ***** 
Sonntag 21 September 2025  01:18:47 +0200 (0:00:00.047)       0:02:13.866 ***** 
Sonntag 21 September 2025  01:18:47 +0200 (0:00:00.049)       0:02:13.915 ***** 
Sonntag 21 September 2025  01:18:47 +0200 (0:00:00.043)       0:02:13.959 ***** 

TASK [stats : Stop Grafana] ***************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/stats/tasks/grafana.yml:65</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:18:48 +0200 (0:00:00.581)       0:02:14.540 ***** 
Sonntag 21 September 2025  01:18:48 +0200 (0:00:00.055)       0:02:14.595 ***** 
Sonntag 21 September 2025  01:18:48 +0200 (0:00:00.042)       0:02:14.637 ***** 

TASK [syncthing : Stop Syncthing] *********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/syncthing/tasks/main.yml:38</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:18:49 +0200 (0:00:00.734)       0:02:15.372 ***** 
Sonntag 21 September 2025  01:18:49 +0200 (0:00:00.057)       0:02:15.430 ***** 
Sonntag 21 September 2025  01:18:49 +0200 (0:00:00.047)       0:02:15.477 ***** 

TASK [tautulli : Stop Tautulli] ***********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/tautulli/tasks/main.yml:40</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:18:49 +0200 (0:00:00.577)       0:02:16.055 ***** 
Sonntag 21 September 2025  01:18:49 +0200 (0:00:00.054)       0:02:16.109 ***** 
Sonntag 21 September 2025  01:18:49 +0200 (0:00:00.048)       0:02:16.158 ***** 
Sonntag 21 September 2025  01:18:49 +0200 (0:00:00.046)       0:02:16.204 ***** 

TASK [thelounge : Stop The Lounge] ********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/thelounge/tasks/main.yml:42</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:18:50 +0200 (0:00:00.607)       0:02:16.812 ***** 
Sonntag 21 September 2025  01:18:50 +0200 (0:00:00.048)       0:02:16.860 ***** 
Sonntag 21 September 2025  01:18:50 +0200 (0:00:00.048)       0:02:16.909 ***** 

TASK [threadfin : Stop Threadfin] *********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/threadfin/tasks/main.yml:34</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:18:51 +0200 (0:00:00.610)       0:02:17.520 ***** 
Sonntag 21 September 2025  01:18:51 +0200 (0:00:00.046)       0:02:17.566 ***** 
Sonntag 21 September 2025  01:18:51 +0200 (0:00:00.041)       0:02:17.608 ***** 

TASK [tiddlywiki : Stop Tiddlywiki] *******************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/tiddlywiki/tasks/main.yml:36</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:18:51 +0200 (0:00:00.584)       0:02:18.192 ***** 
Sonntag 21 September 2025  01:18:52 +0200 (0:00:00.043)       0:02:18.236 ***** 
Sonntag 21 September 2025  01:18:52 +0200 (0:00:00.047)       0:02:18.283 ***** 
Sonntag 21 September 2025  01:18:52 +0200 (0:00:00.049)       0:02:18.333 ***** 
Sonntag 21 September 2025  01:18:52 +0200 (0:00:00.066)       0:02:18.399 ***** 

TASK [timemachine : Stop Time Machine] ****************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/timemachine/tasks/main.yml:45</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:18:52 +0200 (0:00:00.593)       0:02:18.993 ***** 
Sonntag 21 September 2025  01:18:52 +0200 (0:00:00.051)       0:02:19.045 ***** 
Sonntag 21 September 2025  01:18:52 +0200 (0:00:00.136)       0:02:19.181 ***** 
Sonntag 21 September 2025  01:18:53 +0200 (0:00:00.042)       0:02:19.223 ***** 

TASK [traefik : Stop Traefik] *************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/traefik/tasks/main.yml:44</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:18:53 +0200 (0:00:00.577)       0:02:19.801 ***** 
Sonntag 21 September 2025  01:18:53 +0200 (0:00:00.045)       0:02:19.847 ***** 
Sonntag 21 September 2025  01:18:53 +0200 (0:00:00.047)       0:02:19.894 ***** 

TASK [transmission : Stop Transmission] ***************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/transmission/tasks/main.yml:44</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:18:54 +0200 (0:00:00.608)       0:02:20.502 ***** 
Sonntag 21 September 2025  01:18:54 +0200 (0:00:00.043)       0:02:20.545 ***** 
Sonntag 21 September 2025  01:18:54 +0200 (0:00:00.050)       0:02:20.596 ***** 

TASK [transmission-with-openvpn : Stop Transmission with OpenVPM] *************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/transmission-with-openvpn/tasks/main.yml:64</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:18:54 +0200 (0:00:00.578)       0:02:21.174 ***** 
Sonntag 21 September 2025  01:18:55 +0200 (0:00:00.047)       0:02:21.222 ***** 
Sonntag 21 September 2025  01:18:55 +0200 (0:00:00.050)       0:02:21.273 ***** 

TASK [ubooquity : Stop Ubooquity] *********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/ubooquity/tasks/main.yml:42</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:18:55 +0200 (0:00:00.587)       0:02:21.860 ***** 
Sonntag 21 September 2025  01:18:55 +0200 (0:00:00.050)       0:02:21.911 ***** 
Sonntag 21 September 2025  01:18:55 +0200 (0:00:00.048)       0:02:21.959 ***** 

TASK [utorrent : Stop uTorrent] ***********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/utorrent/tasks/main.yml:46</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:18:56 +0200 (0:00:00.597)       0:02:22.557 ***** 
Sonntag 21 September 2025  01:18:56 +0200 (0:00:00.061)       0:02:22.618 ***** 
Sonntag 21 September 2025  01:18:56 +0200 (0:00:00.046)       0:02:22.665 ***** 

TASK [valheim : Stop Valheim] *************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/valheim/tasks/main.yml:44</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:18:57 +0200 (0:00:00.586)       0:02:23.252 ***** 
Sonntag 21 September 2025  01:18:57 +0200 (0:00:00.052)       0:02:23.304 ***** 
Sonntag 21 September 2025  01:18:57 +0200 (0:00:00.146)       0:02:23.450 ***** 
Sonntag 21 September 2025  01:18:57 +0200 (0:00:00.052)       0:02:23.503 ***** 

TASK [virtual_desktop : Stop Virtual Desktop] *********************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/virtual_desktop/tasks/main.yml:37</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:18:57 +0200 (0:00:00.608)       0:02:24.112 ***** 
Sonntag 21 September 2025  01:18:57 +0200 (0:00:00.059)       0:02:24.172 ***** 
Sonntag 21 September 2025  01:18:58 +0200 (0:00:00.047)       0:02:24.219 ***** 

TASK [wallabag : Stop Wallabag] ***********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/wallabag/tasks/main.yml:40</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:18:58 +0200 (0:00:00.588)       0:02:24.807 ***** 
Sonntag 21 September 2025  01:18:58 +0200 (0:00:00.039)       0:02:24.847 ***** 

TASK [watchtower : Stop Watchtower] *******************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/watchtower/tasks/main.yml:20</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:18:59 +0200 (0:00:00.607)       0:02:25.454 ***** 
Sonntag 21 September 2025  01:18:59 +0200 (0:00:00.071)       0:02:25.525 ***** 
Sonntag 21 September 2025  01:18:59 +0200 (0:00:00.054)       0:02:25.580 ***** 

TASK [wireshark : Stop Wireshark] *********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/wireshark/tasks/main.yml:39</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:18:59 +0200 (0:00:00.613)       0:02:26.194 ***** 
Sonntag 21 September 2025  01:19:00 +0200 (0:00:00.046)       0:02:26.241 ***** 
Sonntag 21 September 2025  01:19:00 +0200 (0:00:00.056)       0:02:26.297 ***** 
Sonntag 21 September 2025  01:19:00 +0200 (0:00:00.052)       0:02:26.349 ***** 
Sonntag 21 September 2025  01:19:00 +0200 (0:00:00.057)       0:02:26.407 ***** 
Sonntag 21 September 2025  01:19:00 +0200 (0:00:00.040)       0:02:26.448 ***** 
Sonntag 21 September 2025  01:19:00 +0200 (0:00:00.047)       0:02:26.495 ***** 

TASK [woodpecker-ci : Stop Woodpecker-CI] *************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/woodpecker-ci/tasks/main.yml:78</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:19:00 +0200 (0:00:00.602)       0:02:27.098 ***** 
Sonntag 21 September 2025  01:19:00 +0200 (0:00:00.049)       0:02:27.148 ***** 
Sonntag 21 September 2025  01:19:00 +0200 (0:00:00.042)       0:02:27.191 ***** 

TASK [youtubedlmaterial : Stop Youtubedlmaterial] *****************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/youtubedlmaterial/tasks/main.yml:52</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  01:19:01 +0200 (0:00:00.679)       0:02:27.870 ***** 
Sonntag 21 September 2025  01:19:01 +0200 (0:00:00.059)       0:02:27.929 ***** 
Sonntag 21 September 2025  01:19:01 +0200 (0:00:00.044)       0:02:27.974 ***** 
Sonntag 21 September 2025  01:19:01 +0200 (0:00:00.042)       0:02:28.017 ***** 

TASK [znc : Stop ZNC] *********************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/znc/tasks/main.yml:45</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>

PLAY RECAP ********************************************************************************************************************************************************************************************************
<span style="color:#AA5500">ansible-nas</span>                : <span style="color:#00AA00">ok=157 </span> <span style="color:#AA5500">changed=9   </span> unreachable=0    failed=0    <span style="color:#00AAAA">skipped=307 </span> rescued=0    ignored=0   

Sonntag 21 September 2025  01:19:02 +0200 (0:00:00.568)       0:02:28.586 ***** 
=============================================================================== 
homepage : Create Homepage Docker Container --------------------------------------------------------------------------------------------------------------------------------------------------------------- 14.40s
/media/IT/repos/github/forked/ansible-nas/roles/homepage/tasks/main.yml:23 ---------------------------------------------------------------------------------------------------------------------------------------
geerlingguy.nfs : Ensure directories to export exist ------------------------------------------------------------------------------------------------------------------------------------------------------- 5.77s
/home/dietmar/.ansible/roles/geerlingguy.nfs/tasks/main.yml:19 ---------------------------------------------------------------------------------------------------------------------------------------------------
homepage : Template config files --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 3.09s
/media/IT/repos/github/forked/ansible-nas/roles/homepage/tasks/main.yml:11 ---------------------------------------------------------------------------------------------------------------------------------------
vladgh.samba.server : Samba configuration ------------------------------------------------------------------------------------------------------------------------------------------------------------------ 2.32s
/home/dietmar/.ansible/collections/ansible_collections/vladgh/samba/roles/server/tasks/main.yml:80 ---------------------------------------------------------------------------------------------------------------
vladgh.samba.server : Install Samba packages --------------------------------------------------------------------------------------------------------------------------------------------------------------- 2.24s
/home/dietmar/.ansible/collections/ansible_collections/vladgh/samba/roles/server/tasks/main.yml:12 ---------------------------------------------------------------------------------------------------------------
ansible-nas-general : Update apt-cache --------------------------------------------------------------------------------------------------------------------------------------------------------------------- 2.06s
/media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-general/tasks/main.yml:7 -----------------------------------------------------------------------------------------------------------------------------
ansible-nas-docker : Install docker python module ---------------------------------------------------------------------------------------------------------------------------------------------------------- 1.86s
/media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-docker/tasks/main.yml:26 -----------------------------------------------------------------------------------------------------------------------------
ansible-nas-docker : Restart Docker ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 1.67s
/media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-docker/tasks/main.yml:51 -----------------------------------------------------------------------------------------------------------------------------
vladgh.samba.server : Install Samba VFS extensions packages ------------------------------------------------------------------------------------------------------------------------------------------------ 1.55s
/home/dietmar/.ansible/collections/ansible_collections/vladgh/samba/roles/server/tasks/main.yml:19 ---------------------------------------------------------------------------------------------------------------
geerlingguy.docker : Ensure dependencies are installed. ---------------------------------------------------------------------------------------------------------------------------------------------------- 1.47s
/home/dietmar/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml:10 ----------------------------------------------------------------------------------------------------------------------------------------
geerlingguy.docker : Install docker-compose-plugin (with downgrade option). -------------------------------------------------------------------------------------------------------------------------------- 1.43s
/home/dietmar/.ansible/roles/geerlingguy.docker/tasks/main.yml:44 ------------------------------------------------------------------------------------------------------------------------------------------------
ansible-nas-docker : Install python3-pip ------------------------------------------------------------------------------------------------------------------------------------------------------------------- 1.40s
/media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-docker/tasks/main.yml:2 ------------------------------------------------------------------------------------------------------------------------------
ansible-nas-general : Install some packages ---------------------------------------------------------------------------------------------------------------------------------------------------------------- 1.39s
/media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-general/tasks/main.yml:22 ----------------------------------------------------------------------------------------------------------------------------
geerlingguy.nfs : Ensure NFS utilities are installed. ------------------------------------------------------------------------------------------------------------------------------------------------------ 1.38s
/home/dietmar/.ansible/roles/geerlingguy.nfs/tasks/setup-Debian.yml:2 --------------------------------------------------------------------------------------------------------------------------------------------
geerlingguy.docker : Ensure additional dependencies are installed (on Ubuntu &lt; 20.04 and any other systems). ----------------------------------------------------------------------------------------------- 1.37s
/home/dietmar/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml:18 ----------------------------------------------------------------------------------------------------------------------------------------
geerlingguy.docker : Install Docker packages (with downgrade option). -------------------------------------------------------------------------------------------------------------------------------------- 1.37s
/home/dietmar/.ansible/roles/geerlingguy.docker/tasks/main.yml:27 ------------------------------------------------------------------------------------------------------------------------------------------------
airsonic : Stop Airsonic ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 1.30s
/media/IT/repos/github/forked/ansible-nas/roles/airsonic/tasks/main.yml:37 ---------------------------------------------------------------------------------------------------------------------------------------
ansible-nas-general : Set hostname to RaspiNAS ------------------------------------------------------------------------------------------------------------------------------------------------------------- 1.23s
/media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-general/tasks/main.yml:29 ----------------------------------------------------------------------------------------------------------------------------
ansible-nas-users : Create ansible-nas group --------------------------------------------------------------------------------------------------------------------------------------------------------------- 1.23s
/media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-users/tasks/main.yml:2 -------------------------------------------------------------------------------------------------------------------------------
ansible-nas-docker : Remove docker-py python module -------------------------------------------------------------------------------------------------------------------------------------------------------- 1.12s
/media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-docker/tasks/main.yml:19 -----------------------------------------------------------------------------------------------------------------------------
[<span style="color:#00AA00">2025-09-21 01:19:02</span>] (venv) [<span style="color:#55FF55"><b>dietmar@MiraPi</b></span>] [<span style="color:#5555FF"><b>.../forked/ansible-nas</b></span>] $ 
</pre>
