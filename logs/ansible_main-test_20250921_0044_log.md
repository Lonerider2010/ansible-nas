<pre>[<span style="color:#00AA00">2025-09-21 00:44:46</span>] (venv) [<span style="color:#55FF55"><b>dietmar@MiraPi</b></span>] [<span style="color:#5555FF"><b>.../forked/ansible-nas</b></span>] $ ansible-playbook -i inventories/RaspiNAS/inventory nas.yml -b -K
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
Sonntag 21 September 2025  00:44:54 +0200 (0:00:00.153)       0:00:00.153 ***** 

TASK [ansible-nas-users : Create ansible-nas group] ***************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-users/tasks/main.yml:2</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;gid&quot;: 1001,</span>
<span style="color:#00AA00">    &quot;name&quot;: &quot;ansible-nas&quot;,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;present&quot;,</span>
<span style="color:#00AA00">    &quot;system&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  00:44:55 +0200 (0:00:00.915)       0:00:01.069 ***** 

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
Sonntag 21 September 2025  00:44:56 +0200 (0:00:00.697)       0:00:01.766 ***** 

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
Sonntag 21 September 2025  00:44:56 +0200 (0:00:00.050)       0:00:01.817 ***** 

TASK [vladgh.samba.server : Install Samba packages] ***************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/collections/ansible_collections/vladgh/samba/roles/server/tasks/main.yml:12</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;cache_update_time&quot;: 1758406347,</span>
<span style="color:#00AA00">    &quot;cache_updated&quot;: false,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  00:44:58 +0200 (0:00:01.690)       0:00:03.507 ***** 

TASK [vladgh.samba.server : Install Samba VFS extensions packages] ************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/collections/ansible_collections/vladgh/samba/roles/server/tasks/main.yml:19</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;cache_update_time&quot;: 1758406347,</span>
<span style="color:#00AA00">    &quot;cache_updated&quot;: false,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  00:44:59 +0200 (0:00:01.380)       0:00:04.888 ***** 

TASK [vladgh.samba.server : Register Samba version] ***************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/collections/ansible_collections/vladgh/samba/roles/server/tasks/main.yml:26</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;cmd&quot;: &quot;set -o nounset -o pipefail -o errexit &amp;&amp; smbd --version | sed &apos;s/Version //&apos;\n&quot;,</span>
<span style="color:#00AA00">    &quot;delta&quot;: &quot;0:00:00.044513&quot;,</span>
<span style="color:#00AA00">    &quot;end&quot;: &quot;2025-09-21 00:45:00.095790&quot;,</span>
<span style="color:#00AA00">    &quot;rc&quot;: 0,</span>
<span style="color:#00AA00">    &quot;start&quot;: &quot;2025-09-21 00:45:00.051277&quot;</span>
<span style="color:#00AA00">}</span>

<span style="color:#00AA00">STDOUT:</span>

<span style="color:#00AA00">4.17.12-Debian</span>
Sonntag 21 September 2025  00:45:00 +0200 (0:00:00.638)       0:00:05.526 ***** 
Sonntag 21 September 2025  00:45:00 +0200 (0:00:00.068)       0:00:05.595 ***** 
Sonntag 21 September 2025  00:45:00 +0200 (0:00:00.028)       0:00:05.624 ***** 
Sonntag 21 September 2025  00:45:00 +0200 (0:00:00.063)       0:00:05.688 ***** 
Sonntag 21 September 2025  00:45:00 +0200 (0:00:00.028)       0:00:05.716 ***** 

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
Sonntag 21 September 2025  00:45:01 +0200 (0:00:01.278)       0:00:06.995 ***** 
Sonntag 21 September 2025  00:45:01 +0200 (0:00:00.042)       0:00:07.037 ***** 
Sonntag 21 September 2025  00:45:01 +0200 (0:00:00.049)       0:00:07.087 ***** 
Sonntag 21 September 2025  00:45:01 +0200 (0:00:00.027)       0:00:07.114 ***** 
Sonntag 21 September 2025  00:45:01 +0200 (0:00:00.048)       0:00:07.162 ***** 

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
<span style="color:#00AA00">        &quot;After&quot;: &quot;nmbd.service network-online.target winbind.service sysinit.target system.slice basic.target network.target systemd-journald.socket&quot;,</span>
<span style="color:#00AA00">        &quot;AllowIsolate&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;AssertResult&quot;: &quot;yes&quot;,</span>
<span style="color:#00AA00">        &quot;AssertTimestamp&quot;: &quot;Sun 2025-09-21 00:12:53 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;AssertTimestampMonotonic&quot;: &quot;678347215605&quot;,</span>
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
<span style="color:#00AA00">        &quot;CPUUsageNSec&quot;: &quot;86699000&quot;,</span>
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
<span style="color:#00AA00">        &quot;ExecCondition&quot;: &quot;{ path=/usr/share/samba/is-configured ; argv[]=/usr/share/samba/is-configured smb ; ignore_errors=no ; start_time=[Sun 2025-09-21 00:12:53 CEST] ; stop_time=[Sun 2025-09-21 00:12:53 CEST] ; pid=1371838 ; code=exited ; status=0 }&quot;,</span>
<span style="color:#00AA00">        &quot;ExecConditionEx&quot;: &quot;{ path=/usr/share/samba/is-configured ; argv[]=/usr/share/samba/is-configured smb ; flags= ; start_time=[Sun 2025-09-21 00:12:53 CEST] ; stop_time=[Sun 2025-09-21 00:12:53 CEST] ; pid=1371838 ; code=exited ; status=0 }&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainCode&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainExitTimestampMonotonic&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainPID&quot;: &quot;1371841&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainStartTimestamp&quot;: &quot;Sun 2025-09-21 00:12:53 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainStartTimestampMonotonic&quot;: &quot;678347263654&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainStatus&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;ExecReload&quot;: &quot;{ path=/bin/kill ; argv[]=/bin/kill -HUP $MAINPID ; ignore_errors=no ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }&quot;,</span>
<span style="color:#00AA00">        &quot;ExecReloadEx&quot;: &quot;{ path=/bin/kill ; argv[]=/bin/kill -HUP $MAINPID ; flags= ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }&quot;,</span>
<span style="color:#00AA00">        &quot;ExecStart&quot;: &quot;{ path=/usr/sbin/smbd ; argv[]=/usr/sbin/smbd --foreground --no-process-group $SMBDOPTIONS ; ignore_errors=no ; start_time=[Sun 2025-09-21 00:12:53 CEST] ; stop_time=[n/a] ; pid=1371841 ; code=(null) ; status=0/0 }&quot;,</span>
<span style="color:#00AA00">        &quot;ExecStartEx&quot;: &quot;{ path=/usr/sbin/smbd ; argv[]=/usr/sbin/smbd --foreground --no-process-group $SMBDOPTIONS ; flags= ; start_time=[Sun 2025-09-21 00:12:53 CEST] ; stop_time=[n/a] ; pid=1371841 ; code=(null) ; status=0/0 }&quot;,</span>
<span style="color:#00AA00">        &quot;ExecStartPre&quot;: &quot;{ path=/usr/share/samba/update-apparmor-samba-profile ; argv[]=/usr/share/samba/update-apparmor-samba-profile ; ignore_errors=no ; start_time=[Sun 2025-09-21 00:12:53 CEST] ; stop_time=[Sun 2025-09-21 00:12:53 CEST] ; pid=1371840 ; code=exited ; status=0 }&quot;,</span>
<span style="color:#00AA00">        &quot;ExecStartPreEx&quot;: &quot;{ path=/usr/share/samba/update-apparmor-samba-profile ; argv[]=/usr/share/samba/update-apparmor-samba-profile ; flags= ; start_time=[Sun 2025-09-21 00:12:53 CEST] ; stop_time=[Sun 2025-09-21 00:12:53 CEST] ; pid=1371840 ; code=exited ; status=0 }&quot;,</span>
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
Sonntag 21 September 2025  00:45:02 +0200 (0:00:00.980)       0:00:08.143 ***** 

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
<span style="color:#00AA00">        &quot;After&quot;: &quot;basic.target sysinit.target systemd-journald.socket network-online.target network.target system.slice&quot;,</span>
<span style="color:#00AA00">        &quot;AllowIsolate&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;AssertResult&quot;: &quot;yes&quot;,</span>
<span style="color:#00AA00">        &quot;AssertTimestamp&quot;: &quot;Sun 2025-09-21 00:12:53 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;AssertTimestampMonotonic&quot;: &quot;678347856528&quot;,</span>
<span style="color:#00AA00">        &quot;Before&quot;: &quot;smbd.service shutdown.target multi-user.target&quot;,</span>
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
<span style="color:#00AA00">        &quot;CPUUsageNSec&quot;: &quot;308101000&quot;,</span>
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
<span style="color:#00AA00">        &quot;ExecCondition&quot;: &quot;{ path=/usr/share/samba/is-configured ; argv[]=/usr/share/samba/is-configured nmb ; ignore_errors=no ; start_time=[Sun 2025-09-21 00:12:53 CEST] ; stop_time=[Sun 2025-09-21 00:12:53 CEST] ; pid=1371896 ; code=exited ; status=0 }&quot;,</span>
<span style="color:#00AA00">        &quot;ExecConditionEx&quot;: &quot;{ path=/usr/share/samba/is-configured ; argv[]=/usr/share/samba/is-configured nmb ; flags= ; start_time=[Sun 2025-09-21 00:12:53 CEST] ; stop_time=[Sun 2025-09-21 00:12:53 CEST] ; pid=1371896 ; code=exited ; status=0 }&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainCode&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainExitTimestampMonotonic&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainPID&quot;: &quot;1371899&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainStartTimestamp&quot;: &quot;Sun 2025-09-21 00:12:53 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainStartTimestampMonotonic&quot;: &quot;678347968158&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainStatus&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;ExecReload&quot;: &quot;{ path=/bin/kill ; argv[]=/bin/kill -HUP $MAINPID ; ignore_errors=no ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }&quot;,</span>
<span style="color:#00AA00">        &quot;ExecReloadEx&quot;: &quot;{ path=/bin/kill ; argv[]=/bin/kill -HUP $MAINPID ; flags= ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }&quot;,</span>
<span style="color:#00AA00">        &quot;ExecStart&quot;: &quot;{ path=/usr/sbin/nmbd ; argv[]=/usr/sbin/nmbd --foreground --no-process-group $NMBDOPTIONS ; ignore_errors=no ; start_time=[Sun 2025-09-21 00:12:53 CEST] ; stop_time=[n/a] ; pid=1371899 ; code=(null) ; status=0/0 }&quot;,</span>
<span style="color:#00AA00">        &quot;ExecStartEx&quot;: &quot;{ path=/usr/sbin/nmbd ; argv[]=/usr/sbin/nmbd --foreground --no-process-group $NMBDOPTIONS ; flags= ; start_time=[Sun 2025-09-21 00:12:53 CEST] ; stop_time=[n/a] ; pid=1371899 ; code=(null) ; status=0/0 }&quot;,</span>
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
Sonntag 21 September 2025  00:45:03 +0200 (0:00:00.545)       0:00:08.689 ***** 
Sonntag 21 September 2025  00:45:03 +0200 (0:00:00.042)       0:00:08.731 ***** 

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
Sonntag 21 September 2025  00:45:03 +0200 (0:00:00.045)       0:00:08.776 ***** 
Sonntag 21 September 2025  00:45:03 +0200 (0:00:00.031)       0:00:08.807 ***** 
Sonntag 21 September 2025  00:45:03 +0200 (0:00:00.040)       0:00:08.847 ***** 

TASK [geerlingguy.nfs : include_tasks] ****************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.nfs/tasks/main.yml:16</b></span>
<span style="color:#00AAAA">included: /home/dietmar/.ansible/roles/geerlingguy.nfs/tasks/setup-Debian.yml for ansible-nas</span>
Sonntag 21 September 2025  00:45:03 +0200 (0:00:00.056)       0:00:08.904 ***** 

TASK [geerlingguy.nfs : Ensure NFS utilities are installed.] ******************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.nfs/tasks/setup-Debian.yml:2</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;cache_update_time&quot;: 1758406347,</span>
<span style="color:#00AA00">    &quot;cache_updated&quot;: false,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  00:45:04 +0200 (0:00:01.365)       0:00:10.270 ***** 

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
Sonntag 21 September 2025  00:45:10 +0200 (0:00:05.692)       0:00:15.963 ***** 
<span style="color:#0000AA">Notification for handler reload nfs has been saved.</span>

TASK [geerlingguy.nfs : Copy exports file.] ***********************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.nfs/tasks/main.yml:25</b></span>
<span style="color:#AA5500">changed: [ansible-nas] =&gt; {</span>
<span style="color:#AA5500">    &quot;changed&quot;: true,</span>
<span style="color:#AA5500">    &quot;checksum&quot;: &quot;524aa4b4f1584667de00f8fe8d327c22b1f27f70&quot;,</span>
<span style="color:#AA5500">    &quot;dest&quot;: &quot;/etc/exports&quot;,</span>
<span style="color:#AA5500">    &quot;gid&quot;: 0,</span>
<span style="color:#AA5500">    &quot;group&quot;: &quot;root&quot;,</span>
<span style="color:#AA5500">    &quot;md5sum&quot;: &quot;cd58c94c392512386dd6eed217870c13&quot;,</span>
<span style="color:#AA5500">    &quot;mode&quot;: &quot;0644&quot;,</span>
<span style="color:#AA5500">    &quot;owner&quot;: &quot;root&quot;,</span>
<span style="color:#AA5500">    &quot;size&quot;: 1669,</span>
<span style="color:#AA5500">    &quot;src&quot;: &quot;/home/dietmar/.ansible/tmp/ansible-tmp-1758408310.6532698-16784-131898322216393/source&quot;,</span>
<span style="color:#AA5500">    &quot;state&quot;: &quot;file&quot;,</span>
<span style="color:#AA5500">    &quot;uid&quot;: 0</span>
<span style="color:#AA5500">}</span>
Sonntag 21 September 2025  00:45:11 +0200 (0:00:00.948)       0:00:16.911 ***** 

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
<span style="color:#00AA00">        &quot;After&quot;: &quot;rpc-gssd.service systemd-journald.socket mnt-Volume1.mount gssproxy.service rpc-statd.service nfsdcld.service network-online.target nfs-idmapd.service nfs-mountd.service system.slice rpcbind.socket local-fs.target rpc-svcgssd.service proc-fs-nfsd.mount -.mount&quot;,</span>
<span style="color:#00AA00">        &quot;AllowIsolate&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;AssertResult&quot;: &quot;yes&quot;,</span>
<span style="color:#00AA00">        &quot;AssertTimestamp&quot;: &quot;Sat 2025-09-13 03:47:23 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;AssertTimestampMonotonic&quot;: &quot;17797807&quot;,</span>
<span style="color:#00AA00">        &quot;Before&quot;: &quot;media-Medien.mount media-Produktion.mount rpc-statd-notify.service media-web.mount media-Dokumente.mount&quot;,</span>
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
<span style="color:#00AA00">        &quot;Requires&quot;: &quot;network.target mnt-Volume1.mount system.slice -.mount nfs-mountd.service proc-fs-nfsd.mount&quot;,</span>
<span style="color:#00AA00">        &quot;RequiresMountsFor&quot;: &quot;/mnt/Volume1/local/Audiobooks /mnt/Volume1/docker /mnt/Volume1/local/Persönliches /mnt/Volume1/local/Ägyptologie /mnt/Volume1/local/Documents /mnt/Volume1/local/Versorgung /mnt/Volume1/local/EDV /mnt/Volume1/local/Movies /mnt/Volume1/local/Organisation /mnt/Volume1/local/Download /mnt/Volume1/local/Music /mnt/Volume1/local/Comics /mnt/Volume1/local/Books /mnt/Volume1/local/Photos /mnt/Volume1/local/Media /mnt/Volume1/local/Inventar /mnt/Volume1/local/Podcasts /mnt/Volume1/local/TV&quot;,</span>
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
<span style="color:#00AA00">        &quot;Wants&quot;: &quot;rpcbind.socket rpc-svcgssd.service rpc-statd.service nfs-idmapd.service rpc-statd-notify.service network-online.target nfsdcld.service auth-rpcgss-module.service&quot;,</span>
<span style="color:#00AA00">        &quot;WatchdogSignal&quot;: &quot;6&quot;,</span>
<span style="color:#00AA00">        &quot;WatchdogTimestampMonotonic&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;WatchdogUSec&quot;: &quot;0&quot;</span>
<span style="color:#00AA00">    }</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  00:45:12 +0200 (0:00:00.577)       0:00:17.489 ***** 

TASK [geerlingguy.docker : Load OS-specific vars.] ****************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.docker/tasks/main.yml:2</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;ansible_facts&quot;: {},</span>
<span style="color:#00AA00">    &quot;ansible_included_var_files&quot;: [</span>
<span style="color:#00AA00">        &quot;/home/dietmar/.ansible/roles/geerlingguy.docker/vars/main.yml&quot;</span>
<span style="color:#00AA00">    ],</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  00:45:12 +0200 (0:00:00.045)       0:00:17.535 ***** 
Sonntag 21 September 2025  00:45:12 +0200 (0:00:00.042)       0:00:17.577 ***** 

TASK [geerlingguy.docker : include_tasks] *************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.docker/tasks/main.yml:16</b></span>
<span style="color:#00AAAA">included: /home/dietmar/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml for ansible-nas</span>
Sonntag 21 September 2025  00:45:12 +0200 (0:00:00.081)       0:00:17.659 ***** 

TASK [geerlingguy.docker : Ensure old versions of Docker are not installed.] **************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml:2</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  00:45:13 +0200 (0:00:00.969)       0:00:18.629 ***** 

TASK [geerlingguy.docker : Ensure dependencies are installed.] ****************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml:10</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;cache_update_time&quot;: 1758406347,</span>
<span style="color:#00AA00">    &quot;cache_updated&quot;: false,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  00:45:14 +0200 (0:00:01.551)       0:00:20.180 ***** 

TASK [geerlingguy.docker : Ensure additional dependencies are installed (on Ubuntu &lt; 20.04 and any other systems).] ***********************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml:18</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;cache_update_time&quot;: 1758406347,</span>
<span style="color:#00AA00">    &quot;cache_updated&quot;: false,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  00:45:16 +0200 (0:00:01.384)       0:00:21.564 ***** 
Sonntag 21 September 2025  00:45:16 +0200 (0:00:00.043)       0:00:21.608 ***** 

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
Sonntag 21 September 2025  00:45:16 +0200 (0:00:00.694)       0:00:22.303 ***** 
Sonntag 21 September 2025  00:45:17 +0200 (0:00:00.075)       0:00:22.378 ***** 
Sonntag 21 September 2025  00:45:17 +0200 (0:00:00.069)       0:00:22.447 ***** 

TASK [geerlingguy.docker : Add Docker repository.] ****************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml:50</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;repo&quot;: &quot;deb [arch=arm64 signed-by=/etc/apt/trusted.gpg.d/docker.asc] https://download.docker.com/linux/debian bookworm stable&quot;,</span>
<span style="color:#00AA00">    &quot;sources_added&quot;: [],</span>
<span style="color:#00AA00">    &quot;sources_removed&quot;: [],</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;present&quot;</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  00:45:17 +0200 (0:00:00.826)       0:00:23.273 ***** 
Sonntag 21 September 2025  00:45:17 +0200 (0:00:00.039)       0:00:23.313 ***** 

TASK [geerlingguy.docker : Install Docker packages (with downgrade option).] **************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.docker/tasks/main.yml:27</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;cache_update_time&quot;: 1758406347,</span>
<span style="color:#00AA00">    &quot;cache_updated&quot;: false,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  00:45:19 +0200 (0:00:01.379)       0:00:24.692 ***** 
Sonntag 21 September 2025  00:45:19 +0200 (0:00:00.076)       0:00:24.768 ***** 

TASK [geerlingguy.docker : Install docker-compose-plugin (with downgrade option).] ********************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.docker/tasks/main.yml:44</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;cache_update_time&quot;: 1758406347,</span>
<span style="color:#00AA00">    &quot;cache_updated&quot;: false,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  00:45:20 +0200 (0:00:01.420)       0:00:26.189 ***** 
Sonntag 21 September 2025  00:45:20 +0200 (0:00:00.094)       0:00:26.283 ***** 
Sonntag 21 September 2025  00:45:21 +0200 (0:00:00.089)       0:00:26.373 ***** 

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
<span style="color:#00AA00">        &quot;After&quot;: &quot;containerd.service network-online.target sysinit.target docker.socket time-set.target basic.target firewalld.service nss-lookup.target systemd-journald.socket system.slice&quot;,</span>
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
<span style="color:#00AA00">        &quot;CPUUsageNSec&quot;: &quot;388732000&quot;,</span>
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
<span style="color:#00AA00">        &quot;ExecStart&quot;: &quot;{ path=/usr/bin/dockerd ; argv[]=/usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock ; ignore_errors=no ; start_time=[Sun 2025-09-21 00:12:54 CEST] ; stop_time=[n/a] ; pid=1371972 ; code=(null) ; status=0/0 }&quot;,</span>
<span style="color:#00AA00">        &quot;ExecStartEx&quot;: &quot;{ path=/usr/bin/dockerd ; argv[]=/usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock ; flags= ; start_time=[Sun 2025-09-21 00:12:54 CEST] ; stop_time=[n/a] ; pid=1371972 ; code=(null) ; status=0/0 }&quot;,</span>
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
<span style="color:#00AA00">        &quot;TasksCurrent&quot;: &quot;10&quot;,</span>
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
Sonntag 21 September 2025  00:45:21 +0200 (0:00:00.564)       0:00:26.937 ***** 
<span style="color:#0000AA">NOTIFIED HANDLER geerlingguy.nfs : reload nfs for ansible-nas</span>
<span style="color:#0000AA">META: triggered running handlers for ansible-nas</span>
Sonntag 21 September 2025  00:45:21 +0200 (0:00:00.017)       0:00:26.954 ***** 

RUNNING HANDLER [geerlingguy.nfs : reload nfs] ********************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.nfs/handlers/main.yml:2</b></span>
<span style="color:#AA5500">changed: [ansible-nas] =&gt; {</span>
<span style="color:#AA5500">    &quot;changed&quot;: true,</span>
<span style="color:#AA5500">    &quot;cmd&quot;: [</span>
<span style="color:#AA5500">        &quot;exportfs&quot;,</span>
<span style="color:#AA5500">        &quot;-ra&quot;</span>
<span style="color:#AA5500">    ],</span>
<span style="color:#AA5500">    &quot;delta&quot;: &quot;0:00:00.003781&quot;,</span>
<span style="color:#AA5500">    &quot;end&quot;: &quot;2025-09-21 00:45:21.868471&quot;,</span>
<span style="color:#AA5500">    &quot;rc&quot;: 0,</span>
<span style="color:#AA5500">    &quot;start&quot;: &quot;2025-09-21 00:45:21.864690&quot;</span>
<span style="color:#AA5500">}</span>
Sonntag 21 September 2025  00:45:21 +0200 (0:00:00.328)       0:00:27.282 ***** 
Sonntag 21 September 2025  00:45:21 +0200 (0:00:00.062)       0:00:27.345 ***** 
Sonntag 21 September 2025  00:45:22 +0200 (0:00:00.084)       0:00:27.430 ***** 
Sonntag 21 September 2025  00:45:22 +0200 (0:00:00.037)       0:00:27.467 ***** 
Sonntag 21 September 2025  00:45:22 +0200 (0:00:00.067)       0:00:27.535 ***** 

TASK [ansible-nas-general : Set login banner] *********************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-general/tasks/main.yml:2</b></span>
<span style="color:#AA5500">changed: [ansible-nas] =&gt; {</span>
<span style="color:#AA5500">    &quot;changed&quot;: true,</span>
<span style="color:#AA5500">    &quot;checksum&quot;: &quot;cafe32892b670cb14dcc5f348fbb0b38062e90da&quot;,</span>
<span style="color:#AA5500">    &quot;dest&quot;: &quot;/etc/motd&quot;,</span>
<span style="color:#AA5500">    &quot;gid&quot;: 0,</span>
<span style="color:#AA5500">    &quot;group&quot;: &quot;root&quot;,</span>
<span style="color:#AA5500">    &quot;md5sum&quot;: &quot;9ddd6d0b95897eba77d158b56512c055&quot;,</span>
<span style="color:#AA5500">    &quot;mode&quot;: &quot;0644&quot;,</span>
<span style="color:#AA5500">    &quot;owner&quot;: &quot;root&quot;,</span>
<span style="color:#AA5500">    &quot;size&quot;: 488,</span>
<span style="color:#AA5500">    &quot;src&quot;: &quot;/home/dietmar/.ansible/tmp/ansible-tmp-1758408322.2258365-17125-145062332920959/source&quot;,</span>
<span style="color:#AA5500">    &quot;state&quot;: &quot;file&quot;,</span>
<span style="color:#AA5500">    &quot;uid&quot;: 0</span>
<span style="color:#AA5500">}</span>
Sonntag 21 September 2025  00:45:22 +0200 (0:00:00.607)       0:00:28.142 ***** 

TASK [ansible-nas-general : Update apt-cache] *********************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-general/tasks/main.yml:7</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;attempts&quot;: 1,</span>
<span style="color:#00AA00">    &quot;cache_update_time&quot;: 1758406347,</span>
<span style="color:#00AA00">    &quot;cache_updated&quot;: false,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  00:45:23 +0200 (0:00:00.963)       0:00:29.106 ***** 
Sonntag 21 September 2025  00:45:23 +0200 (0:00:00.036)       0:00:29.143 ***** 

TASK [ansible-nas-general : Install some packages] ****************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-general/tasks/main.yml:22</b></span>
<span style="color:#AA5500">changed: [ansible-nas] =&gt; {</span>
<span style="color:#AA5500">    &quot;attempts&quot;: 1,</span>
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
<span style="color:#AA5500">  dkms libnvpair3linux libuutil3linux libzfs6linux libzpool6linux</span>
<span style="color:#AA5500">  linux-headers-6.1.0-39-arm64 linux-headers-6.1.0-39-common</span>
<span style="color:#AA5500">  linux-headers-arm64 linux-kbuild-6.1 zfs-dkms zfs-zed</span>
<span style="color:#AA5500">Suggested packages:</span>
<span style="color:#AA5500">  menu fancontrol read-edid i2c-tools gsmartcontrol smart-notifier debhelper</span>
<span style="color:#AA5500">  zfs-initramfs | zfs-dracut</span>
<span style="color:#AA5500">Recommended packages:</span>
<span style="color:#AA5500">  linux-libc-dev</span>
<span style="color:#AA5500">The following NEW packages will be installed:</span>
<span style="color:#AA5500">  bonnie++ dkms libnvpair3linux libuutil3linux libzfs6linux libzpool6linux</span>
<span style="color:#AA5500">  linux-headers-6.1.0-39-arm64 linux-headers-6.1.0-39-common</span>
<span style="color:#AA5500">  linux-headers-arm64 linux-kbuild-6.1 lm-sensors smartmontools zfs-dkms</span>
<span style="color:#AA5500">  zfs-zed zfsutils-linux</span>
<span style="color:#AA5500">0 upgraded, 15 newly installed, 0 to remove and 8 not upgraded.</span>
<span style="color:#AA5500">Need to get 19.8 MB of archives.</span>
<span style="color:#AA5500">After this operation, 94.1 MB of additional disk space will be used.</span>
<span style="color:#AA5500">Get:1 http://deb.debian.org/debian bookworm/main arm64 dkms all 3.0.10-8+deb12u1 [48.7 kB]</span>
<span style="color:#AA5500">Get:2 http://archive.raspberrypi.com/debian bookworm/main arm64 zfs-dkms all 2.3.1-1~bpo12+1~rpt1 [3597 kB]</span>
<span style="color:#AA5500">Get:3 http://deb.debian.org/debian bookworm/main arm64 bonnie++ arm64 2.00a+nmu1 [51.5 kB]</span>
<span style="color:#AA5500">Get:4 http://deb.debian.org/debian bookworm/main arm64 linux-headers-6.1.0-39-common all 6.1.148-1 [10.2 MB]</span>
<span style="color:#AA5500">Get:5 http://archive.raspberrypi.com/debian bookworm/main arm64 libnvpair3linux arm64 2.3.1-1~bpo12+1~rpt1 [72.4 kB]</span>
<span style="color:#AA5500">Get:6 http://archive.raspberrypi.com/debian bookworm/main arm64 libuutil3linux arm64 2.3.1-1~bpo12+1~rpt1 [62.7 kB]</span>
<span style="color:#AA5500">Get:7 http://archive.raspberrypi.com/debian bookworm/main arm64 libzfs6linux arm64 2.3.1-1~bpo12+1~rpt1 [286 kB]</span>
<span style="color:#AA5500">Get:8 http://archive.raspberrypi.com/debian bookworm/main arm64 libzpool6linux arm64 2.3.1-1~bpo12+1~rpt1 [1575 kB]</span>
<span style="color:#AA5500">Get:9 http://archive.raspberrypi.com/debian bookworm/main arm64 zfsutils-linux arm64 2.3.1-1~bpo12+1~rpt1 [704 kB]</span>
<span style="color:#AA5500">Get:10 http://archive.raspberrypi.com/debian bookworm/main arm64 zfs-zed arm64 2.3.1-1~bpo12+1~rpt1 [95.9 kB]</span>
<span style="color:#AA5500">Get:11 http://archive.raspberrypi.com/debian bookworm/main arm64 linux-kbuild-6.1 arm64 1:6.1.73-1+rpt1 [913 kB]</span>
<span style="color:#AA5500">Get:12 http://deb.debian.org/debian bookworm/main arm64 linux-headers-6.1.0-39-arm64 arm64 6.1.148-1 [1555 kB]</span>
<span style="color:#AA5500">Get:13 http://deb.debian.org/debian bookworm/main arm64 linux-headers-arm64 arm64 6.1.148-1 [1424 B]</span>
<span style="color:#AA5500">Get:14 http://deb.debian.org/debian bookworm/main arm64 lm-sensors arm64 1:3.6.0-7.1 [88.4 kB]</span>
<span style="color:#AA5500">Get:15 http://deb.debian.org/debian bookworm/main arm64 smartmontools arm64 7.3-1+b1 [561 kB]</span>
<span style="color:#AA5500">Preconfiguring packages ...</span>
<span style="color:#AA5500">Fetched 19.8 MB in 3s (6696 kB/s)</span>
<span style="color:#AA5500">Selecting previously unselected package dkms.</span>
<span style="color:#AA5500">(Reading database ... 99138 files and directories currently installed.)</span>
<span style="color:#AA5500">Preparing to unpack .../00-dkms_3.0.10-8+deb12u1_all.deb ...</span>
<span style="color:#AA5500">Unpacking dkms (3.0.10-8+deb12u1) ...</span>
<span style="color:#AA5500">Selecting previously unselected package zfs-dkms.</span>
<span style="color:#AA5500">Preparing to unpack .../01-zfs-dkms_2.3.1-1~bpo12+1~rpt1_all.deb ...</span>
<span style="color:#AA5500">Unpacking zfs-dkms (2.3.1-1~bpo12+1~rpt1) ...</span>
<span style="color:#AA5500">Selecting previously unselected package libnvpair3linux:arm64.</span>
<span style="color:#AA5500">Preparing to unpack .../02-libnvpair3linux_2.3.1-1~bpo12+1~rpt1_arm64.deb ...</span>
<span style="color:#AA5500">Unpacking libnvpair3linux:arm64 (2.3.1-1~bpo12+1~rpt1) ...</span>
<span style="color:#AA5500">Selecting previously unselected package libuutil3linux:arm64.</span>
<span style="color:#AA5500">Preparing to unpack .../03-libuutil3linux_2.3.1-1~bpo12+1~rpt1_arm64.deb ...</span>
<span style="color:#AA5500">Unpacking libuutil3linux:arm64 (2.3.1-1~bpo12+1~rpt1) ...</span>
<span style="color:#AA5500">Selecting previously unselected package libzfs6linux:arm64.</span>
<span style="color:#AA5500">Preparing to unpack .../04-libzfs6linux_2.3.1-1~bpo12+1~rpt1_arm64.deb ...</span>
<span style="color:#AA5500">Adding &apos;diversion of /lib/aarch64-linux-gnu/libzfs_core.so.3 to /lib/aarch64-linux-gnu/libzfs_core.so.3.usr-is-merged by libzfs6linux&apos;</span>
<span style="color:#AA5500">Adding &apos;diversion of /lib/aarch64-linux-gnu/libzfs_core.so.3.0.0 to /lib/aarch64-linux-gnu/libzfs_core.so.3.0.0.usr-is-merged by libzfs6linux&apos;</span>
<span style="color:#AA5500">Unpacking libzfs6linux:arm64 (2.3.1-1~bpo12+1~rpt1) ...</span>
<span style="color:#AA5500">Selecting previously unselected package libzpool6linux:arm64.</span>
<span style="color:#AA5500">Preparing to unpack .../05-libzpool6linux_2.3.1-1~bpo12+1~rpt1_arm64.deb ...</span>
<span style="color:#AA5500">Unpacking libzpool6linux:arm64 (2.3.1-1~bpo12+1~rpt1) ...</span>
<span style="color:#AA5500">Selecting previously unselected package zfsutils-linux.</span>
<span style="color:#AA5500">Preparing to unpack .../06-zfsutils-linux_2.3.1-1~bpo12+1~rpt1_arm64.deb ...</span>
<span style="color:#AA5500">Unpacking zfsutils-linux (2.3.1-1~bpo12+1~rpt1) ...</span>
<span style="color:#AA5500">Selecting previously unselected package zfs-zed.</span>
<span style="color:#AA5500">Preparing to unpack .../07-zfs-zed_2.3.1-1~bpo12+1~rpt1_arm64.deb ...</span>
<span style="color:#AA5500">Unpacking zfs-zed (2.3.1-1~bpo12+1~rpt1) ...</span>
<span style="color:#AA5500">Selecting previously unselected package bonnie++.</span>
<span style="color:#AA5500">Preparing to unpack .../08-bonnie++_2.00a+nmu1_arm64.deb ...</span>
<span style="color:#AA5500">Unpacking bonnie++ (2.00a+nmu1) ...</span>
<span style="color:#AA5500">Selecting previously unselected package linux-headers-6.1.0-39-common.</span>
<span style="color:#AA5500">Preparing to unpack .../09-linux-headers-6.1.0-39-common_6.1.148-1_all.deb ...</span>
<span style="color:#AA5500">Unpacking linux-headers-6.1.0-39-common (6.1.148-1) ...</span>
<span style="color:#AA5500">Selecting previously unselected package linux-kbuild-6.1.</span>
<span style="color:#AA5500">Preparing to unpack .../10-linux-kbuild-6.1_1%3a6.1.73-1+rpt1_arm64.deb ...</span>
<span style="color:#AA5500">Unpacking linux-kbuild-6.1 (1:6.1.73-1+rpt1) ...</span>
<span style="color:#AA5500">Selecting previously unselected package linux-headers-6.1.0-39-arm64.</span>
<span style="color:#AA5500">Preparing to unpack .../11-linux-headers-6.1.0-39-arm64_6.1.148-1_arm64.deb ...</span>
<span style="color:#AA5500">Unpacking linux-headers-6.1.0-39-arm64 (6.1.148-1) ...</span>
<span style="color:#AA5500">Selecting previously unselected package linux-headers-arm64.</span>
<span style="color:#AA5500">Preparing to unpack .../12-linux-headers-arm64_6.1.148-1_arm64.deb ...</span>
<span style="color:#AA5500">Unpacking linux-headers-arm64 (6.1.148-1) ...</span>
<span style="color:#AA5500">Selecting previously unselected package lm-sensors.</span>
<span style="color:#AA5500">Preparing to unpack .../13-lm-sensors_1%3a3.6.0-7.1_arm64.deb ...</span>
<span style="color:#AA5500">Unpacking lm-sensors (1:3.6.0-7.1) ...</span>
<span style="color:#AA5500">Selecting previously unselected package smartmontools.</span>
<span style="color:#AA5500">Preparing to unpack .../14-smartmontools_7.3-1+b1_arm64.deb ...</span>
<span style="color:#AA5500">Unpacking smartmontools (7.3-1+b1) ...</span>
<span style="color:#AA5500">Setting up smartmontools (7.3-1+b1) ...</span>
<span style="color:#AA5500">Created symlink /etc/systemd/system/smartd.service → /lib/systemd/system/smartmontools.service.</span>
<span style="color:#AA5500">Created symlink /etc/systemd/system/multi-user.target.wants/smartmontools.service → /lib/systemd/system/smartmontools.service.</span>
<span style="color:#AA5500">Setting up libnvpair3linux:arm64 (2.3.1-1~bpo12+1~rpt1) ...</span>
<span style="color:#AA5500">Setting up linux-headers-6.1.0-39-common (6.1.148-1) ...</span>
<span style="color:#AA5500">Setting up bonnie++ (2.00a+nmu1) ...</span>
<span style="color:#AA5500">Setting up dkms (3.0.10-8+deb12u1) ...</span>
<span style="color:#AA5500">Setting up zfs-dkms (2.3.1-1~bpo12+1~rpt1) ...</span>
<span style="color:#AA5500">Loading new zfs-2.3.1 DKMS files...</span>
<span style="color:#AA5500">Building for 6.12.34+rpt-rpi-2712 6.12.34+rpt-rpi-v8</span>
<span style="color:#AA5500">Building initial module for 6.12.34+rpt-rpi-2712</span>
<span style="color:#AA5500">Done.</span>

<span style="color:#AA5500">zfs.ko.xz:</span>
<span style="color:#AA5500">Running module version sanity check.</span>
<span style="color:#AA5500"> - Original module</span>
<span style="color:#AA5500">   - No original module exists within this kernel</span>
<span style="color:#AA5500"> - Installation</span>
<span style="color:#AA5500">   - Installing to /lib/modules/6.12.34+rpt-rpi-2712/updates/dkms/</span>

<span style="color:#AA5500">spl.ko.xz:</span>
<span style="color:#AA5500">Running module version sanity check.</span>
<span style="color:#AA5500"> - Original module</span>
<span style="color:#AA5500">   - No original module exists within this kernel</span>
<span style="color:#AA5500"> - Installation</span>
<span style="color:#AA5500">   - Installing to /lib/modules/6.12.34+rpt-rpi-2712/updates/dkms/</span>
<span style="color:#AA5500">depmod...</span>
<span style="color:#AA5500">Building initial module for 6.12.34+rpt-rpi-v8</span>
<span style="color:#AA5500">Done.</span>

<span style="color:#AA5500">zfs.ko.xz:</span>
<span style="color:#AA5500">Running module version sanity check.</span>
<span style="color:#AA5500"> - Original module</span>
<span style="color:#AA5500">   - No original module exists within this kernel</span>
<span style="color:#AA5500"> - Installation</span>
<span style="color:#AA5500">   - Installing to /lib/modules/6.12.34+rpt-rpi-v8/updates/dkms/</span>

<span style="color:#AA5500">spl.ko.xz:</span>
<span style="color:#AA5500">Running module version sanity check.</span>
<span style="color:#AA5500"> - Original module</span>
<span style="color:#AA5500">   - No original module exists within this kernel</span>
<span style="color:#AA5500"> - Installation</span>
<span style="color:#AA5500">   - Installing to /lib/modules/6.12.34+rpt-rpi-v8/updates/dkms/</span>
<span style="color:#AA5500">depmod...</span>
<span style="color:#AA5500">Setting up lm-sensors (1:3.6.0-7.1) ...</span>
<span style="color:#AA5500">Created symlink /etc/systemd/system/multi-user.target.wants/lm-sensors.service → /lib/systemd/system/lm-sensors.service.</span>
<span style="color:#AA5500">Setting up libuutil3linux:arm64 (2.3.1-1~bpo12+1~rpt1) ...</span>
<span style="color:#AA5500">Setting up linux-kbuild-6.1 (1:6.1.73-1+rpt1) ...</span>
<span style="color:#AA5500">Setting up libzpool6linux:arm64 (2.3.1-1~bpo12+1~rpt1) ...</span>
<span style="color:#AA5500">Setting up libzfs6linux:arm64 (2.3.1-1~bpo12+1~rpt1) ...</span>
<span style="color:#AA5500">Setting up linux-headers-6.1.0-39-arm64 (6.1.148-1) ...</span>
<span style="color:#AA5500">/etc/kernel/header_postinst.d/dkms:</span>
<span style="color:#AA5500">dkms: running auto installation service for kernel 6.1.0-39-arm64.</span>
<span style="color:#AA5500">Sign command: /usr/lib/linux-kbuild-6.1/scripts/sign-file</span>
<span style="color:#AA5500">Signing key: /var/lib/dkms/mok.key</span>
<span style="color:#AA5500">Public certificate (MOK): /var/lib/dkms/mok.pub</span>

<span style="color:#AA5500">Running the pre_build script:</span>
<span style="color:#AA5500">checking for gawk... gawk</span>
<span style="color:#AA5500">checking metadata... META file</span>
<span style="color:#AA5500">checking build system type... aarch64-unknown-linux-gnu</span>
<span style="color:#AA5500">checking host system type... aarch64-unknown-linux-gnu</span>
<span style="color:#AA5500">checking target system type... aarch64-unknown-linux-gnu</span>
<span style="color:#AA5500">checking whether to enable maintainer-specific portions of Makefiles... no</span>
<span style="color:#AA5500">checking whether make supports nested variables... yes</span>
<span style="color:#AA5500">checking for a BSD-compatible install... /usr/bin/install -c</span>
<span style="color:#AA5500">checking whether build environment is sane... yes</span>
<span style="color:#AA5500">checking for a race-free mkdir -p... /usr/bin/mkdir -p</span>
<span style="color:#AA5500">checking whether make sets $(MAKE)... yes</span>
<span style="color:#AA5500">checking how to print strings... printf</span>
<span style="color:#AA5500">checking whether make supports the include directive... yes (GNU style)</span>
<span style="color:#AA5500">checking for gcc... gcc-12</span>
<span style="color:#AA5500">checking whether the C compiler works... yes</span>
<span style="color:#AA5500">checking for C compiler default output file name... a.out</span>
<span style="color:#AA5500">checking for suffix of executables... </span>
<span style="color:#AA5500">checking whether we are cross compiling... no</span>
<span style="color:#AA5500">checking for suffix of object files... o</span>
<span style="color:#AA5500">checking whether the compiler supports GNU C... yes</span>
<span style="color:#AA5500">checking whether gcc-12 accepts -g... yes</span>
<span style="color:#AA5500">checking for gcc-12 option to enable C11 features... none needed</span>
<span style="color:#AA5500">checking whether gcc-12 understands -c and -o together... yes</span>
<span style="color:#AA5500">checking dependency style of gcc-12... none</span>
<span style="color:#AA5500">checking for a sed that does not truncate output... /usr/bin/sed</span>
<span style="color:#AA5500">checking for grep that handles long lines and -e... /usr/bin/grep</span>
<span style="color:#AA5500">checking for egrep... /usr/bin/grep -E</span>
<span style="color:#AA5500">checking for fgrep... /usr/bin/grep -F</span>
<span style="color:#AA5500">checking for ld used by gcc-12... /usr/bin/ld</span>
<span style="color:#AA5500">checking if the linker (/usr/bin/ld) is GNU ld... yes</span>
<span style="color:#AA5500">checking for BSD- or MS-compatible name lister (nm)... /usr/bin/nm -B</span>
<span style="color:#AA5500">checking the name lister (/usr/bin/nm -B) interface... BSD nm</span>
<span style="color:#AA5500">checking whether ln -s works... yes</span>
<span style="color:#AA5500">checking the maximum length of command line arguments... 1572864</span>
<span style="color:#AA5500">checking how to convert aarch64-unknown-linux-gnu file names to aarch64-unknown-linux-gnu format... func_convert_file_noop</span>
<span style="color:#AA5500">checking how to convert aarch64-unknown-linux-gnu file names to toolchain format... func_convert_file_noop</span>
<span style="color:#AA5500">checking for /usr/bin/ld option to reload object files... -r</span>
<span style="color:#AA5500">checking for file... file</span>
<span style="color:#AA5500">checking for objdump... objdump</span>
<span style="color:#AA5500">checking how to recognize dependent libraries... pass_all</span>
<span style="color:#AA5500">checking for dlltool... no</span>
<span style="color:#AA5500">checking how to associate runtime and link libraries... printf %s\n</span>
<span style="color:#AA5500">checking for ar... ar</span>
<span style="color:#AA5500">checking for archiver @FILE support... @</span>
<span style="color:#AA5500">checking for strip... strip</span>
<span style="color:#AA5500">checking for ranlib... ranlib</span>
<span style="color:#AA5500">checking command to parse /usr/bin/nm -B output from gcc-12 object... ok</span>
<span style="color:#AA5500">checking for sysroot... no</span>
<span style="color:#AA5500">checking for a working dd... /usr/bin/dd</span>
<span style="color:#AA5500">checking how to truncate binary pipes... /usr/bin/dd bs=4096 count=1</span>
<span style="color:#AA5500">checking for mt... mt</span>
<span style="color:#AA5500">checking if mt is a manifest tool... no</span>
<span style="color:#AA5500">checking for stdio.h... yes</span>
<span style="color:#AA5500">checking for stdlib.h... yes</span>
<span style="color:#AA5500">checking for string.h... yes</span>
<span style="color:#AA5500">checking for inttypes.h... yes</span>
<span style="color:#AA5500">checking for stdint.h... yes</span>
<span style="color:#AA5500">checking for strings.h... yes</span>
<span style="color:#AA5500">checking for sys/stat.h... yes</span>
<span style="color:#AA5500">checking for sys/types.h... yes</span>
<span style="color:#AA5500">checking for unistd.h... yes</span>
<span style="color:#AA5500">checking for dlfcn.h... yes</span>
<span style="color:#AA5500">checking for objdir... .libs</span>
<span style="color:#AA5500">checking if gcc-12 supports -fno-rtti -fno-exceptions... no</span>
<span style="color:#AA5500">checking for gcc-12 option to produce PIC... -fPIC -DPIC</span>
<span style="color:#AA5500">checking if gcc-12 PIC flag -fPIC -DPIC works... yes</span>
<span style="color:#AA5500">checking if gcc-12 static flag -static works... yes</span>
<span style="color:#AA5500">checking if gcc-12 supports -c -o file.o... yes</span>
<span style="color:#AA5500">checking if gcc-12 supports -c -o file.o... (cached) yes</span>
<span style="color:#AA5500">checking whether the gcc-12 linker (/usr/bin/ld) supports shared libraries... yes</span>
<span style="color:#AA5500">checking whether -lc should be explicitly linked in... no</span>
<span style="color:#AA5500">checking dynamic linker characteristics... GNU/Linux ld.so</span>
<span style="color:#AA5500">checking how to hardcode library paths into programs... immediate</span>
<span style="color:#AA5500">checking whether stripping libraries is possible... yes</span>
<span style="color:#AA5500">checking if libtool supports shared libraries... yes</span>
<span style="color:#AA5500">checking whether to build shared libraries... yes</span>
<span style="color:#AA5500">checking whether to build static libraries... yes</span>
<span style="color:#AA5500">checking for gcc... (cached) gcc-12</span>
<span style="color:#AA5500">checking whether the compiler supports GNU C... (cached) yes</span>
<span style="color:#AA5500">checking whether gcc-12 accepts -g... (cached) yes</span>
<span style="color:#AA5500">checking for gcc-12 option to enable C11 features... (cached) none needed</span>
<span style="color:#AA5500">checking whether gcc-12 understands -c and -o together... (cached) yes</span>
<span style="color:#AA5500">checking dependency style of gcc-12... (cached) none</span>
<span style="color:#AA5500">checking whether ln -s works... yes</span>
<span style="color:#AA5500">checking for pkg-config... /usr/bin/pkg-config</span>
<span style="color:#AA5500">checking pkg-config is at least version 0.9.0... yes</span>
<span style="color:#AA5500">checking dependency style of gcc-12... none</span>
<span style="color:#AA5500">checking whether to build with code coverage support... no</span>
<span style="color:#AA5500">checking how to create a pax tar archive... gnutar</span>
<span style="color:#AA5500">checking zfs author... OpenZFS</span>
<span style="color:#AA5500">checking zfs license... CDDL</span>
<span style="color:#AA5500">checking whether NLS is requested... yes</span>
<span style="color:#AA5500">checking for msgfmt... no</span>
<span style="color:#AA5500">checking for gmsgfmt... :</span>
<span style="color:#AA5500">checking for xgettext... no</span>
<span style="color:#AA5500">checking for msgmerge... no</span>
<span style="color:#AA5500">checking for ld... /usr/bin/ld</span>
<span style="color:#AA5500">checking if the linker (/usr/bin/ld) is GNU ld... yes</span>
<span style="color:#AA5500">checking for shared library run path origin... done</span>
<span style="color:#AA5500">checking 32-bit host C ABI... no</span>
<span style="color:#AA5500">checking for the common suffixes of directories in the library search path... lib,lib</span>
<span style="color:#AA5500">checking zfs config... kernel</span>
<span style="color:#AA5500">checking the number of available CPUs... 4</span>
<span style="color:#AA5500">checking whether gcc-12 supports -Wno-clobbered... yes</span>
<span style="color:#AA5500">checking whether gcc-12 supports -Winfinite-recursion... yes</span>
<span style="color:#AA5500">checking whether  supports -Winfinite-recursion... yes</span>
<span style="color:#AA5500">checking whether gcc-12 supports -Wimplicit-fallthrough... yes</span>
<span style="color:#AA5500">checking whether gcc-12 supports -Wframe-larger-than=&lt;size&gt;... yes</span>
<span style="color:#AA5500">checking whether gcc-12 supports -Wno-format-truncation... yes</span>
<span style="color:#AA5500">checking whether gcc-12 supports -Wno-format-zero-length... yes</span>
<span style="color:#AA5500">checking whether gcc-12 supports -Wformat-overflow... yes</span>
<span style="color:#AA5500">checking whether gcc-12 supports -fno-omit-frame-pointer... yes</span>
<span style="color:#AA5500">checking whether gcc-12 supports -fno-ipa-sra... yes</span>
<span style="color:#AA5500">checking whether  supports -fno-ipa-sra... yes</span>
<span style="color:#AA5500">checking whether to build with -fsanitize=address support... no</span>
<span style="color:#AA5500">checking whether to build with -fsanitize=undefined support... no</span>
<span style="color:#AA5500">checking for system type (linux-gnu)... Linux</span>
<span style="color:#AA5500">checking for python3... python3</span>
<span style="color:#AA5500">checking for python version... 3.11</span>
<span style="color:#AA5500">checking for python platform... linux</span>
<span style="color:#AA5500">checking for GNU default python prefix... ${prefix}</span>
<span style="color:#AA5500">checking for GNU default python exec_prefix... ${exec_prefix}</span>
<span style="color:#AA5500">checking for python script directory (pythondir)... ${PYTHON_PREFIX}/lib/python3.11/site-packages</span>
<span style="color:#AA5500">checking for python extension module directory (pyexecdir)... ${PYTHON_EXEC_PREFIX}/lib/python3.11/site-packages</span>
<span style="color:#AA5500">configure: Disabling pyzfs for kernel/srpm config</span>
<span style="color:#AA5500">checking whether to enable pyzfs: ... no</span>
<span style="color:#AA5500">checking for sed --in-place... --in-place</span>
<span style="color:#AA5500">checking for cppcheck... no</span>
<span style="color:#AA5500">checking for shellcheck... no</span>
<span style="color:#AA5500">checking for checkbashisms... no</span>
<span style="color:#AA5500">checking for parallel... no</span>
<span style="color:#AA5500">checking kernel source and build directories... done</span>
<span style="color:#AA5500">checking kernel source directory... /lib/modules/6.1.0-39-arm64/source</span>
<span style="color:#AA5500">checking kernel build directory... /lib/modules/6.1.0-39-arm64/build</span>
<span style="color:#AA5500">checking kernel source version... 6.1.0-39-arm64</span>
<span style="color:#AA5500">checking for kernel config option compatibility... done</span>
<span style="color:#AA5500">checking whether CONFIG_MODULES is defined... yes</span>
<span style="color:#AA5500">checking whether CONFIG_BLOCK is defined... yes</span>
<span style="color:#AA5500">checking whether mutex_lock() is GPL-only... no</span>
<span style="color:#AA5500">checking whether CONFIG_TRIM_UNUSED_KSYM is disabled... yes</span>
<span style="color:#AA5500">checking whether CONFIG_ZLIB_DEFLATE is defined... yes</span>
<span style="color:#AA5500">checking whether CONFIG_ZLIB_INFLATE is defined... yes</span>
<span style="color:#AA5500">checking kernel file name for module symbols... Module.symvers</span>
<span style="color:#AA5500">checking whether fpu headers are available... i387.h</span>
<span style="color:#AA5500">checking whether objtool header is available... linux/objtool.h</span>
<span style="color:#AA5500">checking whether /dev/zfs minor is available... 249</span>
<span style="color:#AA5500">checking whether DECLARE_EVENT_CLASS() is available... no</span>
<span style="color:#AA5500">checking for available kernel interfaces... done</span>
<span style="color:#AA5500">checking whether kernel defines intptr_t... no</span>
<span style="color:#AA5500">checking whether access_ok() has &apos;type&apos; parameter... no</span>
<span style="color:#AA5500">checking whether compile-time stack validation (objtool) is available... no</span>
<span style="color:#AA5500">checking whether pde_data() is lowercase... yes</span>
<span style="color:#AA5500">checking whether generic_fadvise() is available... yes</span>
<span style="color:#AA5500">checking whether header linux/sched/rt.h exists... yes</span>
<span style="color:#AA5500">checking whether usleep_range() is available... yes</span>
<span style="color:#AA5500">checking whether __vmalloc(ptr, flags, pageflags) is available... no</span>
<span style="color:#AA5500">checking whether timestamp_truncate() exists... yes</span>
<span style="color:#AA5500">checking whether inode_get_ctime() exists... yes</span>
<span style="color:#AA5500">checking whether inode_set_ctime_to_ts() exists... yes</span>
<span style="color:#AA5500">checking whether inode_get_atime() exists... no</span>
<span style="color:#AA5500">checking whether inode_set_atime_to_ts() exists... no</span>
<span style="color:#AA5500">checking whether inode_get_mtime() exists... no</span>
<span style="color:#AA5500">checking whether inode_set_mtime_to_ts() exists... no</span>
<span style="color:#AA5500">checking whether proc_ops structure exists... yes</span>
<span style="color:#AA5500">checking whether bops-&gt;check_events() exists... yes</span>
<span style="color:#AA5500">checking whether bops-&gt;release() is void and takes 2 args... yes</span>
<span style="color:#AA5500">checking whether bops-&gt;revalidate_disk() exists... no</span>
<span style="color:#AA5500">checking whether bio_set_op_attrs is available... yes</span>
<span style="color:#AA5500">checking whether bio_set_dev() is GPL-only... yes</span>
<span style="color:#AA5500">checking whether bio_set_dev() is a macro... no</span>
<span style="color:#AA5500">checking whether current-&gt;bio_list exists... yes</span>
<span style="color:#AA5500">checking whether blkg_tryget() is available... no</span>
<span style="color:#AA5500">checking whether bio-&gt;bi_bdev-&gt;bd_disk exists... yes</span>
<span style="color:#AA5500">checking whether block_device_operations-&gt;submit_bio() returns void... yes</span>
<span style="color:#AA5500">checking whether bio_alloc() wants 4 args... yes</span>
<span style="color:#AA5500">checking whether blkdev_get_by_path() exists and takes 3 args... yes</span>
<span style="color:#AA5500">checking whether blkdev_put() exists... yes</span>
<span style="color:#AA5500">checking whether blkdev_reread_part() exists... no</span>
<span style="color:#AA5500">checking whether invalidate_bdev() exists... yes</span>
<span style="color:#AA5500">checking whether lookup_bdev() wants dev_t arg... yes</span>
<span style="color:#AA5500">checking whether bdev_logical_block_size() is available... yes</span>
<span style="color:#AA5500">checking whether bdev_physical_block_size() is available... yes</span>
<span style="color:#AA5500">checking whether check_disk_change() exists... no</span>
<span style="color:#AA5500">checking whether bdev_check_media_change() exists... yes</span>
<span style="color:#AA5500">checking whether bdev_whole() is available... yes</span>
<span style="color:#AA5500">checking whether bdev_nr_bytes() is available... yes</span>
<span style="color:#AA5500">checking whether bdevname() exists... no</span>
<span style="color:#AA5500">checking whether blkdev_get_by_path() handles ERESTARTSYS... no</span>
<span style="color:#AA5500">checking whether blkdev_issue_discard() is available... yes</span>
<span style="color:#AA5500">checking whether blkdev_issue_discard(flags) is available... no</span>
<span style="color:#AA5500">checking whether __blkdev_issue_discard() is available... yes</span>
<span style="color:#AA5500">checking whether __blkdev_issue_discard(flags) is available... no</span>
<span style="color:#AA5500">checking whether blkdev_issue_secure_erase() is available... yes</span>
<span style="color:#AA5500">checking whether bdev_kobj() exists... yes</span>
<span style="color:#AA5500">checking whether part_to_dev() exists... no</span>
<span style="color:#AA5500">checking whether disk_check_media_change() exists... no</span>
<span style="color:#AA5500">checking whether BLK_STS_RESV_CONFLICT is defined... no</span>
<span style="color:#AA5500">checking whether blk_mode_t is defined... no</span>
<span style="color:#AA5500">checking whether struct blk_plug is available... yes</span>
<span style="color:#AA5500">checking whether blk_queue bdi is dynamic... no</span>
<span style="color:#AA5500">checking whether backing_dev_info is available through queue gendisk... yes</span>
<span style="color:#AA5500">checking whether blk_queue_update_readahead() exists... no</span>
<span style="color:#AA5500">checking whether disk_update_readahead() exists... yes</span>
<span style="color:#AA5500">checking whether bdev_max_discard_sectors() is available... yes</span>
<span style="color:#AA5500">checking whether bdev_max_secure_erase_sectors() is available... yes</span>
<span style="color:#AA5500">checking whether blk_queue_max_hw_sectors() is available... yes</span>
<span style="color:#AA5500">checking whether blk_queue_max_segments() is available... yes</span>
<span style="color:#AA5500">checking whether block multiqueue hardware context is cached in struct request... yes</span>
<span style="color:#AA5500">checking whether GENHD_FL_EXT_DEVT flag is available... no</span>
<span style="color:#AA5500">checking whether GENHD_FL_NO_PART flag is available... yes</span>
<span style="color:#AA5500">checking whether revalidate_disk_size() is available... no</span>
<span style="color:#AA5500">checking whether revalidate_disk() is available... no</span>
<span style="color:#AA5500">checking whether get_disk_ro() is available... yes</span>
<span style="color:#AA5500">checking whether ql-&gt;discard_granularity is available... yes</span>
<span style="color:#AA5500">checking whether inode_owner_or_capable() exists... no</span>
<span style="color:#AA5500">checking whether inode_owner_or_capable() takes user_ns... yes</span>
<span style="color:#AA5500">checking whether super_block uses const struct xattr_handler... yes</span>
<span style="color:#AA5500">checking whether xattr_handler-&gt;get() wants dentry and inode and flags... no</span>
<span style="color:#AA5500">checking whether xattr_handler-&gt;set() wants dentry, inode, and mnt_idmap... no</span>
<span style="color:#AA5500">checking whether xattr_handler-&gt;set() wants dentry, inode, and user_namespace... yes</span>
<span style="color:#AA5500">checking whether posix_acl_equiv_mode() wants umode_t... yes</span>
<span style="color:#AA5500">checking whether iops-&gt;get_acl() exists... yes</span>
<span style="color:#AA5500">checking whether iops-&gt;set_acl() with 4 args exists... yes</span>
<span style="color:#AA5500">checking whether iops-&gt;setattr() takes mnt_idmap... no</span>
<span style="color:#AA5500">checking whether iops-&gt;setattr() takes user_namespace... yes</span>
<span style="color:#AA5500">checking whether iops-&gt;getattr() takes mnt_idmap... no</span>
<span style="color:#AA5500">checking whether iops-&gt;getattr() takes user_namespace... yes</span>
<span style="color:#AA5500">checking whether sops-&gt;show_options() wants dentry... yes</span>
<span style="color:#AA5500">checking whether super_block has s_shrink... yes</span>
<span style="color:#AA5500">checking whether new var-arg register_shrinker() exists... yes</span>
<span style="color:#AA5500">checking whether shrinker_register() exists... no</span>
<span style="color:#AA5500">checking whether iops-&gt;mkdir() takes struct mnt_idmap*... no</span>
<span style="color:#AA5500">checking whether iops-&gt;mkdir() takes struct user_namespace*... yes</span>
<span style="color:#AA5500">checking whether iops-&gt;lookup() passes flags... yes</span>
<span style="color:#AA5500">checking whether iops-&gt;create() takes struct mnt_idmap*... no</span>
<span style="color:#AA5500">checking whether iops-&gt;create() takes struct user_namespace*... yes</span>
<span style="color:#AA5500">checking whether iops-&gt;permission() takes struct mnt_idmap*... no</span>
<span style="color:#AA5500">checking whether iops-&gt;permission() takes struct user_namespace*... yes</span>
<span style="color:#AA5500">checking whether i_op-&gt;tmpfile() exists... yes</span>
<span style="color:#AA5500">checking whether dops-&gt;d_automount() exists... yes</span>
<span style="color:#AA5500">checking whether dops-&gt;d_revalidate() takes 4 args... no</span>
<span style="color:#AA5500">checking whether eops-&gt;commit_metadata() exists... yes</span>
<span style="color:#AA5500">checking whether setattr_prepare() is available and accepts struct mnt_idmap*... no</span>
<span style="color:#AA5500">checking whether setattr_prepare() is available and accepts struct user_namespace*... yes</span>
<span style="color:#AA5500">checking whether insert_inode_locked() is available... yes</span>
<span style="color:#AA5500">checking whether truncate_setsize() is available... yes</span>
<span style="color:#AA5500">checking whether security_inode_init_security wants callback... yes</span>
<span style="color:#AA5500">checking whether fst-&gt;mount() exists... yes</span>
<span style="color:#AA5500">checking whether set_nlink() is available... yes</span>
<span style="color:#AA5500">checking whether sget() wants 5 args... yes</span>
<span style="color:#AA5500">checking whether filemap_dirty_folio exists... yes</span>
<span style="color:#AA5500">checking whether read_folio exists... yes</span>
<span style="color:#AA5500">checking whether migrate_folio exists... yes</span>
<span style="color:#AA5500">checking whether vfs_fsync() wants 2 args... yes</span>
<span style="color:#AA5500">checking whether aops-&gt;readpages exists... no</span>
<span style="color:#AA5500">checking whether __set_page_dirty_nobuffers exists... no</span>
<span style="color:#AA5500">checking whether fault_in_iov_iter_readable() is available... yes</span>
<span style="color:#AA5500">checking whether iov_iter_type() is available... yes</span>
<span style="color:#AA5500">checking whether iov_iter_get_pages2() is available... yes</span>
<span style="color:#AA5500">checking whether iter_is_ubuf() is available... yes</span>
<span style="color:#AA5500">checking whether iter_iov() is available... no</span>
<span style="color:#AA5500">checking whether generic_copy_file_range() is available... yes</span>
<span style="color:#AA5500">checking whether splice_copy_file_range() is available... no</span>
<span style="color:#AA5500">checking whether fops-&gt;remap_file_range() is available... yes</span>
<span style="color:#AA5500">checking whether fops-&gt;clone_file_range() is available... no</span>
<span style="color:#AA5500">checking whether fops-&gt;dedupe_file_range() is available... no</span>
<span style="color:#AA5500">checking whether kmap_atomic wants 1 args... yes</span>
<span style="color:#AA5500">checking whether kmap_local_page exists... yes</span>
<span style="color:#AA5500">checking whether follow_down_one() is available... yes</span>
<span style="color:#AA5500">checking whether submit_bio is member of struct block_device_operations... yes</span>
<span style="color:#AA5500">checking whether blk_alloc_disk() exists... yes</span>
<span style="color:#AA5500">checking whether blk_cleanup_disk() exists... no</span>
<span style="color:#AA5500">checking whether blk_alloc_disk() exists and takes 2 args... no</span>
<span style="color:#AA5500">checking whether 6.3+ bdev_*_io_acct() are available... no</span>
<span style="color:#AA5500">checking whether pre-6.3 bdev_*_io_acct() are available... yes</span>
<span style="color:#AA5500">checking whether kernel fpu is available... kernel_neon_*</span>
<span style="color:#AA5500">checking whether kernel defines fmode_t... yes</span>
<span style="color:#AA5500">checking whether kuid_t/kgid_t is available... yes</span>
<span style="color:#AA5500">checking whether i_(uid|gid)_(read|write) exist... yes</span>
<span style="color:#AA5500">checking whether iops-&gt;rename() takes struct mnt_idmap*... no</span>
<span style="color:#AA5500">checking whether iops-&gt;rename() takes struct user_namespace*... yes</span>
<span style="color:#AA5500">checking whether totalram_pages() exists... yes</span>
<span style="color:#AA5500">checking whether totalhigh_pages() exists... yes</span>
<span style="color:#AA5500">checking whether is inside percpu_ref.data... yes</span>
<span style="color:#AA5500">checking whether generic_fillattr requires struct mnt_idmap* and request_mask... no</span>
<span style="color:#AA5500">checking whether generic_fillattr requires struct mnt_idmap*... no</span>
<span style="color:#AA5500">checking whether generic_fillattr requires struct user_namespace*... yes</span>
<span style="color:#AA5500">checking whether iops-&gt;mknod() takes struct mnt_idmap*... no</span>
<span style="color:#AA5500">checking whether iops-&gt;mknod() takes struct user_namespace*... yes</span>
<span style="color:#AA5500">checking whether iops-&gt;symlink() takes struct mnt_idmap*... no</span>
<span style="color:#AA5500">checking whether iops-&gt;symlink() takes struct user_namespace*... yes</span>
<span style="color:#AA5500">checking whether bio_max_segs() exists... yes</span>
<span style="color:#AA5500">checking whether kernel_siginfo_t tyepedef exists... yes</span>
<span style="color:#AA5500">checking whether struct kobj_type.default_groups exists... yes</span>
<span style="color:#AA5500">checking whether standalone &lt;linux/stdarg.h&gt; exists... yes</span>
<span style="color:#AA5500">checking whether strlcpy() exists... yes</span>
<span style="color:#AA5500">checking whether folio_wait_bit() exists... yes</span>
<span style="color:#AA5500">checking whether add_disk() returns int... yes</span>
<span style="color:#AA5500">checking whether kthread_complete_and_exit() is available... yes</span>
<span style="color:#AA5500">checking whether dequeue_signal() takes 4 arguments... yes</span>
<span style="color:#AA5500">checking whether ZERO_PAGE() is GPL-only... no</span>
<span style="color:#AA5500">checking whether __copy_from_user_inatomic is available... yes</span>
<span style="color:#AA5500">checking whether APIs for idmapped mount are present... yes</span>
<span style="color:#AA5500">checking whether idmapped mounts have a user namespace... no</span>
<span style="color:#AA5500">checking whether iattr-&gt;ia_vfsuid and iattr-&gt;ia_vfsgid exist... yes</span>
<span style="color:#AA5500">checking whether int (*writepage_t)() takes struct folio*... no</span>
<span style="color:#AA5500">checking whether struct reclaim_state has reclaimed field... no</span>
<span style="color:#AA5500">checking whether register_sysctl_table exists... yes</span>
<span style="color:#AA5500">checking whether register_sysctl_sz exists... no</span>
<span style="color:#AA5500">checking whether proc_handler ctl_table arg is const... no</span>
<span style="color:#AA5500">checking whether copy_splice_read() exists... no</span>
<span style="color:#AA5500">checking whether fsync_bdev() exists... yes</span>
<span style="color:#AA5500">checking whether PG_error flag is available... yes</span>
<span style="color:#AA5500">checking whether page_size() is available... yes</span>
<span style="color:#AA5500">checking whether page_mapping() is available... yes</span>
<span style="color:#AA5500">checking whether __assign_str() has one arg... no</span>
<span style="color:#AA5500">checking whether file-&gt;f_version exists... no</span>
<span style="color:#AA5500">checking whether pin_user_pages_unlocked() is available... yes</span>
<span style="color:#AA5500">checking whether assertion support will be enabled... no</span>
<span style="color:#AA5500">checking whether debuginfo support will be forced... no</span>
<span style="color:#AA5500">checking whether basic kmem accounting is enabled... no</span>
<span style="color:#AA5500">checking whether detailed kmem tracking is enabled... no</span>
<span style="color:#AA5500">checking whether FreeBSD kernel INVARIANTS checks are enabled... no</span>
<span style="color:#AA5500">checking that generated files are newer than configure... done</span>
<span style="color:#AA5500">configure: creating ./config.status</span>
<span style="color:#AA5500">config.status: creating Makefile</span>
<span style="color:#AA5500">config.status: creating include/Makefile</span>
<span style="color:#AA5500">config.status: creating module/Kbuild</span>
<span style="color:#AA5500">config.status: creating module/Makefile</span>
<span style="color:#AA5500">config.status: creating zfs.release</span>
<span style="color:#AA5500">config.status: creating zfs_config.h</span>
<span style="color:#AA5500">config.status: executing depfiles commands</span>
<span style="color:#AA5500">config.status: executing libtool commands</span>
<span style="color:#AA5500">config.status: executing po-directories commands</span>

<span style="color:#AA5500">Building module:</span>
<span style="color:#AA5500">Cleaning build area...</span>
<span style="color:#AA5500">make -j4 KERNELRELEASE=6.1.0-39-arm64...................................................</span>
<span style="color:#AA5500">Signing module /var/lib/dkms/zfs/2.3.1/build/module/zfs.ko</span>
<span style="color:#AA5500">Signing module /var/lib/dkms/zfs/2.3.1/build/module/spl.ko</span>

<span style="color:#AA5500">Running the post_build script:</span>
<span style="color:#AA5500">Cleaning build area...</span>

<span style="color:#AA5500">zfs.ko:</span>
<span style="color:#AA5500">Running module version sanity check.</span>
<span style="color:#AA5500"> - Original module</span>
<span style="color:#AA5500">   - No original module exists within this kernel</span>
<span style="color:#AA5500"> - Installation</span>
<span style="color:#AA5500">   - Installing to /lib/modules/6.1.0-39-arm64/updates/dkms/</span>

<span style="color:#AA5500">spl.ko:</span>
<span style="color:#AA5500">Running module version sanity check.</span>
<span style="color:#AA5500"> - Original module</span>
<span style="color:#AA5500">   - No original module exists within this kernel</span>
<span style="color:#AA5500"> - Installation</span>
<span style="color:#AA5500">   - Installing to /lib/modules/6.1.0-39-arm64/updates/dkms/</span>
<span style="color:#AA5500">depmod...</span>
<span style="color:#AA5500">dkms: autoinstall for kernel: 6.1.0-39-arm64.</span>
<span style="color:#AA5500">Setting up linux-headers-arm64 (6.1.148-1) ...</span>
<span style="color:#AA5500">Setting up zfsutils-linux (2.3.1-1~bpo12+1~rpt1) ...</span>
<span style="color:#AA5500">insmod /lib/modules/6.12.34+rpt-rpi-2712/updates/dkms/spl.ko.xz </span>
<span style="color:#AA5500">insmod /lib/modules/6.12.34+rpt-rpi-2712/updates/dkms/zfs.ko.xz </span>
<span style="color:#AA5500">Created symlink /etc/systemd/system/zfs-import.target.wants/zfs-import-cache.service → /lib/systemd/system/zfs-import-cache.service.</span>
<span style="color:#AA5500">Created symlink /etc/systemd/system/zfs.target.wants/zfs-import.target → /lib/systemd/system/zfs-import.target.</span>
<span style="color:#AA5500">Created symlink /etc/systemd/system/zfs-mount.service.wants/zfs-load-module.service → /lib/systemd/system/zfs-load-module.service.</span>
<span style="color:#AA5500">Created symlink /etc/systemd/system/zfs.target.wants/zfs-load-module.service → /lib/systemd/system/zfs-load-module.service.</span>
<span style="color:#AA5500">Created symlink /etc/systemd/system/zfs.target.wants/zfs-mount.service → /lib/systemd/system/zfs-mount.service.</span>
<span style="color:#AA5500">Created symlink /etc/systemd/system/zfs.target.wants/zfs-share.service → /lib/systemd/system/zfs-share.service.</span>
<span style="color:#AA5500">Created symlink /etc/systemd/system/zfs-volumes.target.wants/zfs-volume-wait.service → /lib/systemd/system/zfs-volume-wait.service.</span>
<span style="color:#AA5500">Created symlink /etc/systemd/system/zfs.target.wants/zfs-volumes.target → /lib/systemd/system/zfs-volumes.target.</span>
<span style="color:#AA5500">Created symlink /etc/systemd/system/multi-user.target.wants/zfs.target → /lib/systemd/system/zfs.target.</span>
<span style="color:#AA5500">zfs-import-scan.service is a disabled or a static unit, not starting it.</span>
<span style="color:#AA5500">Processing triggers for initramfs-tools (0.142+rpt4+deb12u3) ...</span>
<span style="color:#AA5500">update-initramfs: Generating /boot/initrd.img-6.12.34+rpt-rpi-v8</span>
<span style="color:#AA5500">&apos;/boot/initrd.img-6.12.34+rpt-rpi-v8&apos; -&gt; &apos;/boot/firmware/initramfs8&apos;</span>
<span style="color:#AA5500">update-initramfs: Generating /boot/initrd.img-6.12.34+rpt-rpi-2712</span>
<span style="color:#AA5500">&apos;/boot/initrd.img-6.12.34+rpt-rpi-2712&apos; -&gt; &apos;/boot/firmware/initramfs_2712&apos;</span>
<span style="color:#AA5500">Processing triggers for libc-bin (2.36-9+rpt2+deb12u12) ...</span>
<span style="color:#AA5500">Processing triggers for man-db (2.11.2-2) ...</span>
<span style="color:#AA5500">Setting up zfs-zed (2.3.1-1~bpo12+1~rpt1) ...</span>
<span style="color:#AA5500">Created symlink /etc/systemd/system/zed.service → /lib/systemd/system/zfs-zed.service.</span>
<span style="color:#AA5500">Created symlink /etc/systemd/system/zfs.target.wants/zfs-zed.service → /lib/systemd/system/zfs-zed.service.</span>

Sonntag 21 September 2025  00:55:09 +0200 (0:09:45.705)       0:10:14.849 ***** 

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
Sonntag 21 September 2025  00:55:11 +0200 (0:00:01.678)       0:10:16.528 ***** 

TASK [ansible-nas-general : Set timezone to Europe/Berlin] ********************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-general/tasks/main.yml:33</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  00:55:11 +0200 (0:00:00.777)       0:10:17.305 ***** 
Sonntag 21 September 2025  00:55:12 +0200 (0:00:00.047)       0:10:17.353 ***** 

TASK [ansible-nas-docker : Install python3-pip] *******************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-docker/tasks/main.yml:2</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;attempts&quot;: 1,</span>
<span style="color:#00AA00">    &quot;cache_update_time&quot;: 1758406347,</span>
<span style="color:#00AA00">    &quot;cache_updated&quot;: false,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Sonntag 21 September 2025  00:55:13 +0200 (0:00:01.394)       0:10:18.747 ***** 
<span style="color:#555555"><b>FAILED - RETRYING: [ansible-nas]: Remove docker-py python module (3 retries left).</b></span>
<span style="color:#555555"><b>FAILED - RETRYING: [ansible-nas]: Remove docker-py python module (2 retries left).</b></span>
<span style="color:#555555"><b>FAILED - RETRYING: [ansible-nas]: Remove docker-py python module (1 retries left).</b></span>

TASK [ansible-nas-docker : Remove docker-py python module] ********************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-docker/tasks/main.yml:9</b></span>
<span style="color:#AA0000">fatal: [ansible-nas]: FAILED! =&gt; {</span>
<span style="color:#AA0000">    &quot;attempts&quot;: 3,</span>
<span style="color:#AA0000">    &quot;changed&quot;: false,</span>
<span style="color:#AA0000">    &quot;cmd&quot;: [</span>
<span style="color:#AA0000">        &quot;/usr/bin/python3&quot;,</span>
<span style="color:#AA0000">        &quot;-m&quot;,</span>
<span style="color:#AA0000">        &quot;pip.__main__&quot;,</span>
<span style="color:#AA0000">        &quot;uninstall&quot;,</span>
<span style="color:#AA0000">        &quot;-y&quot;,</span>
<span style="color:#AA0000">        &quot;docker-py&quot;</span>
<span style="color:#AA0000">    ]</span>
<span style="color:#AA0000">}</span>

<span style="color:#AA0000">MSG:</span>


<span style="color:#AA0000">:stderr: error: externally-managed-environment</span>

<span style="color:#AA0000">× This environment is externally managed</span>
<span style="color:#AA0000">╰─&gt; To install Python packages system-wide, try apt install</span>
<span style="color:#AA0000">    python3-xyz, where xyz is the package you are trying to</span>
<span style="color:#AA0000">    install.</span>
<span style="color:#AA0000">    </span>
<span style="color:#AA0000">    If you wish to install a non-Debian-packaged Python package,</span>
<span style="color:#AA0000">    create a virtual environment using python3 -m venv path/to/venv.</span>
<span style="color:#AA0000">    Then use path/to/venv/bin/python and path/to/venv/bin/pip. Make</span>
<span style="color:#AA0000">    sure you have python3-full installed.</span>
<span style="color:#AA0000">    </span>
<span style="color:#AA0000">    For more information visit http://rptl.io/venv</span>

<span style="color:#AA0000">note: If you believe this is a mistake, please contact your Python installation or OS distribution provider. You can override this, at the risk of breaking your Python installation or OS, by passing --break-system-packages.</span>
<span style="color:#AA0000">hint: See PEP 668 for the detailed specification.</span>


PLAY RECAP ********************************************************************************************************************************************************************************************************
<span style="color:#AA0000">ansible-nas</span>                : <span style="color:#00AA00">ok=32  </span> <span style="color:#AA5500">changed=4   </span> unreachable=0    <span style="color:#AA0000">failed=1   </span> <span style="color:#00AAAA">skipped=25  </span> rescued=0    ignored=0   

Sonntag 21 September 2025  00:55:32 +0200 (0:00:19.017)       0:10:37.765 ***** 
=============================================================================== 
ansible-nas-general : Install some packages -------------------------------------------------------------------------------------------------------------------------------------------------------------- 585.71s
/media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-general/tasks/main.yml:22 ----------------------------------------------------------------------------------------------------------------------------
ansible-nas-docker : Remove docker-py python module ------------------------------------------------------------------------------------------------------------------------------------------------------- 19.02s
/media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-docker/tasks/main.yml:9 ------------------------------------------------------------------------------------------------------------------------------
geerlingguy.nfs : Ensure directories to export exist ------------------------------------------------------------------------------------------------------------------------------------------------------- 5.69s
/home/dietmar/.ansible/roles/geerlingguy.nfs/tasks/main.yml:19 ---------------------------------------------------------------------------------------------------------------------------------------------------
vladgh.samba.server : Install Samba packages --------------------------------------------------------------------------------------------------------------------------------------------------------------- 1.69s
/home/dietmar/.ansible/collections/ansible_collections/vladgh/samba/roles/server/tasks/main.yml:12 ---------------------------------------------------------------------------------------------------------------
ansible-nas-general : Set hostname to RaspiNAS ------------------------------------------------------------------------------------------------------------------------------------------------------------- 1.68s
/media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-general/tasks/main.yml:29 ----------------------------------------------------------------------------------------------------------------------------
geerlingguy.docker : Ensure dependencies are installed. ---------------------------------------------------------------------------------------------------------------------------------------------------- 1.55s
/home/dietmar/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml:10 ----------------------------------------------------------------------------------------------------------------------------------------
geerlingguy.docker : Install docker-compose-plugin (with downgrade option). -------------------------------------------------------------------------------------------------------------------------------- 1.42s
/home/dietmar/.ansible/roles/geerlingguy.docker/tasks/main.yml:44 ------------------------------------------------------------------------------------------------------------------------------------------------
ansible-nas-docker : Install python3-pip ------------------------------------------------------------------------------------------------------------------------------------------------------------------- 1.39s
/media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-docker/tasks/main.yml:2 ------------------------------------------------------------------------------------------------------------------------------
geerlingguy.docker : Ensure additional dependencies are installed (on Ubuntu &lt; 20.04 and any other systems). ----------------------------------------------------------------------------------------------- 1.38s
/home/dietmar/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml:18 ----------------------------------------------------------------------------------------------------------------------------------------
vladgh.samba.server : Install Samba VFS extensions packages ------------------------------------------------------------------------------------------------------------------------------------------------ 1.38s
/home/dietmar/.ansible/collections/ansible_collections/vladgh/samba/roles/server/tasks/main.yml:19 ---------------------------------------------------------------------------------------------------------------
geerlingguy.docker : Install Docker packages (with downgrade option). -------------------------------------------------------------------------------------------------------------------------------------- 1.38s
/home/dietmar/.ansible/roles/geerlingguy.docker/tasks/main.yml:27 ------------------------------------------------------------------------------------------------------------------------------------------------
geerlingguy.nfs : Ensure NFS utilities are installed. ------------------------------------------------------------------------------------------------------------------------------------------------------ 1.37s
/home/dietmar/.ansible/roles/geerlingguy.nfs/tasks/setup-Debian.yml:2 --------------------------------------------------------------------------------------------------------------------------------------------
vladgh.samba.server : Samba configuration ------------------------------------------------------------------------------------------------------------------------------------------------------------------ 1.28s
/home/dietmar/.ansible/collections/ansible_collections/vladgh/samba/roles/server/tasks/main.yml:80 ---------------------------------------------------------------------------------------------------------------
vladgh.samba.server : Start SMB service -------------------------------------------------------------------------------------------------------------------------------------------------------------------- 0.98s
/home/dietmar/.ansible/collections/ansible_collections/vladgh/samba/roles/server/tasks/main.yml:141 --------------------------------------------------------------------------------------------------------------
geerlingguy.docker : Ensure old versions of Docker are not installed. -------------------------------------------------------------------------------------------------------------------------------------- 0.97s
/home/dietmar/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml:2 -----------------------------------------------------------------------------------------------------------------------------------------
ansible-nas-general : Update apt-cache --------------------------------------------------------------------------------------------------------------------------------------------------------------------- 0.96s
/media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-general/tasks/main.yml:7 -----------------------------------------------------------------------------------------------------------------------------
geerlingguy.nfs : Copy exports file. ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- 0.95s
/home/dietmar/.ansible/roles/geerlingguy.nfs/tasks/main.yml:25 ---------------------------------------------------------------------------------------------------------------------------------------------------
ansible-nas-users : Create ansible-nas group --------------------------------------------------------------------------------------------------------------------------------------------------------------- 0.92s
/media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-users/tasks/main.yml:2 -------------------------------------------------------------------------------------------------------------------------------
geerlingguy.docker : Add Docker repository. ---------------------------------------------------------------------------------------------------------------------------------------------------------------- 0.83s
/home/dietmar/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml:50 ----------------------------------------------------------------------------------------------------------------------------------------
ansible-nas-general : Set timezone to Europe/Berlin -------------------------------------------------------------------------------------------------------------------------------------------------------- 0.78s
/media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-general/tasks/main.yml:33 ----------------------------------------------------------------------------------------------------------------------------
[<span style="color:#00AA00">2025-09-21 00:55:32</span>] (venv) [<span style="color:#55FF55"><b>dietmar@MiraPi</b></span>] [<span style="color:#5555FF"><b>.../forked/ansible-nas</b></span>] $ 
</pre>
