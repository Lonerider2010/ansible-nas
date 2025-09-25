<pre>[<span style="color:#00AA00">2025-09-25 05:16:47</span>] (venv) [<span style="color:#55FF55"><b>dietmar@MiraPi</b></span>] [<span style="color:#5555FF"><b>.../forked/ansible-nas</b></span>] $ ansible-playbook -i inventories/RaspiNAS/inventory nas.yml -b 
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
Donnerstag 25 September 2025  05:16:52 +0200 (0:00:00.194)       0:00:00.194 *** 

TASK [ansible-nas-users : Create ansible-nas group] ***************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-users/tasks/main.yml:2</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;gid&quot;: 1001,</span>
<span style="color:#00AA00">    &quot;name&quot;: &quot;ansible-nas&quot;,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;present&quot;,</span>
<span style="color:#00AA00">    &quot;system&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:16:53 +0200 (0:00:01.049)       0:00:01.243 *** 

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
Donnerstag 25 September 2025  05:16:54 +0200 (0:00:00.840)       0:00:02.083 *** 

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
Donnerstag 25 September 2025  05:16:54 +0200 (0:00:00.074)       0:00:02.157 *** 

TASK [vladgh.samba.server : Install Samba packages] ***************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/collections/ansible_collections/vladgh/samba/roles/server/tasks/main.yml:12</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;cache_update_time&quot;: 1758769616,</span>
<span style="color:#00AA00">    &quot;cache_updated&quot;: false,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:16:56 +0200 (0:00:01.842)       0:00:04.000 *** 

TASK [vladgh.samba.server : Install Samba VFS extensions packages] ************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/collections/ansible_collections/vladgh/samba/roles/server/tasks/main.yml:19</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;cache_update_time&quot;: 1758769616,</span>
<span style="color:#00AA00">    &quot;cache_updated&quot;: false,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:16:57 +0200 (0:00:01.416)       0:00:05.417 *** 

TASK [vladgh.samba.server : Register Samba version] ***************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/collections/ansible_collections/vladgh/samba/roles/server/tasks/main.yml:26</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;cmd&quot;: &quot;set -o nounset -o pipefail -o errexit &amp;&amp; smbd --version | sed &apos;s/Version //&apos;\n&quot;,</span>
<span style="color:#00AA00">    &quot;delta&quot;: &quot;0:00:00.043672&quot;,</span>
<span style="color:#00AA00">    &quot;end&quot;: &quot;2025-09-25 05:16:58.437888&quot;,</span>
<span style="color:#00AA00">    &quot;rc&quot;: 0,</span>
<span style="color:#00AA00">    &quot;start&quot;: &quot;2025-09-25 05:16:58.394216&quot;</span>
<span style="color:#00AA00">}</span>

<span style="color:#00AA00">STDOUT:</span>

<span style="color:#00AA00">4.17.12-Debian</span>
Donnerstag 25 September 2025  05:16:58 +0200 (0:00:00.700)       0:00:06.117 *** 
Donnerstag 25 September 2025  05:16:58 +0200 (0:00:00.094)       0:00:06.211 *** 
Donnerstag 25 September 2025  05:16:58 +0200 (0:00:00.041)       0:00:06.253 *** 
Donnerstag 25 September 2025  05:16:58 +0200 (0:00:00.262)       0:00:06.515 *** 
Donnerstag 25 September 2025  05:16:58 +0200 (0:00:00.048)       0:00:06.564 *** 

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
Donnerstag 25 September 2025  05:17:00 +0200 (0:00:01.314)       0:00:07.879 *** 
Donnerstag 25 September 2025  05:17:00 +0200 (0:00:00.058)       0:00:07.937 *** 
Donnerstag 25 September 2025  05:17:00 +0200 (0:00:00.055)       0:00:07.993 *** 
Donnerstag 25 September 2025  05:17:00 +0200 (0:00:00.047)       0:00:08.040 *** 
Donnerstag 25 September 2025  05:17:00 +0200 (0:00:00.052)       0:00:08.093 *** 

TASK [vladgh.samba.server : Start SMB service] ********************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/collections/ansible_collections/vladgh/samba/roles/server/tasks/main.yml:141</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;enabled&quot;: true,</span>
<span style="color:#00AA00">    &quot;name&quot;: &quot;smbd&quot;,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;started&quot;,</span>
<span style="color:#00AA00">    &quot;status&quot;: {</span>
<span style="color:#00AA00">        &quot;ActiveEnterTimestamp&quot;: &quot;Wed 2025-09-24 05:01:24 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;ActiveEnterTimestampMonotonic&quot;: &quot;15779691&quot;,</span>
<span style="color:#00AA00">        &quot;ActiveExitTimestampMonotonic&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;ActiveState&quot;: &quot;active&quot;,</span>
<span style="color:#00AA00">        &quot;After&quot;: &quot;sysinit.target winbind.service nmbd.service system.slice network.target network-online.target basic.target systemd-journald.socket&quot;,</span>
<span style="color:#00AA00">        &quot;AllowIsolate&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;AssertResult&quot;: &quot;yes&quot;,</span>
<span style="color:#00AA00">        &quot;AssertTimestamp&quot;: &quot;Wed 2025-09-24 05:01:24 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;AssertTimestampMonotonic&quot;: &quot;15598410&quot;,</span>
<span style="color:#00AA00">        &quot;Before&quot;: &quot;zfs-share.service multi-user.target shutdown.target&quot;,</span>
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
<span style="color:#00AA00">        &quot;CPUUsageNSec&quot;: &quot;590258000&quot;,</span>
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
<span style="color:#00AA00">        &quot;ConditionTimestamp&quot;: &quot;Wed 2025-09-24 05:01:24 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;ConditionTimestampMonotonic&quot;: &quot;15598406&quot;,</span>
<span style="color:#00AA00">        &quot;ConfigurationDirectoryMode&quot;: &quot;0755&quot;,</span>
<span style="color:#00AA00">        &quot;Conflicts&quot;: &quot;shutdown.target&quot;,</span>
<span style="color:#00AA00">        &quot;ConsistsOf&quot;: &quot;zfs-share.service&quot;,</span>
<span style="color:#00AA00">        &quot;ControlGroup&quot;: &quot;/system.slice/smbd.service&quot;,</span>
<span style="color:#00AA00">        &quot;ControlGroupId&quot;: &quot;3291&quot;,</span>
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
<span style="color:#00AA00">        &quot;ExecCondition&quot;: &quot;{ path=/usr/share/samba/is-configured ; argv[]=/usr/share/samba/is-configured smb ; ignore_errors=no ; start_time=[Wed 2025-09-24 05:01:24 CEST] ; stop_time=[Wed 2025-09-24 05:01:24 CEST] ; pid=1351 ; code=exited ; status=0 }&quot;,</span>
<span style="color:#00AA00">        &quot;ExecConditionEx&quot;: &quot;{ path=/usr/share/samba/is-configured ; argv[]=/usr/share/samba/is-configured smb ; flags= ; start_time=[Wed 2025-09-24 05:01:24 CEST] ; stop_time=[Wed 2025-09-24 05:01:24 CEST] ; pid=1351 ; code=exited ; status=0 }&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainCode&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainExitTimestampMonotonic&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainPID&quot;: &quot;1503&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainStartTimestamp&quot;: &quot;Wed 2025-09-24 05:01:24 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainStartTimestampMonotonic&quot;: &quot;15676525&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainStatus&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;ExecReload&quot;: &quot;{ path=/bin/kill ; argv[]=/bin/kill -HUP $MAINPID ; ignore_errors=no ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }&quot;,</span>
<span style="color:#00AA00">        &quot;ExecReloadEx&quot;: &quot;{ path=/bin/kill ; argv[]=/bin/kill -HUP $MAINPID ; flags= ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }&quot;,</span>
<span style="color:#00AA00">        &quot;ExecStart&quot;: &quot;{ path=/usr/sbin/smbd ; argv[]=/usr/sbin/smbd --foreground --no-process-group $SMBDOPTIONS ; ignore_errors=no ; start_time=[Wed 2025-09-24 05:01:24 CEST] ; stop_time=[n/a] ; pid=1503 ; code=(null) ; status=0/0 }&quot;,</span>
<span style="color:#00AA00">        &quot;ExecStartEx&quot;: &quot;{ path=/usr/sbin/smbd ; argv[]=/usr/sbin/smbd --foreground --no-process-group $SMBDOPTIONS ; flags= ; start_time=[Wed 2025-09-24 05:01:24 CEST] ; stop_time=[n/a] ; pid=1503 ; code=(null) ; status=0/0 }&quot;,</span>
<span style="color:#00AA00">        &quot;ExecStartPre&quot;: &quot;{ path=/usr/share/samba/update-apparmor-samba-profile ; argv[]=/usr/share/samba/update-apparmor-samba-profile ; ignore_errors=no ; start_time=[Wed 2025-09-24 05:01:24 CEST] ; stop_time=[Wed 2025-09-24 05:01:24 CEST] ; pid=1455 ; code=exited ; status=0 }&quot;,</span>
<span style="color:#00AA00">        &quot;ExecStartPreEx&quot;: &quot;{ path=/usr/share/samba/update-apparmor-samba-profile ; argv[]=/usr/share/samba/update-apparmor-samba-profile ; flags= ; start_time=[Wed 2025-09-24 05:01:24 CEST] ; stop_time=[Wed 2025-09-24 05:01:24 CEST] ; pid=1455 ; code=exited ; status=0 }&quot;,</span>
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
<span style="color:#00AA00">        &quot;InactiveExitTimestamp&quot;: &quot;Wed 2025-09-24 05:01:24 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;InactiveExitTimestampMonotonic&quot;: &quot;15616404&quot;,</span>
<span style="color:#00AA00">        &quot;InvocationID&quot;: &quot;58546b6a7ce94188b5cf482d7f9ab477&quot;,</span>
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
<span style="color:#00AA00">        &quot;MainPID&quot;: &quot;1503&quot;,</span>
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
<span style="color:#00AA00">        &quot;StateChangeTimestamp&quot;: &quot;Wed 2025-09-24 05:01:24 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;StateChangeTimestampMonotonic&quot;: &quot;15779691&quot;,</span>
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
Donnerstag 25 September 2025  05:17:01 +0200 (0:00:01.207)       0:00:09.301 *** 

TASK [vladgh.samba.server : Start NMB service] ********************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/collections/ansible_collections/vladgh/samba/roles/server/tasks/main.yml:148</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;enabled&quot;: true,</span>
<span style="color:#00AA00">    &quot;name&quot;: &quot;nmbd&quot;,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;started&quot;,</span>
<span style="color:#00AA00">    &quot;status&quot;: {</span>
<span style="color:#00AA00">        &quot;ActiveEnterTimestamp&quot;: &quot;Wed 2025-09-24 05:01:24 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;ActiveEnterTimestampMonotonic&quot;: &quot;15595577&quot;,</span>
<span style="color:#00AA00">        &quot;ActiveExitTimestampMonotonic&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;ActiveState&quot;: &quot;active&quot;,</span>
<span style="color:#00AA00">        &quot;After&quot;: &quot;network.target system.slice sysinit.target network-online.target systemd-journald.socket basic.target&quot;,</span>
<span style="color:#00AA00">        &quot;AllowIsolate&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;AssertResult&quot;: &quot;yes&quot;,</span>
<span style="color:#00AA00">        &quot;AssertTimestamp&quot;: &quot;Wed 2025-09-24 05:01:24 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;AssertTimestampMonotonic&quot;: &quot;15290171&quot;,</span>
<span style="color:#00AA00">        &quot;Before&quot;: &quot;shutdown.target multi-user.target smbd.service&quot;,</span>
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
<span style="color:#00AA00">        &quot;CPUUsageNSec&quot;: &quot;10211904000&quot;,</span>
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
<span style="color:#00AA00">        &quot;ConditionTimestamp&quot;: &quot;Wed 2025-09-24 05:01:24 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;ConditionTimestampMonotonic&quot;: &quot;15290168&quot;,</span>
<span style="color:#00AA00">        &quot;ConfigurationDirectoryMode&quot;: &quot;0755&quot;,</span>
<span style="color:#00AA00">        &quot;Conflicts&quot;: &quot;shutdown.target&quot;,</span>
<span style="color:#00AA00">        &quot;ControlGroup&quot;: &quot;/system.slice/nmbd.service&quot;,</span>
<span style="color:#00AA00">        &quot;ControlGroupId&quot;: &quot;3019&quot;,</span>
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
<span style="color:#00AA00">        &quot;ExecCondition&quot;: &quot;{ path=/usr/share/samba/is-configured ; argv[]=/usr/share/samba/is-configured nmb ; ignore_errors=no ; start_time=[Wed 2025-09-24 05:01:24 CEST] ; stop_time=[Wed 2025-09-24 05:01:24 CEST] ; pid=1010 ; code=exited ; status=0 }&quot;,</span>
<span style="color:#00AA00">        &quot;ExecConditionEx&quot;: &quot;{ path=/usr/share/samba/is-configured ; argv[]=/usr/share/samba/is-configured nmb ; flags= ; start_time=[Wed 2025-09-24 05:01:24 CEST] ; stop_time=[Wed 2025-09-24 05:01:24 CEST] ; pid=1010 ; code=exited ; status=0 }&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainCode&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainExitTimestampMonotonic&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainPID&quot;: &quot;1159&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainStartTimestamp&quot;: &quot;Wed 2025-09-24 05:01:24 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainStartTimestampMonotonic&quot;: &quot;15515457&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainStatus&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;ExecReload&quot;: &quot;{ path=/bin/kill ; argv[]=/bin/kill -HUP $MAINPID ; ignore_errors=no ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }&quot;,</span>
<span style="color:#00AA00">        &quot;ExecReloadEx&quot;: &quot;{ path=/bin/kill ; argv[]=/bin/kill -HUP $MAINPID ; flags= ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }&quot;,</span>
<span style="color:#00AA00">        &quot;ExecStart&quot;: &quot;{ path=/usr/sbin/nmbd ; argv[]=/usr/sbin/nmbd --foreground --no-process-group $NMBDOPTIONS ; ignore_errors=no ; start_time=[Wed 2025-09-24 05:01:24 CEST] ; stop_time=[n/a] ; pid=1159 ; code=(null) ; status=0/0 }&quot;,</span>
<span style="color:#00AA00">        &quot;ExecStartEx&quot;: &quot;{ path=/usr/sbin/nmbd ; argv[]=/usr/sbin/nmbd --foreground --no-process-group $NMBDOPTIONS ; flags= ; start_time=[Wed 2025-09-24 05:01:24 CEST] ; stop_time=[n/a] ; pid=1159 ; code=(null) ; status=0/0 }&quot;,</span>
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
<span style="color:#00AA00">        &quot;InactiveExitTimestamp&quot;: &quot;Wed 2025-09-24 05:01:24 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;InactiveExitTimestampMonotonic&quot;: &quot;15291624&quot;,</span>
<span style="color:#00AA00">        &quot;InvocationID&quot;: &quot;b6c82df007a84abb9d0fb455912db0b4&quot;,</span>
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
<span style="color:#00AA00">        &quot;MainPID&quot;: &quot;1159&quot;,</span>
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
<span style="color:#00AA00">        &quot;StateChangeTimestamp&quot;: &quot;Wed 2025-09-24 05:01:24 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;StateChangeTimestampMonotonic&quot;: &quot;15595577&quot;,</span>
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
Donnerstag 25 September 2025  05:17:02 +0200 (0:00:00.581)       0:00:09.882 *** 
Donnerstag 25 September 2025  05:17:02 +0200 (0:00:00.059)       0:00:09.941 *** 

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
Donnerstag 25 September 2025  05:17:02 +0200 (0:00:00.060)       0:00:10.002 *** 
Donnerstag 25 September 2025  05:17:02 +0200 (0:00:00.042)       0:00:10.045 *** 
Donnerstag 25 September 2025  05:17:02 +0200 (0:00:00.054)       0:00:10.100 *** 

TASK [geerlingguy.nfs : include_tasks] ****************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.nfs/tasks/main.yml:16</b></span>
<span style="color:#00AAAA">included: /home/dietmar/.ansible/roles/geerlingguy.nfs/tasks/setup-Debian.yml for ansible-nas</span>
Donnerstag 25 September 2025  05:17:02 +0200 (0:00:00.094)       0:00:10.194 *** 

TASK [geerlingguy.nfs : Ensure NFS utilities are installed.] ******************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.nfs/tasks/setup-Debian.yml:2</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;cache_update_time&quot;: 1758769616,</span>
<span style="color:#00AA00">    &quot;cache_updated&quot;: false,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:17:03 +0200 (0:00:01.373)       0:00:11.568 *** 

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
Donnerstag 25 September 2025  05:17:10 +0200 (0:00:06.106)       0:00:17.674 *** 

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
Donnerstag 25 September 2025  05:17:10 +0200 (0:00:00.675)       0:00:18.350 *** 

TASK [geerlingguy.nfs : Ensure nfs is running.] *******************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.nfs/tasks/main.yml:34</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;enabled&quot;: true,</span>
<span style="color:#00AA00">    &quot;name&quot;: &quot;nfs-kernel-server&quot;,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;started&quot;,</span>
<span style="color:#00AA00">    &quot;status&quot;: {</span>
<span style="color:#00AA00">        &quot;ActiveEnterTimestamp&quot;: &quot;Wed 2025-09-24 05:01:25 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;ActiveEnterTimestampMonotonic&quot;: &quot;15957221&quot;,</span>
<span style="color:#00AA00">        &quot;ActiveExitTimestampMonotonic&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;ActiveState&quot;: &quot;active&quot;,</span>
<span style="color:#00AA00">        &quot;After&quot;: &quot;nfs-idmapd.service mnt-Volume1.mount zfs-share.service nfs-mountd.service network-online.target gssproxy.service -.mount local-fs.target rpc-statd.service rpc-gssd.service rpcbind.socket proc-fs-nfsd.mount system.slice nfsdcld.service rpc-svcgssd.service systemd-journald.socket&quot;,</span>
<span style="color:#00AA00">        &quot;AllowIsolate&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;AssertResult&quot;: &quot;yes&quot;,</span>
<span style="color:#00AA00">        &quot;AssertTimestamp&quot;: &quot;Wed 2025-09-24 05:01:25 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;AssertTimestampMonotonic&quot;: &quot;15831194&quot;,</span>
<span style="color:#00AA00">        &quot;Before&quot;: &quot;media-web.mount rpc-statd-notify.service media-Dokumente.mount media-Medien.mount media-Produktion.mount&quot;,</span>
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
<span style="color:#00AA00">        &quot;CPUUsageNSec&quot;: &quot;5851000&quot;,</span>
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
<span style="color:#00AA00">        &quot;ConditionTimestamp&quot;: &quot;Wed 2025-09-24 05:01:25 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;ConditionTimestampMonotonic&quot;: &quot;15831192&quot;,</span>
<span style="color:#00AA00">        &quot;ConfigurationDirectoryMode&quot;: &quot;0755&quot;,</span>
<span style="color:#00AA00">        &quot;ConsistsOf&quot;: &quot;zfs-share.service rpc-svcgssd.service&quot;,</span>
<span style="color:#00AA00">        &quot;ControlGroupId&quot;: &quot;3393&quot;,</span>
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
<span style="color:#00AA00">        &quot;ExecMainExitTimestamp&quot;: &quot;Wed 2025-09-24 05:01:25 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainExitTimestampMonotonic&quot;: &quot;15957094&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainPID&quot;: &quot;1777&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainStartTimestamp&quot;: &quot;Wed 2025-09-24 05:01:25 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainStartTimestampMonotonic&quot;: &quot;15842600&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainStatus&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;ExecReload&quot;: &quot;{ path=/usr/sbin/exportfs ; argv[]=/usr/sbin/exportfs -r ; ignore_errors=yes ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }&quot;,</span>
<span style="color:#00AA00">        &quot;ExecReloadEx&quot;: &quot;{ path=/usr/sbin/exportfs ; argv[]=/usr/sbin/exportfs -r ; flags=ignore-failure ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }&quot;,</span>
<span style="color:#00AA00">        &quot;ExecStart&quot;: &quot;{ path=/usr/sbin/rpc.nfsd ; argv[]=/usr/sbin/rpc.nfsd ; ignore_errors=no ; start_time=[Wed 2025-09-24 05:01:25 CEST] ; stop_time=[Wed 2025-09-24 05:01:25 CEST] ; pid=1777 ; code=exited ; status=0 }&quot;,</span>
<span style="color:#00AA00">        &quot;ExecStartEx&quot;: &quot;{ path=/usr/sbin/rpc.nfsd ; argv[]=/usr/sbin/rpc.nfsd ; flags= ; start_time=[Wed 2025-09-24 05:01:25 CEST] ; stop_time=[Wed 2025-09-24 05:01:25 CEST] ; pid=1777 ; code=exited ; status=0 }&quot;,</span>
<span style="color:#00AA00">        &quot;ExecStartPre&quot;: &quot;{ path=/usr/sbin/exportfs ; argv[]=/usr/sbin/exportfs -r ; ignore_errors=yes ; start_time=[Wed 2025-09-24 05:01:25 CEST] ; stop_time=[Wed 2025-09-24 05:01:25 CEST] ; pid=1764 ; code=exited ; status=0 }&quot;,</span>
<span style="color:#00AA00">        &quot;ExecStartPreEx&quot;: &quot;{ path=/usr/sbin/exportfs ; argv[]=/usr/sbin/exportfs -r ; flags=ignore-failure ; start_time=[Wed 2025-09-24 05:01:25 CEST] ; stop_time=[Wed 2025-09-24 05:01:25 CEST] ; pid=1764 ; code=exited ; status=0 }&quot;,</span>
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
<span style="color:#00AA00">        &quot;InactiveExitTimestamp&quot;: &quot;Wed 2025-09-24 05:01:25 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;InactiveExitTimestampMonotonic&quot;: &quot;15832769&quot;,</span>
<span style="color:#00AA00">        &quot;InvocationID&quot;: &quot;a539cf5d22064cb2951441d9a2a66c47&quot;,</span>
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
<span style="color:#00AA00">        &quot;Requires&quot;: &quot;proc-fs-nfsd.mount mnt-Volume1.mount -.mount nfs-mountd.service network.target system.slice&quot;,</span>
<span style="color:#00AA00">        &quot;RequiresMountsFor&quot;: &quot;/mnt/Volume1/local/Documents /mnt/Volume1/local/Books /mnt/Volume1/local/Media /mnt/Volume1/local/TV /mnt/Volume1/local/Inventar /mnt/Volume1/docker /mnt/Volume1/local/Download /mnt/Volume1/local/Movies /mnt/Volume1/local/IT /mnt/Volume1/local/Comics /mnt/Volume1/local/Persönliches /mnt/Volume1/local/Music /mnt/Volume1/local/Organisation /mnt/Volume1/local/Audiobooks /mnt/Volume1/local/Ägyptologie /mnt/Volume1/local/Podcasts /mnt/Volume1/local/Photos /mnt/Volume1/local/Versorgung&quot;,</span>
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
<span style="color:#00AA00">        &quot;StateChangeTimestamp&quot;: &quot;Wed 2025-09-24 05:01:25 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;StateChangeTimestampMonotonic&quot;: &quot;15957221&quot;,</span>
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
<span style="color:#00AA00">        &quot;Wants&quot;: &quot;rpcbind.socket nfsdcld.service rpc-statd.service rpc-svcgssd.service auth-rpcgss-module.service network-online.target nfs-idmapd.service rpc-statd-notify.service&quot;,</span>
<span style="color:#00AA00">        &quot;WatchdogSignal&quot;: &quot;6&quot;,</span>
<span style="color:#00AA00">        &quot;WatchdogTimestampMonotonic&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;WatchdogUSec&quot;: &quot;0&quot;</span>
<span style="color:#00AA00">    }</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:17:11 +0200 (0:00:00.717)       0:00:19.067 *** 

TASK [geerlingguy.docker : Load OS-specific vars.] ****************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.docker/tasks/main.yml:2</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;ansible_facts&quot;: {},</span>
<span style="color:#00AA00">    &quot;ansible_included_var_files&quot;: [</span>
<span style="color:#00AA00">        &quot;/home/dietmar/.ansible/roles/geerlingguy.docker/vars/main.yml&quot;</span>
<span style="color:#00AA00">    ],</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:17:11 +0200 (0:00:00.049)       0:00:19.117 *** 
Donnerstag 25 September 2025  05:17:11 +0200 (0:00:00.046)       0:00:19.163 *** 

TASK [geerlingguy.docker : include_tasks] *************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.docker/tasks/main.yml:16</b></span>
<span style="color:#00AAAA">included: /home/dietmar/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml for ansible-nas</span>
Donnerstag 25 September 2025  05:17:11 +0200 (0:00:00.080)       0:00:19.243 *** 

TASK [geerlingguy.docker : Ensure old versions of Docker are not installed.] **************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml:2</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:17:12 +0200 (0:00:00.994)       0:00:20.238 *** 

TASK [geerlingguy.docker : Ensure dependencies are installed.] ****************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml:10</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;cache_update_time&quot;: 1758769616,</span>
<span style="color:#00AA00">    &quot;cache_updated&quot;: false,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:17:14 +0200 (0:00:01.409)       0:00:21.647 *** 

TASK [geerlingguy.docker : Ensure additional dependencies are installed (on Ubuntu &lt; 20.04 and any other systems).] ***********************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml:18</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;cache_update_time&quot;: 1758769616,</span>
<span style="color:#00AA00">    &quot;cache_updated&quot;: false,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:17:15 +0200 (0:00:01.381)       0:00:23.029 *** 
Donnerstag 25 September 2025  05:17:15 +0200 (0:00:00.061)       0:00:23.090 *** 

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
Donnerstag 25 September 2025  05:17:16 +0200 (0:00:00.903)       0:00:23.994 *** 
Donnerstag 25 September 2025  05:17:16 +0200 (0:00:00.097)       0:00:24.092 *** 
Donnerstag 25 September 2025  05:17:16 +0200 (0:00:00.080)       0:00:24.172 *** 

TASK [geerlingguy.docker : Add Docker repository.] ****************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml:50</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;repo&quot;: &quot;deb [arch=arm64 signed-by=/etc/apt/trusted.gpg.d/docker.asc] https://download.docker.com/linux/debian bookworm stable&quot;,</span>
<span style="color:#00AA00">    &quot;sources_added&quot;: [],</span>
<span style="color:#00AA00">    &quot;sources_removed&quot;: [],</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;present&quot;</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:17:17 +0200 (0:00:00.916)       0:00:25.089 *** 
Donnerstag 25 September 2025  05:17:17 +0200 (0:00:00.051)       0:00:25.141 *** 

TASK [geerlingguy.docker : Install Docker packages (with downgrade option).] **************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.docker/tasks/main.yml:27</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;cache_update_time&quot;: 1758769616,</span>
<span style="color:#00AA00">    &quot;cache_updated&quot;: false,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:17:18 +0200 (0:00:01.398)       0:00:26.539 *** 
Donnerstag 25 September 2025  05:17:19 +0200 (0:00:00.085)       0:00:26.624 *** 

TASK [geerlingguy.docker : Install docker-compose-plugin (with downgrade option).] ********************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.docker/tasks/main.yml:44</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;cache_update_time&quot;: 1758769616,</span>
<span style="color:#00AA00">    &quot;cache_updated&quot;: false,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:17:20 +0200 (0:00:01.470)       0:00:28.095 *** 
Donnerstag 25 September 2025  05:17:20 +0200 (0:00:00.083)       0:00:28.178 *** 
Donnerstag 25 September 2025  05:17:20 +0200 (0:00:00.090)       0:00:28.268 *** 

TASK [geerlingguy.docker : Ensure Docker is started and enabled at boot.] *****************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.docker/tasks/main.yml:68</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;enabled&quot;: true,</span>
<span style="color:#00AA00">    &quot;name&quot;: &quot;docker&quot;,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;started&quot;,</span>
<span style="color:#00AA00">    &quot;status&quot;: {</span>
<span style="color:#00AA00">        &quot;ActiveEnterTimestamp&quot;: &quot;Wed 2025-09-24 05:01:26 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;ActiveEnterTimestampMonotonic&quot;: &quot;16908581&quot;,</span>
<span style="color:#00AA00">        &quot;ActiveExitTimestampMonotonic&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;ActiveState&quot;: &quot;active&quot;,</span>
<span style="color:#00AA00">        &quot;After&quot;: &quot;time-set.target system.slice firewalld.service docker.socket systemd-journald.socket network-online.target nss-lookup.target basic.target sysinit.target containerd.service&quot;,</span>
<span style="color:#00AA00">        &quot;AllowIsolate&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;AssertResult&quot;: &quot;yes&quot;,</span>
<span style="color:#00AA00">        &quot;AssertTimestamp&quot;: &quot;Wed 2025-09-24 05:01:24 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;AssertTimestampMonotonic&quot;: &quot;15285226&quot;,</span>
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
<span style="color:#00AA00">        &quot;CPUUsageNSec&quot;: &quot;61514109000&quot;,</span>
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
<span style="color:#00AA00">        &quot;ConditionTimestamp&quot;: &quot;Wed 2025-09-24 05:01:24 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;ConditionTimestampMonotonic&quot;: &quot;15285223&quot;,</span>
<span style="color:#00AA00">        &quot;ConfigurationDirectoryMode&quot;: &quot;0755&quot;,</span>
<span style="color:#00AA00">        &quot;Conflicts&quot;: &quot;shutdown.target&quot;,</span>
<span style="color:#00AA00">        &quot;ControlGroup&quot;: &quot;/system.slice/docker.service&quot;,</span>
<span style="color:#00AA00">        &quot;ControlGroupId&quot;: &quot;2951&quot;,</span>
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
<span style="color:#00AA00">        &quot;ExecMainPID&quot;: &quot;1008&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainStartTimestamp&quot;: &quot;Wed 2025-09-24 05:01:24 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainStartTimestampMonotonic&quot;: &quot;15286638&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainStatus&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;ExecReload&quot;: &quot;{ path=/bin/kill ; argv[]=/bin/kill -s HUP $MAINPID ; ignore_errors=no ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }&quot;,</span>
<span style="color:#00AA00">        &quot;ExecReloadEx&quot;: &quot;{ path=/bin/kill ; argv[]=/bin/kill -s HUP $MAINPID ; flags= ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }&quot;,</span>
<span style="color:#00AA00">        &quot;ExecStart&quot;: &quot;{ path=/usr/bin/dockerd ; argv[]=/usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock ; ignore_errors=no ; start_time=[Wed 2025-09-24 05:01:24 CEST] ; stop_time=[n/a] ; pid=1008 ; code=(null) ; status=0/0 }&quot;,</span>
<span style="color:#00AA00">        &quot;ExecStartEx&quot;: &quot;{ path=/usr/bin/dockerd ; argv[]=/usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock ; flags= ; start_time=[Wed 2025-09-24 05:01:24 CEST] ; stop_time=[n/a] ; pid=1008 ; code=(null) ; status=0/0 }&quot;,</span>
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
<span style="color:#00AA00">        &quot;InactiveExitTimestamp&quot;: &quot;Wed 2025-09-24 05:01:24 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;InactiveExitTimestampMonotonic&quot;: &quot;15287016&quot;,</span>
<span style="color:#00AA00">        &quot;InvocationID&quot;: &quot;b0ee2620be884b6780fe55a640bd50e6&quot;,</span>
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
<span style="color:#00AA00">        &quot;MainPID&quot;: &quot;1008&quot;,</span>
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
<span style="color:#00AA00">        &quot;Requires&quot;: &quot;sysinit.target system.slice docker.socket&quot;,</span>
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
<span style="color:#00AA00">        &quot;StateChangeTimestamp&quot;: &quot;Wed 2025-09-24 05:01:26 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;StateChangeTimestampMonotonic&quot;: &quot;16908581&quot;,</span>
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
<span style="color:#00AA00">        &quot;TasksCurrent&quot;: &quot;56&quot;,</span>
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
Donnerstag 25 September 2025  05:17:21 +0200 (0:00:00.587)       0:00:28.855 *** 
<span style="color:#0000AA">META: triggered running handlers for ansible-nas</span>
Donnerstag 25 September 2025  05:17:21 +0200 (0:00:00.023)       0:00:28.879 *** 
Donnerstag 25 September 2025  05:17:21 +0200 (0:00:00.204)       0:00:29.083 *** 
Donnerstag 25 September 2025  05:17:21 +0200 (0:00:00.081)       0:00:29.165 *** 
Donnerstag 25 September 2025  05:17:21 +0200 (0:00:00.036)       0:00:29.202 *** 
Donnerstag 25 September 2025  05:17:21 +0200 (0:00:00.082)       0:00:29.284 *** 

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
Donnerstag 25 September 2025  05:17:22 +0200 (0:00:00.622)       0:00:29.906 *** 

TASK [ansible-nas-general : Update apt-cache] *********************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-general/tasks/main.yml:7</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;attempts&quot;: 1,</span>
<span style="color:#00AA00">    &quot;cache_update_time&quot;: 1758769616,</span>
<span style="color:#00AA00">    &quot;cache_updated&quot;: false,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:17:23 +0200 (0:00:00.998)       0:00:30.905 *** 
Donnerstag 25 September 2025  05:17:23 +0200 (0:00:00.039)       0:00:30.944 *** 

TASK [ansible-nas-general : Install some packages] ****************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-general/tasks/main.yml:22</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;attempts&quot;: 1,</span>
<span style="color:#00AA00">    &quot;cache_update_time&quot;: 1758769616,</span>
<span style="color:#00AA00">    &quot;cache_updated&quot;: false,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:17:24 +0200 (0:00:01.439)       0:00:32.384 *** 

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
Donnerstag 25 September 2025  05:17:26 +0200 (0:00:01.276)       0:00:33.661 *** 

TASK [ansible-nas-general : Set timezone to Europe/Berlin] ********************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-general/tasks/main.yml:33</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:17:26 +0200 (0:00:00.871)       0:00:34.533 *** 
Donnerstag 25 September 2025  05:17:26 +0200 (0:00:00.065)       0:00:34.599 *** 

TASK [ansible-nas-docker : Install python3-pip] *******************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-docker/tasks/main.yml:2</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;attempts&quot;: 1,</span>
<span style="color:#00AA00">    &quot;cache_update_time&quot;: 1758769616,</span>
<span style="color:#00AA00">    &quot;cache_updated&quot;: false,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:17:28 +0200 (0:00:01.371)       0:00:35.970 *** 

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
Donnerstag 25 September 2025  05:17:28 +0200 (0:00:00.634)       0:00:36.604 *** 

TASK [ansible-nas-docker : Remove &quot;ext-managed&quot;] ******************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-docker/tasks/main.yml:14</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;path&quot;: &quot;/usr/lib/python3.11/EXTERNALLY-MANAGED&quot;,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;absent&quot;</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:17:29 +0200 (0:00:00.379)       0:00:36.984 *** 

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

Donnerstag 25 September 2025  05:17:30 +0200 (0:00:01.313)       0:00:38.298 *** 

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

Donnerstag 25 September 2025  05:17:31 +0200 (0:00:01.288)       0:00:39.587 *** 

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
Donnerstag 25 September 2025  05:17:32 +0200 (0:00:00.381)       0:00:39.969 *** 

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
Donnerstag 25 September 2025  05:17:32 +0200 (0:00:00.417)       0:00:40.386 *** 

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
Donnerstag 25 September 2025  05:17:33 +0200 (0:00:00.657)       0:00:41.044 *** 
Donnerstag 25 September 2025  05:17:33 +0200 (0:00:00.191)       0:00:41.235 *** 
Donnerstag 25 September 2025  05:17:33 +0200 (0:00:00.049)       0:00:41.285 *** 

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
Donnerstag 25 September 2025  05:17:33 +0200 (0:00:00.088)       0:00:41.373 *** 
Donnerstag 25 September 2025  05:17:33 +0200 (0:00:00.071)       0:00:41.445 *** 
Donnerstag 25 September 2025  05:17:33 +0200 (0:00:00.058)       0:00:41.504 *** 

TASK [airsonic : Stop Airsonic] ***********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/airsonic/tasks/main.yml:37</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:17:35 +0200 (0:00:01.258)       0:00:42.763 *** 
Donnerstag 25 September 2025  05:17:35 +0200 (0:00:00.062)       0:00:42.825 *** 
Donnerstag 25 September 2025  05:17:35 +0200 (0:00:00.056)       0:00:42.882 *** 
Donnerstag 25 September 2025  05:17:35 +0200 (0:00:00.053)       0:00:42.936 *** 
Donnerstag 25 September 2025  05:17:35 +0200 (0:00:00.056)       0:00:42.993 *** 

TASK [apcupsd : Stop Apcupsd] *************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/apcupsd/tasks/main.yml:44</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:17:35 +0200 (0:00:00.615)       0:00:43.608 *** 
Donnerstag 25 September 2025  05:17:36 +0200 (0:00:00.086)       0:00:43.694 *** 
Donnerstag 25 September 2025  05:17:36 +0200 (0:00:00.063)       0:00:43.758 *** 

TASK [bazarr : Stop Bazarr] ***************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/bazarr/tasks/main.yml:46</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:17:36 +0200 (0:00:00.641)       0:00:44.399 *** 
Donnerstag 25 September 2025  05:17:36 +0200 (0:00:00.056)       0:00:44.456 *** 
Donnerstag 25 September 2025  05:17:36 +0200 (0:00:00.074)       0:00:44.530 *** 
Donnerstag 25 September 2025  05:17:36 +0200 (0:00:00.058)       0:00:44.588 *** 
Donnerstag 25 September 2025  05:17:37 +0200 (0:00:00.184)       0:00:44.772 *** 

TASK [bitwarden : Stop Bitwarden] *********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/bitwarden/tasks/main.yml:64</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:17:37 +0200 (0:00:00.586)       0:00:45.359 *** 

TASK [bitwarden : Stop Bitwarden Backup] **************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/bitwarden/tasks/main.yml:69</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:17:38 +0200 (0:00:00.617)       0:00:45.976 *** 
Donnerstag 25 September 2025  05:17:38 +0200 (0:00:00.077)       0:00:46.054 *** 
Donnerstag 25 September 2025  05:17:38 +0200 (0:00:00.057)       0:00:46.111 *** 

TASK [booksonic : Stop Booksonic] *********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/booksonic/tasks/main.yml:42</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:17:39 +0200 (0:00:00.617)       0:00:46.728 *** 

TASK [calibre : Create Calibre Directories] ***********************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/calibre/tasks/main.yml:4</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; (item=/mnt/Volume1/docker/calibre/data) =&gt; {</span>
<span style="color:#00AA00">    &quot;ansible_loop_var&quot;: &quot;item&quot;,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;gid&quot;: 0,</span>
<span style="color:#00AA00">    &quot;group&quot;: &quot;root&quot;,</span>
<span style="color:#00AA00">    &quot;item&quot;: &quot;/mnt/Volume1/docker/calibre/data&quot;,</span>
<span style="color:#00AA00">    &quot;mode&quot;: &quot;0755&quot;,</span>
<span style="color:#00AA00">    &quot;owner&quot;: &quot;root&quot;,</span>
<span style="color:#00AA00">    &quot;path&quot;: &quot;/mnt/Volume1/docker/calibre/data&quot;,</span>
<span style="color:#00AA00">    &quot;size&quot;: 4096,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;directory&quot;,</span>
<span style="color:#00AA00">    &quot;uid&quot;: 0</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:17:39 +0200 (0:00:00.395)       0:00:47.124 *** 

TASK [calibre : Calibre Docker Container] *************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/calibre/tasks/main.yml:12</b></span>
<span style="color:#FF55FF"><b>[WARNING]: Docker warning: Your kernel does not support memory limit capabilities or the cgroup is not mounted. Limitation discarded.</b></span>
<span style="color:#AA5500">changed: [ansible-nas] =&gt; {</span>
<span style="color:#AA5500">    &quot;changed&quot;: true,</span>
<span style="color:#AA5500">    &quot;container&quot;: {</span>
<span style="color:#AA5500">        &quot;AppArmorProfile&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">        &quot;Args&quot;: [],</span>
<span style="color:#AA5500">        &quot;Config&quot;: {</span>
<span style="color:#AA5500">            &quot;AttachStderr&quot;: true,</span>
<span style="color:#AA5500">            &quot;AttachStdin&quot;: false,</span>
<span style="color:#AA5500">            &quot;AttachStdout&quot;: true,</span>
<span style="color:#AA5500">            &quot;Cmd&quot;: null,</span>
<span style="color:#AA5500">            &quot;Domainname&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;Entrypoint&quot;: [</span>
<span style="color:#AA5500">                &quot;/init&quot;</span>
<span style="color:#AA5500">            ],</span>
<span style="color:#AA5500">            &quot;Env&quot;: [</span>
<span style="color:#AA5500">                &quot;TZ=Europe/Berlin&quot;,</span>
<span style="color:#AA5500">                &quot;PUID=0&quot;,</span>
<span style="color:#AA5500">                &quot;PGID=0&quot;,</span>
<span style="color:#AA5500">                &quot;PASSWORD=&quot;,</span>
<span style="color:#AA5500">                &quot;CLI_ARGS=&quot;,</span>
<span style="color:#AA5500">                &quot;DOCKER_MODS=linuxserver/mods:universal-package-install&quot;,</span>
<span style="color:#AA5500">                &quot;INSTALL_PACKAGES=evince&quot;,</span>
<span style="color:#AA5500">                &quot;PATH=/lsiopy/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin&quot;,</span>
<span style="color:#AA5500">                &quot;HOME=/config&quot;,</span>
<span style="color:#AA5500">                &quot;LANGUAGE=en_US.UTF-8&quot;,</span>
<span style="color:#AA5500">                &quot;LANG=en_US.UTF-8&quot;,</span>
<span style="color:#AA5500">                &quot;TERM=xterm&quot;,</span>
<span style="color:#AA5500">                &quot;S6_CMD_WAIT_FOR_SERVICES_MAXTIME=0&quot;,</span>
<span style="color:#AA5500">                &quot;S6_VERBOSITY=1&quot;,</span>
<span style="color:#AA5500">                &quot;S6_STAGE2_HOOK=/docker-mods&quot;,</span>
<span style="color:#AA5500">                &quot;VIRTUAL_ENV=/lsiopy&quot;,</span>
<span style="color:#AA5500">                &quot;DISPLAY=:1&quot;,</span>
<span style="color:#AA5500">                &quot;PERL5LIB=/usr/local/bin&quot;,</span>
<span style="color:#AA5500">                &quot;OMP_WAIT_POLICY=PASSIVE&quot;,</span>
<span style="color:#AA5500">                &quot;GOMP_SPINCOUNT=0&quot;,</span>
<span style="color:#AA5500">                &quot;START_DOCKER=true&quot;,</span>
<span style="color:#AA5500">                &quot;PULSE_RUNTIME_PATH=/defaults&quot;,</span>
<span style="color:#AA5500">                &quot;NVIDIA_DRIVER_CAPABILITIES=all&quot;,</span>
<span style="color:#AA5500">                &quot;LSIO_FIRST_PARTY=true&quot;,</span>
<span style="color:#AA5500">                &quot;CUSTOM_PORT=8080&quot;,</span>
<span style="color:#AA5500">                &quot;CUSTOM_HTTPS_PORT=8181&quot;,</span>
<span style="color:#AA5500">                &quot;TITLE=Calibre&quot;,</span>
<span style="color:#AA5500">                &quot;QTWEBENGINE_DISABLE_SANDBOX=1&quot;</span>
<span style="color:#AA5500">            ],</span>
<span style="color:#AA5500">            &quot;ExposedPorts&quot;: {</span>
<span style="color:#AA5500">                &quot;3000/tcp&quot;: {},</span>
<span style="color:#AA5500">                &quot;3001/tcp&quot;: {},</span>
<span style="color:#AA5500">                &quot;8080/tcp&quot;: {},</span>
<span style="color:#AA5500">                &quot;8081/tcp&quot;: {}</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            &quot;Hostname&quot;: &quot;f684014bc700&quot;,</span>
<span style="color:#AA5500">            &quot;Image&quot;: &quot;linuxserver/calibre:v8.5.0-ls342&quot;,</span>
<span style="color:#AA5500">            &quot;Labels&quot;: {</span>
<span style="color:#AA5500">                &quot;build_version&quot;: &quot;Linuxserver.io version:- v8.5.0-ls342 Build-date:- 2025-07-02T06:52:10+00:00&quot;,</span>
<span style="color:#AA5500">                &quot;com.kasmweb.image&quot;: &quot;true&quot;,</span>
<span style="color:#AA5500">                &quot;maintainer&quot;: &quot;aptalca&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.authors&quot;: &quot;linuxserver.io&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.created&quot;: &quot;2025-07-02T06:52:10+00:00&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.description&quot;: &quot;[Calibre](https://calibre-ebook.com/) is a powerful and easy to use e-book manager. Users say it&apos;s outstanding and a must-have. It&apos;ll allow you to do nearly everything and it takes things a step beyond normal e-book software. It&apos;s also completely free and open source and great for both casual users and computer experts.&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.documentation&quot;: &quot;https://docs.linuxserver.io/images/docker-calibre&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.licenses&quot;: &quot;GPL-3.0-only&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.ref.name&quot;: &quot;69a9aa2de199a39422e18c5c7ccbffda4d0f973a&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.revision&quot;: &quot;69a9aa2de199a39422e18c5c7ccbffda4d0f973a&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.source&quot;: &quot;https://github.com/linuxserver/docker-calibre&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.title&quot;: &quot;Calibre&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.url&quot;: &quot;https://github.com/linuxserver/docker-calibre/packages&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.vendor&quot;: &quot;linuxserver.io&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.version&quot;: &quot;v8.5.0-ls342&quot;,</span>
<span style="color:#AA5500">                &quot;traefik.enable&quot;: &quot;false&quot;,</span>
<span style="color:#AA5500">                &quot;traefik.http.routers.calibre.rule&quot;: &quot;Host(`calibre.Schneider.nbg`)&quot;,</span>
<span style="color:#AA5500">                &quot;traefik.http.routers.calibre.tls.certresolver&quot;: &quot;letsencrypt&quot;,</span>
<span style="color:#AA5500">                &quot;traefik.http.routers.calibre.tls.domains[0].main&quot;: &quot;Schneider.nbg&quot;,</span>
<span style="color:#AA5500">                &quot;traefik.http.routers.calibre.tls.domains[0].sans&quot;: &quot;*.Schneider.nbg&quot;,</span>
<span style="color:#AA5500">                &quot;traefik.http.services.calibre.loadbalancer.server.port&quot;: &quot;8080&quot;</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            &quot;OnBuild&quot;: null,</span>
<span style="color:#AA5500">            &quot;OpenStdin&quot;: false,</span>
<span style="color:#AA5500">            &quot;StdinOnce&quot;: false,</span>
<span style="color:#AA5500">            &quot;Tty&quot;: false,</span>
<span style="color:#AA5500">            &quot;User&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;Volumes&quot;: {</span>
<span style="color:#AA5500">                &quot;/config&quot;: {}</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            &quot;WorkingDir&quot;: &quot;/&quot;</span>
<span style="color:#AA5500">        },</span>
<span style="color:#AA5500">        &quot;Created&quot;: &quot;2025-09-22T22:06:39.39236107Z&quot;,</span>
<span style="color:#AA5500">        &quot;Driver&quot;: &quot;overlay2&quot;,</span>
<span style="color:#AA5500">        &quot;ExecIDs&quot;: null,</span>
<span style="color:#AA5500">        &quot;GraphDriver&quot;: {</span>
<span style="color:#AA5500">            &quot;Data&quot;: {</span>
<span style="color:#AA5500">                &quot;ID&quot;: &quot;f684014bc700671a290bbaddeb5d9773832bdb8fa5ac8c1d5a78f4441099498d&quot;,</span>
<span style="color:#AA5500">                &quot;LowerDir&quot;: &quot;/var/lib/docker/overlay2/22b6b47b7f2cdab67c9f9d1e73fc7df0184101cdea6fbd793fe67dbebe20eb0b-init/diff:/var/lib/docker/overlay2/11806457bbf8a98e1dd4c29a4f8f1cf559ead486cc3c92f2cb481fe626022456/diff:/var/lib/docker/overlay2/69a78090f02bc414976d1bb711e19a30ec9215a64a5d119c065e531f59915003/diff:/var/lib/docker/overlay2/106ed2454a0a4200ffdf4aed176c6596ca76ab94ece6ae46ce5e17eaa094b574/diff:/var/lib/docker/overlay2/2825ff44cc8023e9c1fa8f28453a865b209221903727e0819f4ba9718f0a914c/diff:/var/lib/docker/overlay2/57742e9f78ceb8c14ad72681383f4d17e22a0a4edd64dd120f293f1945ea7bad/diff:/var/lib/docker/overlay2/0b98fdc6d338a9d820cec1f768cf27f15f0dd312637e22a264ba1592a4357366/diff:/var/lib/docker/overlay2/d658cf210d446fe9a9d791cc21d218c434d90c2f115f524cf2766728473dd66a/diff:/var/lib/docker/overlay2/f46d8b17d3e713cdb9d155a37a23afb034f917180dd2ad787a620e7168980693/diff:/var/lib/docker/overlay2/4636dc4b789bf27dfd9dae8acef3565dc7f55e25cb16ed407be52cb8f7f00bdf/diff:/var/lib/docker/overlay2/15ba3057f9634d96253ddade40cd2591a0d65bc8313f29ca837bcab06062493e/diff:/var/lib/docker/overlay2/59434fb4664377320e412d5c1663f535b88fad648b33b3b06712820a68c4eb32/diff:/var/lib/docker/overlay2/38dbc5f039b4a41c4ed320007a663b840ab410393e18e12ce7769148b9f8bd46/diff:/var/lib/docker/overlay2/37cd6081e7cf496feb4d3b82cbd74be4ec0b9c09b11cb768b93ed43e25822fbf/diff:/var/lib/docker/overlay2/209b78f543ad95e251c2afb52f60bb99abb5798b595d1662894212cfd517baf8/diff&quot;,</span>
<span style="color:#AA5500">                &quot;MergedDir&quot;: &quot;/var/lib/docker/overlay2/22b6b47b7f2cdab67c9f9d1e73fc7df0184101cdea6fbd793fe67dbebe20eb0b/merged&quot;,</span>
<span style="color:#AA5500">                &quot;UpperDir&quot;: &quot;/var/lib/docker/overlay2/22b6b47b7f2cdab67c9f9d1e73fc7df0184101cdea6fbd793fe67dbebe20eb0b/diff&quot;,</span>
<span style="color:#AA5500">                &quot;WorkDir&quot;: &quot;/var/lib/docker/overlay2/22b6b47b7f2cdab67c9f9d1e73fc7df0184101cdea6fbd793fe67dbebe20eb0b/work&quot;</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            &quot;Name&quot;: &quot;overlay2&quot;</span>
<span style="color:#AA5500">        },</span>
<span style="color:#AA5500">        &quot;HostConfig&quot;: {</span>
<span style="color:#AA5500">            &quot;AutoRemove&quot;: false,</span>
<span style="color:#AA5500">            &quot;Binds&quot;: [</span>
<span style="color:#AA5500">                &quot;/mnt/Volume1/docker/calibre/data:/config:rw&quot;,</span>
<span style="color:#AA5500">                &quot;/mnt/Volume1/local/Books:/books:rw&quot;,</span>
<span style="color:#AA5500">                &quot;/mnt/Volume1/local/Comics:/comics:rw&quot;</span>
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
<span style="color:#AA5500">            &quot;Dns&quot;: [],</span>
<span style="color:#AA5500">            &quot;DnsOptions&quot;: [],</span>
<span style="color:#AA5500">            &quot;DnsSearch&quot;: [],</span>
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
<span style="color:#AA5500">                &quot;8080/tcp&quot;: [</span>
<span style="color:#AA5500">                    {</span>
<span style="color:#AA5500">                        &quot;HostIp&quot;: &quot;0.0.0.0&quot;,</span>
<span style="color:#AA5500">                        &quot;HostPort&quot;: &quot;8093&quot;</span>
<span style="color:#AA5500">                    }</span>
<span style="color:#AA5500">                ],</span>
<span style="color:#AA5500">                &quot;8081/tcp&quot;: [</span>
<span style="color:#AA5500">                    {</span>
<span style="color:#AA5500">                        &quot;HostIp&quot;: &quot;0.0.0.0&quot;,</span>
<span style="color:#AA5500">                        &quot;HostPort&quot;: &quot;8094&quot;</span>
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
<span style="color:#AA5500">            &quot;SecurityOpt&quot;: [</span>
<span style="color:#AA5500">                &quot;seccomp=unconfined&quot;</span>
<span style="color:#AA5500">            ],</span>
<span style="color:#AA5500">            &quot;ShmSize&quot;: 67108864,</span>
<span style="color:#AA5500">            &quot;UTSMode&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;Ulimits&quot;: null,</span>
<span style="color:#AA5500">            &quot;UsernsMode&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;VolumeDriver&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;VolumesFrom&quot;: null</span>
<span style="color:#AA5500">        },</span>
<span style="color:#AA5500">        &quot;HostnamePath&quot;: &quot;/var/lib/docker/containers/f684014bc700671a290bbaddeb5d9773832bdb8fa5ac8c1d5a78f4441099498d/hostname&quot;,</span>
<span style="color:#AA5500">        &quot;HostsPath&quot;: &quot;/var/lib/docker/containers/f684014bc700671a290bbaddeb5d9773832bdb8fa5ac8c1d5a78f4441099498d/hosts&quot;,</span>
<span style="color:#AA5500">        &quot;Id&quot;: &quot;f684014bc700671a290bbaddeb5d9773832bdb8fa5ac8c1d5a78f4441099498d&quot;,</span>
<span style="color:#AA5500">        &quot;Image&quot;: &quot;sha256:9b74ab981797b14265293363cc05ac91ff71a0b0dcb0463d65c4480f38ba7ea2&quot;,</span>
<span style="color:#AA5500">        &quot;LogPath&quot;: &quot;/var/lib/docker/containers/f684014bc700671a290bbaddeb5d9773832bdb8fa5ac8c1d5a78f4441099498d/f684014bc700671a290bbaddeb5d9773832bdb8fa5ac8c1d5a78f4441099498d-json.log&quot;,</span>
<span style="color:#AA5500">        &quot;MountLabel&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">        &quot;Mounts&quot;: [</span>
<span style="color:#AA5500">            {</span>
<span style="color:#AA5500">                &quot;Destination&quot;: &quot;/books&quot;,</span>
<span style="color:#AA5500">                &quot;Mode&quot;: &quot;rw&quot;,</span>
<span style="color:#AA5500">                &quot;Propagation&quot;: &quot;rprivate&quot;,</span>
<span style="color:#AA5500">                &quot;RW&quot;: true,</span>
<span style="color:#AA5500">                &quot;Source&quot;: &quot;/mnt/Volume1/local/Books&quot;,</span>
<span style="color:#AA5500">                &quot;Type&quot;: &quot;bind&quot;</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            {</span>
<span style="color:#AA5500">                &quot;Destination&quot;: &quot;/comics&quot;,</span>
<span style="color:#AA5500">                &quot;Mode&quot;: &quot;rw&quot;,</span>
<span style="color:#AA5500">                &quot;Propagation&quot;: &quot;rprivate&quot;,</span>
<span style="color:#AA5500">                &quot;RW&quot;: true,</span>
<span style="color:#AA5500">                &quot;Source&quot;: &quot;/mnt/Volume1/local/Comics&quot;,</span>
<span style="color:#AA5500">                &quot;Type&quot;: &quot;bind&quot;</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            {</span>
<span style="color:#AA5500">                &quot;Destination&quot;: &quot;/config&quot;,</span>
<span style="color:#AA5500">                &quot;Mode&quot;: &quot;rw&quot;,</span>
<span style="color:#AA5500">                &quot;Propagation&quot;: &quot;rprivate&quot;,</span>
<span style="color:#AA5500">                &quot;RW&quot;: true,</span>
<span style="color:#AA5500">                &quot;Source&quot;: &quot;/mnt/Volume1/docker/calibre/data&quot;,</span>
<span style="color:#AA5500">                &quot;Type&quot;: &quot;bind&quot;</span>
<span style="color:#AA5500">            }</span>
<span style="color:#AA5500">        ],</span>
<span style="color:#AA5500">        &quot;Name&quot;: &quot;/calibre&quot;,</span>
<span style="color:#AA5500">        &quot;NetworkSettings&quot;: {</span>
<span style="color:#AA5500">            &quot;Bridge&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;EndpointID&quot;: &quot;2c70536c7ba720b016b2ee2dc5a1140e890ad9264325d3099c2b5a189d7e563d&quot;,</span>
<span style="color:#AA5500">            &quot;Gateway&quot;: &quot;172.17.0.1&quot;,</span>
<span style="color:#AA5500">            &quot;GlobalIPv6Address&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;GlobalIPv6PrefixLen&quot;: 0,</span>
<span style="color:#AA5500">            &quot;HairpinMode&quot;: false,</span>
<span style="color:#AA5500">            &quot;IPAddress&quot;: &quot;172.17.0.3&quot;,</span>
<span style="color:#AA5500">            &quot;IPPrefixLen&quot;: 16,</span>
<span style="color:#AA5500">            &quot;IPv6Gateway&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;LinkLocalIPv6Address&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;LinkLocalIPv6PrefixLen&quot;: 0,</span>
<span style="color:#AA5500">            &quot;MacAddress&quot;: &quot;32:0a:4b:59:0b:b9&quot;,</span>
<span style="color:#AA5500">            &quot;Networks&quot;: {</span>
<span style="color:#AA5500">                &quot;bridge&quot;: {</span>
<span style="color:#AA5500">                    &quot;Aliases&quot;: null,</span>
<span style="color:#AA5500">                    &quot;DNSNames&quot;: null,</span>
<span style="color:#AA5500">                    &quot;DriverOpts&quot;: null,</span>
<span style="color:#AA5500">                    &quot;EndpointID&quot;: &quot;2c70536c7ba720b016b2ee2dc5a1140e890ad9264325d3099c2b5a189d7e563d&quot;,</span>
<span style="color:#AA5500">                    &quot;Gateway&quot;: &quot;172.17.0.1&quot;,</span>
<span style="color:#AA5500">                    &quot;GlobalIPv6Address&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">                    &quot;GlobalIPv6PrefixLen&quot;: 0,</span>
<span style="color:#AA5500">                    &quot;GwPriority&quot;: 0,</span>
<span style="color:#AA5500">                    &quot;IPAMConfig&quot;: null,</span>
<span style="color:#AA5500">                    &quot;IPAddress&quot;: &quot;172.17.0.3&quot;,</span>
<span style="color:#AA5500">                    &quot;IPPrefixLen&quot;: 16,</span>
<span style="color:#AA5500">                    &quot;IPv6Gateway&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">                    &quot;Links&quot;: null,</span>
<span style="color:#AA5500">                    &quot;MacAddress&quot;: &quot;32:0a:4b:59:0b:b9&quot;,</span>
<span style="color:#AA5500">                    &quot;NetworkID&quot;: &quot;bf69c1dd08283d21e1c03cd9d2f9059cf944e578f95c79babe5a23cdb260be15&quot;</span>
<span style="color:#AA5500">                }</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            &quot;Ports&quot;: {</span>
<span style="color:#AA5500">                &quot;3000/tcp&quot;: null,</span>
<span style="color:#AA5500">                &quot;3001/tcp&quot;: null,</span>
<span style="color:#AA5500">                &quot;8080/tcp&quot;: [</span>
<span style="color:#AA5500">                    {</span>
<span style="color:#AA5500">                        &quot;HostIp&quot;: &quot;0.0.0.0&quot;,</span>
<span style="color:#AA5500">                        &quot;HostPort&quot;: &quot;8093&quot;</span>
<span style="color:#AA5500">                    }</span>
<span style="color:#AA5500">                ],</span>
<span style="color:#AA5500">                &quot;8081/tcp&quot;: [</span>
<span style="color:#AA5500">                    {</span>
<span style="color:#AA5500">                        &quot;HostIp&quot;: &quot;0.0.0.0&quot;,</span>
<span style="color:#AA5500">                        &quot;HostPort&quot;: &quot;8094&quot;</span>
<span style="color:#AA5500">                    }</span>
<span style="color:#AA5500">                ]</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            &quot;SandboxID&quot;: &quot;db6a3e090b9ef07fd312a2501feae7e67868fe721857da4e5bbfae4745c6e15d&quot;,</span>
<span style="color:#AA5500">            &quot;SandboxKey&quot;: &quot;/var/run/docker/netns/db6a3e090b9e&quot;,</span>
<span style="color:#AA5500">            &quot;SecondaryIPAddresses&quot;: null,</span>
<span style="color:#AA5500">            &quot;SecondaryIPv6Addresses&quot;: null</span>
<span style="color:#AA5500">        },</span>
<span style="color:#AA5500">        &quot;Path&quot;: &quot;/init&quot;,</span>
<span style="color:#AA5500">        &quot;Platform&quot;: &quot;linux&quot;,</span>
<span style="color:#AA5500">        &quot;ProcessLabel&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">        &quot;ResolvConfPath&quot;: &quot;/var/lib/docker/containers/f684014bc700671a290bbaddeb5d9773832bdb8fa5ac8c1d5a78f4441099498d/resolv.conf&quot;,</span>
<span style="color:#AA5500">        &quot;RestartCount&quot;: 0,</span>
<span style="color:#AA5500">        &quot;State&quot;: {</span>
<span style="color:#AA5500">            &quot;Dead&quot;: false,</span>
<span style="color:#AA5500">            &quot;Error&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;ExitCode&quot;: 0,</span>
<span style="color:#AA5500">            &quot;FinishedAt&quot;: &quot;2025-09-24T03:00:31.724171254Z&quot;,</span>
<span style="color:#AA5500">            &quot;OOMKilled&quot;: false,</span>
<span style="color:#AA5500">            &quot;Paused&quot;: false,</span>
<span style="color:#AA5500">            &quot;Pid&quot;: 2753,</span>
<span style="color:#AA5500">            &quot;Restarting&quot;: false,</span>
<span style="color:#AA5500">            &quot;Running&quot;: true,</span>
<span style="color:#AA5500">            &quot;StartedAt&quot;: &quot;2025-09-24T03:01:25.589145546Z&quot;,</span>
<span style="color:#AA5500">            &quot;Status&quot;: &quot;running&quot;</span>
<span style="color:#AA5500">        }</span>
<span style="color:#AA5500">    }</span>
<span style="color:#AA5500">}</span>
Donnerstag 25 September 2025  05:17:41 +0200 (0:00:02.016)       0:00:49.140 *** 
Donnerstag 25 September 2025  05:17:41 +0200 (0:00:00.072)       0:00:49.213 *** 

TASK [calibreweb : Create Calibre-web Directories] ****************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/calibreweb/tasks/main.yml:4</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; (item=/mnt/Volume1/docker/calibreweb/config) =&gt; {</span>
<span style="color:#00AA00">    &quot;ansible_loop_var&quot;: &quot;item&quot;,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;gid&quot;: 0,</span>
<span style="color:#00AA00">    &quot;group&quot;: &quot;root&quot;,</span>
<span style="color:#00AA00">    &quot;item&quot;: &quot;/mnt/Volume1/docker/calibreweb/config&quot;,</span>
<span style="color:#00AA00">    &quot;mode&quot;: &quot;0777&quot;,</span>
<span style="color:#00AA00">    &quot;owner&quot;: &quot;root&quot;,</span>
<span style="color:#00AA00">    &quot;path&quot;: &quot;/mnt/Volume1/docker/calibreweb/config&quot;,</span>
<span style="color:#00AA00">    &quot;size&quot;: 4096,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;directory&quot;,</span>
<span style="color:#00AA00">    &quot;uid&quot;: 0</span>
<span style="color:#00AA00">}</span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; (item=/mnt/Volume1/docker/calibreweb/data) =&gt; {</span>
<span style="color:#00AA00">    &quot;ansible_loop_var&quot;: &quot;item&quot;,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;gid&quot;: 1001,</span>
<span style="color:#00AA00">    &quot;group&quot;: &quot;ansible-nas&quot;,</span>
<span style="color:#00AA00">    &quot;item&quot;: &quot;/mnt/Volume1/docker/calibreweb/data&quot;,</span>
<span style="color:#00AA00">    &quot;mode&quot;: &quot;0777&quot;,</span>
<span style="color:#00AA00">    &quot;owner&quot;: &quot;1001&quot;,</span>
<span style="color:#00AA00">    &quot;path&quot;: &quot;/mnt/Volume1/docker/calibreweb/data&quot;,</span>
<span style="color:#00AA00">    &quot;size&quot;: 4096,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;directory&quot;,</span>
<span style="color:#00AA00">    &quot;uid&quot;: 1001</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:17:42 +0200 (0:00:00.770)       0:00:49.983 *** 

TASK [calibreweb : Calibre-web Docker Container] ******************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/calibreweb/tasks/main.yml:12</b></span>
<span style="color:#AA5500">changed: [ansible-nas] =&gt; {</span>
<span style="color:#AA5500">    &quot;changed&quot;: true,</span>
<span style="color:#AA5500">    &quot;container&quot;: {</span>
<span style="color:#AA5500">        &quot;AppArmorProfile&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">        &quot;Args&quot;: [],</span>
<span style="color:#AA5500">        &quot;Config&quot;: {</span>
<span style="color:#AA5500">            &quot;AttachStderr&quot;: true,</span>
<span style="color:#AA5500">            &quot;AttachStdin&quot;: false,</span>
<span style="color:#AA5500">            &quot;AttachStdout&quot;: true,</span>
<span style="color:#AA5500">            &quot;Cmd&quot;: null,</span>
<span style="color:#AA5500">            &quot;Domainname&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;Entrypoint&quot;: [</span>
<span style="color:#AA5500">                &quot;/init&quot;</span>
<span style="color:#AA5500">            ],</span>
<span style="color:#AA5500">            &quot;Env&quot;: [</span>
<span style="color:#AA5500">                &quot;TZ=Europe/Berlin&quot;,</span>
<span style="color:#AA5500">                &quot;PUID=0&quot;,</span>
<span style="color:#AA5500">                &quot;PGID=0&quot;,</span>
<span style="color:#AA5500">                &quot;DOCKER_MODS=linuxserver/calibre-web:calibre&quot;,</span>
<span style="color:#AA5500">                &quot;PATH=/lsiopy/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin&quot;,</span>
<span style="color:#AA5500">                &quot;HOME=/root&quot;,</span>
<span style="color:#AA5500">                &quot;LANGUAGE=en_US.UTF-8&quot;,</span>
<span style="color:#AA5500">                &quot;LANG=en_US.UTF-8&quot;,</span>
<span style="color:#AA5500">                &quot;TERM=xterm&quot;,</span>
<span style="color:#AA5500">                &quot;S6_CMD_WAIT_FOR_SERVICES_MAXTIME=0&quot;,</span>
<span style="color:#AA5500">                &quot;S6_VERBOSITY=1&quot;,</span>
<span style="color:#AA5500">                &quot;S6_STAGE2_HOOK=/docker-mods&quot;,</span>
<span style="color:#AA5500">                &quot;VIRTUAL_ENV=/lsiopy&quot;,</span>
<span style="color:#AA5500">                &quot;LSIO_FIRST_PARTY=true&quot;</span>
<span style="color:#AA5500">            ],</span>
<span style="color:#AA5500">            &quot;ExposedPorts&quot;: {</span>
<span style="color:#AA5500">                &quot;8083/tcp&quot;: {}</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            &quot;Hostname&quot;: &quot;930efe3baffa&quot;,</span>
<span style="color:#AA5500">            &quot;Image&quot;: &quot;linuxserver/calibre-web:latest&quot;,</span>
<span style="color:#AA5500">            &quot;Labels&quot;: {</span>
<span style="color:#AA5500">                &quot;build_version&quot;: &quot;Linuxserver.io version:- 0.6.25-ls348 Build-date:- 2025-09-21T02:13:54+00:00&quot;,</span>
<span style="color:#AA5500">                &quot;maintainer&quot;: &quot;notdriz&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.authors&quot;: &quot;linuxserver.io&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.created&quot;: &quot;2025-09-21T02:13:54+00:00&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.description&quot;: &quot;[Calibre-web](https://github.com/janeczku/calibre-web) is a web app providing a clean interface for browsing, reading and downloading eBooks using an existing Calibre database.   It is also possible to integrate google drive and edit metadata and your calibre library through the app itself.    This software is a fork of library and licensed under the GPL v3 License.  &quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.documentation&quot;: &quot;https://docs.linuxserver.io/images/docker-calibre-web&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.licenses&quot;: &quot;GPL-3.0-only&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.ref.name&quot;: &quot;0120fa7eb5599aa3fd3f716096ce882521f55111&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.revision&quot;: &quot;0120fa7eb5599aa3fd3f716096ce882521f55111&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.source&quot;: &quot;https://github.com/linuxserver/docker-calibre-web&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.title&quot;: &quot;Calibre-web&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.url&quot;: &quot;https://github.com/linuxserver/docker-calibre-web/packages&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.vendor&quot;: &quot;linuxserver.io&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.version&quot;: &quot;0.6.25-ls348&quot;,</span>
<span style="color:#AA5500">                &quot;traefik.enable&quot;: &quot;False&quot;,</span>
<span style="color:#AA5500">                &quot;traefik.http.routers.calibreweb.rule&quot;: &quot;Host(`calibreweb.Schneider.nbg`)&quot;,</span>
<span style="color:#AA5500">                &quot;traefik.http.routers.calibreweb.tls.certresolver&quot;: &quot;letsencrypt&quot;,</span>
<span style="color:#AA5500">                &quot;traefik.http.routers.calibreweb.tls.domains[0].main&quot;: &quot;Schneider.nbg&quot;,</span>
<span style="color:#AA5500">                &quot;traefik.http.routers.calibreweb.tls.domains[0].sans&quot;: &quot;*.Schneider.nbg&quot;,</span>
<span style="color:#AA5500">                &quot;traefik.http.services.calibreweb.loadbalancer.server.port&quot;: &quot;8083&quot;</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            &quot;OnBuild&quot;: null,</span>
<span style="color:#AA5500">            &quot;OpenStdin&quot;: false,</span>
<span style="color:#AA5500">            &quot;StdinOnce&quot;: false,</span>
<span style="color:#AA5500">            &quot;Tty&quot;: false,</span>
<span style="color:#AA5500">            &quot;User&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;Volumes&quot;: {</span>
<span style="color:#AA5500">                &quot;/config&quot;: {}</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            &quot;WorkingDir&quot;: &quot;/&quot;</span>
<span style="color:#AA5500">        },</span>
<span style="color:#AA5500">        &quot;Created&quot;: &quot;2025-09-22T22:06:42.225697373Z&quot;,</span>
<span style="color:#AA5500">        &quot;Driver&quot;: &quot;overlay2&quot;,</span>
<span style="color:#AA5500">        &quot;ExecIDs&quot;: null,</span>
<span style="color:#AA5500">        &quot;GraphDriver&quot;: {</span>
<span style="color:#AA5500">            &quot;Data&quot;: {</span>
<span style="color:#AA5500">                &quot;ID&quot;: &quot;930efe3baffaa3a15e545f79ba035a0dee17ceb7c4a45cf59782cc8b0fd4f933&quot;,</span>
<span style="color:#AA5500">                &quot;LowerDir&quot;: &quot;/var/lib/docker/overlay2/0058ad9c324a217d763d460b7de8f1906ab27d7cfa3e841eb26fa768b0d0f373-init/diff:/var/lib/docker/overlay2/e72bd2ef2dcbaafd4d88242c546682f676fe11f3ca02084aea59abb9dee6d39b/diff:/var/lib/docker/overlay2/68fae43c9775297a2a285855ea568a4e1c199587b7356f33313fd73a5e577b40/diff:/var/lib/docker/overlay2/6db510d8c9d02300a7662ad1095cb784a6c41aa9fe8df0d1833c55560656537f/diff:/var/lib/docker/overlay2/1462b433fe0f0270ce01a1193c8fb9474fcacb50060d5d9c03b85dc909760fe6/diff:/var/lib/docker/overlay2/975091e7008975c926e090f6b1894bb0895661b6863381f6428fab261b3d673a/diff:/var/lib/docker/overlay2/d12983daa6c908d6c65014b60fc505b5369065194c39ecbb85ad6c254e4c6594/diff:/var/lib/docker/overlay2/c4224181ed89efa2641a9febec3bed2038e138570059046cc47bdcf82e36e3a6/diff:/var/lib/docker/overlay2/2ad904055a0cc68df9e9fd73ab04e3c739e9d5ddbaa69bdb5bcb6866fd1ba406/diff:/var/lib/docker/overlay2/4f182d8b2a66993fe4bca4982442a3070b1416b0c4be88fd4e1d1acff3a401f1/diff:/var/lib/docker/overlay2/15d90a5d157041a23561f609fbfdcb84faa05a4f89004c566f7515f2caa50d74/diff:/var/lib/docker/overlay2/e7f8c53b573ffb68f123802bea401bfa40cdbff38771a98731866dde43e9f3a6/diff&quot;,</span>
<span style="color:#AA5500">                &quot;MergedDir&quot;: &quot;/var/lib/docker/overlay2/0058ad9c324a217d763d460b7de8f1906ab27d7cfa3e841eb26fa768b0d0f373/merged&quot;,</span>
<span style="color:#AA5500">                &quot;UpperDir&quot;: &quot;/var/lib/docker/overlay2/0058ad9c324a217d763d460b7de8f1906ab27d7cfa3e841eb26fa768b0d0f373/diff&quot;,</span>
<span style="color:#AA5500">                &quot;WorkDir&quot;: &quot;/var/lib/docker/overlay2/0058ad9c324a217d763d460b7de8f1906ab27d7cfa3e841eb26fa768b0d0f373/work&quot;</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            &quot;Name&quot;: &quot;overlay2&quot;</span>
<span style="color:#AA5500">        },</span>
<span style="color:#AA5500">        &quot;HostConfig&quot;: {</span>
<span style="color:#AA5500">            &quot;AutoRemove&quot;: false,</span>
<span style="color:#AA5500">            &quot;Binds&quot;: [</span>
<span style="color:#AA5500">                &quot;/mnt/Volume1/docker/calibreweb/config:/config:rw&quot;,</span>
<span style="color:#AA5500">                &quot;/mnt/Volume1/local/Books:/books:rw&quot;,</span>
<span style="color:#AA5500">                &quot;/mnt/Volume1/docker/calibreweb/data:/data:rw&quot;</span>
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
<span style="color:#AA5500">            &quot;Dns&quot;: [],</span>
<span style="color:#AA5500">            &quot;DnsOptions&quot;: [],</span>
<span style="color:#AA5500">            &quot;DnsSearch&quot;: [],</span>
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
<span style="color:#AA5500">                &quot;8083/tcp&quot;: [</span>
<span style="color:#AA5500">                    {</span>
<span style="color:#AA5500">                        &quot;HostIp&quot;: &quot;0.0.0.0&quot;,</span>
<span style="color:#AA5500">                        &quot;HostPort&quot;: &quot;8084&quot;</span>
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
<span style="color:#AA5500">        &quot;HostnamePath&quot;: &quot;/var/lib/docker/containers/930efe3baffaa3a15e545f79ba035a0dee17ceb7c4a45cf59782cc8b0fd4f933/hostname&quot;,</span>
<span style="color:#AA5500">        &quot;HostsPath&quot;: &quot;/var/lib/docker/containers/930efe3baffaa3a15e545f79ba035a0dee17ceb7c4a45cf59782cc8b0fd4f933/hosts&quot;,</span>
<span style="color:#AA5500">        &quot;Id&quot;: &quot;930efe3baffaa3a15e545f79ba035a0dee17ceb7c4a45cf59782cc8b0fd4f933&quot;,</span>
<span style="color:#AA5500">        &quot;Image&quot;: &quot;sha256:104b65c2ca165c9ff7c02388755b393fdcc521ee13023c9f7977626935eabe3d&quot;,</span>
<span style="color:#AA5500">        &quot;LogPath&quot;: &quot;/var/lib/docker/containers/930efe3baffaa3a15e545f79ba035a0dee17ceb7c4a45cf59782cc8b0fd4f933/930efe3baffaa3a15e545f79ba035a0dee17ceb7c4a45cf59782cc8b0fd4f933-json.log&quot;,</span>
<span style="color:#AA5500">        &quot;MountLabel&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">        &quot;Mounts&quot;: [</span>
<span style="color:#AA5500">            {</span>
<span style="color:#AA5500">                &quot;Destination&quot;: &quot;/books&quot;,</span>
<span style="color:#AA5500">                &quot;Mode&quot;: &quot;rw&quot;,</span>
<span style="color:#AA5500">                &quot;Propagation&quot;: &quot;rprivate&quot;,</span>
<span style="color:#AA5500">                &quot;RW&quot;: true,</span>
<span style="color:#AA5500">                &quot;Source&quot;: &quot;/mnt/Volume1/local/Books&quot;,</span>
<span style="color:#AA5500">                &quot;Type&quot;: &quot;bind&quot;</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            {</span>
<span style="color:#AA5500">                &quot;Destination&quot;: &quot;/config&quot;,</span>
<span style="color:#AA5500">                &quot;Mode&quot;: &quot;rw&quot;,</span>
<span style="color:#AA5500">                &quot;Propagation&quot;: &quot;rprivate&quot;,</span>
<span style="color:#AA5500">                &quot;RW&quot;: true,</span>
<span style="color:#AA5500">                &quot;Source&quot;: &quot;/mnt/Volume1/docker/calibreweb/config&quot;,</span>
<span style="color:#AA5500">                &quot;Type&quot;: &quot;bind&quot;</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            {</span>
<span style="color:#AA5500">                &quot;Destination&quot;: &quot;/data&quot;,</span>
<span style="color:#AA5500">                &quot;Mode&quot;: &quot;rw&quot;,</span>
<span style="color:#AA5500">                &quot;Propagation&quot;: &quot;rprivate&quot;,</span>
<span style="color:#AA5500">                &quot;RW&quot;: true,</span>
<span style="color:#AA5500">                &quot;Source&quot;: &quot;/mnt/Volume1/docker/calibreweb/data&quot;,</span>
<span style="color:#AA5500">                &quot;Type&quot;: &quot;bind&quot;</span>
<span style="color:#AA5500">            }</span>
<span style="color:#AA5500">        ],</span>
<span style="color:#AA5500">        &quot;Name&quot;: &quot;/calibreweb&quot;,</span>
<span style="color:#AA5500">        &quot;NetworkSettings&quot;: {</span>
<span style="color:#AA5500">            &quot;Bridge&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;EndpointID&quot;: &quot;4d6e12715afd093070fd4604406801810f3e9dff88247a15936fd4098c444a26&quot;,</span>
<span style="color:#AA5500">            &quot;Gateway&quot;: &quot;172.17.0.1&quot;,</span>
<span style="color:#AA5500">            &quot;GlobalIPv6Address&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;GlobalIPv6PrefixLen&quot;: 0,</span>
<span style="color:#AA5500">            &quot;HairpinMode&quot;: false,</span>
<span style="color:#AA5500">            &quot;IPAddress&quot;: &quot;172.17.0.4&quot;,</span>
<span style="color:#AA5500">            &quot;IPPrefixLen&quot;: 16,</span>
<span style="color:#AA5500">            &quot;IPv6Gateway&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;LinkLocalIPv6Address&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;LinkLocalIPv6PrefixLen&quot;: 0,</span>
<span style="color:#AA5500">            &quot;MacAddress&quot;: &quot;ca:5c:36:51:42:0c&quot;,</span>
<span style="color:#AA5500">            &quot;Networks&quot;: {</span>
<span style="color:#AA5500">                &quot;bridge&quot;: {</span>
<span style="color:#AA5500">                    &quot;Aliases&quot;: null,</span>
<span style="color:#AA5500">                    &quot;DNSNames&quot;: null,</span>
<span style="color:#AA5500">                    &quot;DriverOpts&quot;: null,</span>
<span style="color:#AA5500">                    &quot;EndpointID&quot;: &quot;4d6e12715afd093070fd4604406801810f3e9dff88247a15936fd4098c444a26&quot;,</span>
<span style="color:#AA5500">                    &quot;Gateway&quot;: &quot;172.17.0.1&quot;,</span>
<span style="color:#AA5500">                    &quot;GlobalIPv6Address&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">                    &quot;GlobalIPv6PrefixLen&quot;: 0,</span>
<span style="color:#AA5500">                    &quot;GwPriority&quot;: 0,</span>
<span style="color:#AA5500">                    &quot;IPAMConfig&quot;: null,</span>
<span style="color:#AA5500">                    &quot;IPAddress&quot;: &quot;172.17.0.4&quot;,</span>
<span style="color:#AA5500">                    &quot;IPPrefixLen&quot;: 16,</span>
<span style="color:#AA5500">                    &quot;IPv6Gateway&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">                    &quot;Links&quot;: null,</span>
<span style="color:#AA5500">                    &quot;MacAddress&quot;: &quot;ca:5c:36:51:42:0c&quot;,</span>
<span style="color:#AA5500">                    &quot;NetworkID&quot;: &quot;bf69c1dd08283d21e1c03cd9d2f9059cf944e578f95c79babe5a23cdb260be15&quot;</span>
<span style="color:#AA5500">                }</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            &quot;Ports&quot;: {</span>
<span style="color:#AA5500">                &quot;8083/tcp&quot;: [</span>
<span style="color:#AA5500">                    {</span>
<span style="color:#AA5500">                        &quot;HostIp&quot;: &quot;0.0.0.0&quot;,</span>
<span style="color:#AA5500">                        &quot;HostPort&quot;: &quot;8084&quot;</span>
<span style="color:#AA5500">                    }</span>
<span style="color:#AA5500">                ]</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            &quot;SandboxID&quot;: &quot;2abff91db59b96b311e1b1075dbe778ee2a95971fd991a7c4e0aa580d8d048b4&quot;,</span>
<span style="color:#AA5500">            &quot;SandboxKey&quot;: &quot;/var/run/docker/netns/2abff91db59b&quot;,</span>
<span style="color:#AA5500">            &quot;SecondaryIPAddresses&quot;: null,</span>
<span style="color:#AA5500">            &quot;SecondaryIPv6Addresses&quot;: null</span>
<span style="color:#AA5500">        },</span>
<span style="color:#AA5500">        &quot;Path&quot;: &quot;/init&quot;,</span>
<span style="color:#AA5500">        &quot;Platform&quot;: &quot;linux&quot;,</span>
<span style="color:#AA5500">        &quot;ProcessLabel&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">        &quot;ResolvConfPath&quot;: &quot;/var/lib/docker/containers/930efe3baffaa3a15e545f79ba035a0dee17ceb7c4a45cf59782cc8b0fd4f933/resolv.conf&quot;,</span>
<span style="color:#AA5500">        &quot;RestartCount&quot;: 0,</span>
<span style="color:#AA5500">        &quot;State&quot;: {</span>
<span style="color:#AA5500">            &quot;Dead&quot;: false,</span>
<span style="color:#AA5500">            &quot;Error&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;ExitCode&quot;: 0,</span>
<span style="color:#AA5500">            &quot;FinishedAt&quot;: &quot;2025-09-24T03:00:32.410888489Z&quot;,</span>
<span style="color:#AA5500">            &quot;OOMKilled&quot;: false,</span>
<span style="color:#AA5500">            &quot;Paused&quot;: false,</span>
<span style="color:#AA5500">            &quot;Pid&quot;: 2749,</span>
<span style="color:#AA5500">            &quot;Restarting&quot;: false,</span>
<span style="color:#AA5500">            &quot;Running&quot;: true,</span>
<span style="color:#AA5500">            &quot;StartedAt&quot;: &quot;2025-09-24T03:01:25.583748657Z&quot;,</span>
<span style="color:#AA5500">            &quot;Status&quot;: &quot;running&quot;</span>
<span style="color:#AA5500">        }</span>
<span style="color:#AA5500">    }</span>
<span style="color:#AA5500">}</span>
Donnerstag 25 September 2025  05:17:44 +0200 (0:00:01.768)       0:00:51.751 *** 
Donnerstag 25 September 2025  05:17:44 +0200 (0:00:00.068)       0:00:51.820 *** 
Donnerstag 25 September 2025  05:17:44 +0200 (0:00:00.062)       0:00:51.882 *** 
Donnerstag 25 September 2025  05:17:44 +0200 (0:00:00.053)       0:00:51.935 *** 

TASK [cloudcmd : Stop Cloudcmd] ***********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/cloudcmd/tasks/main.yml:38</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:17:44 +0200 (0:00:00.627)       0:00:52.563 *** 
Donnerstag 25 September 2025  05:17:45 +0200 (0:00:00.058)       0:00:52.621 *** 
Donnerstag 25 September 2025  05:17:45 +0200 (0:00:00.185)       0:00:52.807 *** 
Donnerstag 25 September 2025  05:17:45 +0200 (0:00:00.058)       0:00:52.865 *** 
Donnerstag 25 September 2025  05:17:45 +0200 (0:00:00.057)       0:00:52.922 *** 

TASK [cloudflare_ddns : Stop Cloudflare DDNS] *********************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/cloudflare_ddns/tasks/main.yml:34</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:17:45 +0200 (0:00:00.596)       0:00:53.519 *** 
Donnerstag 25 September 2025  05:17:45 +0200 (0:00:00.079)       0:00:53.599 *** 
Donnerstag 25 September 2025  05:17:46 +0200 (0:00:00.057)       0:00:53.656 *** 

TASK [couchdb : Stop CouchDB] *************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/couchdb/tasks/main.yml:38</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:17:46 +0200 (0:00:00.626)       0:00:54.283 *** 
Donnerstag 25 September 2025  05:17:46 +0200 (0:00:00.051)       0:00:54.334 *** 

TASK [code-server : Stop Code Server] *****************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/code-server/tasks/main.yml:32</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:17:47 +0200 (0:00:00.619)       0:00:54.954 *** 
Donnerstag 25 September 2025  05:17:47 +0200 (0:00:00.069)       0:00:55.023 *** 
Donnerstag 25 September 2025  05:17:47 +0200 (0:00:00.063)       0:00:55.086 *** 

TASK [couchpotato : Stop Couchpotato] *****************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/couchpotato/tasks/main.yml:41</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:17:48 +0200 (0:00:00.647)       0:00:55.734 *** 
Donnerstag 25 September 2025  05:17:48 +0200 (0:00:00.067)       0:00:55.801 *** 
Donnerstag 25 September 2025  05:17:48 +0200 (0:00:00.055)       0:00:55.857 *** 
Donnerstag 25 September 2025  05:17:48 +0200 (0:00:00.056)       0:00:55.914 *** 

TASK [dashy : Stop Dashy] *****************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/dashy/tasks/main.yml:39</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:17:48 +0200 (0:00:00.612)       0:00:56.526 *** 
Donnerstag 25 September 2025  05:17:48 +0200 (0:00:00.056)       0:00:56.583 *** 
Donnerstag 25 September 2025  05:17:49 +0200 (0:00:00.199)       0:00:56.783 *** 
Donnerstag 25 September 2025  05:17:49 +0200 (0:00:00.050)       0:00:56.833 *** 
Donnerstag 25 September 2025  05:17:49 +0200 (0:00:00.066)       0:00:56.900 *** 

TASK [ddns_updater : Stop DDNS Updater] ***************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/ddns_updater/tasks/main.yml:54</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:17:49 +0200 (0:00:00.622)       0:00:57.523 *** 
Donnerstag 25 September 2025  05:17:49 +0200 (0:00:00.065)       0:00:57.588 *** 
Donnerstag 25 September 2025  05:17:50 +0200 (0:00:00.063)       0:00:57.651 *** 

TASK [deluge : Stop Deluge] ***************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/deluge/tasks/main.yml:46</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:17:50 +0200 (0:00:00.621)       0:00:58.273 *** 
Donnerstag 25 September 2025  05:17:50 +0200 (0:00:00.068)       0:00:58.342 *** 
Donnerstag 25 September 2025  05:17:50 +0200 (0:00:00.052)       0:00:58.394 *** 

TASK [dokuwiki : Stop Dokuwiki] ***********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/dokuwiki/tasks/main.yml:37</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:17:51 +0200 (0:00:00.612)       0:00:59.007 *** 
Donnerstag 25 September 2025  05:17:51 +0200 (0:00:00.062)       0:00:59.070 *** 
Donnerstag 25 September 2025  05:17:51 +0200 (0:00:00.058)       0:00:59.128 *** 
Donnerstag 25 September 2025  05:17:51 +0200 (0:00:00.066)       0:00:59.194 *** 
Donnerstag 25 September 2025  05:17:51 +0200 (0:00:00.055)       0:00:59.250 *** 
Donnerstag 25 September 2025  05:17:51 +0200 (0:00:00.061)       0:00:59.311 *** 
Donnerstag 25 September 2025  05:17:51 +0200 (0:00:00.059)       0:00:59.370 *** 

TASK [drone-ci : Stop Drone-CI] ***********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/drone-ci/tasks/main.yml:79</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:17:52 +0200 (0:00:00.617)       0:00:59.988 *** 

TASK [drone-ci : Stop Drone-CI Runner] ****************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/drone-ci/tasks/main.yml:84</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:17:53 +0200 (0:00:00.752)       0:01:00.741 *** 
Donnerstag 25 September 2025  05:17:53 +0200 (0:00:00.090)       0:01:00.832 *** 
Donnerstag 25 September 2025  05:17:53 +0200 (0:00:00.063)       0:01:00.895 *** 

TASK [duplicacy : Stop Duplicacy] *********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/duplicacy/tasks/main.yml:44</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:17:53 +0200 (0:00:00.615)       0:01:01.510 *** 
Donnerstag 25 September 2025  05:17:53 +0200 (0:00:00.074)       0:01:01.585 *** 
Donnerstag 25 September 2025  05:17:54 +0200 (0:00:00.060)       0:01:01.646 *** 

TASK [duplicati : Stop Duplicati] *********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/duplicati/tasks/main.yml:40</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:17:54 +0200 (0:00:00.625)       0:01:02.271 *** 
Donnerstag 25 September 2025  05:17:54 +0200 (0:00:00.085)       0:01:02.357 *** 
Donnerstag 25 September 2025  05:17:54 +0200 (0:00:00.052)       0:01:02.409 *** 

TASK [emby : Stop Emby] *******************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/emby/tasks/main.yml:41</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:17:55 +0200 (0:00:00.617)       0:01:03.026 *** 
Donnerstag 25 September 2025  05:17:55 +0200 (0:00:00.062)       0:01:03.089 *** 
Donnerstag 25 September 2025  05:17:55 +0200 (0:00:00.056)       0:01:03.146 *** 

TASK [esphome : Stop EspHome] *************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/esphome/tasks/main.yml:38</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:17:56 +0200 (0:00:00.624)       0:01:03.771 *** 
Donnerstag 25 September 2025  05:17:56 +0200 (0:00:00.081)       0:01:03.853 *** 
Donnerstag 25 September 2025  05:17:56 +0200 (0:00:00.066)       0:01:03.919 *** 
Donnerstag 25 September 2025  05:17:56 +0200 (0:00:00.065)       0:01:03.985 *** 
Donnerstag 25 September 2025  05:17:56 +0200 (0:00:00.056)       0:01:04.041 *** 

TASK [firefly : Stop Firefly] *************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/firefly/tasks/main.yml:68</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:17:57 +0200 (0:00:00.733)       0:01:04.774 *** 

TASK [firefly : Stop Firefly MySQL] *******************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/firefly/tasks/main.yml:73</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:17:57 +0200 (0:00:00.649)       0:01:05.424 *** 
Donnerstag 25 September 2025  05:17:57 +0200 (0:00:00.058)       0:01:05.482 *** 
Donnerstag 25 September 2025  05:17:57 +0200 (0:00:00.067)       0:01:05.549 *** 

TASK [flaresolverr : Stop FlareSolverr] ***************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/flaresolverr/tasks/main.yml:35</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:17:58 +0200 (0:00:00.648)       0:01:06.198 *** 
Donnerstag 25 September 2025  05:17:58 +0200 (0:00:00.081)       0:01:06.279 *** 
Donnerstag 25 September 2025  05:17:58 +0200 (0:00:00.062)       0:01:06.342 *** 

TASK [freshrss : Stop FreshRSS] ***********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/freshrss/tasks/main.yml:38</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:17:59 +0200 (0:00:00.624)       0:01:06.967 *** 
Donnerstag 25 September 2025  05:17:59 +0200 (0:00:00.070)       0:01:07.037 *** 
Donnerstag 25 September 2025  05:17:59 +0200 (0:00:00.054)       0:01:07.092 *** 

TASK [get_iplayer : Stop get_iplayer] *****************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/get_iplayer/tasks/main.yml:28</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:18:00 +0200 (0:00:00.618)       0:01:07.710 *** 
Donnerstag 25 September 2025  05:18:00 +0200 (0:00:00.076)       0:01:07.787 *** 
Donnerstag 25 September 2025  05:18:00 +0200 (0:00:00.055)       0:01:07.842 *** 
Donnerstag 25 September 2025  05:18:00 +0200 (0:00:00.052)       0:01:07.894 *** 

TASK [gitea : Stop Gitea] *****************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/gitea/tasks/main.yml:65</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:18:00 +0200 (0:00:00.601)       0:01:08.496 *** 

TASK [gitea : Stop Gitea Mysql] ***********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/gitea/tasks/main.yml:70</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:18:01 +0200 (0:00:00.637)       0:01:09.133 *** 
Donnerstag 25 September 2025  05:18:01 +0200 (0:00:00.057)       0:01:09.191 *** 
Donnerstag 25 September 2025  05:18:01 +0200 (0:00:00.180)       0:01:09.371 *** 
Donnerstag 25 September 2025  05:18:01 +0200 (0:00:00.081)       0:01:09.453 *** 
Donnerstag 25 September 2025  05:18:01 +0200 (0:00:00.059)       0:01:09.512 *** 

TASK [gitlab : Stop Gitlab] ***************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/gitlab/tasks/main.yml:64</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:18:02 +0200 (0:00:00.622)       0:01:10.135 *** 
Donnerstag 25 September 2025  05:18:02 +0200 (0:00:00.076)       0:01:10.212 *** 

TASK [glances : Stop Glances] *************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/glances/tasks/main.yml:32</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:18:03 +0200 (0:00:00.666)       0:01:10.879 *** 
Donnerstag 25 September 2025  05:18:03 +0200 (0:00:00.067)       0:01:10.946 *** 
Donnerstag 25 September 2025  05:18:03 +0200 (0:00:00.058)       0:01:11.004 *** 

TASK [gotify : Stop Gotify] ***************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/gotify/tasks/main.yml:38</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:18:04 +0200 (0:00:00.637)       0:01:11.642 *** 
Donnerstag 25 September 2025  05:18:04 +0200 (0:00:00.082)       0:01:11.724 *** 
Donnerstag 25 September 2025  05:18:04 +0200 (0:00:00.068)       0:01:11.793 *** 
Donnerstag 25 September 2025  05:18:04 +0200 (0:00:00.055)       0:01:11.848 *** 
Donnerstag 25 September 2025  05:18:04 +0200 (0:00:00.070)       0:01:11.919 *** 
Donnerstag 25 September 2025  05:18:04 +0200 (0:00:00.056)       0:01:11.975 *** 
Donnerstag 25 September 2025  05:18:04 +0200 (0:00:00.059)       0:01:12.035 *** 

TASK [guacamole : Stop Guacamole] *********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/guacamole/tasks/main.yml:59</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:18:05 +0200 (0:00:00.616)       0:01:12.652 *** 
Donnerstag 25 September 2025  05:18:05 +0200 (0:00:00.072)       0:01:12.725 *** 

TASK [healthchecks.io : Remove healthchecks.io cronjob] ***********************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/healthchecks.io/tasks/main.yml:14</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;envs&quot;: [],</span>
<span style="color:#00AA00">    &quot;jobs&quot;: []</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:18:05 +0200 (0:00:00.875)       0:01:13.600 *** 
Donnerstag 25 September 2025  05:18:06 +0200 (0:00:00.072)       0:01:13.673 *** 
Donnerstag 25 September 2025  05:18:06 +0200 (0:00:00.064)       0:01:13.738 *** 

TASK [heimdall : Stop Heimdall] ***********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/heimdall/tasks/main.yml:36</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:18:06 +0200 (0:00:00.626)       0:01:14.365 *** 
Donnerstag 25 September 2025  05:18:06 +0200 (0:00:00.064)       0:01:14.430 *** 
Donnerstag 25 September 2025  05:18:06 +0200 (0:00:00.046)       0:01:14.477 *** 

TASK [hello_world : Stop Hello World] *****************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/hello_world/tasks/main.yml:33</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:18:07 +0200 (0:00:00.610)       0:01:15.087 *** 
Donnerstag 25 September 2025  05:18:07 +0200 (0:00:00.067)       0:01:15.154 *** 
Donnerstag 25 September 2025  05:18:07 +0200 (0:00:00.051)       0:01:15.205 *** 

TASK [homeassistant : Stop homeassistant] *************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/homeassistant/tasks/main.yml:34</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:18:08 +0200 (0:00:00.649)       0:01:15.855 *** 
Donnerstag 25 September 2025  05:18:08 +0200 (0:00:00.074)       0:01:15.929 *** 
Donnerstag 25 September 2025  05:18:08 +0200 (0:00:00.061)       0:01:15.991 *** 

TASK [homebridge : Stop Homebridge] *******************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/homebridge/tasks/main.yml:39</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:18:09 +0200 (0:00:00.626)       0:01:16.618 *** 

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
Donnerstag 25 September 2025  05:18:09 +0200 (0:00:00.436)       0:01:17.055 *** 

TASK [homepage : Template config files] ***************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/homepage/tasks/main.yml:11</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; (item=bookmarks.yaml) =&gt; {</span>
<span style="color:#00AA00">    &quot;ansible_loop_var&quot;: &quot;item&quot;,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;checksum&quot;: &quot;a2783fdfb95c4d6e0f77924c506c26b968ae6dc6&quot;,</span>
<span style="color:#00AA00">    &quot;dest&quot;: &quot;/mnt/Volume1/docker/homepage/bookmarks.yaml&quot;,</span>
<span style="color:#00AA00">    &quot;gid&quot;: 1000,</span>
<span style="color:#00AA00">    &quot;group&quot;: &quot;dietmar&quot;,</span>
<span style="color:#00AA00">    &quot;item&quot;: &quot;bookmarks.yaml&quot;,</span>
<span style="color:#00AA00">    &quot;mode&quot;: &quot;0777&quot;,</span>
<span style="color:#00AA00">    &quot;owner&quot;: &quot;dietmar&quot;,</span>
<span style="color:#00AA00">    &quot;path&quot;: &quot;/mnt/Volume1/docker/homepage/bookmarks.yaml&quot;,</span>
<span style="color:#00AA00">    &quot;size&quot;: 527,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;file&quot;,</span>
<span style="color:#00AA00">    &quot;uid&quot;: 1000</span>
<span style="color:#00AA00">}</span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; (item=docker.yaml) =&gt; {</span>
<span style="color:#00AA00">    &quot;ansible_loop_var&quot;: &quot;item&quot;,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;checksum&quot;: &quot;c9c9f5d43dab59e638c885b21bba46d28f5c0509&quot;,</span>
<span style="color:#00AA00">    &quot;dest&quot;: &quot;/mnt/Volume1/docker/homepage/docker.yaml&quot;,</span>
<span style="color:#00AA00">    &quot;gid&quot;: 1000,</span>
<span style="color:#00AA00">    &quot;group&quot;: &quot;dietmar&quot;,</span>
<span style="color:#00AA00">    &quot;item&quot;: &quot;docker.yaml&quot;,</span>
<span style="color:#00AA00">    &quot;mode&quot;: &quot;0777&quot;,</span>
<span style="color:#00AA00">    &quot;owner&quot;: &quot;dietmar&quot;,</span>
<span style="color:#00AA00">    &quot;path&quot;: &quot;/mnt/Volume1/docker/homepage/docker.yaml&quot;,</span>
<span style="color:#00AA00">    &quot;size&quot;: 45,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;file&quot;,</span>
<span style="color:#00AA00">    &quot;uid&quot;: 1000</span>
<span style="color:#00AA00">}</span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; (item=settings.yaml) =&gt; {</span>
<span style="color:#00AA00">    &quot;ansible_loop_var&quot;: &quot;item&quot;,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;checksum&quot;: &quot;12ad15433ee55e9f49b4346cb3d5765ecac6dd08&quot;,</span>
<span style="color:#00AA00">    &quot;dest&quot;: &quot;/mnt/Volume1/docker/homepage/settings.yaml&quot;,</span>
<span style="color:#00AA00">    &quot;gid&quot;: 1000,</span>
<span style="color:#00AA00">    &quot;group&quot;: &quot;dietmar&quot;,</span>
<span style="color:#00AA00">    &quot;item&quot;: &quot;settings.yaml&quot;,</span>
<span style="color:#00AA00">    &quot;mode&quot;: &quot;0777&quot;,</span>
<span style="color:#00AA00">    &quot;owner&quot;: &quot;dietmar&quot;,</span>
<span style="color:#00AA00">    &quot;path&quot;: &quot;/mnt/Volume1/docker/homepage/settings.yaml&quot;,</span>
<span style="color:#00AA00">    &quot;size&quot;: 64,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;file&quot;,</span>
<span style="color:#00AA00">    &quot;uid&quot;: 1000</span>
<span style="color:#00AA00">}</span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; (item=services.yaml) =&gt; {</span>
<span style="color:#00AA00">    &quot;ansible_loop_var&quot;: &quot;item&quot;,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;checksum&quot;: &quot;701d82d2ab4f38f259110d140d1c66bfdd9ef2ba&quot;,</span>
<span style="color:#00AA00">    &quot;dest&quot;: &quot;/mnt/Volume1/docker/homepage/services.yaml&quot;,</span>
<span style="color:#00AA00">    &quot;gid&quot;: 1000,</span>
<span style="color:#00AA00">    &quot;group&quot;: &quot;dietmar&quot;,</span>
<span style="color:#00AA00">    &quot;item&quot;: &quot;services.yaml&quot;,</span>
<span style="color:#00AA00">    &quot;mode&quot;: &quot;0777&quot;,</span>
<span style="color:#00AA00">    &quot;owner&quot;: &quot;dietmar&quot;,</span>
<span style="color:#00AA00">    &quot;path&quot;: &quot;/mnt/Volume1/docker/homepage/services.yaml&quot;,</span>
<span style="color:#00AA00">    &quot;size&quot;: 141,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;file&quot;,</span>
<span style="color:#00AA00">    &quot;uid&quot;: 1000</span>
<span style="color:#00AA00">}</span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; (item=widgets.yaml) =&gt; {</span>
<span style="color:#00AA00">    &quot;ansible_loop_var&quot;: &quot;item&quot;,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;checksum&quot;: &quot;7c716bdbcc8065135fbe8f1a314a3dae569cedb2&quot;,</span>
<span style="color:#00AA00">    &quot;dest&quot;: &quot;/mnt/Volume1/docker/homepage/widgets.yaml&quot;,</span>
<span style="color:#00AA00">    &quot;gid&quot;: 1000,</span>
<span style="color:#00AA00">    &quot;group&quot;: &quot;dietmar&quot;,</span>
<span style="color:#00AA00">    &quot;item&quot;: &quot;widgets.yaml&quot;,</span>
<span style="color:#00AA00">    &quot;mode&quot;: &quot;0777&quot;,</span>
<span style="color:#00AA00">    &quot;owner&quot;: &quot;dietmar&quot;,</span>
<span style="color:#00AA00">    &quot;path&quot;: &quot;/mnt/Volume1/docker/homepage/widgets.yaml&quot;,</span>
<span style="color:#00AA00">    &quot;size&quot;: 288,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;file&quot;,</span>
<span style="color:#00AA00">    &quot;uid&quot;: 1000</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:18:12 +0200 (0:00:03.062)       0:01:20.117 *** 

TASK [homepage : Create Homepage Docker Container] ****************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/homepage/tasks/main.yml:23</b></span>
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
<span style="color:#AA5500">                &quot;NODE_VERSION=22.19.0&quot;,</span>
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
<span style="color:#AA5500">            &quot;Hostname&quot;: &quot;6f31fd659817&quot;,</span>
<span style="color:#AA5500">            &quot;Image&quot;: &quot;ghcr.io/gethomepage/homepage:latest&quot;,</span>
<span style="color:#AA5500">            &quot;Labels&quot;: {</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.created&quot;: &quot;2025-09-22T15:23:40.735Z&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.description&quot;: &quot;A highly customizable homepage (or startpage / application dashboard) with Docker and service API integrations.&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.documentation&quot;: &quot;https://github.com/gethomepage/homepage/wiki&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.licenses&quot;: &quot;GPL-3.0&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.revision&quot;: &quot;4028194830f3b4a66706ba43ea6847e348a7dba0&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.source&quot;: &quot;https://github.com/gethomepage/homepage&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.title&quot;: &quot;homepage&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.url&quot;: &quot;https://github.com/gethomepage/homepage&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.version&quot;: &quot;v1.5.0&quot;,</span>
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
<span style="color:#AA5500">        &quot;Created&quot;: &quot;2025-09-22T15:27:49.090162758Z&quot;,</span>
<span style="color:#AA5500">        &quot;Driver&quot;: &quot;overlay2&quot;,</span>
<span style="color:#AA5500">        &quot;ExecIDs&quot;: null,</span>
<span style="color:#AA5500">        &quot;GraphDriver&quot;: {</span>
<span style="color:#AA5500">            &quot;Data&quot;: {</span>
<span style="color:#AA5500">                &quot;ID&quot;: &quot;6f31fd659817199cd23577ba7591a7854808b328ade4f4f056fd25c5b664d04c&quot;,</span>
<span style="color:#AA5500">                &quot;LowerDir&quot;: &quot;/var/lib/docker/overlay2/a94740cdbd24ccbdc3c74a409b9805f2458db032b196d92e0e885b06ba9659c5-init/diff:/var/lib/docker/overlay2/23a9385149d0f49800ed7f1d18a7975e3e6c6cc0ddeb75551e30acbb3fe8acab/diff:/var/lib/docker/overlay2/48247c240df240adc75d0560240e5bdcea1e5b0e3421511997fbd49098c4f177/diff:/var/lib/docker/overlay2/1757a842b2db6b66f4e139af38e2a438f72effe4b9b13ef6d21e4b161e76484e/diff:/var/lib/docker/overlay2/7fbced54ce4f73d785820c4ec8bee72324553f5df29851e8e682f6a81bdacada/diff:/var/lib/docker/overlay2/a37637f159082e890f586ca87fe6b86cc7f704bb28bd9a148a16d5be78fcf3c9/diff:/var/lib/docker/overlay2/cc19d88f3f5740d1286616e33561d4bcf45479331a0103ef4bf291c2abcfee00/diff:/var/lib/docker/overlay2/3fbd10128c4266d5886821096047ca645ff55c0a76dd99e2115e24756abe8889/diff:/var/lib/docker/overlay2/d035f3715f0b05e119f1cc508d4178bc870691590ad5897c298e685f64e7e4f6/diff:/var/lib/docker/overlay2/f40b5fef4490f7de32848a38a5c19a15f50fc99f0016f98f4214304c8496b150/diff:/var/lib/docker/overlay2/502c7107094a5bb68299bb6f3d8d9b644daf0a27a5836740ac357984351c9297/diff&quot;,</span>
<span style="color:#AA5500">                &quot;MergedDir&quot;: &quot;/var/lib/docker/overlay2/a94740cdbd24ccbdc3c74a409b9805f2458db032b196d92e0e885b06ba9659c5/merged&quot;,</span>
<span style="color:#AA5500">                &quot;UpperDir&quot;: &quot;/var/lib/docker/overlay2/a94740cdbd24ccbdc3c74a409b9805f2458db032b196d92e0e885b06ba9659c5/diff&quot;,</span>
<span style="color:#AA5500">                &quot;WorkDir&quot;: &quot;/var/lib/docker/overlay2/a94740cdbd24ccbdc3c74a409b9805f2458db032b196d92e0e885b06ba9659c5/work&quot;</span>
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
<span style="color:#AA5500">            &quot;Dns&quot;: [],</span>
<span style="color:#AA5500">            &quot;DnsOptions&quot;: [],</span>
<span style="color:#AA5500">            &quot;DnsSearch&quot;: [],</span>
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
<span style="color:#AA5500">        &quot;HostnamePath&quot;: &quot;/var/lib/docker/containers/6f31fd659817199cd23577ba7591a7854808b328ade4f4f056fd25c5b664d04c/hostname&quot;,</span>
<span style="color:#AA5500">        &quot;HostsPath&quot;: &quot;/var/lib/docker/containers/6f31fd659817199cd23577ba7591a7854808b328ade4f4f056fd25c5b664d04c/hosts&quot;,</span>
<span style="color:#AA5500">        &quot;Id&quot;: &quot;6f31fd659817199cd23577ba7591a7854808b328ade4f4f056fd25c5b664d04c&quot;,</span>
<span style="color:#AA5500">        &quot;Image&quot;: &quot;sha256:2833b1df3f84c40c0f35b25d7e7fac123d5d1f89883515e431c10149d7d7c6dd&quot;,</span>
<span style="color:#AA5500">        &quot;LogPath&quot;: &quot;/var/lib/docker/containers/6f31fd659817199cd23577ba7591a7854808b328ade4f4f056fd25c5b664d04c/6f31fd659817199cd23577ba7591a7854808b328ade4f4f056fd25c5b664d04c-json.log&quot;,</span>
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
<span style="color:#AA5500">            &quot;EndpointID&quot;: &quot;2d5512701ea5d2d30fd2c9486c2ab501fa60ef48c92f1dad3e7ae98ebfa69233&quot;,</span>
<span style="color:#AA5500">            &quot;Gateway&quot;: &quot;172.17.0.1&quot;,</span>
<span style="color:#AA5500">            &quot;GlobalIPv6Address&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;GlobalIPv6PrefixLen&quot;: 0,</span>
<span style="color:#AA5500">            &quot;HairpinMode&quot;: false,</span>
<span style="color:#AA5500">            &quot;IPAddress&quot;: &quot;172.17.0.2&quot;,</span>
<span style="color:#AA5500">            &quot;IPPrefixLen&quot;: 16,</span>
<span style="color:#AA5500">            &quot;IPv6Gateway&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;LinkLocalIPv6Address&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;LinkLocalIPv6PrefixLen&quot;: 0,</span>
<span style="color:#AA5500">            &quot;MacAddress&quot;: &quot;96:52:2b:9a:14:a2&quot;,</span>
<span style="color:#AA5500">            &quot;Networks&quot;: {</span>
<span style="color:#AA5500">                &quot;bridge&quot;: {</span>
<span style="color:#AA5500">                    &quot;Aliases&quot;: null,</span>
<span style="color:#AA5500">                    &quot;DNSNames&quot;: null,</span>
<span style="color:#AA5500">                    &quot;DriverOpts&quot;: null,</span>
<span style="color:#AA5500">                    &quot;EndpointID&quot;: &quot;2d5512701ea5d2d30fd2c9486c2ab501fa60ef48c92f1dad3e7ae98ebfa69233&quot;,</span>
<span style="color:#AA5500">                    &quot;Gateway&quot;: &quot;172.17.0.1&quot;,</span>
<span style="color:#AA5500">                    &quot;GlobalIPv6Address&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">                    &quot;GlobalIPv6PrefixLen&quot;: 0,</span>
<span style="color:#AA5500">                    &quot;GwPriority&quot;: 0,</span>
<span style="color:#AA5500">                    &quot;IPAMConfig&quot;: null,</span>
<span style="color:#AA5500">                    &quot;IPAddress&quot;: &quot;172.17.0.2&quot;,</span>
<span style="color:#AA5500">                    &quot;IPPrefixLen&quot;: 16,</span>
<span style="color:#AA5500">                    &quot;IPv6Gateway&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">                    &quot;Links&quot;: null,</span>
<span style="color:#AA5500">                    &quot;MacAddress&quot;: &quot;96:52:2b:9a:14:a2&quot;,</span>
<span style="color:#AA5500">                    &quot;NetworkID&quot;: &quot;bf69c1dd08283d21e1c03cd9d2f9059cf944e578f95c79babe5a23cdb260be15&quot;</span>
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
<span style="color:#AA5500">            &quot;SandboxID&quot;: &quot;02ad357f89f633a676b10966cb86616acf30f6866987c46316a20f748173f0c7&quot;,</span>
<span style="color:#AA5500">            &quot;SandboxKey&quot;: &quot;/var/run/docker/netns/02ad357f89f6&quot;,</span>
<span style="color:#AA5500">            &quot;SecondaryIPAddresses&quot;: null,</span>
<span style="color:#AA5500">            &quot;SecondaryIPv6Addresses&quot;: null</span>
<span style="color:#AA5500">        },</span>
<span style="color:#AA5500">        &quot;Path&quot;: &quot;docker-entrypoint.sh&quot;,</span>
<span style="color:#AA5500">        &quot;Platform&quot;: &quot;linux&quot;,</span>
<span style="color:#AA5500">        &quot;ProcessLabel&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">        &quot;ResolvConfPath&quot;: &quot;/var/lib/docker/containers/6f31fd659817199cd23577ba7591a7854808b328ade4f4f056fd25c5b664d04c/resolv.conf&quot;,</span>
<span style="color:#AA5500">        &quot;RestartCount&quot;: 0,</span>
<span style="color:#AA5500">        &quot;State&quot;: {</span>
<span style="color:#AA5500">            &quot;Dead&quot;: false,</span>
<span style="color:#AA5500">            &quot;Error&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;ExitCode&quot;: 0,</span>
<span style="color:#AA5500">            &quot;FinishedAt&quot;: &quot;2025-09-25T02:09:47.860473277Z&quot;,</span>
<span style="color:#AA5500">            &quot;Health&quot;: {</span>
<span style="color:#AA5500">                &quot;FailingStreak&quot;: 0,</span>
<span style="color:#AA5500">                &quot;Log&quot;: [</span>
<span style="color:#AA5500">                    {</span>
<span style="color:#AA5500">                        &quot;End&quot;: &quot;2025-09-25T05:17:28.971905591+02:00&quot;,</span>
<span style="color:#AA5500">                        &quot;ExitCode&quot;: 0,</span>
<span style="color:#AA5500">                        &quot;Output&quot;: &quot;Connecting to 127.0.0.1:3000 (127.0.0.1:3000)\nremote file exists\n&quot;,</span>
<span style="color:#AA5500">                        &quot;Start&quot;: &quot;2025-09-25T05:17:28.920584266+02:00&quot;</span>
<span style="color:#AA5500">                    },</span>
<span style="color:#AA5500">                    {</span>
<span style="color:#AA5500">                        &quot;End&quot;: &quot;2025-09-25T05:17:39.037778886+02:00&quot;,</span>
<span style="color:#AA5500">                        &quot;ExitCode&quot;: 0,</span>
<span style="color:#AA5500">                        &quot;Output&quot;: &quot;Connecting to 127.0.0.1:3000 (127.0.0.1:3000)\nremote file exists\n&quot;,</span>
<span style="color:#AA5500">                        &quot;Start&quot;: &quot;2025-09-25T05:17:38.972392258+02:00&quot;</span>
<span style="color:#AA5500">                    },</span>
<span style="color:#AA5500">                    {</span>
<span style="color:#AA5500">                        &quot;End&quot;: &quot;2025-09-25T05:17:49.111058802+02:00&quot;,</span>
<span style="color:#AA5500">                        &quot;ExitCode&quot;: 0,</span>
<span style="color:#AA5500">                        &quot;Output&quot;: &quot;Connecting to 127.0.0.1:3000 (127.0.0.1:3000)\nremote file exists\n&quot;,</span>
<span style="color:#AA5500">                        &quot;Start&quot;: &quot;2025-09-25T05:17:49.038322727+02:00&quot;</span>
<span style="color:#AA5500">                    },</span>
<span style="color:#AA5500">                    {</span>
<span style="color:#AA5500">                        &quot;End&quot;: &quot;2025-09-25T05:17:59.170858333+02:00&quot;,</span>
<span style="color:#AA5500">                        &quot;ExitCode&quot;: 0,</span>
<span style="color:#AA5500">                        &quot;Output&quot;: &quot;Connecting to 127.0.0.1:3000 (127.0.0.1:3000)\nremote file exists\n&quot;,</span>
<span style="color:#AA5500">                        &quot;Start&quot;: &quot;2025-09-25T05:17:59.111629947+02:00&quot;</span>
<span style="color:#AA5500">                    },</span>
<span style="color:#AA5500">                    {</span>
<span style="color:#AA5500">                        &quot;End&quot;: &quot;2025-09-25T05:18:09.229760351+02:00&quot;,</span>
<span style="color:#AA5500">                        &quot;ExitCode&quot;: 0,</span>
<span style="color:#AA5500">                        &quot;Output&quot;: &quot;Connecting to 127.0.0.1:3000 (127.0.0.1:3000)\nremote file exists\n&quot;,</span>
<span style="color:#AA5500">                        &quot;Start&quot;: &quot;2025-09-25T05:18:09.172244804+02:00&quot;</span>
<span style="color:#AA5500">                    }</span>
<span style="color:#AA5500">                ],</span>
<span style="color:#AA5500">                &quot;Status&quot;: &quot;healthy&quot;</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            &quot;OOMKilled&quot;: false,</span>
<span style="color:#AA5500">            &quot;Paused&quot;: false,</span>
<span style="color:#AA5500">            &quot;Pid&quot;: 346421,</span>
<span style="color:#AA5500">            &quot;Restarting&quot;: false,</span>
<span style="color:#AA5500">            &quot;Running&quot;: true,</span>
<span style="color:#AA5500">            &quot;StartedAt&quot;: &quot;2025-09-25T02:09:48.05453125Z&quot;,</span>
<span style="color:#AA5500">            &quot;Status&quot;: &quot;running&quot;</span>
<span style="color:#AA5500">        }</span>
<span style="color:#AA5500">    }</span>
<span style="color:#AA5500">}</span>
Donnerstag 25 September 2025  05:18:13 +0200 (0:00:01.263)       0:01:21.380 *** 
Donnerstag 25 September 2025  05:18:13 +0200 (0:00:00.206)       0:01:21.587 *** 
Donnerstag 25 September 2025  05:18:14 +0200 (0:00:00.068)       0:01:21.655 *** 
Donnerstag 25 September 2025  05:18:14 +0200 (0:00:00.071)       0:01:21.727 *** 

TASK [ispyagentdvr : Stop iSpyAgentDVR] ***************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/ispyagentdvr/tasks/main.yml:50</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:18:14 +0200 (0:00:00.640)       0:01:22.367 *** 
Donnerstag 25 September 2025  05:18:14 +0200 (0:00:00.078)       0:01:22.446 *** 
Donnerstag 25 September 2025  05:18:14 +0200 (0:00:00.062)       0:01:22.509 *** 

TASK [jackett : Stop Jackett] *************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/jackett/tasks/main.yml:41</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:18:15 +0200 (0:00:00.627)       0:01:23.136 *** 
Donnerstag 25 September 2025  05:18:15 +0200 (0:00:00.065)       0:01:23.202 *** 
Donnerstag 25 September 2025  05:18:15 +0200 (0:00:00.068)       0:01:23.270 *** 

TASK [jellyfin : Stop jellyfin] ***********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/jellyfin/tasks/main.yml:52</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:18:16 +0200 (0:00:00.620)       0:01:23.891 *** 
Donnerstag 25 September 2025  05:18:16 +0200 (0:00:00.066)       0:01:23.958 *** 
Donnerstag 25 September 2025  05:18:16 +0200 (0:00:00.068)       0:01:24.027 *** 
Donnerstag 25 September 2025  05:18:16 +0200 (0:00:00.052)       0:01:24.079 *** 
Donnerstag 25 September 2025  05:18:16 +0200 (0:00:00.062)       0:01:24.142 *** 

TASK [joomla : Stop Joomla] ***************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/joomla/tasks/main.yml:62</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:18:17 +0200 (0:00:00.586)       0:01:24.728 *** 

TASK [joomla : Stop Joomla DB] ************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/joomla/tasks/main.yml:66</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:18:17 +0200 (0:00:00.619)       0:01:25.348 *** 
Donnerstag 25 September 2025  05:18:17 +0200 (0:00:00.191)       0:01:25.540 *** 
Donnerstag 25 September 2025  05:18:17 +0200 (0:00:00.062)       0:01:25.602 *** 

TASK [komga : Stop Komga] *****************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/komga/tasks/main.yml:42</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:18:18 +0200 (0:00:00.668)       0:01:26.270 *** 
Donnerstag 25 September 2025  05:18:18 +0200 (0:00:00.063)       0:01:26.333 *** 
Donnerstag 25 September 2025  05:18:18 +0200 (0:00:00.055)       0:01:26.389 *** 

TASK [krusader : Stop Krusader] ***********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/krusader/tasks/main.yml:43</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:18:19 +0200 (0:00:00.626)       0:01:27.015 *** 
Donnerstag 25 September 2025  05:18:19 +0200 (0:00:00.061)       0:01:27.077 *** 
Donnerstag 25 September 2025  05:18:19 +0200 (0:00:00.064)       0:01:27.141 *** 

TASK [lidarr : Stop Lidarr] ***************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/lidarr/tasks/main.yml:37</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:18:20 +0200 (0:00:00.637)       0:01:27.779 *** 
Donnerstag 25 September 2025  05:18:20 +0200 (0:00:00.061)       0:01:27.840 *** 
Donnerstag 25 September 2025  05:18:20 +0200 (0:00:00.062)       0:01:27.902 *** 
Donnerstag 25 September 2025  05:18:20 +0200 (0:00:00.059)       0:01:27.961 *** 
Donnerstag 25 September 2025  05:18:20 +0200 (0:00:00.057)       0:01:28.019 *** 
Donnerstag 25 September 2025  05:18:20 +0200 (0:00:00.081)       0:01:28.100 *** 
Donnerstag 25 September 2025  05:18:20 +0200 (0:00:00.060)       0:01:28.161 *** 
Donnerstag 25 September 2025  05:18:20 +0200 (0:00:00.057)       0:01:28.218 *** 
Donnerstag 25 September 2025  05:18:20 +0200 (0:00:00.053)       0:01:28.272 *** 

TASK [loki : Stop loki] *******************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/loki/tasks/main.yml:74</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:18:21 +0200 (0:00:00.613)       0:01:28.885 *** 
Donnerstag 25 September 2025  05:18:21 +0200 (0:00:00.194)       0:01:29.080 *** 
Donnerstag 25 September 2025  05:18:21 +0200 (0:00:00.048)       0:01:29.128 *** 

TASK [mealie : Stop Mealie] ***************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/mealie/tasks/main.yml:44</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:18:22 +0200 (0:00:00.624)       0:01:29.753 *** 

TASK [mediathekview : Create Mediathekview Directories] ***********************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/mediathekview/tasks/main.yml:5</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; (item=/mnt/Volume1/docker/mediathekview/config) =&gt; {</span>
<span style="color:#00AA00">    &quot;ansible_loop_var&quot;: &quot;item&quot;,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;gid&quot;: 1001,</span>
<span style="color:#00AA00">    &quot;group&quot;: &quot;ansible-nas&quot;,</span>
<span style="color:#00AA00">    &quot;item&quot;: &quot;/mnt/Volume1/docker/mediathekview/config&quot;,</span>
<span style="color:#00AA00">    &quot;mode&quot;: &quot;0777&quot;,</span>
<span style="color:#00AA00">    &quot;owner&quot;: &quot;1001&quot;,</span>
<span style="color:#00AA00">    &quot;path&quot;: &quot;/mnt/Volume1/docker/mediathekview/config&quot;,</span>
<span style="color:#00AA00">    &quot;size&quot;: 4096,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;directory&quot;,</span>
<span style="color:#00AA00">    &quot;uid&quot;: 1001</span>
<span style="color:#00AA00">}</span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; (item=/mnt/Volume1/docker/mediathekview/data) =&gt; {</span>
<span style="color:#00AA00">    &quot;ansible_loop_var&quot;: &quot;item&quot;,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;gid&quot;: 1001,</span>
<span style="color:#00AA00">    &quot;group&quot;: &quot;ansible-nas&quot;,</span>
<span style="color:#00AA00">    &quot;item&quot;: &quot;/mnt/Volume1/docker/mediathekview/data&quot;,</span>
<span style="color:#00AA00">    &quot;mode&quot;: &quot;0777&quot;,</span>
<span style="color:#00AA00">    &quot;owner&quot;: &quot;1001&quot;,</span>
<span style="color:#00AA00">    &quot;path&quot;: &quot;/mnt/Volume1/docker/mediathekview/data&quot;,</span>
<span style="color:#00AA00">    &quot;size&quot;: 4096,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;directory&quot;,</span>
<span style="color:#00AA00">    &quot;uid&quot;: 1001</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:18:22 +0200 (0:00:00.729)       0:01:30.482 *** 

TASK [mediathekview : Mediathekview Docker Container] *************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/mediathekview/tasks/main.yml:13</b></span>
<span style="color:#AA5500">changed: [ansible-nas] =&gt; {</span>
<span style="color:#AA5500">    &quot;changed&quot;: true,</span>
<span style="color:#AA5500">    &quot;container&quot;: {</span>
<span style="color:#AA5500">        &quot;AppArmorProfile&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">        &quot;Args&quot;: [],</span>
<span style="color:#AA5500">        &quot;Config&quot;: {</span>
<span style="color:#AA5500">            &quot;AttachStderr&quot;: true,</span>
<span style="color:#AA5500">            &quot;AttachStdin&quot;: false,</span>
<span style="color:#AA5500">            &quot;AttachStdout&quot;: true,</span>
<span style="color:#AA5500">            &quot;Cmd&quot;: [</span>
<span style="color:#AA5500">                &quot;/init&quot;</span>
<span style="color:#AA5500">            ],</span>
<span style="color:#AA5500">            &quot;Domainname&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;Entrypoint&quot;: null,</span>
<span style="color:#AA5500">            &quot;Env&quot;: [</span>
<span style="color:#AA5500">                &quot;TZ=Europe/Berlin&quot;,</span>
<span style="color:#AA5500">                &quot;PUID=0&quot;,</span>
<span style="color:#AA5500">                &quot;PGID=0&quot;,</span>
<span style="color:#AA5500">                &quot;PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/opt/base/sbin:/opt/base/bin&quot;,</span>
<span style="color:#AA5500">                &quot;ENV=/root/.docker_rc&quot;,</span>
<span style="color:#AA5500">                &quot;USER_ID=0&quot;,</span>
<span style="color:#AA5500">                &quot;GROUP_ID=0&quot;,</span>
<span style="color:#AA5500">                &quot;SUP_GROUP_IDS=&quot;,</span>
<span style="color:#AA5500">                &quot;UMASK=0022&quot;,</span>
<span style="color:#AA5500">                &quot;LANG=en_US.UTF-8&quot;,</span>
<span style="color:#AA5500">                &quot;KEEP_APP_RUNNING=0&quot;,</span>
<span style="color:#AA5500">                &quot;APP_NICENESS=0&quot;,</span>
<span style="color:#AA5500">                &quot;INSTALL_PACKAGES=&quot;,</span>
<span style="color:#AA5500">                &quot;PACKAGES_MIRROR=&quot;,</span>
<span style="color:#AA5500">                &quot;CONTAINER_DEBUG=0&quot;,</span>
<span style="color:#AA5500">                &quot;DISPLAY_WIDTH=1920&quot;,</span>
<span style="color:#AA5500">                &quot;DISPLAY_HEIGHT=1080&quot;,</span>
<span style="color:#AA5500">                &quot;DARK_MODE=0&quot;,</span>
<span style="color:#AA5500">                &quot;SECURE_CONNECTION=0&quot;,</span>
<span style="color:#AA5500">                &quot;SECURE_CONNECTION_VNC_METHOD=SSL&quot;,</span>
<span style="color:#AA5500">                &quot;SECURE_CONNECTION_CERTS_CHECK_INTERVAL=60&quot;,</span>
<span style="color:#AA5500">                &quot;WEB_LISTENING_PORT=5800&quot;,</span>
<span style="color:#AA5500">                &quot;VNC_LISTENING_PORT=5900&quot;,</span>
<span style="color:#AA5500">                &quot;VNC_PASSWORD=&quot;,</span>
<span style="color:#AA5500">                &quot;ENABLE_CJK_FONT=0&quot;,</span>
<span style="color:#AA5500">                &quot;WEB_AUDIO=0&quot;,</span>
<span style="color:#AA5500">                &quot;WEB_AUTHENTICATION=0&quot;,</span>
<span style="color:#AA5500">                &quot;WEB_AUTHENTICATION_TOKEN_VALIDITY_TIME=24&quot;,</span>
<span style="color:#AA5500">                &quot;WEB_AUTHENTICATION_DEFAULT_USERNAME=&quot;,</span>
<span style="color:#AA5500">                &quot;WEB_AUTHENTICATION_DEFAULT_PASSWORD=&quot;,</span>
<span style="color:#AA5500">                &quot;TERM=xterm&quot;,</span>
<span style="color:#AA5500">                &quot;MEDIATHEK_VERSION=14.3.1&quot;,</span>
<span style="color:#AA5500">                &quot;LC_ALL=en_US.UTF-8&quot;,</span>
<span style="color:#AA5500">                &quot;LANGUAGE=en_US.UTF-8&quot;,</span>
<span style="color:#AA5500">                &quot;APP_NAME=Mediathekview&quot;,</span>
<span style="color:#AA5500">                &quot;S6_KILL_GRACETIME=8000&quot;</span>
<span style="color:#AA5500">            ],</span>
<span style="color:#AA5500">            &quot;ExposedPorts&quot;: {</span>
<span style="color:#AA5500">                &quot;5800/tcp&quot;: {},</span>
<span style="color:#AA5500">                &quot;5900/tcp&quot;: {},</span>
<span style="color:#AA5500">                &quot;8084/tcp&quot;: {}</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            &quot;Hostname&quot;: &quot;6b23d924c59a&quot;,</span>
<span style="color:#AA5500">            &quot;Image&quot;: &quot;conrad784/mediathekview-webinterface:latest&quot;,</span>
<span style="color:#AA5500">            &quot;Labels&quot;: {</span>
<span style="color:#AA5500">                &quot;org.label-schema.description&quot;: &quot;Docker container for Mediathekview&quot;,</span>
<span style="color:#AA5500">                &quot;org.label-schema.name&quot;: &quot;mediathekview&quot;,</span>
<span style="color:#AA5500">                &quot;org.label-schema.schema-version&quot;: &quot;1.0&quot;,</span>
<span style="color:#AA5500">                &quot;org.label-schema.vcs-url&quot;: &quot;https://github.com/conrad784/docker-mediathekview-webinterface&quot;,</span>
<span style="color:#AA5500">                &quot;org.label-schema.version&quot;: &quot;14.3.1&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.created&quot;: &quot;2025-06-18T15:31:59.014Z&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.description&quot;: &quot;X11rdp Version of Mediathekview&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.licenses&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.revision&quot;: &quot;2d02d291626dee3871a4f41227794eee1c55a662&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.source&quot;: &quot;https://github.com/conrad784/docker-mediathekview-webinterface&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.title&quot;: &quot;docker-mediathekview-webinterface&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.url&quot;: &quot;https://github.com/conrad784/docker-mediathekview-webinterface&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.version&quot;: &quot;14.3.1&quot;,</span>
<span style="color:#AA5500">                &quot;traefik.enable&quot;: &quot;True&quot;,</span>
<span style="color:#AA5500">                &quot;traefik.http.routers.mediathekview.rule&quot;: &quot;Host(`mediathekview.Schneider.nbg`)&quot;,</span>
<span style="color:#AA5500">                &quot;traefik.http.routers.mediathekview.tls.certresolver&quot;: &quot;letsencrypt&quot;,</span>
<span style="color:#AA5500">                &quot;traefik.http.routers.mediathekview.tls.domains[0].main&quot;: &quot;Schneider.nbg&quot;,</span>
<span style="color:#AA5500">                &quot;traefik.http.routers.mediathekview.tls.domains[0].sans&quot;: &quot;*.Schneider.nbg&quot;,</span>
<span style="color:#AA5500">                &quot;traefik.http.services.mediathekview.loadbalancer.server.port&quot;: &quot;5800&quot;</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            &quot;OnBuild&quot;: null,</span>
<span style="color:#AA5500">            &quot;OpenStdin&quot;: false,</span>
<span style="color:#AA5500">            &quot;StdinOnce&quot;: false,</span>
<span style="color:#AA5500">            &quot;Tty&quot;: false,</span>
<span style="color:#AA5500">            &quot;User&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;Volumes&quot;: {</span>
<span style="color:#AA5500">                &quot;/config&quot;: {},</span>
<span style="color:#AA5500">                &quot;/output&quot;: {}</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            &quot;WorkingDir&quot;: &quot;/tmp&quot;</span>
<span style="color:#AA5500">        },</span>
<span style="color:#AA5500">        &quot;Created&quot;: &quot;2025-09-25T03:19:50.713160601Z&quot;,</span>
<span style="color:#AA5500">        &quot;Driver&quot;: &quot;overlay2&quot;,</span>
<span style="color:#AA5500">        &quot;ExecIDs&quot;: null,</span>
<span style="color:#AA5500">        &quot;GraphDriver&quot;: {</span>
<span style="color:#AA5500">            &quot;Data&quot;: {</span>
<span style="color:#AA5500">                &quot;ID&quot;: &quot;6b23d924c59ade56b90be7efbbc08e57dfbd35d5393678598e1e188e5fd7343a&quot;,</span>
<span style="color:#AA5500">                &quot;LowerDir&quot;: &quot;/var/lib/docker/overlay2/1757d50d2ed2f92a88626bec44de28fa49cdfe3cb9e645ec808e2dc7a549d288-init/diff:/var/lib/docker/overlay2/47c79add305bcd31e450bc3999d951eac4240e1c9f79ddc8dd79196ffbb24324/diff:/var/lib/docker/overlay2/d4bf86c5f967670dc3e06dc4380d8f70396b2921c224a7268c60d5ddf7775abf/diff:/var/lib/docker/overlay2/922e69c2945e785a814abf203d4faa1ab5d1161a007bde43b810964c4f675889/diff:/var/lib/docker/overlay2/c867e12a7c67971018378de4e74c37210e06c382f6007eabc7162e183f9ea80e/diff:/var/lib/docker/overlay2/e26e19f972b7c8dee482e02084a6384deac2b1a22a3960653f707b77a30f3631/diff:/var/lib/docker/overlay2/1a78d0d54ea4c684b5aaaf59fc8b4446279a9bf85b7fa2779540a843912a4c02/diff:/var/lib/docker/overlay2/a00e9a1b34ea97f8ede22243b1f575a8693cb71b96b9f0307e4a2667ae133c8c/diff:/var/lib/docker/overlay2/17dd1bfcec478d137d4087e0eccdc01b42b8f653cb9b2f7631e4b50ab68f3c58/diff:/var/lib/docker/overlay2/9829c610cc1fde69fe106eca2bfffa753920fbf1d8cdda4e7f87c46fd114b216/diff:/var/lib/docker/overlay2/af7fe550b99b30e1105d2e333dcb4a926750e7ebe4d56e971b1594e120ceae2c/diff:/var/lib/docker/overlay2/fe5fef276cc829ed3dfe0222e35b369ad465e2354e473e3f97e68d7121a0fb8a/diff:/var/lib/docker/overlay2/494b19e1b20762c8f37487ec6d154d08bc5592bec7e3459e0d9cdbc80e4b9063/diff:/var/lib/docker/overlay2/121f1cd83a67684bdd69f291423079fbc743e6495f73ad65b3eded8dc77a4bee/diff:/var/lib/docker/overlay2/cffd8dadf9aef3e4c5b96c31eb6e52d157ef6753e332c520df37d79fc73a1b68/diff:/var/lib/docker/overlay2/1fd0eb1875c48ab75f505aba3e810d5bfaadfb2e758696e20c41bb7e75115e09/diff:/var/lib/docker/overlay2/5b7c667cfb526c0c56653352b5dfa6b927e553321f8f44e57b35c8b0d240af74/diff:/var/lib/docker/overlay2/33b1ab434b8c80e16492b4b10bf765aecbedaf1f264d6b8af53f8bcbac87a8c1/diff:/var/lib/docker/overlay2/bd5088f6c8eefd4df553a45f5e1385762dc85ea0283537aae94e61a624c93a12/diff:/var/lib/docker/overlay2/4d8decbd31fbdf2ea745fbe8e5146f864bb8af13557b2607611c67f6787a8af1/diff:/var/lib/docker/overlay2/2d643368e530c18f51ce02a41fcd76791e29d05a9d04c24731e301bcbe7bb3d5/diff:/var/lib/docker/overlay2/1ffaf0c368838a2f30acc48432b0076effbe9488bd1a66e6085fb570b62caf86/diff:/var/lib/docker/overlay2/84e074e2b6eee24a69f4e3d3c5ad8524668bbb374268b07e2bebe94d3854fe5a/diff:/var/lib/docker/overlay2/11de7cc43314e1d80f128d7e1578ecf90b1cdb9389a683e99138c96b0c2795b0/diff:/var/lib/docker/overlay2/26a123c65fbb2e68affd1a165a97659543c39f1c16e422f3b60297230b640f48/diff:/var/lib/docker/overlay2/359fe72e36a12c222822fe6d3e41c30445e94a5bf1f756b22028198a05a93cf4/diff:/var/lib/docker/overlay2/fde00f173ded433f261fcaee2afc488bc662359b48e01efdcf2e23b3630e50d8/diff:/var/lib/docker/overlay2/e868d2e6c341722753c61f985cd2367dae5409aa7f29d1da60d2386dd14190fd/diff:/var/lib/docker/overlay2/e4ef55e3cbce4ed94764dd2762f60312f5ed4e2c472437fb4e1895d952819b02/diff:/var/lib/docker/overlay2/bec16ebf11a5e4da25b10d61ba09adf76a56ab48446a7dbe049e0004ef6a149f/diff:/var/lib/docker/overlay2/0868b332fa26449386f6a25b4d76e34fd21046a55a5d3c171b340eb8d033b2e1/diff:/var/lib/docker/overlay2/cb8b420bb98771ff68988cfbdfae7b5cc2603b3dce9f16a86977635ff437b4de/diff:/var/lib/docker/overlay2/c1a30c92da5237d534c7e98a6ce1b7c98cd1730ca8d56b3fa31504d984061439/diff:/var/lib/docker/overlay2/d5b6cd8d8a8c7cf4aa16f24f89f0cfb3efa5e03d6e74518701c7cd66782ca8a7/diff:/var/lib/docker/overlay2/78e5fc022bae5d67646d9facaa3fffb209e4802ec716c35e254ba37d21551faa/diff:/var/lib/docker/overlay2/63c99bd00610a894ee87913483d3856a2da516f045375477e12a0be2cc5374f9/diff:/var/lib/docker/overlay2/01f1a93235ac8540b0ec1ff610e86734c471881949b057c63310d520c63452d2/diff:/var/lib/docker/overlay2/897dcf1dafd5e1d4d384a6fa131f3e4f82cd9208130252c227987ad3e4c5785b/diff:/var/lib/docker/overlay2/95d0698e6c7e91a5bd337b443787d104cd93d1eff4d7a894ac0b82eb05997102/diff:/var/lib/docker/overlay2/856c7709c74d8aaeef7371d2bdf0142e20cddef95af007b2b255d2f59bedfce6/diff:/var/lib/docker/overlay2/8e51559e83eecbdd8119f96c82fa44ffbf4771185e5832d7a5110b2b1bcd4332/diff:/var/lib/docker/overlay2/5850b41a0a14254b6dc74bd780a13cd403e9738fd213587773c12d43dc3442cd/diff:/var/lib/docker/overlay2/5fc43ffd9386dd48e17a11d243cd2dc3193404b3a7eeef1ad8132d46c368886b/diff:/var/lib/docker/overlay2/6f29cf5ec2368ef4008b69ee954bab159bb5bd9b39618799b783de8ec9a69382/diff&quot;,</span>
<span style="color:#AA5500">                &quot;MergedDir&quot;: &quot;/var/lib/docker/overlay2/1757d50d2ed2f92a88626bec44de28fa49cdfe3cb9e645ec808e2dc7a549d288/merged&quot;,</span>
<span style="color:#AA5500">                &quot;UpperDir&quot;: &quot;/var/lib/docker/overlay2/1757d50d2ed2f92a88626bec44de28fa49cdfe3cb9e645ec808e2dc7a549d288/diff&quot;,</span>
<span style="color:#AA5500">                &quot;WorkDir&quot;: &quot;/var/lib/docker/overlay2/1757d50d2ed2f92a88626bec44de28fa49cdfe3cb9e645ec808e2dc7a549d288/work&quot;</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            &quot;Name&quot;: &quot;overlay2&quot;</span>
<span style="color:#AA5500">        },</span>
<span style="color:#AA5500">        &quot;HostConfig&quot;: {</span>
<span style="color:#AA5500">            &quot;AutoRemove&quot;: false,</span>
<span style="color:#AA5500">            &quot;Binds&quot;: [</span>
<span style="color:#AA5500">                &quot;/mnt/Volume1/docker/mediathekview/config:/config:rw&quot;,</span>
<span style="color:#AA5500">                &quot;/mnt/Volume1/local/TV:/tv:rw&quot;,</span>
<span style="color:#AA5500">                &quot;/mnt/Volume1/docker/mediathekview/data:/data:rw&quot;</span>
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
<span style="color:#AA5500">                &quot;8084/tcp&quot;: [</span>
<span style="color:#AA5500">                    {</span>
<span style="color:#AA5500">                        &quot;HostIp&quot;: &quot;0.0.0.0&quot;,</span>
<span style="color:#AA5500">                        &quot;HostPort&quot;: &quot;5800&quot;</span>
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
<span style="color:#AA5500">        &quot;HostnamePath&quot;: &quot;/var/lib/docker/containers/6b23d924c59ade56b90be7efbbc08e57dfbd35d5393678598e1e188e5fd7343a/hostname&quot;,</span>
<span style="color:#AA5500">        &quot;HostsPath&quot;: &quot;/var/lib/docker/containers/6b23d924c59ade56b90be7efbbc08e57dfbd35d5393678598e1e188e5fd7343a/hosts&quot;,</span>
<span style="color:#AA5500">        &quot;Id&quot;: &quot;6b23d924c59ade56b90be7efbbc08e57dfbd35d5393678598e1e188e5fd7343a&quot;,</span>
<span style="color:#AA5500">        &quot;Image&quot;: &quot;sha256:6297281640bba0c9ce42251f78c78c996bfff6184e0b7ebb5aa35bce879f2e0b&quot;,</span>
<span style="color:#AA5500">        &quot;LogPath&quot;: &quot;/var/lib/docker/containers/6b23d924c59ade56b90be7efbbc08e57dfbd35d5393678598e1e188e5fd7343a/6b23d924c59ade56b90be7efbbc08e57dfbd35d5393678598e1e188e5fd7343a-json.log&quot;,</span>
<span style="color:#AA5500">        &quot;MountLabel&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">        &quot;Mounts&quot;: [</span>
<span style="color:#AA5500">            {</span>
<span style="color:#AA5500">                &quot;Destination&quot;: &quot;/config&quot;,</span>
<span style="color:#AA5500">                &quot;Mode&quot;: &quot;rw&quot;,</span>
<span style="color:#AA5500">                &quot;Propagation&quot;: &quot;rprivate&quot;,</span>
<span style="color:#AA5500">                &quot;RW&quot;: true,</span>
<span style="color:#AA5500">                &quot;Source&quot;: &quot;/mnt/Volume1/docker/mediathekview/config&quot;,</span>
<span style="color:#AA5500">                &quot;Type&quot;: &quot;bind&quot;</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            {</span>
<span style="color:#AA5500">                &quot;Destination&quot;: &quot;/tv&quot;,</span>
<span style="color:#AA5500">                &quot;Mode&quot;: &quot;rw&quot;,</span>
<span style="color:#AA5500">                &quot;Propagation&quot;: &quot;rprivate&quot;,</span>
<span style="color:#AA5500">                &quot;RW&quot;: true,</span>
<span style="color:#AA5500">                &quot;Source&quot;: &quot;/mnt/Volume1/local/TV&quot;,</span>
<span style="color:#AA5500">                &quot;Type&quot;: &quot;bind&quot;</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            {</span>
<span style="color:#AA5500">                &quot;Destination&quot;: &quot;/data&quot;,</span>
<span style="color:#AA5500">                &quot;Mode&quot;: &quot;rw&quot;,</span>
<span style="color:#AA5500">                &quot;Propagation&quot;: &quot;rprivate&quot;,</span>
<span style="color:#AA5500">                &quot;RW&quot;: true,</span>
<span style="color:#AA5500">                &quot;Source&quot;: &quot;/mnt/Volume1/docker/mediathekview/data&quot;,</span>
<span style="color:#AA5500">                &quot;Type&quot;: &quot;bind&quot;</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            {</span>
<span style="color:#AA5500">                &quot;Destination&quot;: &quot;/output&quot;,</span>
<span style="color:#AA5500">                &quot;Driver&quot;: &quot;local&quot;,</span>
<span style="color:#AA5500">                &quot;Mode&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">                &quot;Name&quot;: &quot;f63e3a4d87be33831d4c87d47557a2d9004d22b7453ac7ee3919abd6c358f85a&quot;,</span>
<span style="color:#AA5500">                &quot;Propagation&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">                &quot;RW&quot;: true,</span>
<span style="color:#AA5500">                &quot;Source&quot;: &quot;/var/lib/docker/volumes/f63e3a4d87be33831d4c87d47557a2d9004d22b7453ac7ee3919abd6c358f85a/_data&quot;,</span>
<span style="color:#AA5500">                &quot;Type&quot;: &quot;volume&quot;</span>
<span style="color:#AA5500">            }</span>
<span style="color:#AA5500">        ],</span>
<span style="color:#AA5500">        &quot;Name&quot;: &quot;/mediathekview&quot;,</span>
<span style="color:#AA5500">        &quot;NetworkSettings&quot;: {</span>
<span style="color:#AA5500">            &quot;Bridge&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;EndpointID&quot;: &quot;2fceecfef0308e68de91dfa780e4132f2475b7ac49dcde175bcfa3c10006ad01&quot;,</span>
<span style="color:#AA5500">            &quot;Gateway&quot;: &quot;172.17.0.1&quot;,</span>
<span style="color:#AA5500">            &quot;GlobalIPv6Address&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;GlobalIPv6PrefixLen&quot;: 0,</span>
<span style="color:#AA5500">            &quot;HairpinMode&quot;: false,</span>
<span style="color:#AA5500">            &quot;IPAddress&quot;: &quot;172.17.0.6&quot;,</span>
<span style="color:#AA5500">            &quot;IPPrefixLen&quot;: 16,</span>
<span style="color:#AA5500">            &quot;IPv6Gateway&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;LinkLocalIPv6Address&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;LinkLocalIPv6PrefixLen&quot;: 0,</span>
<span style="color:#AA5500">            &quot;MacAddress&quot;: &quot;8a:8e:a7:6c:11:13&quot;,</span>
<span style="color:#AA5500">            &quot;Networks&quot;: {</span>
<span style="color:#AA5500">                &quot;bridge&quot;: {</span>
<span style="color:#AA5500">                    &quot;Aliases&quot;: null,</span>
<span style="color:#AA5500">                    &quot;DNSNames&quot;: null,</span>
<span style="color:#AA5500">                    &quot;DriverOpts&quot;: null,</span>
<span style="color:#AA5500">                    &quot;EndpointID&quot;: &quot;2fceecfef0308e68de91dfa780e4132f2475b7ac49dcde175bcfa3c10006ad01&quot;,</span>
<span style="color:#AA5500">                    &quot;Gateway&quot;: &quot;172.17.0.1&quot;,</span>
<span style="color:#AA5500">                    &quot;GlobalIPv6Address&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">                    &quot;GlobalIPv6PrefixLen&quot;: 0,</span>
<span style="color:#AA5500">                    &quot;GwPriority&quot;: 0,</span>
<span style="color:#AA5500">                    &quot;IPAMConfig&quot;: null,</span>
<span style="color:#AA5500">                    &quot;IPAddress&quot;: &quot;172.17.0.6&quot;,</span>
<span style="color:#AA5500">                    &quot;IPPrefixLen&quot;: 16,</span>
<span style="color:#AA5500">                    &quot;IPv6Gateway&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">                    &quot;Links&quot;: null,</span>
<span style="color:#AA5500">                    &quot;MacAddress&quot;: &quot;8a:8e:a7:6c:11:13&quot;,</span>
<span style="color:#AA5500">                    &quot;NetworkID&quot;: &quot;bf69c1dd08283d21e1c03cd9d2f9059cf944e578f95c79babe5a23cdb260be15&quot;</span>
<span style="color:#AA5500">                }</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            &quot;Ports&quot;: {</span>
<span style="color:#AA5500">                &quot;5800/tcp&quot;: null,</span>
<span style="color:#AA5500">                &quot;5900/tcp&quot;: null,</span>
<span style="color:#AA5500">                &quot;8084/tcp&quot;: [</span>
<span style="color:#AA5500">                    {</span>
<span style="color:#AA5500">                        &quot;HostIp&quot;: &quot;0.0.0.0&quot;,</span>
<span style="color:#AA5500">                        &quot;HostPort&quot;: &quot;5800&quot;</span>
<span style="color:#AA5500">                    }</span>
<span style="color:#AA5500">                ]</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            &quot;SandboxID&quot;: &quot;3d9812326feec220930954f2c8f48e7813967fa15452bbb7df7732b68447d6af&quot;,</span>
<span style="color:#AA5500">            &quot;SandboxKey&quot;: &quot;/var/run/docker/netns/3d9812326fee&quot;,</span>
<span style="color:#AA5500">            &quot;SecondaryIPAddresses&quot;: null,</span>
<span style="color:#AA5500">            &quot;SecondaryIPv6Addresses&quot;: null</span>
<span style="color:#AA5500">        },</span>
<span style="color:#AA5500">        &quot;Path&quot;: &quot;/init&quot;,</span>
<span style="color:#AA5500">        &quot;Platform&quot;: &quot;linux&quot;,</span>
<span style="color:#AA5500">        &quot;ProcessLabel&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">        &quot;ResolvConfPath&quot;: &quot;/var/lib/docker/containers/6b23d924c59ade56b90be7efbbc08e57dfbd35d5393678598e1e188e5fd7343a/resolv.conf&quot;,</span>
<span style="color:#AA5500">        &quot;RestartCount&quot;: 0,</span>
<span style="color:#AA5500">        &quot;State&quot;: {</span>
<span style="color:#AA5500">            &quot;Dead&quot;: false,</span>
<span style="color:#AA5500">            &quot;Error&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;ExitCode&quot;: 0,</span>
<span style="color:#AA5500">            &quot;FinishedAt&quot;: &quot;0001-01-01T00:00:00Z&quot;,</span>
<span style="color:#AA5500">            &quot;OOMKilled&quot;: false,</span>
<span style="color:#AA5500">            &quot;Paused&quot;: false,</span>
<span style="color:#AA5500">            &quot;Pid&quot;: 376364,</span>
<span style="color:#AA5500">            &quot;Restarting&quot;: false,</span>
<span style="color:#AA5500">            &quot;Running&quot;: true,</span>
<span style="color:#AA5500">            &quot;StartedAt&quot;: &quot;2025-09-25T03:19:52.009951586Z&quot;,</span>
<span style="color:#AA5500">            &quot;Status&quot;: &quot;running&quot;</span>
<span style="color:#AA5500">        }</span>
<span style="color:#AA5500">    }</span>
<span style="color:#AA5500">}</span>
Donnerstag 25 September 2025  05:19:52 +0200 (0:01:29.422)       0:02:59.904 *** 
Donnerstag 25 September 2025  05:19:52 +0200 (0:00:00.092)       0:02:59.997 *** 
Donnerstag 25 September 2025  05:19:52 +0200 (0:00:00.079)       0:03:00.076 *** 
Donnerstag 25 September 2025  05:19:52 +0200 (0:00:00.058)       0:03:00.135 *** 

TASK [minecraft-bedrock-server : Stop Minecraft Bedrock Server] ***************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/minecraft-bedrock-server/tasks/main.yml:34</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:19:53 +0200 (0:00:00.629)       0:03:00.764 *** 
Donnerstag 25 September 2025  05:19:53 +0200 (0:00:00.067)       0:03:00.832 *** 
Donnerstag 25 September 2025  05:19:53 +0200 (0:00:00.060)       0:03:00.893 *** 

TASK [minecraft-server : Stop Minecraft Server] *******************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/minecraft-server/tasks/main.yml:27</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:19:53 +0200 (0:00:00.623)       0:03:01.516 *** 
Donnerstag 25 September 2025  05:19:53 +0200 (0:00:00.058)       0:03:01.575 *** 

TASK [minidlna : Stop MiniDLNA] ***********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/minidlna/tasks/main.yml:24</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:19:54 +0200 (0:00:00.633)       0:03:02.209 *** 
Donnerstag 25 September 2025  05:19:54 +0200 (0:00:00.066)       0:03:02.275 *** 
Donnerstag 25 September 2025  05:19:54 +0200 (0:00:00.063)       0:03:02.338 *** 
Donnerstag 25 September 2025  05:19:54 +0200 (0:00:00.194)       0:03:02.533 *** 
Donnerstag 25 September 2025  05:19:54 +0200 (0:00:00.058)       0:03:02.591 *** 

TASK [miniflux : Stop Miniflux] ***********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/miniflux/tasks/main.yml:60</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:19:55 +0200 (0:00:00.633)       0:03:03.225 *** 
Donnerstag 25 September 2025  05:19:55 +0200 (0:00:00.080)       0:03:03.306 *** 
Donnerstag 25 September 2025  05:19:55 +0200 (0:00:00.060)       0:03:03.366 *** 

TASK [minio : Stop minio] *****************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/minio/tasks/main.yml:40</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:19:56 +0200 (0:00:00.698)       0:03:04.064 *** 
Donnerstag 25 September 2025  05:19:56 +0200 (0:00:00.079)       0:03:04.144 *** 
Donnerstag 25 September 2025  05:19:56 +0200 (0:00:00.061)       0:03:04.205 *** 
Donnerstag 25 September 2025  05:19:56 +0200 (0:00:00.056)       0:03:04.261 *** 

TASK [mosquitto : Stop Mosquitto] *********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/mosquitto/tasks/main.yml:38</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:19:57 +0200 (0:00:00.615)       0:03:04.877 *** 
Donnerstag 25 September 2025  05:19:57 +0200 (0:00:00.067)       0:03:04.945 *** 
Donnerstag 25 September 2025  05:19:57 +0200 (0:00:00.050)       0:03:04.995 *** 

TASK [mumble : Stop Mumble] ***************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/mumble/tasks/main.yml:39</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:19:58 +0200 (0:00:00.653)       0:03:05.648 *** 
Donnerstag 25 September 2025  05:19:58 +0200 (0:00:00.086)       0:03:05.735 *** 
Donnerstag 25 September 2025  05:19:58 +0200 (0:00:00.054)       0:03:05.789 *** 

TASK [mylar : Stop Mylar] *****************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/mylar/tasks/main.yml:41</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:19:58 +0200 (0:00:00.631)       0:03:06.421 *** 
Donnerstag 25 September 2025  05:19:59 +0200 (0:00:00.371)       0:03:06.792 *** 
Donnerstag 25 September 2025  05:19:59 +0200 (0:00:00.053)       0:03:06.846 *** 

TASK [mymediaforalexa : Stop Mymediaforalexa] *********************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/mymediaforalexa/tasks/main.yml:27</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:19:59 +0200 (0:00:00.621)       0:03:07.468 *** 
Donnerstag 25 September 2025  05:19:59 +0200 (0:00:00.074)       0:03:07.543 *** 
Donnerstag 25 September 2025  05:19:59 +0200 (0:00:00.064)       0:03:07.607 *** 

TASK [n8n : Stop n8n] *********************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/n8n/tasks/main.yml:40</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:20:00 +0200 (0:00:00.768)       0:03:08.375 *** 
Donnerstag 25 September 2025  05:20:00 +0200 (0:00:00.077)       0:03:08.453 *** 
Donnerstag 25 September 2025  05:20:00 +0200 (0:00:00.069)       0:03:08.523 *** 

TASK [navidrome : Stop Navidrome] *********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/navidrome/tasks/main.yml:42</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:20:01 +0200 (0:00:00.643)       0:03:09.166 *** 
Donnerstag 25 September 2025  05:20:01 +0200 (0:00:00.075)       0:03:09.242 *** 
Donnerstag 25 September 2025  05:20:01 +0200 (0:00:00.060)       0:03:09.302 *** 

TASK [netbootxyz : Stop Netbootxyz] *******************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/netbootxyz/tasks/main.yml:41</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:20:02 +0200 (0:00:00.632)       0:03:09.935 *** 
Donnerstag 25 September 2025  05:20:02 +0200 (0:00:00.059)       0:03:09.994 *** 
Donnerstag 25 September 2025  05:20:02 +0200 (0:00:00.062)       0:03:10.057 *** 

TASK [netdata : Stop Netdata] *************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/netdata/tasks/main.yml:41</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:20:03 +0200 (0:00:00.643)       0:03:10.700 *** 
Donnerstag 25 September 2025  05:20:03 +0200 (0:00:00.067)       0:03:10.767 *** 
Donnerstag 25 September 2025  05:20:03 +0200 (0:00:00.203)       0:03:10.971 *** 
Donnerstag 25 September 2025  05:20:03 +0200 (0:00:00.049)       0:03:11.021 *** 
Donnerstag 25 September 2025  05:20:03 +0200 (0:00:00.057)       0:03:11.078 *** 

TASK [nextcloud : Stop Nextcloud] *********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/nextcloud/tasks/main.yml:72</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:20:04 +0200 (0:00:00.633)       0:03:11.711 *** 

TASK [nextcloud : Stop Nextcloud DB] ******************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/nextcloud/tasks/main.yml:76</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:20:04 +0200 (0:00:00.624)       0:03:12.336 *** 
Donnerstag 25 September 2025  05:20:04 +0200 (0:00:00.054)       0:03:12.390 *** 
Donnerstag 25 September 2025  05:20:04 +0200 (0:00:00.061)       0:03:12.452 *** 
Donnerstag 25 September 2025  05:20:04 +0200 (0:00:00.059)       0:03:12.512 *** 
Donnerstag 25 September 2025  05:20:04 +0200 (0:00:00.055)       0:03:12.567 *** 
Donnerstag 25 September 2025  05:20:05 +0200 (0:00:00.061)       0:03:12.629 *** 

TASK [nomad : Check if Nomad is installed] ************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/nomad/tasks/main.yml:37</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;stat&quot;: {</span>
<span style="color:#00AA00">        &quot;exists&quot;: false</span>
<span style="color:#00AA00">    }</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:20:05 +0200 (0:00:00.392)       0:03:13.021 *** 
Donnerstag 25 September 2025  05:20:05 +0200 (0:00:00.063)       0:03:13.084 *** 
Donnerstag 25 September 2025  05:20:05 +0200 (0:00:00.090)       0:03:13.175 *** 
Donnerstag 25 September 2025  05:20:05 +0200 (0:00:00.075)       0:03:13.250 *** 
Donnerstag 25 September 2025  05:20:05 +0200 (0:00:00.047)       0:03:13.298 *** 

TASK [nzbget : Stop NZBget] ***************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/nzbget/tasks/main.yml:38</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:20:06 +0200 (0:00:00.636)       0:03:13.934 *** 
Donnerstag 25 September 2025  05:20:06 +0200 (0:00:00.065)       0:03:14.000 *** 
Donnerstag 25 September 2025  05:20:06 +0200 (0:00:00.063)       0:03:14.063 *** 

TASK [octoprint : Stop Octoprint] *********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/octoprint/tasks/main.yml:40</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:20:07 +0200 (0:00:00.759)       0:03:14.823 *** 
Donnerstag 25 September 2025  05:20:07 +0200 (0:00:00.064)       0:03:14.887 *** 
Donnerstag 25 September 2025  05:20:07 +0200 (0:00:00.051)       0:03:14.939 *** 

TASK [ombi : Stop Ombi] *******************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/ombi/tasks/main.yml:35</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:20:07 +0200 (0:00:00.628)       0:03:15.567 *** 
Donnerstag 25 September 2025  05:20:08 +0200 (0:00:00.067)       0:03:15.634 *** 
Donnerstag 25 September 2025  05:20:08 +0200 (0:00:00.065)       0:03:15.700 *** 
Donnerstag 25 September 2025  05:20:08 +0200 (0:00:00.094)       0:03:15.794 *** 
Donnerstag 25 September 2025  05:20:08 +0200 (0:00:00.063)       0:03:15.857 *** 

TASK [openhab : Stop openHAB] *************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/openhab/tasks/main.yml:60</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:20:08 +0200 (0:00:00.669)       0:03:16.527 *** 
Donnerstag 25 September 2025  05:20:08 +0200 (0:00:00.064)       0:03:16.591 *** 
Donnerstag 25 September 2025  05:20:09 +0200 (0:00:00.066)       0:03:16.658 *** 

TASK [organizr : Stop Organizr] ***********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/organizr/tasks/main.yml:38</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:20:09 +0200 (0:00:00.704)       0:03:17.362 *** 
Donnerstag 25 September 2025  05:20:09 +0200 (0:00:00.066)       0:03:17.428 *** 
Donnerstag 25 September 2025  05:20:09 +0200 (0:00:00.065)       0:03:17.494 *** 

TASK [overseerr : Stop Overseerr] *********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/overseerr/tasks/main.yml:43</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:20:10 +0200 (0:00:00.618)       0:03:18.112 *** 
Donnerstag 25 September 2025  05:20:10 +0200 (0:00:00.111)       0:03:18.224 *** 
Donnerstag 25 September 2025  05:20:10 +0200 (0:00:00.199)       0:03:18.423 *** 
Donnerstag 25 September 2025  05:20:10 +0200 (0:00:00.050)       0:03:18.474 *** 
Donnerstag 25 September 2025  05:20:10 +0200 (0:00:00.068)       0:03:18.542 *** 
Donnerstag 25 September 2025  05:20:10 +0200 (0:00:00.062)       0:03:18.605 *** 

TASK [paperless_ng : Stop paperless_ng] ***************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/paperless_ng/tasks/main.yml:83</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:20:11 +0200 (0:00:00.619)       0:03:19.224 *** 

TASK [paperless_ng : Stop paperless_ng redis] *********************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/paperless_ng/tasks/main.yml:87</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:20:12 +0200 (0:00:00.598)       0:03:19.823 *** 

TASK [paperless_ng : Stop paperless_ng db] ************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/paperless_ng/tasks/main.yml:91</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:20:12 +0200 (0:00:00.638)       0:03:20.461 *** 
Donnerstag 25 September 2025  05:20:12 +0200 (0:00:00.079)       0:03:20.540 *** 
Donnerstag 25 September 2025  05:20:12 +0200 (0:00:00.051)       0:03:20.592 *** 
Donnerstag 25 September 2025  05:20:13 +0200 (0:00:00.053)       0:03:20.646 *** 
Donnerstag 25 September 2025  05:20:13 +0200 (0:00:00.073)       0:03:20.720 *** 

TASK [piwigo : Stop Piwigo] ***************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/piwigo/tasks/main.yml:71</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:20:13 +0200 (0:00:00.656)       0:03:21.376 *** 

TASK [piwigo : Stop Piwigo Db] ************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/piwigo/tasks/main.yml:75</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:20:14 +0200 (0:00:00.601)       0:03:21.978 *** 
Donnerstag 25 September 2025  05:20:14 +0200 (0:00:00.075)       0:03:22.054 *** 
Donnerstag 25 September 2025  05:20:14 +0200 (0:00:00.069)       0:03:22.124 *** 

TASK [plex : Stop Plex] *******************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/plex/tasks/main.yml:51</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:20:15 +0200 (0:00:00.667)       0:03:22.791 *** 
Donnerstag 25 September 2025  05:20:15 +0200 (0:00:00.064)       0:03:22.855 *** 

TASK [portainer : Create Portainer Directories] *******************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/portainer/tasks/main.yml:9</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; (item=/mnt/Volume1/docker/portainer/config) =&gt; {</span>
<span style="color:#00AA00">    &quot;ansible_loop_var&quot;: &quot;item&quot;,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;gid&quot;: 1001,</span>
<span style="color:#00AA00">    &quot;group&quot;: &quot;ansible-nas&quot;,</span>
<span style="color:#00AA00">    &quot;item&quot;: &quot;/mnt/Volume1/docker/portainer/config&quot;,</span>
<span style="color:#00AA00">    &quot;mode&quot;: &quot;0777&quot;,</span>
<span style="color:#00AA00">    &quot;owner&quot;: &quot;1001&quot;,</span>
<span style="color:#00AA00">    &quot;path&quot;: &quot;/mnt/Volume1/docker/portainer/config&quot;,</span>
<span style="color:#00AA00">    &quot;size&quot;: 4096,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;directory&quot;,</span>
<span style="color:#00AA00">    &quot;uid&quot;: 1001</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:20:15 +0200 (0:00:00.399)       0:03:23.255 *** 

TASK [portainer : Portainer Docker Container] *********************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/portainer/tasks/main.yml:16</b></span>
<span style="color:#AA5500">changed: [ansible-nas] =&gt; {</span>
<span style="color:#AA5500">    &quot;changed&quot;: true,</span>
<span style="color:#AA5500">    &quot;container&quot;: {</span>
<span style="color:#AA5500">        &quot;AppArmorProfile&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">        &quot;Args&quot;: [],</span>
<span style="color:#AA5500">        &quot;Config&quot;: {</span>
<span style="color:#AA5500">            &quot;AttachStderr&quot;: true,</span>
<span style="color:#AA5500">            &quot;AttachStdin&quot;: false,</span>
<span style="color:#AA5500">            &quot;AttachStdout&quot;: true,</span>
<span style="color:#AA5500">            &quot;Cmd&quot;: null,</span>
<span style="color:#AA5500">            &quot;Domainname&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;Entrypoint&quot;: [</span>
<span style="color:#AA5500">                &quot;/portainer&quot;</span>
<span style="color:#AA5500">            ],</span>
<span style="color:#AA5500">            &quot;Env&quot;: [</span>
<span style="color:#AA5500">                &quot;PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin&quot;</span>
<span style="color:#AA5500">            ],</span>
<span style="color:#AA5500">            &quot;ExposedPorts&quot;: {</span>
<span style="color:#AA5500">                &quot;8000/tcp&quot;: {},</span>
<span style="color:#AA5500">                &quot;9000/tcp&quot;: {},</span>
<span style="color:#AA5500">                &quot;9443/tcp&quot;: {}</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            &quot;Hostname&quot;: &quot;8bd48bdd9564&quot;,</span>
<span style="color:#AA5500">            &quot;Image&quot;: &quot;portainer/portainer-ce:latest&quot;,</span>
<span style="color:#AA5500">            &quot;Labels&quot;: {</span>
<span style="color:#AA5500">                &quot;com.docker.desktop.extension.api.version&quot;: &quot;&gt;= 0.2.2&quot;,</span>
<span style="color:#AA5500">                &quot;com.docker.desktop.extension.icon&quot;: &quot;https://portainer-io-assets.sfo2.cdn.digitaloceanspaces.com/logos/portainer.png&quot;,</span>
<span style="color:#AA5500">                &quot;com.docker.extension.additional-urls&quot;: &quot;[{\&quot;title\&quot;:\&quot;Website\&quot;,\&quot;url\&quot;:\&quot;https://www.portainer.io?utm_campaign=DockerCon&amp;utm_source=DockerDesktop\&quot;},{\&quot;title\&quot;:\&quot;Documentation\&quot;,\&quot;url\&quot;:\&quot;https://docs.portainer.io\&quot;},{\&quot;title\&quot;:\&quot;Support\&quot;,\&quot;url\&quot;:\&quot;https://join.slack.com/t/portainer/shared_invite/zt-txh3ljab-52QHTyjCqbe5RibC2lcjKA\&quot;}]&quot;,</span>
<span style="color:#AA5500">                &quot;com.docker.extension.detailed-description&quot;: &quot;&lt;p data-renderer-start-pos=\&quot;226\&quot;&gt;Portainer&amp;rsquo;s Docker Desktop extension gives you access to all of Portainer&amp;rsquo;s rich management functionality within your docker desktop experience.&lt;/p&gt;&lt;h2 data-renderer-start-pos=\&quot;374\&quot;&gt;With Portainer you can:&lt;/h2&gt;&lt;ul&gt;&lt;li&gt;See all your running containers&lt;/li&gt;&lt;li&gt;Easily view all of your container logs&lt;/li&gt;&lt;li&gt;Console into containers&lt;/li&gt;&lt;li&gt;Easily deploy your code into containers using a simple form&lt;/li&gt;&lt;li&gt;Turn your YAML into custom templates for easy reuse&lt;/li&gt;&lt;/ul&gt;&lt;h2 data-renderer-start-pos=\&quot;660\&quot;&gt;About Portainer&amp;nbsp;&lt;/h2&gt;&lt;p data-renderer-start-pos=\&quot;680\&quot;&gt;Portainer is the worlds&amp;rsquo; most popular universal container management platform with more than 650,000 active monthly users. Portainer can be used to manage Docker Standalone, Kubernetes and Docker Swarm environments through a single common interface. It includes a simple GitOps automation engine and a Kube API.&amp;nbsp;&lt;/p&gt;&lt;p data-renderer-start-pos=\&quot;1006\&quot;&gt;Portainer Business Edition is our fully supported commercial grade product for business-wide use. It includes all the functionality that businesses need to manage containers at scale. Visit &lt;a class=\&quot;sc-jKJlTe dPfAtb\&quot; href=\&quot;http://portainer.io/\&quot; title=\&quot;http://Portainer.io\&quot; data-renderer-mark=\&quot;true\&quot;&gt;Portainer.io&lt;/a&gt; to learn more about Portainer Business and &lt;a class=\&quot;sc-jKJlTe dPfAtb\&quot; href=\&quot;http://portainer.io/take-3?utm_campaign=DockerCon&amp;amp;utm_source=Docker%20Desktop\&quot; title=\&quot;http://portainer.io/take-3?utm_campaign=DockerCon&amp;amp;utm_source=Docker%20Desktop\&quot; data-renderer-mark=\&quot;true\&quot;&gt;get 3 free nodes.&lt;/a&gt;&lt;/p&gt;&quot;,</span>
<span style="color:#AA5500">                &quot;com.docker.extension.publisher-url&quot;: &quot;https://www.portainer.io&quot;,</span>
<span style="color:#AA5500">                &quot;com.docker.extension.screenshots&quot;: &quot;[{\&quot;alt\&quot;: \&quot;screenshot one\&quot;, \&quot;url\&quot;: \&quot;https://portainer-io-assets.sfo2.digitaloceanspaces.com/screenshots/docker-extension-1.png\&quot;},{\&quot;alt\&quot;: \&quot;screenshot two\&quot;, \&quot;url\&quot;: \&quot;https://portainer-io-assets.sfo2.digitaloceanspaces.com/screenshots/docker-extension-2.png\&quot;},{\&quot;alt\&quot;: \&quot;screenshot three\&quot;, \&quot;url\&quot;: \&quot;https://portainer-io-assets.sfo2.digitaloceanspaces.com/screenshots/docker-extension-3.png\&quot;},{\&quot;alt\&quot;: \&quot;screenshot four\&quot;, \&quot;url\&quot;: \&quot;https://portainer-io-assets.sfo2.digitaloceanspaces.com/screenshots/docker-extension-4.png\&quot;},{\&quot;alt\&quot;: \&quot;screenshot five\&quot;, \&quot;url\&quot;: \&quot;https://portainer-io-assets.sfo2.digitaloceanspaces.com/screenshots/docker-extension-5.png\&quot;},{\&quot;alt\&quot;: \&quot;screenshot six\&quot;, \&quot;url\&quot;: \&quot;https://portainer-io-assets.sfo2.digitaloceanspaces.com/screenshots/docker-extension-6.png\&quot;},{\&quot;alt\&quot;: \&quot;screenshot seven\&quot;, \&quot;url\&quot;: \&quot;https://portainer-io-assets.sfo2.digitaloceanspaces.com/screenshots/docker-extension-7.png\&quot;},{\&quot;alt\&quot;: \&quot;screenshot eight\&quot;, \&quot;url\&quot;: \&quot;https://portainer-io-assets.sfo2.digitaloceanspaces.com/screenshots/docker-extension-8.png\&quot;},{\&quot;alt\&quot;: \&quot;screenshot nine\&quot;, \&quot;url\&quot;: \&quot;https://portainer-io-assets.sfo2.digitaloceanspaces.com/screenshots/docker-extension-9.png\&quot;}]&quot;,</span>
<span style="color:#AA5500">                &quot;homepage.description&quot;: &quot;Container management&quot;,</span>
<span style="color:#AA5500">                &quot;homepage.group&quot;: &quot;System Tools&quot;,</span>
<span style="color:#AA5500">                &quot;homepage.href&quot;: &quot;https://192.168.2.181:9000&quot;,</span>
<span style="color:#AA5500">                &quot;homepage.icon&quot;: &quot;portainer.png&quot;,</span>
<span style="color:#AA5500">                &quot;homepage.name&quot;: &quot;Portainer&quot;,</span>
<span style="color:#AA5500">                &quot;homepage.widget.type&quot;: &quot;portainer&quot;,</span>
<span style="color:#AA5500">                &quot;homepage.widget.url&quot;: &quot;https://192.168.2.181:9000&quot;,</span>
<span style="color:#AA5500">                &quot;io.portainer.server&quot;: &quot;true&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.description&quot;: &quot;Docker container management made simple, with the world’s most popular GUI-based container management platform.&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.title&quot;: &quot;Portainer&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.vendor&quot;: &quot;Portainer.io&quot;,</span>
<span style="color:#AA5500">                &quot;traefik.enable&quot;: &quot;False&quot;,</span>
<span style="color:#AA5500">                &quot;traefik.http.middlewares.portainer-ipallowlist.ipallowlist.sourcerange&quot;: &quot;0.0.0.0/0&quot;,</span>
<span style="color:#AA5500">                &quot;traefik.http.routers.portainer.middlewares&quot;: &quot;portainer-ipallowlist@docker&quot;,</span>
<span style="color:#AA5500">                &quot;traefik.http.routers.portainer.rule&quot;: &quot;Host(`portainer.Schneider.nbg`)&quot;,</span>
<span style="color:#AA5500">                &quot;traefik.http.routers.portainer.tls.certresolver&quot;: &quot;letsencrypt&quot;,</span>
<span style="color:#AA5500">                &quot;traefik.http.routers.portainer.tls.domains[0].main&quot;: &quot;Schneider.nbg&quot;,</span>
<span style="color:#AA5500">                &quot;traefik.http.routers.portainer.tls.domains[0].sans&quot;: &quot;*.Schneider.nbg&quot;,</span>
<span style="color:#AA5500">                &quot;traefik.http.services.portainer.loadbalancer.server.port&quot;: &quot;9443&quot;</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            &quot;OnBuild&quot;: null,</span>
<span style="color:#AA5500">            &quot;OpenStdin&quot;: false,</span>
<span style="color:#AA5500">            &quot;StdinOnce&quot;: false,</span>
<span style="color:#AA5500">            &quot;Tty&quot;: false,</span>
<span style="color:#AA5500">            &quot;User&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;Volumes&quot;: {</span>
<span style="color:#AA5500">                &quot;/data&quot;: {}</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            &quot;WorkingDir&quot;: &quot;/&quot;</span>
<span style="color:#AA5500">        },</span>
<span style="color:#AA5500">        &quot;Created&quot;: &quot;2025-09-22T15:03:42.214285185Z&quot;,</span>
<span style="color:#AA5500">        &quot;Driver&quot;: &quot;overlay2&quot;,</span>
<span style="color:#AA5500">        &quot;ExecIDs&quot;: null,</span>
<span style="color:#AA5500">        &quot;GraphDriver&quot;: {</span>
<span style="color:#AA5500">            &quot;Data&quot;: {</span>
<span style="color:#AA5500">                &quot;ID&quot;: &quot;8bd48bdd95640c7b95c74843ddfa5b2e54381ee39a0925dc663749d8896d5b44&quot;,</span>
<span style="color:#AA5500">                &quot;LowerDir&quot;: &quot;/var/lib/docker/overlay2/d9fabc2e82996daaf0aa2645a279954083d36480bea3b1be244449d2f8fceba0-init/diff:/var/lib/docker/overlay2/7259765902b1100fb72d7d93d515bbb7604d23657536c6583eeed4c13b7b8bd3/diff:/var/lib/docker/overlay2/eecf25b1729d6ae4886988a8c2f9c9010c909e2bd03d6029e6c1f86e54bc9d35/diff:/var/lib/docker/overlay2/d33e7a84636be4dcb89d60999a76e32f236c0300813d13defe6b9a4a3beb66de/diff:/var/lib/docker/overlay2/2fd04b9b675a1966fdec635c32b0ec934cbe47f224e42dd065cf7380bb85e691/diff:/var/lib/docker/overlay2/958fefdfe86205b11dc7d04d8c8fbc278a797a4adff49439362baa9808ba7e71/diff:/var/lib/docker/overlay2/7a1065870391d0861bcd390fee37a5b205ddaa8c8667ac8b89a3f6b86537492c/diff:/var/lib/docker/overlay2/5ba63b9e2db5bd874609631d2bf596dac32910ecee07daa72844c6033bd9df0b/diff:/var/lib/docker/overlay2/172c41da2cf53b18495524e60bd198cfe7a94be589ef3453cce56549a395fd49/diff&quot;,</span>
<span style="color:#AA5500">                &quot;MergedDir&quot;: &quot;/var/lib/docker/overlay2/d9fabc2e82996daaf0aa2645a279954083d36480bea3b1be244449d2f8fceba0/merged&quot;,</span>
<span style="color:#AA5500">                &quot;UpperDir&quot;: &quot;/var/lib/docker/overlay2/d9fabc2e82996daaf0aa2645a279954083d36480bea3b1be244449d2f8fceba0/diff&quot;,</span>
<span style="color:#AA5500">                &quot;WorkDir&quot;: &quot;/var/lib/docker/overlay2/d9fabc2e82996daaf0aa2645a279954083d36480bea3b1be244449d2f8fceba0/work&quot;</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            &quot;Name&quot;: &quot;overlay2&quot;</span>
<span style="color:#AA5500">        },</span>
<span style="color:#AA5500">        &quot;HostConfig&quot;: {</span>
<span style="color:#AA5500">            &quot;AutoRemove&quot;: false,</span>
<span style="color:#AA5500">            &quot;Binds&quot;: [</span>
<span style="color:#AA5500">                &quot;/mnt/Volume1/docker/portainer/config:/data:rw&quot;,</span>
<span style="color:#AA5500">                &quot;/var/run/docker.sock:/var/run/docker.sock:ro&quot;,</span>
<span style="color:#AA5500">                &quot;/etc/timezone:/etc/timezone:ro&quot;</span>
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
<span style="color:#AA5500">            &quot;Dns&quot;: [],</span>
<span style="color:#AA5500">            &quot;DnsOptions&quot;: [],</span>
<span style="color:#AA5500">            &quot;DnsSearch&quot;: [],</span>
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
<span style="color:#AA5500">                &quot;9000/tcp&quot;: [</span>
<span style="color:#AA5500">                    {</span>
<span style="color:#AA5500">                        &quot;HostIp&quot;: &quot;0.0.0.0&quot;,</span>
<span style="color:#AA5500">                        &quot;HostPort&quot;: &quot;9000&quot;</span>
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
<span style="color:#AA5500">        &quot;HostnamePath&quot;: &quot;/var/lib/docker/containers/8bd48bdd95640c7b95c74843ddfa5b2e54381ee39a0925dc663749d8896d5b44/hostname&quot;,</span>
<span style="color:#AA5500">        &quot;HostsPath&quot;: &quot;/var/lib/docker/containers/8bd48bdd95640c7b95c74843ddfa5b2e54381ee39a0925dc663749d8896d5b44/hosts&quot;,</span>
<span style="color:#AA5500">        &quot;Id&quot;: &quot;8bd48bdd95640c7b95c74843ddfa5b2e54381ee39a0925dc663749d8896d5b44&quot;,</span>
<span style="color:#AA5500">        &quot;Image&quot;: &quot;sha256:af759842dc6de1ed62294ed21d7358a913a2f439521492e15c699783b2732ba9&quot;,</span>
<span style="color:#AA5500">        &quot;LogPath&quot;: &quot;/var/lib/docker/containers/8bd48bdd95640c7b95c74843ddfa5b2e54381ee39a0925dc663749d8896d5b44/8bd48bdd95640c7b95c74843ddfa5b2e54381ee39a0925dc663749d8896d5b44-json.log&quot;,</span>
<span style="color:#AA5500">        &quot;MountLabel&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">        &quot;Mounts&quot;: [</span>
<span style="color:#AA5500">            {</span>
<span style="color:#AA5500">                &quot;Destination&quot;: &quot;/etc/timezone&quot;,</span>
<span style="color:#AA5500">                &quot;Mode&quot;: &quot;ro&quot;,</span>
<span style="color:#AA5500">                &quot;Propagation&quot;: &quot;rprivate&quot;,</span>
<span style="color:#AA5500">                &quot;RW&quot;: false,</span>
<span style="color:#AA5500">                &quot;Source&quot;: &quot;/etc/timezone&quot;,</span>
<span style="color:#AA5500">                &quot;Type&quot;: &quot;bind&quot;</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            {</span>
<span style="color:#AA5500">                &quot;Destination&quot;: &quot;/var/run/docker.sock&quot;,</span>
<span style="color:#AA5500">                &quot;Mode&quot;: &quot;ro&quot;,</span>
<span style="color:#AA5500">                &quot;Propagation&quot;: &quot;rprivate&quot;,</span>
<span style="color:#AA5500">                &quot;RW&quot;: false,</span>
<span style="color:#AA5500">                &quot;Source&quot;: &quot;/var/run/docker.sock&quot;,</span>
<span style="color:#AA5500">                &quot;Type&quot;: &quot;bind&quot;</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            {</span>
<span style="color:#AA5500">                &quot;Destination&quot;: &quot;/data&quot;,</span>
<span style="color:#AA5500">                &quot;Mode&quot;: &quot;rw&quot;,</span>
<span style="color:#AA5500">                &quot;Propagation&quot;: &quot;rprivate&quot;,</span>
<span style="color:#AA5500">                &quot;RW&quot;: true,</span>
<span style="color:#AA5500">                &quot;Source&quot;: &quot;/mnt/Volume1/docker/portainer/config&quot;,</span>
<span style="color:#AA5500">                &quot;Type&quot;: &quot;bind&quot;</span>
<span style="color:#AA5500">            }</span>
<span style="color:#AA5500">        ],</span>
<span style="color:#AA5500">        &quot;Name&quot;: &quot;/portainer&quot;,</span>
<span style="color:#AA5500">        &quot;NetworkSettings&quot;: {</span>
<span style="color:#AA5500">            &quot;Bridge&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;EndpointID&quot;: &quot;a0887ab1cffae0cafbe8186dcca55615a67dfbec17ba00ca18b4ddfcd655c689&quot;,</span>
<span style="color:#AA5500">            &quot;Gateway&quot;: &quot;172.17.0.1&quot;,</span>
<span style="color:#AA5500">            &quot;GlobalIPv6Address&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;GlobalIPv6PrefixLen&quot;: 0,</span>
<span style="color:#AA5500">            &quot;HairpinMode&quot;: false,</span>
<span style="color:#AA5500">            &quot;IPAddress&quot;: &quot;172.17.0.5&quot;,</span>
<span style="color:#AA5500">            &quot;IPPrefixLen&quot;: 16,</span>
<span style="color:#AA5500">            &quot;IPv6Gateway&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;LinkLocalIPv6Address&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;LinkLocalIPv6PrefixLen&quot;: 0,</span>
<span style="color:#AA5500">            &quot;MacAddress&quot;: &quot;1e:85:84:f7:c1:99&quot;,</span>
<span style="color:#AA5500">            &quot;Networks&quot;: {</span>
<span style="color:#AA5500">                &quot;bridge&quot;: {</span>
<span style="color:#AA5500">                    &quot;Aliases&quot;: null,</span>
<span style="color:#AA5500">                    &quot;DNSNames&quot;: null,</span>
<span style="color:#AA5500">                    &quot;DriverOpts&quot;: null,</span>
<span style="color:#AA5500">                    &quot;EndpointID&quot;: &quot;a0887ab1cffae0cafbe8186dcca55615a67dfbec17ba00ca18b4ddfcd655c689&quot;,</span>
<span style="color:#AA5500">                    &quot;Gateway&quot;: &quot;172.17.0.1&quot;,</span>
<span style="color:#AA5500">                    &quot;GlobalIPv6Address&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">                    &quot;GlobalIPv6PrefixLen&quot;: 0,</span>
<span style="color:#AA5500">                    &quot;GwPriority&quot;: 0,</span>
<span style="color:#AA5500">                    &quot;IPAMConfig&quot;: null,</span>
<span style="color:#AA5500">                    &quot;IPAddress&quot;: &quot;172.17.0.5&quot;,</span>
<span style="color:#AA5500">                    &quot;IPPrefixLen&quot;: 16,</span>
<span style="color:#AA5500">                    &quot;IPv6Gateway&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">                    &quot;Links&quot;: null,</span>
<span style="color:#AA5500">                    &quot;MacAddress&quot;: &quot;1e:85:84:f7:c1:99&quot;,</span>
<span style="color:#AA5500">                    &quot;NetworkID&quot;: &quot;bf69c1dd08283d21e1c03cd9d2f9059cf944e578f95c79babe5a23cdb260be15&quot;</span>
<span style="color:#AA5500">                }</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            &quot;Ports&quot;: {</span>
<span style="color:#AA5500">                &quot;8000/tcp&quot;: null,</span>
<span style="color:#AA5500">                &quot;9000/tcp&quot;: [</span>
<span style="color:#AA5500">                    {</span>
<span style="color:#AA5500">                        &quot;HostIp&quot;: &quot;0.0.0.0&quot;,</span>
<span style="color:#AA5500">                        &quot;HostPort&quot;: &quot;9000&quot;</span>
<span style="color:#AA5500">                    }</span>
<span style="color:#AA5500">                ],</span>
<span style="color:#AA5500">                &quot;9443/tcp&quot;: null</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            &quot;SandboxID&quot;: &quot;3b22050e5f0346b7fced48c29f122e1b95f196d93d288de796c834ff11699df6&quot;,</span>
<span style="color:#AA5500">            &quot;SandboxKey&quot;: &quot;/var/run/docker/netns/3b22050e5f03&quot;,</span>
<span style="color:#AA5500">            &quot;SecondaryIPAddresses&quot;: null,</span>
<span style="color:#AA5500">            &quot;SecondaryIPv6Addresses&quot;: null</span>
<span style="color:#AA5500">        },</span>
<span style="color:#AA5500">        &quot;Path&quot;: &quot;/portainer&quot;,</span>
<span style="color:#AA5500">        &quot;Platform&quot;: &quot;linux&quot;,</span>
<span style="color:#AA5500">        &quot;ProcessLabel&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">        &quot;ResolvConfPath&quot;: &quot;/var/lib/docker/containers/8bd48bdd95640c7b95c74843ddfa5b2e54381ee39a0925dc663749d8896d5b44/resolv.conf&quot;,</span>
<span style="color:#AA5500">        &quot;RestartCount&quot;: 0,</span>
<span style="color:#AA5500">        &quot;State&quot;: {</span>
<span style="color:#AA5500">            &quot;Dead&quot;: false,</span>
<span style="color:#AA5500">            &quot;Error&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;ExitCode&quot;: 0,</span>
<span style="color:#AA5500">            &quot;FinishedAt&quot;: &quot;2025-09-24T03:00:28.309738469Z&quot;,</span>
<span style="color:#AA5500">            &quot;OOMKilled&quot;: false,</span>
<span style="color:#AA5500">            &quot;Paused&quot;: false,</span>
<span style="color:#AA5500">            &quot;Pid&quot;: 2748,</span>
<span style="color:#AA5500">            &quot;Restarting&quot;: false,</span>
<span style="color:#AA5500">            &quot;Running&quot;: true,</span>
<span style="color:#AA5500">            &quot;StartedAt&quot;: &quot;2025-09-24T03:01:25.585868379Z&quot;,</span>
<span style="color:#AA5500">            &quot;Status&quot;: &quot;running&quot;</span>
<span style="color:#AA5500">        }</span>
<span style="color:#AA5500">    }</span>
<span style="color:#AA5500">}</span>
Donnerstag 25 September 2025  05:20:17 +0200 (0:00:02.018)       0:03:25.273 *** 
Donnerstag 25 September 2025  05:20:17 +0200 (0:00:00.216)       0:03:25.490 *** 
Donnerstag 25 September 2025  05:20:17 +0200 (0:00:00.064)       0:03:25.555 *** 
Donnerstag 25 September 2025  05:20:18 +0200 (0:00:00.058)       0:03:25.613 *** 

TASK [prowlarr : Stop Prowlarr] ***********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/prowlarr/tasks/main.yml:43</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:20:18 +0200 (0:00:00.618)       0:03:26.232 *** 
Donnerstag 25 September 2025  05:20:18 +0200 (0:00:00.063)       0:03:26.296 *** 
Donnerstag 25 September 2025  05:20:18 +0200 (0:00:00.062)       0:03:26.359 *** 
Donnerstag 25 September 2025  05:20:18 +0200 (0:00:00.078)       0:03:26.437 *** 
Donnerstag 25 September 2025  05:20:18 +0200 (0:00:00.051)       0:03:26.489 *** 
Donnerstag 25 September 2025  05:20:18 +0200 (0:00:00.063)       0:03:26.552 *** 

TASK [promtail : Stop promtail] ***********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/promtail/tasks/main.yml:50</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:20:19 +0200 (0:00:00.668)       0:03:27.221 *** 
Donnerstag 25 September 2025  05:20:19 +0200 (0:00:00.061)       0:03:27.283 *** 
Donnerstag 25 September 2025  05:20:19 +0200 (0:00:00.054)       0:03:27.338 *** 

TASK [pyload : Stop pyLoad] ***************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/pyload/tasks/main.yml:45</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:20:20 +0200 (0:00:00.628)       0:03:27.967 *** 
Donnerstag 25 September 2025  05:20:20 +0200 (0:00:00.063)       0:03:28.030 *** 
Donnerstag 25 September 2025  05:20:20 +0200 (0:00:00.067)       0:03:28.098 *** 

TASK [pytivo : Stop Pytivo] ***************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/pytivo/tasks/main.yml:45</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:20:21 +0200 (0:00:00.624)       0:03:28.722 *** 
Donnerstag 25 September 2025  05:20:21 +0200 (0:00:00.062)       0:03:28.784 *** 
Donnerstag 25 September 2025  05:20:21 +0200 (0:00:00.197)       0:03:28.982 *** 

TASK [radarr : Stop Radarr] ***************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/radarr/tasks/main.yml:44</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:20:21 +0200 (0:00:00.609)       0:03:29.592 *** 
Donnerstag 25 September 2025  05:20:22 +0200 (0:00:00.083)       0:03:29.675 *** 
Donnerstag 25 September 2025  05:20:22 +0200 (0:00:00.067)       0:03:29.742 *** 
Donnerstag 25 September 2025  05:20:22 +0200 (0:00:00.067)       0:03:29.810 *** 
Donnerstag 25 September 2025  05:20:22 +0200 (0:00:00.058)       0:03:29.868 *** 

TASK [romm : Stop Romm] *******************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/romm/tasks/main.yml:84</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:20:22 +0200 (0:00:00.626)       0:03:30.495 *** 

TASK [romm : Stop Romm DB] ****************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/romm/tasks/main.yml:89</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:20:23 +0200 (0:00:00.638)       0:03:31.133 *** 
Donnerstag 25 September 2025  05:20:23 +0200 (0:00:00.058)       0:03:31.192 *** 
Donnerstag 25 September 2025  05:20:23 +0200 (0:00:00.065)       0:03:31.257 *** 
Donnerstag 25 September 2025  05:20:23 +0200 (0:00:00.063)       0:03:31.321 *** 
Donnerstag 25 September 2025  05:20:23 +0200 (0:00:00.078)       0:03:31.400 *** 
Donnerstag 25 September 2025  05:20:23 +0200 (0:00:00.071)       0:03:31.472 *** 
Donnerstag 25 September 2025  05:20:23 +0200 (0:00:00.058)       0:03:31.530 *** 

TASK [rssbridge : Stop RSSBridge] *********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/rssbridge/tasks/main.yml:34</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:20:24 +0200 (0:00:00.664)       0:03:32.194 *** 
Donnerstag 25 September 2025  05:20:24 +0200 (0:00:00.071)       0:03:32.265 *** 
Donnerstag 25 September 2025  05:20:24 +0200 (0:00:00.054)       0:03:32.320 *** 

TASK [sabnzbd : Stop Sabnzbd] *************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/sabnzbd/tasks/main.yml:38</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:20:25 +0200 (0:00:00.743)       0:03:33.064 *** 
Donnerstag 25 September 2025  05:20:25 +0200 (0:00:00.067)       0:03:33.132 *** 
Donnerstag 25 September 2025  05:20:25 +0200 (0:00:00.060)       0:03:33.192 *** 

TASK [sickchill : Stop Sickchill] *********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/sickchill/tasks/main.yml:40</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:20:26 +0200 (0:00:00.634)       0:03:33.826 *** 
Donnerstag 25 September 2025  05:20:26 +0200 (0:00:00.072)       0:03:33.899 *** 
Donnerstag 25 September 2025  05:20:26 +0200 (0:00:00.059)       0:03:33.958 *** 

TASK [silverbullet : Stop silverbullet] ***************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/silverbullet/tasks/main.yml:40</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:20:26 +0200 (0:00:00.617)       0:03:34.576 *** 
Donnerstag 25 September 2025  05:20:27 +0200 (0:00:00.065)       0:03:34.642 *** 
Donnerstag 25 September 2025  05:20:27 +0200 (0:00:00.072)       0:03:34.714 *** 

TASK [sonarr : Stop Sonarr] ***************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/sonarr/tasks/main.yml:39</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:20:27 +0200 (0:00:00.607)       0:03:35.322 *** 
Donnerstag 25 September 2025  05:20:27 +0200 (0:00:00.073)       0:03:35.395 *** 
Donnerstag 25 September 2025  05:20:27 +0200 (0:00:00.062)       0:03:35.457 *** 
Donnerstag 25 September 2025  05:20:27 +0200 (0:00:00.063)       0:03:35.521 *** 
Donnerstag 25 September 2025  05:20:27 +0200 (0:00:00.091)       0:03:35.612 *** 
Donnerstag 25 September 2025  05:20:28 +0200 (0:00:00.085)       0:03:35.698 *** 
Donnerstag 25 September 2025  05:20:28 +0200 (0:00:00.079)       0:03:35.777 *** 
Donnerstag 25 September 2025  05:20:28 +0200 (0:00:00.049)       0:03:35.827 *** 
Donnerstag 25 September 2025  05:20:28 +0200 (0:00:00.187)       0:03:36.015 *** 

TASK [stats : Stop Prometheus] ************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/stats/tasks/prometheus.yml:60</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:20:28 +0200 (0:00:00.596)       0:03:36.611 *** 
Donnerstag 25 September 2025  05:20:29 +0200 (0:00:00.079)       0:03:36.691 *** 
Donnerstag 25 September 2025  05:20:29 +0200 (0:00:00.069)       0:03:36.760 *** 
Donnerstag 25 September 2025  05:20:29 +0200 (0:00:00.063)       0:03:36.824 *** 
Donnerstag 25 September 2025  05:20:29 +0200 (0:00:00.059)       0:03:36.883 *** 

TASK [stats : Stop stats_telegraf] ********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/stats/tasks/telegraf.yml:56</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:20:29 +0200 (0:00:00.610)       0:03:37.494 *** 
Donnerstag 25 September 2025  05:20:29 +0200 (0:00:00.060)       0:03:37.554 *** 
Donnerstag 25 September 2025  05:20:30 +0200 (0:00:00.065)       0:03:37.620 *** 
Donnerstag 25 September 2025  05:20:30 +0200 (0:00:00.072)       0:03:37.692 *** 

TASK [stats : Stop Smartctl Exporter] *****************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/stats/tasks/exporters.yml:45</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:20:30 +0200 (0:00:00.590)       0:03:38.282 *** 

TASK [stats : Stop Speedtest Exporter] ****************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/stats/tasks/exporters.yml:49</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:20:31 +0200 (0:00:00.604)       0:03:38.886 *** 
Donnerstag 25 September 2025  05:20:31 +0200 (0:00:00.083)       0:03:38.970 *** 
Donnerstag 25 September 2025  05:20:31 +0200 (0:00:00.062)       0:03:39.033 *** 
Donnerstag 25 September 2025  05:20:31 +0200 (0:00:00.061)       0:03:39.094 *** 
Donnerstag 25 September 2025  05:20:31 +0200 (0:00:00.053)       0:03:39.147 *** 
Donnerstag 25 September 2025  05:20:31 +0200 (0:00:00.060)       0:03:39.208 *** 

TASK [stats : Stop Grafana] ***************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/stats/tasks/grafana.yml:65</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:20:32 +0200 (0:00:00.621)       0:03:39.829 *** 
Donnerstag 25 September 2025  05:20:32 +0200 (0:00:00.064)       0:03:39.893 *** 
Donnerstag 25 September 2025  05:20:32 +0200 (0:00:00.061)       0:03:39.955 *** 

TASK [syncthing : Stop Syncthing] *********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/syncthing/tasks/main.yml:38</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:20:33 +0200 (0:00:00.872)       0:03:40.827 *** 
Donnerstag 25 September 2025  05:20:33 +0200 (0:00:00.078)       0:03:40.906 *** 
Donnerstag 25 September 2025  05:20:33 +0200 (0:00:00.060)       0:03:40.966 *** 

TASK [tautulli : Stop Tautulli] ***********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/tautulli/tasks/main.yml:40</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:20:33 +0200 (0:00:00.617)       0:03:41.583 *** 
Donnerstag 25 September 2025  05:20:34 +0200 (0:00:00.080)       0:03:41.664 *** 
Donnerstag 25 September 2025  05:20:34 +0200 (0:00:00.063)       0:03:41.728 *** 
Donnerstag 25 September 2025  05:20:34 +0200 (0:00:00.057)       0:03:41.786 *** 

TASK [thelounge : Stop The Lounge] ********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/thelounge/tasks/main.yml:42</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:20:34 +0200 (0:00:00.648)       0:03:42.435 *** 
Donnerstag 25 September 2025  05:20:34 +0200 (0:00:00.066)       0:03:42.501 *** 
Donnerstag 25 September 2025  05:20:34 +0200 (0:00:00.057)       0:03:42.559 *** 

TASK [threadfin : Stop Threadfin] *********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/threadfin/tasks/main.yml:34</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:20:35 +0200 (0:00:00.621)       0:03:43.180 *** 
Donnerstag 25 September 2025  05:20:35 +0200 (0:00:00.060)       0:03:43.240 *** 
Donnerstag 25 September 2025  05:20:35 +0200 (0:00:00.068)       0:03:43.309 *** 

TASK [tiddlywiki : Stop Tiddlywiki] *******************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/tiddlywiki/tasks/main.yml:36</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:20:36 +0200 (0:00:00.625)       0:03:43.935 *** 
Donnerstag 25 September 2025  05:20:36 +0200 (0:00:00.061)       0:03:43.997 *** 
Donnerstag 25 September 2025  05:20:36 +0200 (0:00:00.051)       0:03:44.048 *** 
Donnerstag 25 September 2025  05:20:36 +0200 (0:00:00.057)       0:03:44.105 *** 
Donnerstag 25 September 2025  05:20:36 +0200 (0:00:00.349)       0:03:44.455 *** 

TASK [timemachine : Stop Time Machine] ****************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/timemachine/tasks/main.yml:45</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:20:37 +0200 (0:00:00.618)       0:03:45.073 *** 
Donnerstag 25 September 2025  05:20:37 +0200 (0:00:00.076)       0:03:45.150 *** 
Donnerstag 25 September 2025  05:20:37 +0200 (0:00:00.051)       0:03:45.201 *** 
Donnerstag 25 September 2025  05:20:37 +0200 (0:00:00.060)       0:03:45.261 *** 

TASK [traefik : Stop Traefik] *************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/traefik/tasks/main.yml:44</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:20:38 +0200 (0:00:00.633)       0:03:45.895 *** 
Donnerstag 25 September 2025  05:20:38 +0200 (0:00:00.073)       0:03:45.968 *** 
Donnerstag 25 September 2025  05:20:38 +0200 (0:00:00.062)       0:03:46.031 *** 

TASK [transmission : Stop Transmission] ***************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/transmission/tasks/main.yml:44</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:20:39 +0200 (0:00:00.605)       0:03:46.637 *** 
Donnerstag 25 September 2025  05:20:39 +0200 (0:00:00.069)       0:03:46.707 *** 
Donnerstag 25 September 2025  05:20:39 +0200 (0:00:00.066)       0:03:46.774 *** 

TASK [transmission-with-openvpn : Stop Transmission with OpenVPM] *************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/transmission-with-openvpn/tasks/main.yml:64</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:20:39 +0200 (0:00:00.629)       0:03:47.403 *** 
Donnerstag 25 September 2025  05:20:39 +0200 (0:00:00.066)       0:03:47.470 *** 
Donnerstag 25 September 2025  05:20:39 +0200 (0:00:00.063)       0:03:47.533 *** 

TASK [ubooquity : Stop Ubooquity] *********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/ubooquity/tasks/main.yml:42</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:20:40 +0200 (0:00:00.625)       0:03:48.159 *** 
Donnerstag 25 September 2025  05:20:40 +0200 (0:00:00.052)       0:03:48.212 *** 
Donnerstag 25 September 2025  05:20:40 +0200 (0:00:00.186)       0:03:48.398 *** 

TASK [utorrent : Stop uTorrent] ***********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/utorrent/tasks/main.yml:46</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:20:41 +0200 (0:00:00.632)       0:03:49.031 *** 
Donnerstag 25 September 2025  05:20:41 +0200 (0:00:00.088)       0:03:49.119 *** 
Donnerstag 25 September 2025  05:20:41 +0200 (0:00:00.061)       0:03:49.181 *** 

TASK [valheim : Stop Valheim] *************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/valheim/tasks/main.yml:44</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:20:42 +0200 (0:00:00.604)       0:03:49.786 *** 
Donnerstag 25 September 2025  05:20:42 +0200 (0:00:00.077)       0:03:49.863 *** 
Donnerstag 25 September 2025  05:20:42 +0200 (0:00:00.059)       0:03:49.922 *** 
Donnerstag 25 September 2025  05:20:42 +0200 (0:00:00.058)       0:03:49.981 *** 

TASK [virtual_desktop : Stop Virtual Desktop] *********************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/virtual_desktop/tasks/main.yml:37</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:20:42 +0200 (0:00:00.626)       0:03:50.607 *** 
Donnerstag 25 September 2025  05:20:43 +0200 (0:00:00.089)       0:03:50.697 *** 
Donnerstag 25 September 2025  05:20:43 +0200 (0:00:00.064)       0:03:50.762 *** 

TASK [wallabag : Stop Wallabag] ***********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/wallabag/tasks/main.yml:40</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:20:43 +0200 (0:00:00.631)       0:03:51.393 *** 
Donnerstag 25 September 2025  05:20:43 +0200 (0:00:00.066)       0:03:51.460 *** 

TASK [watchtower : Stop Watchtower] *******************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/watchtower/tasks/main.yml:20</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:20:44 +0200 (0:00:00.618)       0:03:52.079 *** 
Donnerstag 25 September 2025  05:20:44 +0200 (0:00:00.073)       0:03:52.152 *** 
Donnerstag 25 September 2025  05:20:44 +0200 (0:00:00.059)       0:03:52.211 *** 

TASK [wireshark : Stop Wireshark] *********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/wireshark/tasks/main.yml:39</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:20:45 +0200 (0:00:00.744)       0:03:52.955 *** 
Donnerstag 25 September 2025  05:20:45 +0200 (0:00:00.057)       0:03:53.013 *** 
Donnerstag 25 September 2025  05:20:45 +0200 (0:00:00.060)       0:03:53.073 *** 
Donnerstag 25 September 2025  05:20:45 +0200 (0:00:00.067)       0:03:53.141 *** 
Donnerstag 25 September 2025  05:20:45 +0200 (0:00:00.051)       0:03:53.193 *** 
Donnerstag 25 September 2025  05:20:45 +0200 (0:00:00.059)       0:03:53.252 *** 
Donnerstag 25 September 2025  05:20:45 +0200 (0:00:00.051)       0:03:53.303 *** 

TASK [woodpecker-ci : Stop Woodpecker-CI] *************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/woodpecker-ci/tasks/main.yml:78</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:20:46 +0200 (0:00:00.603)       0:03:53.907 *** 
Donnerstag 25 September 2025  05:20:46 +0200 (0:00:00.070)       0:03:53.978 *** 
Donnerstag 25 September 2025  05:20:46 +0200 (0:00:00.050)       0:03:54.028 *** 

TASK [youtubedlmaterial : Stop Youtubedlmaterial] *****************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/youtubedlmaterial/tasks/main.yml:52</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 25 September 2025  05:20:47 +0200 (0:00:00.622)       0:03:54.650 *** 
Donnerstag 25 September 2025  05:20:47 +0200 (0:00:00.094)       0:03:54.745 *** 
Donnerstag 25 September 2025  05:20:47 +0200 (0:00:00.050)       0:03:54.795 *** 
Donnerstag 25 September 2025  05:20:47 +0200 (0:00:00.056)       0:03:54.852 *** 

TASK [znc : Stop ZNC] *********************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/znc/tasks/main.yml:45</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>

PLAY RECAP ********************************************************************************************************************************************************************************************************
<span style="color:#AA5500">ansible-nas</span>                : <span style="color:#00AA00">ok=161 </span> <span style="color:#AA5500">changed=5   </span> unreachable=0    failed=0    <span style="color:#00AAAA">skipped=306 </span> rescued=0    ignored=0   

Donnerstag 25 September 2025  05:20:47 +0200 (0:00:00.594)       0:03:55.447 *** 
=============================================================================== 
mediathekview : Mediathekview Docker Container ------------------------------------------------------------------------------------------------------------------------------------------------------------ 89.42s
/media/IT/repos/github/forked/ansible-nas/roles/mediathekview/tasks/main.yml:13 ----------------------------------------------------------------------------------------------------------------------------------
geerlingguy.nfs : Ensure directories to export exist ------------------------------------------------------------------------------------------------------------------------------------------------------- 6.11s
/home/dietmar/.ansible/roles/geerlingguy.nfs/tasks/main.yml:19 ---------------------------------------------------------------------------------------------------------------------------------------------------
homepage : Template config files --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 3.06s
/media/IT/repos/github/forked/ansible-nas/roles/homepage/tasks/main.yml:11 ---------------------------------------------------------------------------------------------------------------------------------------
portainer : Portainer Docker Container --------------------------------------------------------------------------------------------------------------------------------------------------------------------- 2.02s
/media/IT/repos/github/forked/ansible-nas/roles/portainer/tasks/main.yml:16 --------------------------------------------------------------------------------------------------------------------------------------
calibre : Calibre Docker Container ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 2.02s
/media/IT/repos/github/forked/ansible-nas/roles/calibre/tasks/main.yml:12 ----------------------------------------------------------------------------------------------------------------------------------------
vladgh.samba.server : Install Samba packages --------------------------------------------------------------------------------------------------------------------------------------------------------------- 1.84s
/home/dietmar/.ansible/collections/ansible_collections/vladgh/samba/roles/server/tasks/main.yml:12 ---------------------------------------------------------------------------------------------------------------
calibreweb : Calibre-web Docker Container ------------------------------------------------------------------------------------------------------------------------------------------------------------------ 1.77s
/media/IT/repos/github/forked/ansible-nas/roles/calibreweb/tasks/main.yml:12 -------------------------------------------------------------------------------------------------------------------------------------
geerlingguy.docker : Install docker-compose-plugin (with downgrade option). -------------------------------------------------------------------------------------------------------------------------------- 1.47s
/home/dietmar/.ansible/roles/geerlingguy.docker/tasks/main.yml:44 ------------------------------------------------------------------------------------------------------------------------------------------------
ansible-nas-general : Install some packages ---------------------------------------------------------------------------------------------------------------------------------------------------------------- 1.44s
/media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-general/tasks/main.yml:22 ----------------------------------------------------------------------------------------------------------------------------
vladgh.samba.server : Install Samba VFS extensions packages ------------------------------------------------------------------------------------------------------------------------------------------------ 1.42s
/home/dietmar/.ansible/collections/ansible_collections/vladgh/samba/roles/server/tasks/main.yml:19 ---------------------------------------------------------------------------------------------------------------
geerlingguy.docker : Ensure dependencies are installed. ---------------------------------------------------------------------------------------------------------------------------------------------------- 1.41s
/home/dietmar/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml:10 ----------------------------------------------------------------------------------------------------------------------------------------
geerlingguy.docker : Install Docker packages (with downgrade option). -------------------------------------------------------------------------------------------------------------------------------------- 1.40s
/home/dietmar/.ansible/roles/geerlingguy.docker/tasks/main.yml:27 ------------------------------------------------------------------------------------------------------------------------------------------------
geerlingguy.docker : Ensure additional dependencies are installed (on Ubuntu &lt; 20.04 and any other systems). ----------------------------------------------------------------------------------------------- 1.38s
/home/dietmar/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml:18 ----------------------------------------------------------------------------------------------------------------------------------------
geerlingguy.nfs : Ensure NFS utilities are installed. ------------------------------------------------------------------------------------------------------------------------------------------------------ 1.37s
/home/dietmar/.ansible/roles/geerlingguy.nfs/tasks/setup-Debian.yml:2 --------------------------------------------------------------------------------------------------------------------------------------------
ansible-nas-docker : Install python3-pip ------------------------------------------------------------------------------------------------------------------------------------------------------------------- 1.37s
/media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-docker/tasks/main.yml:2 ------------------------------------------------------------------------------------------------------------------------------
vladgh.samba.server : Samba configuration ------------------------------------------------------------------------------------------------------------------------------------------------------------------ 1.31s
/home/dietmar/.ansible/collections/ansible_collections/vladgh/samba/roles/server/tasks/main.yml:80 ---------------------------------------------------------------------------------------------------------------
ansible-nas-docker : Remove docker-py python module -------------------------------------------------------------------------------------------------------------------------------------------------------- 1.31s
/media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-docker/tasks/main.yml:19 -----------------------------------------------------------------------------------------------------------------------------
ansible-nas-docker : Install docker python module ---------------------------------------------------------------------------------------------------------------------------------------------------------- 1.29s
/media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-docker/tasks/main.yml:26 -----------------------------------------------------------------------------------------------------------------------------
ansible-nas-general : Set hostname to RaspiNAS ------------------------------------------------------------------------------------------------------------------------------------------------------------- 1.28s
/media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-general/tasks/main.yml:29 ----------------------------------------------------------------------------------------------------------------------------
homepage : Create Homepage Docker Container ---------------------------------------------------------------------------------------------------------------------------------------------------------------- 1.26s
/media/IT/repos/github/forked/ansible-nas/roles/homepage/tasks/main.yml:23 ---------------------------------------------------------------------------------------------------------------------------------------
[<span style="color:#00AA00">2025-09-25 05:20:48</span>] (venv) [<span style="color:#55FF55"><b>dietmar@MiraPi</b></span>] [<span style="color:#5555FF"><b>.../forked/ansible-nas</b></span>] $ 

</pre>
