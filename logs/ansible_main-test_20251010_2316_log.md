<pre>[<span style="color:#00AA00">2025-10-10 23:16:17</span>] (Venv) [<span style="color:#55FF55"><b>dietmar@MiraPi</b></span>] [<span style="color:#5555FF"><b>.../forked/ansible-nas</b></span>] $ ansible-playbook -i inventories/RaspiNAS/inventory nas.yml -b
<span style="color:#0000AA">ansible-playbook [core 2.17.6]</span>
<span style="color:#0000AA">  config file = /media/IT/repos/github/forked/ansible-nas/ansible.cfg</span>
<span style="color:#0000AA">  configured module search path = [&apos;/home/dietmar/.ansible/plugins/modules&apos;, &apos;/usr/share/ansible/plugins/modules&apos;]</span>
<span style="color:#0000AA">  ansible python module location = /home/dietmar/.local/pipx/venvs/debops/lib/python3.11/site-packages/ansible</span>
<span style="color:#0000AA">  ansible collection location = /home/dietmar/.ansible/collections:/usr/share/ansible/collections</span>
<span style="color:#0000AA">  executable location = /home/dietmar/.local/bin/ansible-playbook</span>
<span style="color:#0000AA">  python version = 3.11.2 (main, Apr 28 2025, 14:11:48) [GCC 12.2.0] (/home/dietmar/.local/pipx/venvs/debops/bin/python)</span>
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
Freitag 10 Oktober 2025  23:16:35 +0200 (0:00:00.160)       0:00:00.160 ******* 

TASK [ansible-nas-users : Create ansible-nas group] ***************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-users/tasks/main.yml:2</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;gid&quot;: 1001,</span>
<span style="color:#00AA00">    &quot;name&quot;: &quot;ansible-nas&quot;,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;present&quot;,</span>
<span style="color:#00AA00">    &quot;system&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:16:37 +0200 (0:00:01.768)       0:00:01.929 ******* 

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
Freitag 10 Oktober 2025  23:16:37 +0200 (0:00:00.657)       0:00:02.587 ******* 

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
Freitag 10 Oktober 2025  23:16:37 +0200 (0:00:00.049)       0:00:02.637 ******* 

TASK [vladgh.samba.server : Install Samba packages] ***************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/collections/ansible_collections/vladgh/samba/roles/server/tasks/main.yml:12</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;cache_update_time&quot;: 1760096819,</span>
<span style="color:#00AA00">    &quot;cache_updated&quot;: false,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:16:39 +0200 (0:00:01.688)       0:00:04.325 ******* 

TASK [vladgh.samba.server : Install Samba VFS extensions packages] ************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/collections/ansible_collections/vladgh/samba/roles/server/tasks/main.yml:19</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;cache_update_time&quot;: 1760096819,</span>
<span style="color:#00AA00">    &quot;cache_updated&quot;: false,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:16:41 +0200 (0:00:01.498)       0:00:05.823 ******* 

TASK [vladgh.samba.server : Register Samba version] ***************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/collections/ansible_collections/vladgh/samba/roles/server/tasks/main.yml:26</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;cmd&quot;: &quot;set -o nounset -o pipefail -o errexit &amp;&amp; smbd --version | sed &apos;s/Version //&apos;\n&quot;,</span>
<span style="color:#00AA00">    &quot;delta&quot;: &quot;0:00:00.046081&quot;,</span>
<span style="color:#00AA00">    &quot;end&quot;: &quot;2025-10-10 23:16:41.545295&quot;,</span>
<span style="color:#00AA00">    &quot;rc&quot;: 0,</span>
<span style="color:#00AA00">    &quot;start&quot;: &quot;2025-10-10 23:16:41.499214&quot;</span>
<span style="color:#00AA00">}</span>

<span style="color:#00AA00">STDOUT:</span>

<span style="color:#00AA00">4.17.12-Debian</span>
Freitag 10 Oktober 2025  23:16:41 +0200 (0:00:00.580)       0:00:06.403 ******* 
Freitag 10 Oktober 2025  23:16:41 +0200 (0:00:00.139)       0:00:06.543 ******* 
Freitag 10 Oktober 2025  23:16:41 +0200 (0:00:00.034)       0:00:06.578 ******* 
Freitag 10 Oktober 2025  23:16:41 +0200 (0:00:00.062)       0:00:06.641 ******* 
Freitag 10 Oktober 2025  23:16:41 +0200 (0:00:00.033)       0:00:06.674 ******* 

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
Freitag 10 Oktober 2025  23:16:42 +0200 (0:00:00.962)       0:00:07.637 ******* 
Freitag 10 Oktober 2025  23:16:42 +0200 (0:00:00.042)       0:00:07.680 ******* 
Freitag 10 Oktober 2025  23:16:42 +0200 (0:00:00.052)       0:00:07.732 ******* 
Freitag 10 Oktober 2025  23:16:42 +0200 (0:00:00.036)       0:00:07.768 ******* 
Freitag 10 Oktober 2025  23:16:43 +0200 (0:00:00.051)       0:00:07.819 ******* 

TASK [vladgh.samba.server : Start SMB service] ********************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/collections/ansible_collections/vladgh/samba/roles/server/tasks/main.yml:141</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;enabled&quot;: true,</span>
<span style="color:#00AA00">    &quot;name&quot;: &quot;smbd&quot;,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;started&quot;,</span>
<span style="color:#00AA00">    &quot;status&quot;: {</span>
<span style="color:#00AA00">        &quot;ActiveEnterTimestamp&quot;: &quot;Sun 2025-10-05 14:54:06 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;ActiveEnterTimestampMonotonic&quot;: &quot;15534417&quot;,</span>
<span style="color:#00AA00">        &quot;ActiveExitTimestampMonotonic&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;ActiveState&quot;: &quot;active&quot;,</span>
<span style="color:#00AA00">        &quot;After&quot;: &quot;sysinit.target systemd-journald.socket basic.target nmbd.service network-online.target system.slice winbind.service network.target&quot;,</span>
<span style="color:#00AA00">        &quot;AllowIsolate&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;AssertResult&quot;: &quot;yes&quot;,</span>
<span style="color:#00AA00">        &quot;AssertTimestamp&quot;: &quot;Sun 2025-10-05 14:54:06 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;AssertTimestampMonotonic&quot;: &quot;15341479&quot;,</span>
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
<span style="color:#00AA00">        &quot;CPUUsageNSec&quot;: &quot;2130593000&quot;,</span>
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
<span style="color:#00AA00">        &quot;ConditionTimestamp&quot;: &quot;Sun 2025-10-05 14:54:06 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;ConditionTimestampMonotonic&quot;: &quot;15341477&quot;,</span>
<span style="color:#00AA00">        &quot;ConfigurationDirectoryMode&quot;: &quot;0755&quot;,</span>
<span style="color:#00AA00">        &quot;Conflicts&quot;: &quot;shutdown.target&quot;,</span>
<span style="color:#00AA00">        &quot;ConsistsOf&quot;: &quot;zfs-share.service&quot;,</span>
<span style="color:#00AA00">        &quot;ControlGroup&quot;: &quot;/system.slice/smbd.service&quot;,</span>
<span style="color:#00AA00">        &quot;ControlGroupId&quot;: &quot;3382&quot;,</span>
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
<span style="color:#00AA00">        &quot;ExecMainPID&quot;: &quot;1485&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainStartTimestamp&quot;: &quot;Sun 2025-10-05 14:54:06 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainStartTimestampMonotonic&quot;: &quot;15429565&quot;,</span>
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
<span style="color:#00AA00">        &quot;InactiveEnterTimestampMonotonic&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;InactiveExitTimestamp&quot;: &quot;Sun 2025-10-05 14:54:06 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;InactiveExitTimestampMonotonic&quot;: &quot;15368576&quot;,</span>
<span style="color:#00AA00">        &quot;InvocationID&quot;: &quot;031f3b35dd854abe908984abc2e3b715&quot;,</span>
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
<span style="color:#00AA00">        &quot;LimitNPROC&quot;: &quot;31915&quot;,</span>
<span style="color:#00AA00">        &quot;LimitNPROCSoft&quot;: &quot;31915&quot;,</span>
<span style="color:#00AA00">        &quot;LimitRSS&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;LimitRSSSoft&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;LimitRTPRIO&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;LimitRTPRIOSoft&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;LimitRTTIME&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;LimitRTTIMESoft&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;LimitSIGPENDING&quot;: &quot;31915&quot;,</span>
<span style="color:#00AA00">        &quot;LimitSIGPENDINGSoft&quot;: &quot;31915&quot;,</span>
<span style="color:#00AA00">        &quot;LimitSTACK&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;LimitSTACKSoft&quot;: &quot;8388608&quot;,</span>
<span style="color:#00AA00">        &quot;LoadState&quot;: &quot;loaded&quot;,</span>
<span style="color:#00AA00">        &quot;LockPersonality&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;LogLevelMax&quot;: &quot;-1&quot;,</span>
<span style="color:#00AA00">        &quot;LogRateLimitBurst&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;LogRateLimitIntervalUSec&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;LogsDirectoryMode&quot;: &quot;0755&quot;,</span>
<span style="color:#00AA00">        &quot;MainPID&quot;: &quot;1485&quot;,</span>
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
<span style="color:#00AA00">        &quot;StateChangeTimestamp&quot;: &quot;Sun 2025-10-05 14:54:06 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;StateChangeTimestampMonotonic&quot;: &quot;15534417&quot;,</span>
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
Freitag 10 Oktober 2025  23:16:43 +0200 (0:00:00.871)       0:00:08.691 ******* 

TASK [vladgh.samba.server : Start NMB service] ********************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/collections/ansible_collections/vladgh/samba/roles/server/tasks/main.yml:148</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;enabled&quot;: true,</span>
<span style="color:#00AA00">    &quot;name&quot;: &quot;nmbd&quot;,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;started&quot;,</span>
<span style="color:#00AA00">    &quot;status&quot;: {</span>
<span style="color:#00AA00">        &quot;ActiveEnterTimestamp&quot;: &quot;Sun 2025-10-05 14:54:06 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;ActiveEnterTimestampMonotonic&quot;: &quot;15339692&quot;,</span>
<span style="color:#00AA00">        &quot;ActiveExitTimestampMonotonic&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;ActiveState&quot;: &quot;active&quot;,</span>
<span style="color:#00AA00">        &quot;After&quot;: &quot;network-online.target systemd-journald.socket basic.target system.slice sysinit.target network.target&quot;,</span>
<span style="color:#00AA00">        &quot;AllowIsolate&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;AssertResult&quot;: &quot;yes&quot;,</span>
<span style="color:#00AA00">        &quot;AssertTimestamp&quot;: &quot;Sun 2025-10-05 14:54:06 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;AssertTimestampMonotonic&quot;: &quot;15042627&quot;,</span>
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
<span style="color:#00AA00">        &quot;CPUUsageNSec&quot;: &quot;52457627000&quot;,</span>
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
<span style="color:#00AA00">        &quot;ConditionTimestamp&quot;: &quot;Sun 2025-10-05 14:54:06 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;ConditionTimestampMonotonic&quot;: &quot;15042625&quot;,</span>
<span style="color:#00AA00">        &quot;ConfigurationDirectoryMode&quot;: &quot;0755&quot;,</span>
<span style="color:#00AA00">        &quot;Conflicts&quot;: &quot;shutdown.target&quot;,</span>
<span style="color:#00AA00">        &quot;ControlGroup&quot;: &quot;/system.slice/nmbd.service&quot;,</span>
<span style="color:#00AA00">        &quot;ControlGroupId&quot;: &quot;3110&quot;,</span>
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
<span style="color:#00AA00">        &quot;ExecMainPID&quot;: &quot;1129&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainStartTimestamp&quot;: &quot;Sun 2025-10-05 14:54:06 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainStartTimestampMonotonic&quot;: &quot;15260222&quot;,</span>
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
<span style="color:#00AA00">        &quot;InactiveEnterTimestampMonotonic&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;InactiveExitTimestamp&quot;: &quot;Sun 2025-10-05 14:54:06 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;InactiveExitTimestampMonotonic&quot;: &quot;15044271&quot;,</span>
<span style="color:#00AA00">        &quot;InvocationID&quot;: &quot;2cd031bf53f4473d90209aa435aa0e6a&quot;,</span>
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
<span style="color:#00AA00">        &quot;LimitNPROC&quot;: &quot;31915&quot;,</span>
<span style="color:#00AA00">        &quot;LimitNPROCSoft&quot;: &quot;31915&quot;,</span>
<span style="color:#00AA00">        &quot;LimitRSS&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;LimitRSSSoft&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;LimitRTPRIO&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;LimitRTPRIOSoft&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;LimitRTTIME&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;LimitRTTIMESoft&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;LimitSIGPENDING&quot;: &quot;31915&quot;,</span>
<span style="color:#00AA00">        &quot;LimitSIGPENDINGSoft&quot;: &quot;31915&quot;,</span>
<span style="color:#00AA00">        &quot;LimitSTACK&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;LimitSTACKSoft&quot;: &quot;8388608&quot;,</span>
<span style="color:#00AA00">        &quot;LoadState&quot;: &quot;loaded&quot;,</span>
<span style="color:#00AA00">        &quot;LockPersonality&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;LogLevelMax&quot;: &quot;-1&quot;,</span>
<span style="color:#00AA00">        &quot;LogRateLimitBurst&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;LogRateLimitIntervalUSec&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;LogsDirectoryMode&quot;: &quot;0755&quot;,</span>
<span style="color:#00AA00">        &quot;MainPID&quot;: &quot;1129&quot;,</span>
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
<span style="color:#00AA00">        &quot;StateChangeTimestamp&quot;: &quot;Sun 2025-10-05 14:54:06 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;StateChangeTimestampMonotonic&quot;: &quot;15339692&quot;,</span>
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
Freitag 10 Oktober 2025  23:16:44 +0200 (0:00:00.579)       0:00:09.270 ******* 
Freitag 10 Oktober 2025  23:16:44 +0200 (0:00:00.069)       0:00:09.339 ******* 

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
Freitag 10 Oktober 2025  23:16:44 +0200 (0:00:00.044)       0:00:09.383 ******* 
Freitag 10 Oktober 2025  23:16:44 +0200 (0:00:00.043)       0:00:09.427 ******* 
Freitag 10 Oktober 2025  23:16:44 +0200 (0:00:00.036)       0:00:09.464 ******* 

TASK [geerlingguy.nfs : include_tasks] ****************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.nfs/tasks/main.yml:16</b></span>
<span style="color:#00AAAA">included: /home/dietmar/.ansible/roles/geerlingguy.nfs/tasks/setup-Debian.yml for ansible-nas</span>
Freitag 10 Oktober 2025  23:16:44 +0200 (0:00:00.158)       0:00:09.622 ******* 

TASK [geerlingguy.nfs : Ensure NFS utilities are installed.] ******************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.nfs/tasks/setup-Debian.yml:2</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;cache_update_time&quot;: 1760096819,</span>
<span style="color:#00AA00">    &quot;cache_updated&quot;: false,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:16:46 +0200 (0:00:01.460)       0:00:11.083 ******* 

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
Freitag 10 Oktober 2025  23:16:52 +0200 (0:00:06.078)       0:00:17.162 ******* 

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
Freitag 10 Oktober 2025  23:16:52 +0200 (0:00:00.636)       0:00:17.799 ******* 

TASK [geerlingguy.nfs : Ensure nfs is running.] *******************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.nfs/tasks/main.yml:34</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;enabled&quot;: true,</span>
<span style="color:#00AA00">    &quot;name&quot;: &quot;nfs-kernel-server&quot;,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;started&quot;,</span>
<span style="color:#00AA00">    &quot;status&quot;: {</span>
<span style="color:#00AA00">        &quot;ActiveEnterTimestamp&quot;: &quot;Sun 2025-10-05 14:54:06 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;ActiveEnterTimestampMonotonic&quot;: &quot;15606541&quot;,</span>
<span style="color:#00AA00">        &quot;ActiveExitTimestampMonotonic&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;ActiveState&quot;: &quot;active&quot;,</span>
<span style="color:#00AA00">        &quot;After&quot;: &quot;nfs-idmapd.service network-online.target nfsdcld.service rpcbind.socket system.slice mnt-Volume1.mount zfs-share.service rpc-gssd.service proc-fs-nfsd.mount -.mount nfs-mountd.service rpc-statd.service systemd-journald.socket gssproxy.service rpc-svcgssd.service local-fs.target&quot;,</span>
<span style="color:#00AA00">        &quot;AllowIsolate&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;AssertResult&quot;: &quot;yes&quot;,</span>
<span style="color:#00AA00">        &quot;AssertTimestamp&quot;: &quot;Sun 2025-10-05 14:54:06 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;AssertTimestampMonotonic&quot;: &quot;15580387&quot;,</span>
<span style="color:#00AA00">        &quot;Before&quot;: &quot;media-Medien.mount media-web.mount media-Dokumente.mount rpc-statd-notify.service media-Produktion.mount&quot;,</span>
<span style="color:#00AA00">        &quot;BlockIOAccounting&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;BlockIOWeight&quot;: &quot;[not set]&quot;,</span>
<span style="color:#00AA00">        &quot;BoundBy&quot;: &quot;nfs-mountd.service nfs-idmapd.service&quot;,</span>
<span style="color:#00AA00">        &quot;CPUAccounting&quot;: &quot;yes&quot;,</span>
<span style="color:#00AA00">        &quot;CPUAffinityFromNUMA&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;CPUQuotaPerSecUSec&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;CPUQuotaPeriodUSec&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;CPUSchedulingPolicy&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;CPUSchedulingPriority&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;CPUSchedulingResetOnFork&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;CPUShares&quot;: &quot;[not set]&quot;,</span>
<span style="color:#00AA00">        &quot;CPUUsageNSec&quot;: &quot;5793000&quot;,</span>
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
<span style="color:#00AA00">        &quot;ConditionTimestamp&quot;: &quot;Sun 2025-10-05 14:54:06 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;ConditionTimestampMonotonic&quot;: &quot;15580384&quot;,</span>
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
<span style="color:#00AA00">        &quot;ExecMainExitTimestamp&quot;: &quot;Sun 2025-10-05 14:54:06 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainExitTimestampMonotonic&quot;: &quot;15606374&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainPID&quot;: &quot;1761&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainStartTimestamp&quot;: &quot;Sun 2025-10-05 14:54:06 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainStartTimestampMonotonic&quot;: &quot;15591225&quot;,</span>
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
<span style="color:#00AA00">        &quot;InactiveExitTimestamp&quot;: &quot;Sun 2025-10-05 14:54:06 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;InactiveExitTimestampMonotonic&quot;: &quot;15582220&quot;,</span>
<span style="color:#00AA00">        &quot;InvocationID&quot;: &quot;76ea3499c41e4e98bd9642bdfcc9abd0&quot;,</span>
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
<span style="color:#00AA00">        &quot;LimitNPROC&quot;: &quot;31915&quot;,</span>
<span style="color:#00AA00">        &quot;LimitNPROCSoft&quot;: &quot;31915&quot;,</span>
<span style="color:#00AA00">        &quot;LimitRSS&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;LimitRSSSoft&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;LimitRTPRIO&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;LimitRTPRIOSoft&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;LimitRTTIME&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;LimitRTTIMESoft&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;LimitSIGPENDING&quot;: &quot;31915&quot;,</span>
<span style="color:#00AA00">        &quot;LimitSIGPENDINGSoft&quot;: &quot;31915&quot;,</span>
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
<span style="color:#00AA00">        &quot;Requires&quot;: &quot;mnt-Volume1.mount network.target system.slice nfs-mountd.service proc-fs-nfsd.mount -.mount&quot;,</span>
<span style="color:#00AA00">        &quot;RequiresMountsFor&quot;: &quot;/mnt/Volume1/local/Photos /mnt/Volume1/local/Organisation /mnt/Volume1/local/Books /mnt/Volume1/local/Download /mnt/Volume1/local/IT /mnt/Volume1/local/Audiobooks /mnt/Volume1/local/Documents /mnt/Volume1/local/Music /mnt/Volume1/docker /mnt/Volume1/local/Ägyptologie /mnt/Volume1/local/Persönliches /mnt/Volume1/local/Media /mnt/Volume1/local/Movies /mnt/Volume1/local/TV /mnt/Volume1/local/Versorgung /mnt/Volume1/local/Podcasts /mnt/Volume1/local/Comics /mnt/Volume1/local/Inventar&quot;,</span>
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
<span style="color:#00AA00">        &quot;StateChangeTimestamp&quot;: &quot;Sun 2025-10-05 14:54:06 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;StateChangeTimestampMonotonic&quot;: &quot;15606541&quot;,</span>
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
<span style="color:#00AA00">        &quot;Wants&quot;: &quot;nfs-idmapd.service rpc-statd-notify.service rpcbind.socket rpc-statd.service nfsdcld.service rpc-svcgssd.service auth-rpcgss-module.service network-online.target&quot;,</span>
<span style="color:#00AA00">        &quot;WatchdogSignal&quot;: &quot;6&quot;,</span>
<span style="color:#00AA00">        &quot;WatchdogTimestampMonotonic&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;WatchdogUSec&quot;: &quot;0&quot;</span>
<span style="color:#00AA00">    }</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:16:53 +0200 (0:00:00.602)       0:00:18.402 ******* 

TASK [geerlingguy.docker : Load OS-specific vars.] ****************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.docker/tasks/main.yml:2</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;ansible_facts&quot;: {},</span>
<span style="color:#00AA00">    &quot;ansible_included_var_files&quot;: [</span>
<span style="color:#00AA00">        &quot;/home/dietmar/.ansible/roles/geerlingguy.docker/vars/main.yml&quot;</span>
<span style="color:#00AA00">    ],</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:16:53 +0200 (0:00:00.047)       0:00:18.449 ******* 
Freitag 10 Oktober 2025  23:16:53 +0200 (0:00:00.038)       0:00:18.488 ******* 

TASK [geerlingguy.docker : include_tasks] *************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.docker/tasks/main.yml:16</b></span>
<span style="color:#00AAAA">included: /home/dietmar/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml for ansible-nas</span>
Freitag 10 Oktober 2025  23:16:53 +0200 (0:00:00.070)       0:00:18.559 ******* 

TASK [geerlingguy.docker : Ensure old versions of Docker are not installed.] **************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml:2</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:16:54 +0200 (0:00:01.060)       0:00:19.620 ******* 

TASK [geerlingguy.docker : Ensure dependencies are installed.] ****************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml:10</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;cache_update_time&quot;: 1760096819,</span>
<span style="color:#00AA00">    &quot;cache_updated&quot;: false,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:16:56 +0200 (0:00:01.463)       0:00:21.083 ******* 

TASK [geerlingguy.docker : Ensure additional dependencies are installed (on Ubuntu &lt; 20.04 and any other systems).] ***********************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml:18</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;cache_update_time&quot;: 1760096819,</span>
<span style="color:#00AA00">    &quot;cache_updated&quot;: false,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:16:57 +0200 (0:00:01.507)       0:00:22.591 ******* 
Freitag 10 Oktober 2025  23:16:57 +0200 (0:00:00.044)       0:00:22.635 ******* 

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
Freitag 10 Oktober 2025  23:16:58 +0200 (0:00:00.707)       0:00:23.343 ******* 
Freitag 10 Oktober 2025  23:16:58 +0200 (0:00:00.159)       0:00:23.503 ******* 
Freitag 10 Oktober 2025  23:16:58 +0200 (0:00:00.061)       0:00:23.564 ******* 

TASK [geerlingguy.docker : Add Docker repository.] ****************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml:50</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;repo&quot;: &quot;deb [arch=arm64 signed-by=/etc/apt/trusted.gpg.d/docker.asc] https://download.docker.com/linux/debian bookworm stable&quot;,</span>
<span style="color:#00AA00">    &quot;sources_added&quot;: [],</span>
<span style="color:#00AA00">    &quot;sources_removed&quot;: [],</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;present&quot;</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:16:59 +0200 (0:00:00.645)       0:00:24.210 ******* 
Freitag 10 Oktober 2025  23:16:59 +0200 (0:00:00.040)       0:00:24.251 ******* 

TASK [geerlingguy.docker : Install Docker packages (with downgrade option).] **************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.docker/tasks/main.yml:27</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;cache_update_time&quot;: 1760096819,</span>
<span style="color:#00AA00">    &quot;cache_updated&quot;: false,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:17:00 +0200 (0:00:01.501)       0:00:25.753 ******* 
Freitag 10 Oktober 2025  23:17:01 +0200 (0:00:00.085)       0:00:25.839 ******* 

TASK [geerlingguy.docker : Install docker-compose-plugin (with downgrade option).] ********************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.docker/tasks/main.yml:44</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;cache_update_time&quot;: 1760096819,</span>
<span style="color:#00AA00">    &quot;cache_updated&quot;: false,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:17:02 +0200 (0:00:01.467)       0:00:27.306 ******* 
Freitag 10 Oktober 2025  23:17:02 +0200 (0:00:00.059)       0:00:27.365 ******* 
Freitag 10 Oktober 2025  23:17:02 +0200 (0:00:00.064)       0:00:27.430 ******* 

TASK [geerlingguy.docker : Ensure Docker is started and enabled at boot.] *****************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.docker/tasks/main.yml:68</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;enabled&quot;: true,</span>
<span style="color:#00AA00">    &quot;name&quot;: &quot;docker&quot;,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;started&quot;,</span>
<span style="color:#00AA00">    &quot;status&quot;: {</span>
<span style="color:#00AA00">        &quot;ActiveEnterTimestamp&quot;: &quot;Fri 2025-10-10 06:02:55 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;ActiveEnterTimestampMonotonic&quot;: &quot;400144120482&quot;,</span>
<span style="color:#00AA00">        &quot;ActiveExitTimestamp&quot;: &quot;Fri 2025-10-10 06:02:45 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;ActiveExitTimestampMonotonic&quot;: &quot;400134599927&quot;,</span>
<span style="color:#00AA00">        &quot;ActiveState&quot;: &quot;active&quot;,</span>
<span style="color:#00AA00">        &quot;After&quot;: &quot;time-set.target systemd-journald.socket system.slice sysinit.target nss-lookup.target network-online.target basic.target docker.socket containerd.service firewalld.service&quot;,</span>
<span style="color:#00AA00">        &quot;AllowIsolate&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;AssertResult&quot;: &quot;yes&quot;,</span>
<span style="color:#00AA00">        &quot;AssertTimestamp&quot;: &quot;Fri 2025-10-10 06:02:52 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;AssertTimestampMonotonic&quot;: &quot;400141426334&quot;,</span>
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
<span style="color:#00AA00">        &quot;CPUUsageNSec&quot;: &quot;1530920357000&quot;,</span>
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
<span style="color:#00AA00">        &quot;ConditionTimestamp&quot;: &quot;Fri 2025-10-10 06:02:52 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;ConditionTimestampMonotonic&quot;: &quot;400141426332&quot;,</span>
<span style="color:#00AA00">        &quot;ConfigurationDirectoryMode&quot;: &quot;0755&quot;,</span>
<span style="color:#00AA00">        &quot;Conflicts&quot;: &quot;shutdown.target&quot;,</span>
<span style="color:#00AA00">        &quot;ControlGroup&quot;: &quot;/system.slice/docker.service&quot;,</span>
<span style="color:#00AA00">        &quot;ControlGroupId&quot;: &quot;44918&quot;,</span>
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
<span style="color:#00AA00">        &quot;ExecMainPID&quot;: &quot;2126411&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainStartTimestamp&quot;: &quot;Fri 2025-10-10 06:02:52 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainStartTimestampMonotonic&quot;: &quot;400141448243&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainStatus&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;ExecReload&quot;: &quot;{ path=/bin/kill ; argv[]=/bin/kill -s HUP $MAINPID ; ignore_errors=no ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }&quot;,</span>
<span style="color:#00AA00">        &quot;ExecReloadEx&quot;: &quot;{ path=/bin/kill ; argv[]=/bin/kill -s HUP $MAINPID ; flags= ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }&quot;,</span>
<span style="color:#00AA00">        &quot;ExecStart&quot;: &quot;{ path=/usr/bin/dockerd ; argv[]=/usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock ; ignore_errors=no ; start_time=[Fri 2025-10-10 06:02:52 CEST] ; stop_time=[n/a] ; pid=2126411 ; code=(null) ; status=0/0 }&quot;,</span>
<span style="color:#00AA00">        &quot;ExecStartEx&quot;: &quot;{ path=/usr/bin/dockerd ; argv[]=/usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock ; flags= ; start_time=[Fri 2025-10-10 06:02:52 CEST] ; stop_time=[n/a] ; pid=2126411 ; code=(null) ; status=0/0 }&quot;,</span>
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
<span style="color:#00AA00">        &quot;InactiveEnterTimestamp&quot;: &quot;Fri 2025-10-10 06:02:52 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;InactiveEnterTimestampMonotonic&quot;: &quot;400141425859&quot;,</span>
<span style="color:#00AA00">        &quot;InactiveExitTimestamp&quot;: &quot;Fri 2025-10-10 06:02:52 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;InactiveExitTimestampMonotonic&quot;: &quot;400141448842&quot;,</span>
<span style="color:#00AA00">        &quot;InvocationID&quot;: &quot;9a50bf4eb0474d18914540f123cf7abc&quot;,</span>
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
<span style="color:#00AA00">        &quot;LimitSIGPENDING&quot;: &quot;31915&quot;,</span>
<span style="color:#00AA00">        &quot;LimitSIGPENDINGSoft&quot;: &quot;31915&quot;,</span>
<span style="color:#00AA00">        &quot;LimitSTACK&quot;: &quot;infinity&quot;,</span>
<span style="color:#00AA00">        &quot;LimitSTACKSoft&quot;: &quot;8388608&quot;,</span>
<span style="color:#00AA00">        &quot;LoadState&quot;: &quot;loaded&quot;,</span>
<span style="color:#00AA00">        &quot;LockPersonality&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;LogLevelMax&quot;: &quot;-1&quot;,</span>
<span style="color:#00AA00">        &quot;LogRateLimitBurst&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;LogRateLimitIntervalUSec&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;LogsDirectoryMode&quot;: &quot;0755&quot;,</span>
<span style="color:#00AA00">        &quot;MainPID&quot;: &quot;2126411&quot;,</span>
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
<span style="color:#00AA00">        &quot;Requires&quot;: &quot;docker.socket system.slice sysinit.target&quot;,</span>
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
<span style="color:#00AA00">        &quot;StateChangeTimestamp&quot;: &quot;Fri 2025-10-10 06:02:55 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;StateChangeTimestampMonotonic&quot;: &quot;400144120482&quot;,</span>
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
<span style="color:#00AA00">        &quot;TasksCurrent&quot;: &quot;160&quot;,</span>
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
Freitag 10 Oktober 2025  23:17:03 +0200 (0:00:00.599)       0:00:28.030 ******* 
<span style="color:#0000AA">META: triggered running handlers for ansible-nas</span>
Freitag 10 Oktober 2025  23:17:03 +0200 (0:00:00.018)       0:00:28.049 ******* 
Freitag 10 Oktober 2025  23:17:03 +0200 (0:00:00.068)       0:00:28.117 ******* 
Freitag 10 Oktober 2025  23:17:03 +0200 (0:00:00.074)       0:00:28.191 ******* 
Freitag 10 Oktober 2025  23:17:03 +0200 (0:00:00.039)       0:00:28.231 ******* 
Freitag 10 Oktober 2025  23:17:03 +0200 (0:00:00.064)       0:00:28.295 ******* 

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
Freitag 10 Oktober 2025  23:17:04 +0200 (0:00:00.722)       0:00:29.018 ******* 

TASK [ansible-nas-general : Update apt-cache] *********************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-general/tasks/main.yml:7</b></span>
<span style="color:#AA5500">changed: [ansible-nas] =&gt; {</span>
<span style="color:#AA5500">    &quot;attempts&quot;: 1,</span>
<span style="color:#AA5500">    &quot;cache_update_time&quot;: 1760131025,</span>
<span style="color:#AA5500">    &quot;cache_updated&quot;: true,</span>
<span style="color:#AA5500">    &quot;changed&quot;: true</span>
<span style="color:#AA5500">}</span>
Freitag 10 Oktober 2025  23:17:08 +0200 (0:00:04.141)       0:00:33.159 ******* 
Freitag 10 Oktober 2025  23:17:08 +0200 (0:00:00.042)       0:00:33.202 ******* 

TASK [ansible-nas-general : Install some packages] ****************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-general/tasks/main.yml:22</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;attempts&quot;: 1,</span>
<span style="color:#00AA00">    &quot;cache_update_time&quot;: 1760131025,</span>
<span style="color:#00AA00">    &quot;cache_updated&quot;: false,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:17:09 +0200 (0:00:01.490)       0:00:34.692 ******* 

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
Freitag 10 Oktober 2025  23:17:10 +0200 (0:00:01.048)       0:00:35.741 ******* 

TASK [ansible-nas-general : Set timezone to Europe/Berlin] ********************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-general/tasks/main.yml:33</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:17:11 +0200 (0:00:00.674)       0:00:36.415 ******* 
Freitag 10 Oktober 2025  23:17:11 +0200 (0:00:00.067)       0:00:36.483 ******* 

TASK [ansible-nas-docker : Install python3-pip] *******************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-docker/tasks/main.yml:2</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;attempts&quot;: 1,</span>
<span style="color:#00AA00">    &quot;cache_update_time&quot;: 1760131025,</span>
<span style="color:#00AA00">    &quot;cache_updated&quot;: false,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:17:13 +0200 (0:00:01.443)       0:00:37.927 ******* 

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
Freitag 10 Oktober 2025  23:17:13 +0200 (0:00:00.616)       0:00:38.544 ******* 

TASK [ansible-nas-docker : Remove &quot;ext-managed&quot;] ******************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-docker/tasks/main.yml:14</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;path&quot;: &quot;/usr/lib/python3.11/EXTERNALLY-MANAGED&quot;,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;absent&quot;</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:17:14 +0200 (0:00:00.356)       0:00:38.901 ******* 

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

Freitag 10 Oktober 2025  23:17:15 +0200 (0:00:01.246)       0:00:40.147 ******* 

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

Freitag 10 Oktober 2025  23:17:17 +0200 (0:00:01.682)       0:00:41.830 ******* 

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
Freitag 10 Oktober 2025  23:17:17 +0200 (0:00:00.366)       0:00:42.196 ******* 

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
Freitag 10 Oktober 2025  23:17:17 +0200 (0:00:00.442)       0:00:42.639 ******* 

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
Freitag 10 Oktober 2025  23:17:18 +0200 (0:00:00.622)       0:00:43.262 ******* 
Freitag 10 Oktober 2025  23:17:18 +0200 (0:00:00.149)       0:00:43.411 ******* 
Freitag 10 Oktober 2025  23:17:18 +0200 (0:00:00.046)       0:00:43.458 ******* 

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
Freitag 10 Oktober 2025  23:17:18 +0200 (0:00:00.070)       0:00:43.528 ******* 
Freitag 10 Oktober 2025  23:17:18 +0200 (0:00:00.056)       0:00:43.585 ******* 
Freitag 10 Oktober 2025  23:17:18 +0200 (0:00:00.039)       0:00:43.625 ******* 

TASK [airsonic : Stop Airsonic] ***********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/airsonic/tasks/main.yml:37</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:17:19 +0200 (0:00:01.001)       0:00:44.626 ******* 
Freitag 10 Oktober 2025  23:17:19 +0200 (0:00:00.047)       0:00:44.674 ******* 
Freitag 10 Oktober 2025  23:17:19 +0200 (0:00:00.043)       0:00:44.717 ******* 
Freitag 10 Oktober 2025  23:17:19 +0200 (0:00:00.053)       0:00:44.770 ******* 
Freitag 10 Oktober 2025  23:17:20 +0200 (0:00:00.043)       0:00:44.814 ******* 

TASK [apcupsd : Stop Apcupsd] *************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/apcupsd/tasks/main.yml:44</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:17:20 +0200 (0:00:00.595)       0:00:45.409 ******* 
Freitag 10 Oktober 2025  23:17:20 +0200 (0:00:00.049)       0:00:45.459 ******* 
Freitag 10 Oktober 2025  23:17:20 +0200 (0:00:00.044)       0:00:45.504 ******* 

TASK [bazarr : Stop Bazarr] ***************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/bazarr/tasks/main.yml:46</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:17:21 +0200 (0:00:00.733)       0:00:46.238 ******* 
Freitag 10 Oktober 2025  23:17:21 +0200 (0:00:00.048)       0:00:46.287 ******* 
Freitag 10 Oktober 2025  23:17:21 +0200 (0:00:00.052)       0:00:46.339 ******* 
Freitag 10 Oktober 2025  23:17:21 +0200 (0:00:00.040)       0:00:46.380 ******* 
Freitag 10 Oktober 2025  23:17:21 +0200 (0:00:00.049)       0:00:46.429 ******* 

TASK [bitwarden : Stop Bitwarden] *********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/bitwarden/tasks/main.yml:64</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:17:22 +0200 (0:00:00.620)       0:00:47.050 ******* 

TASK [bitwarden : Stop Bitwarden Backup] **************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/bitwarden/tasks/main.yml:69</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:17:22 +0200 (0:00:00.653)       0:00:47.703 ******* 
Freitag 10 Oktober 2025  23:17:22 +0200 (0:00:00.058)       0:00:47.762 ******* 
Freitag 10 Oktober 2025  23:17:23 +0200 (0:00:00.042)       0:00:47.804 ******* 

TASK [booksonic : Stop Booksonic] *********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/booksonic/tasks/main.yml:42</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:17:23 +0200 (0:00:00.599)       0:00:48.404 ******* 

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
Freitag 10 Oktober 2025  23:17:23 +0200 (0:00:00.379)       0:00:48.783 ******* 

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
<span style="color:#AA5500">            &quot;EndpointID&quot;: &quot;6b9242eb784eb2f5e0831e343e5371d30fd10c873d69c58603ca6ab47c6abfa6&quot;,</span>
<span style="color:#AA5500">            &quot;Gateway&quot;: &quot;172.17.0.1&quot;,</span>
<span style="color:#AA5500">            &quot;GlobalIPv6Address&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;GlobalIPv6PrefixLen&quot;: 0,</span>
<span style="color:#AA5500">            &quot;HairpinMode&quot;: false,</span>
<span style="color:#AA5500">            &quot;IPAddress&quot;: &quot;172.17.0.10&quot;,</span>
<span style="color:#AA5500">            &quot;IPPrefixLen&quot;: 16,</span>
<span style="color:#AA5500">            &quot;IPv6Gateway&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;LinkLocalIPv6Address&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;LinkLocalIPv6PrefixLen&quot;: 0,</span>
<span style="color:#AA5500">            &quot;MacAddress&quot;: &quot;ca:f1:71:1c:57:19&quot;,</span>
<span style="color:#AA5500">            &quot;Networks&quot;: {</span>
<span style="color:#AA5500">                &quot;bridge&quot;: {</span>
<span style="color:#AA5500">                    &quot;Aliases&quot;: null,</span>
<span style="color:#AA5500">                    &quot;DNSNames&quot;: null,</span>
<span style="color:#AA5500">                    &quot;DriverOpts&quot;: null,</span>
<span style="color:#AA5500">                    &quot;EndpointID&quot;: &quot;6b9242eb784eb2f5e0831e343e5371d30fd10c873d69c58603ca6ab47c6abfa6&quot;,</span>
<span style="color:#AA5500">                    &quot;Gateway&quot;: &quot;172.17.0.1&quot;,</span>
<span style="color:#AA5500">                    &quot;GlobalIPv6Address&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">                    &quot;GlobalIPv6PrefixLen&quot;: 0,</span>
<span style="color:#AA5500">                    &quot;GwPriority&quot;: 0,</span>
<span style="color:#AA5500">                    &quot;IPAMConfig&quot;: null,</span>
<span style="color:#AA5500">                    &quot;IPAddress&quot;: &quot;172.17.0.10&quot;,</span>
<span style="color:#AA5500">                    &quot;IPPrefixLen&quot;: 16,</span>
<span style="color:#AA5500">                    &quot;IPv6Gateway&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">                    &quot;Links&quot;: null,</span>
<span style="color:#AA5500">                    &quot;MacAddress&quot;: &quot;ca:f1:71:1c:57:19&quot;,</span>
<span style="color:#AA5500">                    &quot;NetworkID&quot;: &quot;fce42755ebf1352d21e037493e0c33a917b08a8fe5d9ea19e3af1d873ab69e67&quot;</span>
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
<span style="color:#AA5500">            &quot;SandboxID&quot;: &quot;cd9fef2baf91fec670c3dcb3149155088dcda2d347b68289fa1660b6fd0e795c&quot;,</span>
<span style="color:#AA5500">            &quot;SandboxKey&quot;: &quot;/var/run/docker/netns/cd9fef2baf91&quot;,</span>
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
<span style="color:#AA5500">            &quot;FinishedAt&quot;: &quot;2025-10-10T04:02:52.0251915Z&quot;,</span>
<span style="color:#AA5500">            &quot;OOMKilled&quot;: false,</span>
<span style="color:#AA5500">            &quot;Paused&quot;: false,</span>
<span style="color:#AA5500">            &quot;Pid&quot;: 2127016,</span>
<span style="color:#AA5500">            &quot;Restarting&quot;: false,</span>
<span style="color:#AA5500">            &quot;Running&quot;: true,</span>
<span style="color:#AA5500">            &quot;StartedAt&quot;: &quot;2025-10-10T04:02:54.004865968Z&quot;,</span>
<span style="color:#AA5500">            &quot;Status&quot;: &quot;running&quot;</span>
<span style="color:#AA5500">        }</span>
<span style="color:#AA5500">    }</span>
<span style="color:#AA5500">}</span>
Freitag 10 Oktober 2025  23:17:25 +0200 (0:00:01.922)       0:00:50.706 ******* 
Freitag 10 Oktober 2025  23:17:25 +0200 (0:00:00.063)       0:00:50.769 ******* 

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
Freitag 10 Oktober 2025  23:17:26 +0200 (0:00:00.833)       0:00:51.603 ******* 

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
<span style="color:#AA5500">            &quot;Hostname&quot;: &quot;fed5b4cd7881&quot;,</span>
<span style="color:#AA5500">            &quot;Image&quot;: &quot;linuxserver/calibre-web:latest&quot;,</span>
<span style="color:#AA5500">            &quot;Labels&quot;: {</span>
<span style="color:#AA5500">                &quot;build_version&quot;: &quot;Linuxserver.io version:- 0.6.25-ls350 Build-date:- 2025-10-05T02:14:11+00:00&quot;,</span>
<span style="color:#AA5500">                &quot;maintainer&quot;: &quot;notdriz&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.authors&quot;: &quot;linuxserver.io&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.created&quot;: &quot;2025-10-05T02:14:11+00:00&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.description&quot;: &quot;[Calibre-web](https://github.com/janeczku/calibre-web) is a web app providing a clean interface for browsing, reading and downloading eBooks using an existing Calibre database.   It is also possible to integrate google drive and edit metadata and your calibre library through the app itself.    This software is a fork of library and licensed under the GPL v3 License.  &quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.documentation&quot;: &quot;https://docs.linuxserver.io/images/docker-calibre-web&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.licenses&quot;: &quot;GPL-3.0-only&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.ref.name&quot;: &quot;558ef3441641bcdb17fca44de3606bb2122db305&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.revision&quot;: &quot;558ef3441641bcdb17fca44de3606bb2122db305&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.source&quot;: &quot;https://github.com/linuxserver/docker-calibre-web&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.title&quot;: &quot;Calibre-web&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.url&quot;: &quot;https://github.com/linuxserver/docker-calibre-web/packages&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.vendor&quot;: &quot;linuxserver.io&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.version&quot;: &quot;0.6.25-ls350&quot;,</span>
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
<span style="color:#AA5500">        &quot;Created&quot;: &quot;2025-10-09T16:52:12.945826614Z&quot;,</span>
<span style="color:#AA5500">        &quot;Driver&quot;: &quot;overlay2&quot;,</span>
<span style="color:#AA5500">        &quot;ExecIDs&quot;: null,</span>
<span style="color:#AA5500">        &quot;GraphDriver&quot;: {</span>
<span style="color:#AA5500">            &quot;Data&quot;: {</span>
<span style="color:#AA5500">                &quot;ID&quot;: &quot;fed5b4cd7881b3b22d2a1e3c5156adefc3c00ac07ef7465b004518f427360987&quot;,</span>
<span style="color:#AA5500">                &quot;LowerDir&quot;: &quot;/var/lib/docker/overlay2/bff9762a38d3d0750b3e014f3604b1ddfa8e8e55b7484b277163b6c2b270fcb0-init/diff:/var/lib/docker/overlay2/c7c3c925a7fb50e199d566acc3c17543f4824f571f9da9aeeda6700208f407e8/diff:/var/lib/docker/overlay2/b3baa885ba5fab0cacda61142529da432d4c0c480955960c358874566d559abe/diff:/var/lib/docker/overlay2/eba71cd0abaad61fadca3c2b44d8386ad39c467673b08ea5222383816edecd61/diff:/var/lib/docker/overlay2/4d7c7e60d93aecbaac9ef71873b0cf055309bf27b9926fe955f21b2a388f7f1e/diff:/var/lib/docker/overlay2/2141895bc06f8f451521fb9bebc4fc0f826c7e25db117138e3b8d27dbe12d2e7/diff:/var/lib/docker/overlay2/28a928b54e0f6e13b05a83d7e8f86f7c0fd42426dc5e15dad94f6de1add234f0/diff:/var/lib/docker/overlay2/e378081c38e8268e5796fbb98ccf7f6e9eaffb6c1c247b0c31b5a3779da47ac1/diff:/var/lib/docker/overlay2/25d51f29ebf52444fadf14bc57b45ecee8a65e5163969773ac6d3a10b7246c4d/diff:/var/lib/docker/overlay2/6dffaeb822887889a6e67905acb7afefb48a136305da001c341f5a1dd0f08bc5/diff:/var/lib/docker/overlay2/783e36746afc301e30ef754ea860f388eb91cfd7c0efbde820487b204063bf60/diff:/var/lib/docker/overlay2/170fee65a5b57a72609e1dcce34699f9a849be617c4be4db49a12ff2423cd71b/diff&quot;,</span>
<span style="color:#AA5500">                &quot;MergedDir&quot;: &quot;/var/lib/docker/overlay2/bff9762a38d3d0750b3e014f3604b1ddfa8e8e55b7484b277163b6c2b270fcb0/merged&quot;,</span>
<span style="color:#AA5500">                &quot;UpperDir&quot;: &quot;/var/lib/docker/overlay2/bff9762a38d3d0750b3e014f3604b1ddfa8e8e55b7484b277163b6c2b270fcb0/diff&quot;,</span>
<span style="color:#AA5500">                &quot;WorkDir&quot;: &quot;/var/lib/docker/overlay2/bff9762a38d3d0750b3e014f3604b1ddfa8e8e55b7484b277163b6c2b270fcb0/work&quot;</span>
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
<span style="color:#AA5500">        &quot;HostnamePath&quot;: &quot;/var/lib/docker/containers/fed5b4cd7881b3b22d2a1e3c5156adefc3c00ac07ef7465b004518f427360987/hostname&quot;,</span>
<span style="color:#AA5500">        &quot;HostsPath&quot;: &quot;/var/lib/docker/containers/fed5b4cd7881b3b22d2a1e3c5156adefc3c00ac07ef7465b004518f427360987/hosts&quot;,</span>
<span style="color:#AA5500">        &quot;Id&quot;: &quot;fed5b4cd7881b3b22d2a1e3c5156adefc3c00ac07ef7465b004518f427360987&quot;,</span>
<span style="color:#AA5500">        &quot;Image&quot;: &quot;sha256:e9a03a79126f4f40d726c4d57fcef30490dd5d5ad3f59d4de03498432a0bfeaa&quot;,</span>
<span style="color:#AA5500">        &quot;LogPath&quot;: &quot;/var/lib/docker/containers/fed5b4cd7881b3b22d2a1e3c5156adefc3c00ac07ef7465b004518f427360987/fed5b4cd7881b3b22d2a1e3c5156adefc3c00ac07ef7465b004518f427360987-json.log&quot;,</span>
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
<span style="color:#AA5500">            &quot;EndpointID&quot;: &quot;7f83e5f2cf34e5ff614fbb7daca16d2036a411611340ca1c718ba6fc854cf6c3&quot;,</span>
<span style="color:#AA5500">            &quot;Gateway&quot;: &quot;172.17.0.1&quot;,</span>
<span style="color:#AA5500">            &quot;GlobalIPv6Address&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;GlobalIPv6PrefixLen&quot;: 0,</span>
<span style="color:#AA5500">            &quot;HairpinMode&quot;: false,</span>
<span style="color:#AA5500">            &quot;IPAddress&quot;: &quot;172.17.0.4&quot;,</span>
<span style="color:#AA5500">            &quot;IPPrefixLen&quot;: 16,</span>
<span style="color:#AA5500">            &quot;IPv6Gateway&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;LinkLocalIPv6Address&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;LinkLocalIPv6PrefixLen&quot;: 0,</span>
<span style="color:#AA5500">            &quot;MacAddress&quot;: &quot;ee:92:2e:57:27:2f&quot;,</span>
<span style="color:#AA5500">            &quot;Networks&quot;: {</span>
<span style="color:#AA5500">                &quot;bridge&quot;: {</span>
<span style="color:#AA5500">                    &quot;Aliases&quot;: null,</span>
<span style="color:#AA5500">                    &quot;DNSNames&quot;: null,</span>
<span style="color:#AA5500">                    &quot;DriverOpts&quot;: null,</span>
<span style="color:#AA5500">                    &quot;EndpointID&quot;: &quot;7f83e5f2cf34e5ff614fbb7daca16d2036a411611340ca1c718ba6fc854cf6c3&quot;,</span>
<span style="color:#AA5500">                    &quot;Gateway&quot;: &quot;172.17.0.1&quot;,</span>
<span style="color:#AA5500">                    &quot;GlobalIPv6Address&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">                    &quot;GlobalIPv6PrefixLen&quot;: 0,</span>
<span style="color:#AA5500">                    &quot;GwPriority&quot;: 0,</span>
<span style="color:#AA5500">                    &quot;IPAMConfig&quot;: null,</span>
<span style="color:#AA5500">                    &quot;IPAddress&quot;: &quot;172.17.0.4&quot;,</span>
<span style="color:#AA5500">                    &quot;IPPrefixLen&quot;: 16,</span>
<span style="color:#AA5500">                    &quot;IPv6Gateway&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">                    &quot;Links&quot;: null,</span>
<span style="color:#AA5500">                    &quot;MacAddress&quot;: &quot;ee:92:2e:57:27:2f&quot;,</span>
<span style="color:#AA5500">                    &quot;NetworkID&quot;: &quot;fce42755ebf1352d21e037493e0c33a917b08a8fe5d9ea19e3af1d873ab69e67&quot;</span>
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
<span style="color:#AA5500">            &quot;SandboxID&quot;: &quot;555f0503bda1da8288990b507dba235f3169cf8ce6b98be5c1d526af1388f8d0&quot;,</span>
<span style="color:#AA5500">            &quot;SandboxKey&quot;: &quot;/var/run/docker/netns/555f0503bda1&quot;,</span>
<span style="color:#AA5500">            &quot;SecondaryIPAddresses&quot;: null,</span>
<span style="color:#AA5500">            &quot;SecondaryIPv6Addresses&quot;: null</span>
<span style="color:#AA5500">        },</span>
<span style="color:#AA5500">        &quot;Path&quot;: &quot;/init&quot;,</span>
<span style="color:#AA5500">        &quot;Platform&quot;: &quot;linux&quot;,</span>
<span style="color:#AA5500">        &quot;ProcessLabel&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">        &quot;ResolvConfPath&quot;: &quot;/var/lib/docker/containers/fed5b4cd7881b3b22d2a1e3c5156adefc3c00ac07ef7465b004518f427360987/resolv.conf&quot;,</span>
<span style="color:#AA5500">        &quot;RestartCount&quot;: 0,</span>
<span style="color:#AA5500">        &quot;State&quot;: {</span>
<span style="color:#AA5500">            &quot;Dead&quot;: false,</span>
<span style="color:#AA5500">            &quot;Error&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;ExitCode&quot;: 0,</span>
<span style="color:#AA5500">            &quot;FinishedAt&quot;: &quot;2025-10-10T04:02:52.583199928Z&quot;,</span>
<span style="color:#AA5500">            &quot;OOMKilled&quot;: false,</span>
<span style="color:#AA5500">            &quot;Paused&quot;: false,</span>
<span style="color:#AA5500">            &quot;Pid&quot;: 2126782,</span>
<span style="color:#AA5500">            &quot;Restarting&quot;: false,</span>
<span style="color:#AA5500">            &quot;Running&quot;: true,</span>
<span style="color:#AA5500">            &quot;StartedAt&quot;: &quot;2025-10-10T04:02:53.966089533Z&quot;,</span>
<span style="color:#AA5500">            &quot;Status&quot;: &quot;running&quot;</span>
<span style="color:#AA5500">        }</span>
<span style="color:#AA5500">    }</span>
<span style="color:#AA5500">}</span>
Freitag 10 Oktober 2025  23:17:28 +0200 (0:00:01.761)       0:00:53.365 ******* 
Freitag 10 Oktober 2025  23:17:28 +0200 (0:00:00.080)       0:00:53.445 ******* 
Freitag 10 Oktober 2025  23:17:28 +0200 (0:00:00.061)       0:00:53.506 ******* 
Freitag 10 Oktober 2025  23:17:28 +0200 (0:00:00.055)       0:00:53.562 ******* 

TASK [cloudcmd : Stop Cloudcmd] ***********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/cloudcmd/tasks/main.yml:38</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:17:29 +0200 (0:00:00.625)       0:00:54.188 ******* 
Freitag 10 Oktober 2025  23:17:29 +0200 (0:00:00.046)       0:00:54.234 ******* 
Freitag 10 Oktober 2025  23:17:29 +0200 (0:00:00.044)       0:00:54.278 ******* 
Freitag 10 Oktober 2025  23:17:29 +0200 (0:00:00.050)       0:00:54.328 ******* 
Freitag 10 Oktober 2025  23:17:29 +0200 (0:00:00.041)       0:00:54.370 ******* 

TASK [cloudflare_ddns : Stop Cloudflare DDNS] *********************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/cloudflare_ddns/tasks/main.yml:34</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:17:30 +0200 (0:00:00.637)       0:00:55.008 ******* 
Freitag 10 Oktober 2025  23:17:30 +0200 (0:00:00.064)       0:00:55.072 ******* 
Freitag 10 Oktober 2025  23:17:30 +0200 (0:00:00.047)       0:00:55.120 ******* 

TASK [couchdb : Stop CouchDB] *************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/couchdb/tasks/main.yml:38</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:17:31 +0200 (0:00:00.711)       0:00:55.831 ******* 
Freitag 10 Oktober 2025  23:17:31 +0200 (0:00:00.048)       0:00:55.879 ******* 

TASK [code-server : Stop Code Server] *****************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/code-server/tasks/main.yml:32</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:17:31 +0200 (0:00:00.672)       0:00:56.552 ******* 
Freitag 10 Oktober 2025  23:17:31 +0200 (0:00:00.062)       0:00:56.614 ******* 
Freitag 10 Oktober 2025  23:17:31 +0200 (0:00:00.046)       0:00:56.661 ******* 

TASK [couchpotato : Stop Couchpotato] *****************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/couchpotato/tasks/main.yml:41</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:17:32 +0200 (0:00:00.606)       0:00:57.267 ******* 
Freitag 10 Oktober 2025  23:17:32 +0200 (0:00:00.051)       0:00:57.318 ******* 
Freitag 10 Oktober 2025  23:17:32 +0200 (0:00:00.044)       0:00:57.362 ******* 
Freitag 10 Oktober 2025  23:17:32 +0200 (0:00:00.044)       0:00:57.407 ******* 

TASK [dashy : Stop Dashy] *****************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/dashy/tasks/main.yml:39</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:17:33 +0200 (0:00:00.617)       0:00:58.025 ******* 
Freitag 10 Oktober 2025  23:17:33 +0200 (0:00:00.045)       0:00:58.071 ******* 
Freitag 10 Oktober 2025  23:17:33 +0200 (0:00:00.052)       0:00:58.123 ******* 
Freitag 10 Oktober 2025  23:17:33 +0200 (0:00:00.140)       0:00:58.264 ******* 
Freitag 10 Oktober 2025  23:17:33 +0200 (0:00:00.042)       0:00:58.306 ******* 

TASK [ddns_updater : Stop DDNS Updater] ***************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/ddns_updater/tasks/main.yml:54</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:17:34 +0200 (0:00:00.636)       0:00:58.943 ******* 
Freitag 10 Oktober 2025  23:17:34 +0200 (0:00:00.060)       0:00:59.004 ******* 
Freitag 10 Oktober 2025  23:17:34 +0200 (0:00:00.045)       0:00:59.049 ******* 

TASK [deluge : Stop Deluge] ***************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/deluge/tasks/main.yml:46</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:17:34 +0200 (0:00:00.650)       0:00:59.700 ******* 

TASK [dokuwiki : Create DokuWiki Directories] *********************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/dokuwiki/tasks/main.yml:4</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; (item=/mnt/Volume1/docker/dokuwiki/data) =&gt; {</span>
<span style="color:#00AA00">    &quot;ansible_loop_var&quot;: &quot;item&quot;,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;gid&quot;: 1001,</span>
<span style="color:#00AA00">    &quot;group&quot;: &quot;ansible-nas&quot;,</span>
<span style="color:#00AA00">    &quot;item&quot;: &quot;/mnt/Volume1/docker/dokuwiki/data&quot;,</span>
<span style="color:#00AA00">    &quot;mode&quot;: &quot;0777&quot;,</span>
<span style="color:#00AA00">    &quot;owner&quot;: &quot;1001&quot;,</span>
<span style="color:#00AA00">    &quot;path&quot;: &quot;/mnt/Volume1/docker/dokuwiki/data&quot;,</span>
<span style="color:#00AA00">    &quot;size&quot;: 4096,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;directory&quot;,</span>
<span style="color:#00AA00">    &quot;uid&quot;: 1001</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:17:35 +0200 (0:00:00.391)       0:01:00.092 ******* 

TASK [dokuwiki : DokuWiki Docker Container] ***********************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/dokuwiki/tasks/main.yml:11</b></span>
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
<span style="color:#AA5500">                &quot;PUID=1000&quot;,</span>
<span style="color:#AA5500">                &quot;PGID=1000&quot;,</span>
<span style="color:#AA5500">                &quot;PATH=/lsiopy/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin&quot;,</span>
<span style="color:#AA5500">                &quot;PS1=$(whoami)@$(hostname):$(pwd)\\$ &quot;,</span>
<span style="color:#AA5500">                &quot;HOME=/root&quot;,</span>
<span style="color:#AA5500">                &quot;TERM=xterm&quot;,</span>
<span style="color:#AA5500">                &quot;S6_CMD_WAIT_FOR_SERVICES_MAXTIME=0&quot;,</span>
<span style="color:#AA5500">                &quot;S6_VERBOSITY=1&quot;,</span>
<span style="color:#AA5500">                &quot;S6_STAGE2_HOOK=/docker-mods&quot;,</span>
<span style="color:#AA5500">                &quot;VIRTUAL_ENV=/lsiopy&quot;,</span>
<span style="color:#AA5500">                &quot;PHP_INI_SCAN_DIR=:/config/php&quot;,</span>
<span style="color:#AA5500">                &quot;LSIO_FIRST_PARTY=true&quot;</span>
<span style="color:#AA5500">            ],</span>
<span style="color:#AA5500">            &quot;ExposedPorts&quot;: {</span>
<span style="color:#AA5500">                &quot;443/tcp&quot;: {},</span>
<span style="color:#AA5500">                &quot;80/tcp&quot;: {}</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            &quot;Hostname&quot;: &quot;41b10f8b7d2c&quot;,</span>
<span style="color:#AA5500">            &quot;Image&quot;: &quot;linuxserver/dokuwiki:latest&quot;,</span>
<span style="color:#AA5500">            &quot;Labels&quot;: {</span>
<span style="color:#AA5500">                &quot;build_version&quot;: &quot;Linuxserver.io version:- 2025-05-14b-ls281 Build-date:- 2025-10-10T15:46:10+00:00&quot;,</span>
<span style="color:#AA5500">                &quot;maintainer&quot;: &quot;chbmb&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.authors&quot;: &quot;linuxserver.io&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.created&quot;: &quot;2025-10-10T15:46:10+00:00&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.description&quot;: &quot;[Dokuwiki](https://www.dokuwiki.org/dokuwiki/) is a simple to use and highly versatile Open Source wiki software that doesn&apos;t require a database. It is loved by users for its clean and readable syntax. The ease of maintenance, backup and integration makes it an administrator&apos;s favorite. Built in access controls and authentication connectors make DokuWiki especially useful in the enterprise context and the large number of plugins contributed by its vibrant community allow for a broad range of use cases beyond a traditional wiki.  &quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.documentation&quot;: &quot;https://docs.linuxserver.io/images/docker-dokuwiki&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.licenses&quot;: &quot;GPL-3.0-only&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.ref.name&quot;: &quot;aa498c7fa9aa7560bf12b19ac00feeea226bfcb2&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.revision&quot;: &quot;aa498c7fa9aa7560bf12b19ac00feeea226bfcb2&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.source&quot;: &quot;https://github.com/linuxserver/docker-dokuwiki&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.title&quot;: &quot;Dokuwiki&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.url&quot;: &quot;https://github.com/linuxserver/docker-dokuwiki/packages&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.vendor&quot;: &quot;linuxserver.io&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.version&quot;: &quot;2025-05-14b-ls281&quot;,</span>
<span style="color:#AA5500">                &quot;traefik.enable&quot;: &quot;False&quot;,</span>
<span style="color:#AA5500">                &quot;traefik.http.routers.dokuwiki.rule&quot;: &quot;Host(`dokuwiki.Schneider.nbg`)&quot;,</span>
<span style="color:#AA5500">                &quot;traefik.http.routers.dokuwiki.tls.certresolver&quot;: &quot;letsencrypt&quot;,</span>
<span style="color:#AA5500">                &quot;traefik.http.routers.dokuwiki.tls.domains[0].main&quot;: &quot;Schneider.nbg&quot;,</span>
<span style="color:#AA5500">                &quot;traefik.http.routers.dokuwiki.tls.domains[0].sans&quot;: &quot;*.Schneider.nbg&quot;,</span>
<span style="color:#AA5500">                &quot;traefik.http.services.dokuwiki.loadbalancer.server.port&quot;: &quot;80&quot;</span>
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
<span style="color:#AA5500">        &quot;Created&quot;: &quot;2025-10-10T21:17:45.946634555Z&quot;,</span>
<span style="color:#AA5500">        &quot;Driver&quot;: &quot;overlay2&quot;,</span>
<span style="color:#AA5500">        &quot;ExecIDs&quot;: null,</span>
<span style="color:#AA5500">        &quot;GraphDriver&quot;: {</span>
<span style="color:#AA5500">            &quot;Data&quot;: {</span>
<span style="color:#AA5500">                &quot;ID&quot;: &quot;41b10f8b7d2c4bcf0742b62b0560d7224b370a7db16293404005262970b720d5&quot;,</span>
<span style="color:#AA5500">                &quot;LowerDir&quot;: &quot;/var/lib/docker/overlay2/c4e4f1798cea669f16c889e7a3601f9e8e48ed514447824e2d6a8848bad4f7b3-init/diff:/var/lib/docker/overlay2/a45ee6718f42afd3f7b351d1ca9cc0e1f19cad195775afd4e6d2b1a56f7122bb/diff:/var/lib/docker/overlay2/5593899ce1f99ac3ba22d76a35f5483d4ec7f98e8d1ceccc6981c4051efc2d67/diff:/var/lib/docker/overlay2/412f52797e04a029f3733cd3b34e8b1a69142b94af21bb64341474277a468ce8/diff:/var/lib/docker/overlay2/c65474575418f82fc95c6b51d5af15110298ac13657e9aa93d546b3c485426ac/diff:/var/lib/docker/overlay2/bae18296ac795e3a58067314bef595ea3366f7a07020299ec71dd388884abc2d/diff:/var/lib/docker/overlay2/ecace77797951c8eccd4157913f5bb7322b0fc701d2f4294ab0cc1588f51051c/diff:/var/lib/docker/overlay2/ac258b31591ebba1d54d96d51ff4782409a008f08820b09c764cd9e64fc407f9/diff:/var/lib/docker/overlay2/1cce617b0200ef640c28e8d8dd1b33ec965710057e009c06d414f647332ec1bb/diff:/var/lib/docker/overlay2/83519fb5fdd88bc64702fde4dfc35774f9565e188ec97c31618b70084205bb4a/diff:/var/lib/docker/overlay2/949f2db1051bce293a65a394dae168a5e8b02f708ebdfb1c16710a73a0955353/diff:/var/lib/docker/overlay2/f9b971f278688a9bdb00666744a95167f83d50c47ff9f940f969788efe478ca5/diff&quot;,</span>
<span style="color:#AA5500">                &quot;MergedDir&quot;: &quot;/var/lib/docker/overlay2/c4e4f1798cea669f16c889e7a3601f9e8e48ed514447824e2d6a8848bad4f7b3/merged&quot;,</span>
<span style="color:#AA5500">                &quot;UpperDir&quot;: &quot;/var/lib/docker/overlay2/c4e4f1798cea669f16c889e7a3601f9e8e48ed514447824e2d6a8848bad4f7b3/diff&quot;,</span>
<span style="color:#AA5500">                &quot;WorkDir&quot;: &quot;/var/lib/docker/overlay2/c4e4f1798cea669f16c889e7a3601f9e8e48ed514447824e2d6a8848bad4f7b3/work&quot;</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            &quot;Name&quot;: &quot;overlay2&quot;</span>
<span style="color:#AA5500">        },</span>
<span style="color:#AA5500">        &quot;HostConfig&quot;: {</span>
<span style="color:#AA5500">            &quot;AutoRemove&quot;: false,</span>
<span style="color:#AA5500">            &quot;Binds&quot;: [</span>
<span style="color:#AA5500">                &quot;/mnt/Volume1/docker/dokuwiki:/config/dokuwiki/data:rw&quot;</span>
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
<span style="color:#AA5500">                &quot;80/tcp&quot;: [</span>
<span style="color:#AA5500">                    {</span>
<span style="color:#AA5500">                        &quot;HostIp&quot;: &quot;0.0.0.0&quot;,</span>
<span style="color:#AA5500">                        &quot;HostPort&quot;: &quot;8085&quot;</span>
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
<span style="color:#AA5500">        &quot;HostnamePath&quot;: &quot;/var/lib/docker/containers/41b10f8b7d2c4bcf0742b62b0560d7224b370a7db16293404005262970b720d5/hostname&quot;,</span>
<span style="color:#AA5500">        &quot;HostsPath&quot;: &quot;/var/lib/docker/containers/41b10f8b7d2c4bcf0742b62b0560d7224b370a7db16293404005262970b720d5/hosts&quot;,</span>
<span style="color:#AA5500">        &quot;Id&quot;: &quot;41b10f8b7d2c4bcf0742b62b0560d7224b370a7db16293404005262970b720d5&quot;,</span>
<span style="color:#AA5500">        &quot;Image&quot;: &quot;sha256:1c07e368545188facb5999565c69974f67a280ceede203b10a39873a385ddc25&quot;,</span>
<span style="color:#AA5500">        &quot;LogPath&quot;: &quot;/var/lib/docker/containers/41b10f8b7d2c4bcf0742b62b0560d7224b370a7db16293404005262970b720d5/41b10f8b7d2c4bcf0742b62b0560d7224b370a7db16293404005262970b720d5-json.log&quot;,</span>
<span style="color:#AA5500">        &quot;MountLabel&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">        &quot;Mounts&quot;: [</span>
<span style="color:#AA5500">            {</span>
<span style="color:#AA5500">                &quot;Destination&quot;: &quot;/config/dokuwiki/data&quot;,</span>
<span style="color:#AA5500">                &quot;Mode&quot;: &quot;rw&quot;,</span>
<span style="color:#AA5500">                &quot;Propagation&quot;: &quot;rprivate&quot;,</span>
<span style="color:#AA5500">                &quot;RW&quot;: true,</span>
<span style="color:#AA5500">                &quot;Source&quot;: &quot;/mnt/Volume1/docker/dokuwiki&quot;,</span>
<span style="color:#AA5500">                &quot;Type&quot;: &quot;bind&quot;</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            {</span>
<span style="color:#AA5500">                &quot;Destination&quot;: &quot;/config&quot;,</span>
<span style="color:#AA5500">                &quot;Driver&quot;: &quot;local&quot;,</span>
<span style="color:#AA5500">                &quot;Mode&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">                &quot;Name&quot;: &quot;bf73f1231b621b78e2277352ea76a8eaac68e4aea03df166e1ed12a4fc36bf44&quot;,</span>
<span style="color:#AA5500">                &quot;Propagation&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">                &quot;RW&quot;: true,</span>
<span style="color:#AA5500">                &quot;Source&quot;: &quot;/var/lib/docker/volumes/bf73f1231b621b78e2277352ea76a8eaac68e4aea03df166e1ed12a4fc36bf44/_data&quot;,</span>
<span style="color:#AA5500">                &quot;Type&quot;: &quot;volume&quot;</span>
<span style="color:#AA5500">            }</span>
<span style="color:#AA5500">        ],</span>
<span style="color:#AA5500">        &quot;Name&quot;: &quot;/dokuwiki&quot;,</span>
<span style="color:#AA5500">        &quot;NetworkSettings&quot;: {</span>
<span style="color:#AA5500">            &quot;Bridge&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;EndpointID&quot;: &quot;167b550c4d77a086cd347afaecfcf80e2bdbf0b4aad17d768f977b50ca252ba2&quot;,</span>
<span style="color:#AA5500">            &quot;Gateway&quot;: &quot;172.17.0.1&quot;,</span>
<span style="color:#AA5500">            &quot;GlobalIPv6Address&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;GlobalIPv6PrefixLen&quot;: 0,</span>
<span style="color:#AA5500">            &quot;HairpinMode&quot;: false,</span>
<span style="color:#AA5500">            &quot;IPAddress&quot;: &quot;172.17.0.9&quot;,</span>
<span style="color:#AA5500">            &quot;IPPrefixLen&quot;: 16,</span>
<span style="color:#AA5500">            &quot;IPv6Gateway&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;LinkLocalIPv6Address&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;LinkLocalIPv6PrefixLen&quot;: 0,</span>
<span style="color:#AA5500">            &quot;MacAddress&quot;: &quot;06:23:ee:2c:64:e2&quot;,</span>
<span style="color:#AA5500">            &quot;Networks&quot;: {</span>
<span style="color:#AA5500">                &quot;bridge&quot;: {</span>
<span style="color:#AA5500">                    &quot;Aliases&quot;: null,</span>
<span style="color:#AA5500">                    &quot;DNSNames&quot;: null,</span>
<span style="color:#AA5500">                    &quot;DriverOpts&quot;: null,</span>
<span style="color:#AA5500">                    &quot;EndpointID&quot;: &quot;167b550c4d77a086cd347afaecfcf80e2bdbf0b4aad17d768f977b50ca252ba2&quot;,</span>
<span style="color:#AA5500">                    &quot;Gateway&quot;: &quot;172.17.0.1&quot;,</span>
<span style="color:#AA5500">                    &quot;GlobalIPv6Address&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">                    &quot;GlobalIPv6PrefixLen&quot;: 0,</span>
<span style="color:#AA5500">                    &quot;GwPriority&quot;: 0,</span>
<span style="color:#AA5500">                    &quot;IPAMConfig&quot;: null,</span>
<span style="color:#AA5500">                    &quot;IPAddress&quot;: &quot;172.17.0.9&quot;,</span>
<span style="color:#AA5500">                    &quot;IPPrefixLen&quot;: 16,</span>
<span style="color:#AA5500">                    &quot;IPv6Gateway&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">                    &quot;Links&quot;: null,</span>
<span style="color:#AA5500">                    &quot;MacAddress&quot;: &quot;06:23:ee:2c:64:e2&quot;,</span>
<span style="color:#AA5500">                    &quot;NetworkID&quot;: &quot;fce42755ebf1352d21e037493e0c33a917b08a8fe5d9ea19e3af1d873ab69e67&quot;</span>
<span style="color:#AA5500">                }</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            &quot;Ports&quot;: {</span>
<span style="color:#AA5500">                &quot;443/tcp&quot;: null,</span>
<span style="color:#AA5500">                &quot;80/tcp&quot;: [</span>
<span style="color:#AA5500">                    {</span>
<span style="color:#AA5500">                        &quot;HostIp&quot;: &quot;0.0.0.0&quot;,</span>
<span style="color:#AA5500">                        &quot;HostPort&quot;: &quot;8085&quot;</span>
<span style="color:#AA5500">                    }</span>
<span style="color:#AA5500">                ]</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            &quot;SandboxID&quot;: &quot;439537138be318f88b732f23fa7c67d3fa3ae7a520347bd42acf4f0b5f2f6c99&quot;,</span>
<span style="color:#AA5500">            &quot;SandboxKey&quot;: &quot;/var/run/docker/netns/439537138be3&quot;,</span>
<span style="color:#AA5500">            &quot;SecondaryIPAddresses&quot;: null,</span>
<span style="color:#AA5500">            &quot;SecondaryIPv6Addresses&quot;: null</span>
<span style="color:#AA5500">        },</span>
<span style="color:#AA5500">        &quot;Path&quot;: &quot;/init&quot;,</span>
<span style="color:#AA5500">        &quot;Platform&quot;: &quot;linux&quot;,</span>
<span style="color:#AA5500">        &quot;ProcessLabel&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">        &quot;ResolvConfPath&quot;: &quot;/var/lib/docker/containers/41b10f8b7d2c4bcf0742b62b0560d7224b370a7db16293404005262970b720d5/resolv.conf&quot;,</span>
<span style="color:#AA5500">        &quot;RestartCount&quot;: 0,</span>
<span style="color:#AA5500">        &quot;State&quot;: {</span>
<span style="color:#AA5500">            &quot;Dead&quot;: false,</span>
<span style="color:#AA5500">            &quot;Error&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;ExitCode&quot;: 0,</span>
<span style="color:#AA5500">            &quot;FinishedAt&quot;: &quot;0001-01-01T00:00:00Z&quot;,</span>
<span style="color:#AA5500">            &quot;OOMKilled&quot;: false,</span>
<span style="color:#AA5500">            &quot;Paused&quot;: false,</span>
<span style="color:#AA5500">            &quot;Pid&quot;: 2570448,</span>
<span style="color:#AA5500">            &quot;Restarting&quot;: false,</span>
<span style="color:#AA5500">            &quot;Running&quot;: true,</span>
<span style="color:#AA5500">            &quot;StartedAt&quot;: &quot;2025-10-10T21:17:46.015282482Z&quot;,</span>
<span style="color:#AA5500">            &quot;Status&quot;: &quot;running&quot;</span>
<span style="color:#AA5500">        }</span>
<span style="color:#AA5500">    }</span>
<span style="color:#AA5500">}</span>
Freitag 10 Oktober 2025  23:17:46 +0200 (0:00:10.975)       0:01:11.067 ******* 
Freitag 10 Oktober 2025  23:17:46 +0200 (0:00:00.069)       0:01:11.137 ******* 
Freitag 10 Oktober 2025  23:17:46 +0200 (0:00:00.047)       0:01:11.184 ******* 
Freitag 10 Oktober 2025  23:17:46 +0200 (0:00:00.044)       0:01:11.229 ******* 
Freitag 10 Oktober 2025  23:17:46 +0200 (0:00:00.053)       0:01:11.282 ******* 
Freitag 10 Oktober 2025  23:17:46 +0200 (0:00:00.052)       0:01:11.335 ******* 
Freitag 10 Oktober 2025  23:17:46 +0200 (0:00:00.039)       0:01:11.374 ******* 
Freitag 10 Oktober 2025  23:17:46 +0200 (0:00:00.138)       0:01:11.512 ******* 

TASK [drone-ci : Stop Drone-CI] ***********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/drone-ci/tasks/main.yml:79</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:17:47 +0200 (0:00:00.624)       0:01:12.137 ******* 

TASK [drone-ci : Stop Drone-CI Runner] ****************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/drone-ci/tasks/main.yml:84</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:17:48 +0200 (0:00:00.764)       0:01:12.901 ******* 

TASK [dupeguru : Create dupeGuru Directories] *********************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/dupeguru/tasks/main.yml:4</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; (item=/mnt/Volume1/docker/dupeguru) =&gt; {</span>
<span style="color:#00AA00">    &quot;ansible_loop_var&quot;: &quot;item&quot;,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;gid&quot;: 1000,</span>
<span style="color:#00AA00">    &quot;group&quot;: &quot;dietmar&quot;,</span>
<span style="color:#00AA00">    &quot;item&quot;: &quot;/mnt/Volume1/docker/dupeguru&quot;,</span>
<span style="color:#00AA00">    &quot;mode&quot;: &quot;0755&quot;,</span>
<span style="color:#00AA00">    &quot;owner&quot;: &quot;dietmar&quot;,</span>
<span style="color:#00AA00">    &quot;path&quot;: &quot;/mnt/Volume1/docker/dupeguru&quot;,</span>
<span style="color:#00AA00">    &quot;size&quot;: 4096,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;directory&quot;,</span>
<span style="color:#00AA00">    &quot;uid&quot;: 1000</span>
<span style="color:#00AA00">}</span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; (item=/mnt/Volume1/local/) =&gt; {</span>
<span style="color:#00AA00">    &quot;ansible_loop_var&quot;: &quot;item&quot;,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;gid&quot;: 0,</span>
<span style="color:#00AA00">    &quot;group&quot;: &quot;root&quot;,</span>
<span style="color:#00AA00">    &quot;item&quot;: &quot;/mnt/Volume1/local/&quot;,</span>
<span style="color:#00AA00">    &quot;mode&quot;: &quot;0777&quot;,</span>
<span style="color:#00AA00">    &quot;owner&quot;: &quot;root&quot;,</span>
<span style="color:#00AA00">    &quot;path&quot;: &quot;/mnt/Volume1/local/&quot;,</span>
<span style="color:#00AA00">    &quot;size&quot;: 4096,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;directory&quot;,</span>
<span style="color:#00AA00">    &quot;uid&quot;: 0</span>
<span style="color:#00AA00">}</span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; (item=/mnt/Volume1/local/TRASH) =&gt; {</span>
<span style="color:#00AA00">    &quot;ansible_loop_var&quot;: &quot;item&quot;,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;gid&quot;: 0,</span>
<span style="color:#00AA00">    &quot;group&quot;: &quot;root&quot;,</span>
<span style="color:#00AA00">    &quot;item&quot;: &quot;/mnt/Volume1/local/TRASH&quot;,</span>
<span style="color:#00AA00">    &quot;mode&quot;: &quot;0755&quot;,</span>
<span style="color:#00AA00">    &quot;owner&quot;: &quot;root&quot;,</span>
<span style="color:#00AA00">    &quot;path&quot;: &quot;/mnt/Volume1/local/TRASH&quot;,</span>
<span style="color:#00AA00">    &quot;size&quot;: 4096,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;directory&quot;,</span>
<span style="color:#00AA00">    &quot;uid&quot;: 0</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:17:49 +0200 (0:00:01.043)       0:01:13.945 ******* 

TASK [dupeguru : dupeGuru Docker Container] ***********************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/dupeguru/tasks/main.yml:13</b></span>
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
<span style="color:#AA5500">                &quot;WEB_FILE_MANAGER=1&quot;,</span>
<span style="color:#AA5500">                &quot;DARK_MODE=1&quot;,</span>
<span style="color:#AA5500">                &quot;LANG=de_DE:UTF-8&quot;,</span>
<span style="color:#AA5500">                &quot;WEB_LISTENING_PORT=5801&quot;,</span>
<span style="color:#AA5500">                &quot;VNC_LISTENING_PORT=5901&quot;,</span>
<span style="color:#AA5500">                &quot;PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/opt/base/sbin:/opt/base/bin&quot;,</span>
<span style="color:#AA5500">                &quot;ENV=/root/.docker_rc&quot;,</span>
<span style="color:#AA5500">                &quot;USER_ID=1000&quot;,</span>
<span style="color:#AA5500">                &quot;GROUP_ID=1000&quot;,</span>
<span style="color:#AA5500">                &quot;SUP_GROUP_IDS=&quot;,</span>
<span style="color:#AA5500">                &quot;UMASK=0022&quot;,</span>
<span style="color:#AA5500">                &quot;KEEP_APP_RUNNING=0&quot;,</span>
<span style="color:#AA5500">                &quot;APP_NICENESS=0&quot;,</span>
<span style="color:#AA5500">                &quot;INSTALL_PACKAGES=&quot;,</span>
<span style="color:#AA5500">                &quot;PACKAGES_MIRROR=&quot;,</span>
<span style="color:#AA5500">                &quot;CONTAINER_DEBUG=0&quot;,</span>
<span style="color:#AA5500">                &quot;DISPLAY_WIDTH=1920&quot;,</span>
<span style="color:#AA5500">                &quot;DISPLAY_HEIGHT=1080&quot;,</span>
<span style="color:#AA5500">                &quot;SECURE_CONNECTION=0&quot;,</span>
<span style="color:#AA5500">                &quot;SECURE_CONNECTION_VNC_METHOD=SSL&quot;,</span>
<span style="color:#AA5500">                &quot;SECURE_CONNECTION_CERTS_CHECK_INTERVAL=60&quot;,</span>
<span style="color:#AA5500">                &quot;VNC_PASSWORD=&quot;,</span>
<span style="color:#AA5500">                &quot;ENABLE_CJK_FONT=0&quot;,</span>
<span style="color:#AA5500">                &quot;WEB_AUDIO=0&quot;,</span>
<span style="color:#AA5500">                &quot;WEB_AUTHENTICATION=0&quot;,</span>
<span style="color:#AA5500">                &quot;WEB_AUTHENTICATION_TOKEN_VALIDITY_TIME=24&quot;,</span>
<span style="color:#AA5500">                &quot;WEB_AUTHENTICATION_USERNAME=&quot;,</span>
<span style="color:#AA5500">                &quot;WEB_AUTHENTICATION_PASSWORD=&quot;,</span>
<span style="color:#AA5500">                &quot;WEB_FILE_MANAGER_ALLOWED_PATHS=AUTO&quot;,</span>
<span style="color:#AA5500">                &quot;WEB_FILE_MANAGER_DENIED_PATHS=&quot;</span>
<span style="color:#AA5500">            ],</span>
<span style="color:#AA5500">            &quot;ExposedPorts&quot;: {</span>
<span style="color:#AA5500">                &quot;5800/tcp&quot;: {},</span>
<span style="color:#AA5500">                &quot;5801/tcp&quot;: {},</span>
<span style="color:#AA5500">                &quot;5900/tcp&quot;: {}</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            &quot;Hostname&quot;: &quot;99521cd23f5e&quot;,</span>
<span style="color:#AA5500">            &quot;Image&quot;: &quot;jlesage/dupeguru&quot;,</span>
<span style="color:#AA5500">            &quot;Labels&quot;: {</span>
<span style="color:#AA5500">                &quot;org.label-schema.description&quot;: &quot;Docker container for dupeGuru&quot;,</span>
<span style="color:#AA5500">                &quot;org.label-schema.name&quot;: &quot;dupeguru&quot;,</span>
<span style="color:#AA5500">                &quot;org.label-schema.schema-version&quot;: &quot;1.0&quot;,</span>
<span style="color:#AA5500">                &quot;org.label-schema.vcs-url&quot;: &quot;https://github.com/jlesage/docker-dupeguru&quot;,</span>
<span style="color:#AA5500">                &quot;org.label-schema.version&quot;: &quot;25.07.2&quot;</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            &quot;OnBuild&quot;: null,</span>
<span style="color:#AA5500">            &quot;OpenStdin&quot;: false,</span>
<span style="color:#AA5500">            &quot;StdinOnce&quot;: false,</span>
<span style="color:#AA5500">            &quot;Tty&quot;: false,</span>
<span style="color:#AA5500">            &quot;User&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;Volumes&quot;: {</span>
<span style="color:#AA5500">                &quot;/config&quot;: {},</span>
<span style="color:#AA5500">                &quot;/storage&quot;: {},</span>
<span style="color:#AA5500">                &quot;/trash&quot;: {}</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            &quot;WorkingDir&quot;: &quot;/tmp&quot;</span>
<span style="color:#AA5500">        },</span>
<span style="color:#AA5500">        &quot;Created&quot;: &quot;2025-10-09T22:33:07.704238128Z&quot;,</span>
<span style="color:#AA5500">        &quot;Driver&quot;: &quot;overlay2&quot;,</span>
<span style="color:#AA5500">        &quot;ExecIDs&quot;: [</span>
<span style="color:#AA5500">            &quot;e5549bca9bb45793719a9adf61e815ccbae026f80bde25f1fa5c1592db29cad8&quot;</span>
<span style="color:#AA5500">        ],</span>
<span style="color:#AA5500">        &quot;GraphDriver&quot;: {</span>
<span style="color:#AA5500">            &quot;Data&quot;: {</span>
<span style="color:#AA5500">                &quot;ID&quot;: &quot;99521cd23f5e31ba8d2fa48e7508efae5f6668bef1cd5eaac483b614351fc984&quot;,</span>
<span style="color:#AA5500">                &quot;LowerDir&quot;: &quot;/var/lib/docker/overlay2/e1a21f786c2f0dc41ae02b7790f441f523cb2986f7c6c35b1593d3d524c4347c-init/diff:/var/lib/docker/overlay2/c5de5ad53081b3d2bc370531b703139b1c17c9d440de8c0a398405cd5385a0b9/diff:/var/lib/docker/overlay2/9bde606078d6f9c5b786424d7bbb4da1507ba7fb16de84b7494413250628eba4/diff:/var/lib/docker/overlay2/a57958b8c2ce3952e7b950d1155abb10b3e001cdfed097469328a12247dcc49b/diff:/var/lib/docker/overlay2/45daa012100c4b8a1e0b9c8a7e380a396ed4d868e0b46dc828c3f47042665ece/diff:/var/lib/docker/overlay2/299f69b69b8f6f8626005b56f415b52c1b5ad928233ffb6bb69d36e50774eb42/diff:/var/lib/docker/overlay2/b21683c93461405e0fe0083c5ec0ed66ed2e51871bd524c931741128125ac671/diff:/var/lib/docker/overlay2/a33551a139f502c062fc65fc72b13a0806e85050c97212ef832300ab5d17fc0a/diff:/var/lib/docker/overlay2/1d940ae7dcf07f6186af400268f6a70956356a5ff1b06272c0fd280e7681deae/diff:/var/lib/docker/overlay2/71c3945b10d5ec0d3b9074cf87d233805044987e7cc234629b68327f90782f80/diff:/var/lib/docker/overlay2/eaea86005b5ddb34dbf469e7ff96ab538d3af3f25c83f8884c33a3f07ac7736f/diff:/var/lib/docker/overlay2/26c1e8192ab8d8325c093e05b0fe00366159c1e10f1b5d2e17a718bdbe870365/diff:/var/lib/docker/overlay2/6e1034b872e7e9780850ea3ce367ab7b74df0c2400e39833034180621749f303/diff:/var/lib/docker/overlay2/b044e1eb447e594c2d10b959fdff4deb042a989c09aff027643a2ae3e9e43937/diff:/var/lib/docker/overlay2/34af5ccbdd6ad56bcc6cae86add101a69be164dd788d58867a6709f6edcf5b79/diff:/var/lib/docker/overlay2/e4ddb07933fc2d592fed740f421bb9a83fc6a770f34e3cdfa3df961b2c6c5c1b/diff:/var/lib/docker/overlay2/a60d5e613bbce09da83a41f76214ba64400e5c0c6c111205706347ad3757fe0a/diff:/var/lib/docker/overlay2/29cba5ce6497ba971437074abfaa9dd035a88a66792b255bd65a4f4c0e9c546f/diff&quot;,</span>
<span style="color:#AA5500">                &quot;MergedDir&quot;: &quot;/var/lib/docker/overlay2/e1a21f786c2f0dc41ae02b7790f441f523cb2986f7c6c35b1593d3d524c4347c/merged&quot;,</span>
<span style="color:#AA5500">                &quot;UpperDir&quot;: &quot;/var/lib/docker/overlay2/e1a21f786c2f0dc41ae02b7790f441f523cb2986f7c6c35b1593d3d524c4347c/diff&quot;,</span>
<span style="color:#AA5500">                &quot;WorkDir&quot;: &quot;/var/lib/docker/overlay2/e1a21f786c2f0dc41ae02b7790f441f523cb2986f7c6c35b1593d3d524c4347c/work&quot;</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            &quot;Name&quot;: &quot;overlay2&quot;</span>
<span style="color:#AA5500">        },</span>
<span style="color:#AA5500">        &quot;HostConfig&quot;: {</span>
<span style="color:#AA5500">            &quot;AutoRemove&quot;: false,</span>
<span style="color:#AA5500">            &quot;Binds&quot;: [</span>
<span style="color:#AA5500">                &quot;/mnt/Volume1/docker/dupeguru:/config:rw&quot;,</span>
<span style="color:#AA5500">                &quot;/mnt/Volume1/local/:/storage:rw&quot;,</span>
<span style="color:#AA5500">                &quot;/mnt/Volume1/local/TRASH:/trash:rw&quot;</span>
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
<span style="color:#AA5500">                &quot;5801/tcp&quot;: [</span>
<span style="color:#AA5500">                    {</span>
<span style="color:#AA5500">                        &quot;HostIp&quot;: &quot;0.0.0.0&quot;,</span>
<span style="color:#AA5500">                        &quot;HostPort&quot;: &quot;5801&quot;</span>
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
<span style="color:#AA5500">        &quot;HostnamePath&quot;: &quot;/var/lib/docker/containers/99521cd23f5e31ba8d2fa48e7508efae5f6668bef1cd5eaac483b614351fc984/hostname&quot;,</span>
<span style="color:#AA5500">        &quot;HostsPath&quot;: &quot;/var/lib/docker/containers/99521cd23f5e31ba8d2fa48e7508efae5f6668bef1cd5eaac483b614351fc984/hosts&quot;,</span>
<span style="color:#AA5500">        &quot;Id&quot;: &quot;99521cd23f5e31ba8d2fa48e7508efae5f6668bef1cd5eaac483b614351fc984&quot;,</span>
<span style="color:#AA5500">        &quot;Image&quot;: &quot;sha256:d144c964a6caad1a4fa89f7d0b0d57055750b12d4a9f57697b1ecdc70a088c12&quot;,</span>
<span style="color:#AA5500">        &quot;LogPath&quot;: &quot;/var/lib/docker/containers/99521cd23f5e31ba8d2fa48e7508efae5f6668bef1cd5eaac483b614351fc984/99521cd23f5e31ba8d2fa48e7508efae5f6668bef1cd5eaac483b614351fc984-json.log&quot;,</span>
<span style="color:#AA5500">        &quot;MountLabel&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">        &quot;Mounts&quot;: [</span>
<span style="color:#AA5500">            {</span>
<span style="color:#AA5500">                &quot;Destination&quot;: &quot;/config&quot;,</span>
<span style="color:#AA5500">                &quot;Mode&quot;: &quot;rw&quot;,</span>
<span style="color:#AA5500">                &quot;Propagation&quot;: &quot;rprivate&quot;,</span>
<span style="color:#AA5500">                &quot;RW&quot;: true,</span>
<span style="color:#AA5500">                &quot;Source&quot;: &quot;/mnt/Volume1/docker/dupeguru&quot;,</span>
<span style="color:#AA5500">                &quot;Type&quot;: &quot;bind&quot;</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            {</span>
<span style="color:#AA5500">                &quot;Destination&quot;: &quot;/storage&quot;,</span>
<span style="color:#AA5500">                &quot;Mode&quot;: &quot;rw&quot;,</span>
<span style="color:#AA5500">                &quot;Propagation&quot;: &quot;rprivate&quot;,</span>
<span style="color:#AA5500">                &quot;RW&quot;: true,</span>
<span style="color:#AA5500">                &quot;Source&quot;: &quot;/mnt/Volume1/local&quot;,</span>
<span style="color:#AA5500">                &quot;Type&quot;: &quot;bind&quot;</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            {</span>
<span style="color:#AA5500">                &quot;Destination&quot;: &quot;/trash&quot;,</span>
<span style="color:#AA5500">                &quot;Mode&quot;: &quot;rw&quot;,</span>
<span style="color:#AA5500">                &quot;Propagation&quot;: &quot;rprivate&quot;,</span>
<span style="color:#AA5500">                &quot;RW&quot;: true,</span>
<span style="color:#AA5500">                &quot;Source&quot;: &quot;/mnt/Volume1/local/TRASH&quot;,</span>
<span style="color:#AA5500">                &quot;Type&quot;: &quot;bind&quot;</span>
<span style="color:#AA5500">            }</span>
<span style="color:#AA5500">        ],</span>
<span style="color:#AA5500">        &quot;Name&quot;: &quot;/dupeguru&quot;,</span>
<span style="color:#AA5500">        &quot;NetworkSettings&quot;: {</span>
<span style="color:#AA5500">            &quot;Bridge&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;EndpointID&quot;: &quot;207b0da9f366e9b2840ef6c46629a51a3964aa7e121b50a2ceb7b316d1aeaeb6&quot;,</span>
<span style="color:#AA5500">            &quot;Gateway&quot;: &quot;172.17.0.1&quot;,</span>
<span style="color:#AA5500">            &quot;GlobalIPv6Address&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;GlobalIPv6PrefixLen&quot;: 0,</span>
<span style="color:#AA5500">            &quot;HairpinMode&quot;: false,</span>
<span style="color:#AA5500">            &quot;IPAddress&quot;: &quot;172.17.0.6&quot;,</span>
<span style="color:#AA5500">            &quot;IPPrefixLen&quot;: 16,</span>
<span style="color:#AA5500">            &quot;IPv6Gateway&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;LinkLocalIPv6Address&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;LinkLocalIPv6PrefixLen&quot;: 0,</span>
<span style="color:#AA5500">            &quot;MacAddress&quot;: &quot;86:80:b2:25:e5:fe&quot;,</span>
<span style="color:#AA5500">            &quot;Networks&quot;: {</span>
<span style="color:#AA5500">                &quot;bridge&quot;: {</span>
<span style="color:#AA5500">                    &quot;Aliases&quot;: null,</span>
<span style="color:#AA5500">                    &quot;DNSNames&quot;: null,</span>
<span style="color:#AA5500">                    &quot;DriverOpts&quot;: null,</span>
<span style="color:#AA5500">                    &quot;EndpointID&quot;: &quot;207b0da9f366e9b2840ef6c46629a51a3964aa7e121b50a2ceb7b316d1aeaeb6&quot;,</span>
<span style="color:#AA5500">                    &quot;Gateway&quot;: &quot;172.17.0.1&quot;,</span>
<span style="color:#AA5500">                    &quot;GlobalIPv6Address&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">                    &quot;GlobalIPv6PrefixLen&quot;: 0,</span>
<span style="color:#AA5500">                    &quot;GwPriority&quot;: 0,</span>
<span style="color:#AA5500">                    &quot;IPAMConfig&quot;: null,</span>
<span style="color:#AA5500">                    &quot;IPAddress&quot;: &quot;172.17.0.6&quot;,</span>
<span style="color:#AA5500">                    &quot;IPPrefixLen&quot;: 16,</span>
<span style="color:#AA5500">                    &quot;IPv6Gateway&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">                    &quot;Links&quot;: null,</span>
<span style="color:#AA5500">                    &quot;MacAddress&quot;: &quot;86:80:b2:25:e5:fe&quot;,</span>
<span style="color:#AA5500">                    &quot;NetworkID&quot;: &quot;fce42755ebf1352d21e037493e0c33a917b08a8fe5d9ea19e3af1d873ab69e67&quot;</span>
<span style="color:#AA5500">                }</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            &quot;Ports&quot;: {</span>
<span style="color:#AA5500">                &quot;5800/tcp&quot;: null,</span>
<span style="color:#AA5500">                &quot;5801/tcp&quot;: [</span>
<span style="color:#AA5500">                    {</span>
<span style="color:#AA5500">                        &quot;HostIp&quot;: &quot;0.0.0.0&quot;,</span>
<span style="color:#AA5500">                        &quot;HostPort&quot;: &quot;5801&quot;</span>
<span style="color:#AA5500">                    }</span>
<span style="color:#AA5500">                ],</span>
<span style="color:#AA5500">                &quot;5900/tcp&quot;: null</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            &quot;SandboxID&quot;: &quot;7e08e21d83a8369c6c5c5875adb0ba445d92693059e3a87cee50b379d12751e2&quot;,</span>
<span style="color:#AA5500">            &quot;SandboxKey&quot;: &quot;/var/run/docker/netns/7e08e21d83a8&quot;,</span>
<span style="color:#AA5500">            &quot;SecondaryIPAddresses&quot;: null,</span>
<span style="color:#AA5500">            &quot;SecondaryIPv6Addresses&quot;: null</span>
<span style="color:#AA5500">        },</span>
<span style="color:#AA5500">        &quot;Path&quot;: &quot;/init&quot;,</span>
<span style="color:#AA5500">        &quot;Platform&quot;: &quot;linux&quot;,</span>
<span style="color:#AA5500">        &quot;ProcessLabel&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">        &quot;ResolvConfPath&quot;: &quot;/var/lib/docker/containers/99521cd23f5e31ba8d2fa48e7508efae5f6668bef1cd5eaac483b614351fc984/resolv.conf&quot;,</span>
<span style="color:#AA5500">        &quot;RestartCount&quot;: 0,</span>
<span style="color:#AA5500">        &quot;State&quot;: {</span>
<span style="color:#AA5500">            &quot;Dead&quot;: false,</span>
<span style="color:#AA5500">            &quot;Error&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;ExitCode&quot;: 0,</span>
<span style="color:#AA5500">            &quot;FinishedAt&quot;: &quot;2025-10-10T04:02:48.336333751Z&quot;,</span>
<span style="color:#AA5500">            &quot;OOMKilled&quot;: false,</span>
<span style="color:#AA5500">            &quot;Paused&quot;: false,</span>
<span style="color:#AA5500">            &quot;Pid&quot;: 2127038,</span>
<span style="color:#AA5500">            &quot;Restarting&quot;: false,</span>
<span style="color:#AA5500">            &quot;Running&quot;: true,</span>
<span style="color:#AA5500">            &quot;StartedAt&quot;: &quot;2025-10-10T04:02:54.028098348Z&quot;,</span>
<span style="color:#AA5500">            &quot;Status&quot;: &quot;running&quot;</span>
<span style="color:#AA5500">        }</span>
<span style="color:#AA5500">    }</span>
<span style="color:#AA5500">}</span>
Freitag 10 Oktober 2025  23:17:51 +0200 (0:00:01.910)       0:01:15.855 ******* 
Freitag 10 Oktober 2025  23:17:51 +0200 (0:00:00.075)       0:01:15.931 ******* 
Freitag 10 Oktober 2025  23:17:51 +0200 (0:00:00.058)       0:01:15.989 ******* 
Freitag 10 Oktober 2025  23:17:51 +0200 (0:00:00.047)       0:01:16.037 ******* 

TASK [duplicacy : Stop Duplicacy] *********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/duplicacy/tasks/main.yml:44</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:17:51 +0200 (0:00:00.638)       0:01:16.675 ******* 
Freitag 10 Oktober 2025  23:17:51 +0200 (0:00:00.060)       0:01:16.736 ******* 
Freitag 10 Oktober 2025  23:17:51 +0200 (0:00:00.044)       0:01:16.781 ******* 

TASK [duplicati : Stop Duplicati] *********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/duplicati/tasks/main.yml:40</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:17:52 +0200 (0:00:00.633)       0:01:17.414 ******* 
Freitag 10 Oktober 2025  23:17:52 +0200 (0:00:00.147)       0:01:17.561 ******* 
Freitag 10 Oktober 2025  23:17:52 +0200 (0:00:00.045)       0:01:17.607 ******* 

TASK [emby : Stop Emby] *******************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/emby/tasks/main.yml:41</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:17:53 +0200 (0:00:00.623)       0:01:18.231 ******* 
Freitag 10 Oktober 2025  23:17:53 +0200 (0:00:00.059)       0:01:18.290 ******* 
Freitag 10 Oktober 2025  23:17:53 +0200 (0:00:00.046)       0:01:18.336 ******* 

TASK [esphome : Stop EspHome] *************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/esphome/tasks/main.yml:38</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:17:54 +0200 (0:00:00.642)       0:01:18.979 ******* 
Freitag 10 Oktober 2025  23:17:54 +0200 (0:00:00.059)       0:01:19.038 ******* 
Freitag 10 Oktober 2025  23:17:54 +0200 (0:00:00.045)       0:01:19.084 ******* 
Freitag 10 Oktober 2025  23:17:54 +0200 (0:00:00.051)       0:01:19.135 ******* 
Freitag 10 Oktober 2025  23:17:54 +0200 (0:00:00.043)       0:01:19.178 ******* 

TASK [firefly : Stop Firefly] *************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/firefly/tasks/main.yml:68</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:17:55 +0200 (0:00:00.631)       0:01:19.810 ******* 

TASK [firefly : Stop Firefly MySQL] *******************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/firefly/tasks/main.yml:73</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:17:55 +0200 (0:00:00.638)       0:01:20.449 ******* 
Freitag 10 Oktober 2025  23:17:55 +0200 (0:00:00.049)       0:01:20.499 ******* 
Freitag 10 Oktober 2025  23:17:55 +0200 (0:00:00.147)       0:01:20.646 ******* 

TASK [flaresolverr : Stop FlareSolverr] ***************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/flaresolverr/tasks/main.yml:35</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:17:56 +0200 (0:00:00.608)       0:01:21.255 ******* 

TASK [freshrss : Create FreshRSS Directories] *********************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/freshrss/tasks/main.yml:4</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; (item=/mnt/Volume1/docker/freshrss/data) =&gt; {</span>
<span style="color:#00AA00">    &quot;ansible_loop_var&quot;: &quot;item&quot;,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;gid&quot;: 33,</span>
<span style="color:#00AA00">    &quot;group&quot;: &quot;www-data&quot;,</span>
<span style="color:#00AA00">    &quot;item&quot;: &quot;/mnt/Volume1/docker/freshrss/data&quot;,</span>
<span style="color:#00AA00">    &quot;mode&quot;: &quot;0777&quot;,</span>
<span style="color:#00AA00">    &quot;owner&quot;: &quot;1001&quot;,</span>
<span style="color:#00AA00">    &quot;path&quot;: &quot;/mnt/Volume1/docker/freshrss/data&quot;,</span>
<span style="color:#00AA00">    &quot;size&quot;: 4096,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;directory&quot;,</span>
<span style="color:#00AA00">    &quot;uid&quot;: 1001</span>
<span style="color:#00AA00">}</span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; (item=/mnt/Volume1/docker/freshrss/extensions) =&gt; {</span>
<span style="color:#00AA00">    &quot;ansible_loop_var&quot;: &quot;item&quot;,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;gid&quot;: 33,</span>
<span style="color:#00AA00">    &quot;group&quot;: &quot;www-data&quot;,</span>
<span style="color:#00AA00">    &quot;item&quot;: &quot;/mnt/Volume1/docker/freshrss/extensions&quot;,</span>
<span style="color:#00AA00">    &quot;mode&quot;: &quot;0777&quot;,</span>
<span style="color:#00AA00">    &quot;owner&quot;: &quot;1001&quot;,</span>
<span style="color:#00AA00">    &quot;path&quot;: &quot;/mnt/Volume1/docker/freshrss/extensions&quot;,</span>
<span style="color:#00AA00">    &quot;size&quot;: 4096,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;directory&quot;,</span>
<span style="color:#00AA00">    &quot;uid&quot;: 1001</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:17:57 +0200 (0:00:00.744)       0:01:22.000 ******* 

TASK [freshrss : FreshRSS Docker Container] ***********************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/freshrss/tasks/main.yml:12</b></span>
<span style="color:#AA5500">changed: [ansible-nas] =&gt; {</span>
<span style="color:#AA5500">    &quot;changed&quot;: true,</span>
<span style="color:#AA5500">    &quot;container&quot;: {</span>
<span style="color:#AA5500">        &quot;AppArmorProfile&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">        &quot;Args&quot;: [</span>
<span style="color:#AA5500">            &quot;/bin/bash&quot;,</span>
<span style="color:#AA5500">            &quot;-o&quot;,</span>
<span style="color:#AA5500">            &quot;pipefail&quot;,</span>
<span style="color:#AA5500">            &quot;-c&quot;,</span>
<span style="color:#AA5500">            &quot;([ -z \&quot;$CRON_MIN\&quot; ] || cron) &amp;&amp; \t. /etc/apache2/envvars &amp;&amp; \texec apache2 -D FOREGROUND $([ -n \&quot;$OIDC_ENABLED\&quot; ] &amp;&amp; [ \&quot;$OIDC_ENABLED\&quot; -ne 0 ] &amp;&amp; echo \&quot;-D OIDC_ENABLED\&quot;)&quot;</span>
<span style="color:#AA5500">        ],</span>
<span style="color:#AA5500">        &quot;Config&quot;: {</span>
<span style="color:#AA5500">            &quot;AttachStderr&quot;: true,</span>
<span style="color:#AA5500">            &quot;AttachStdin&quot;: false,</span>
<span style="color:#AA5500">            &quot;AttachStdout&quot;: true,</span>
<span style="color:#AA5500">            &quot;Cmd&quot;: [</span>
<span style="color:#AA5500">                &quot;/bin/bash&quot;,</span>
<span style="color:#AA5500">                &quot;-o&quot;,</span>
<span style="color:#AA5500">                &quot;pipefail&quot;,</span>
<span style="color:#AA5500">                &quot;-c&quot;,</span>
<span style="color:#AA5500">                &quot;([ -z \&quot;$CRON_MIN\&quot; ] || cron) &amp;&amp; \t. /etc/apache2/envvars &amp;&amp; \texec apache2 -D FOREGROUND $([ -n \&quot;$OIDC_ENABLED\&quot; ] &amp;&amp; [ \&quot;$OIDC_ENABLED\&quot; -ne 0 ] &amp;&amp; echo \&quot;-D OIDC_ENABLED\&quot;)&quot;</span>
<span style="color:#AA5500">            ],</span>
<span style="color:#AA5500">            &quot;Domainname&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;Entrypoint&quot;: [</span>
<span style="color:#AA5500">                &quot;./Docker/entrypoint.sh&quot;</span>
<span style="color:#AA5500">            ],</span>
<span style="color:#AA5500">            &quot;Env&quot;: [</span>
<span style="color:#AA5500">                &quot;TZ=Europe/Berlin&quot;,</span>
<span style="color:#AA5500">                &quot;CRON_MIN=1,31&quot;,</span>
<span style="color:#AA5500">                &quot;PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin&quot;,</span>
<span style="color:#AA5500">                &quot;COPY_LOG_TO_SYSLOG=On&quot;,</span>
<span style="color:#AA5500">                &quot;COPY_SYSLOG_TO_STDERR=On&quot;,</span>
<span style="color:#AA5500">                &quot;DATA_PATH=&quot;,</span>
<span style="color:#AA5500">                &quot;FRESHRSS_ENV=&quot;,</span>
<span style="color:#AA5500">                &quot;LISTEN=&quot;,</span>
<span style="color:#AA5500">                &quot;OIDC_ENABLED=&quot;,</span>
<span style="color:#AA5500">                &quot;TRUSTED_PROXY=&quot;</span>
<span style="color:#AA5500">            ],</span>
<span style="color:#AA5500">            &quot;ExposedPorts&quot;: {</span>
<span style="color:#AA5500">                &quot;80/tcp&quot;: {}</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            &quot;Hostname&quot;: &quot;727f6885d9e8&quot;,</span>
<span style="color:#AA5500">            &quot;Image&quot;: &quot;freshrss/freshrss:latest&quot;,</span>
<span style="color:#AA5500">            &quot;Labels&quot;: {</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.authors&quot;: &quot;Alkarex&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.created&quot;: &quot;2025-09-27T13:07:48.547Z&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.description&quot;: &quot;A free, self-hostable news aggregator…&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.documentation&quot;: &quot;https://freshrss.github.io/FreshRSS/&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.licenses&quot;: &quot;AGPL-3.0&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.revision&quot;: &quot;3f9b7b333102fed5803d06b2366250860a9314c5&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.source&quot;: &quot;https://github.com/FreshRSS/FreshRSS&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.title&quot;: &quot;FreshRSS&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.url&quot;: &quot;https://freshrss.org/&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.vendor&quot;: &quot;FreshRSS&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.version&quot;: &quot;1.27.1&quot;,</span>
<span style="color:#AA5500">                &quot;traefik.enable&quot;: &quot;False&quot;,</span>
<span style="color:#AA5500">                &quot;traefik.http.routers.freshrss.rule&quot;: &quot;Host(`freshrss.Schneider.nbg`)&quot;,</span>
<span style="color:#AA5500">                &quot;traefik.http.routers.freshrss.tls.certresolver&quot;: &quot;letsencrypt&quot;,</span>
<span style="color:#AA5500">                &quot;traefik.http.routers.freshrss.tls.domains[0].main&quot;: &quot;Schneider.nbg&quot;,</span>
<span style="color:#AA5500">                &quot;traefik.http.routers.freshrss.tls.domains[0].sans&quot;: &quot;*.Schneider.nbg&quot;,</span>
<span style="color:#AA5500">                &quot;traefik.http.services.freshrss.loadbalancer.server.port&quot;: &quot;80&quot;</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            &quot;OnBuild&quot;: null,</span>
<span style="color:#AA5500">            &quot;OpenStdin&quot;: false,</span>
<span style="color:#AA5500">            &quot;StdinOnce&quot;: false,</span>
<span style="color:#AA5500">            &quot;Tty&quot;: false,</span>
<span style="color:#AA5500">            &quot;User&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;Volumes&quot;: null,</span>
<span style="color:#AA5500">            &quot;WorkingDir&quot;: &quot;/var/www/FreshRSS&quot;</span>
<span style="color:#AA5500">        },</span>
<span style="color:#AA5500">        &quot;Created&quot;: &quot;2025-10-01T21:46:06.680260503Z&quot;,</span>
<span style="color:#AA5500">        &quot;Driver&quot;: &quot;overlay2&quot;,</span>
<span style="color:#AA5500">        &quot;ExecIDs&quot;: null,</span>
<span style="color:#AA5500">        &quot;GraphDriver&quot;: {</span>
<span style="color:#AA5500">            &quot;Data&quot;: {</span>
<span style="color:#AA5500">                &quot;ID&quot;: &quot;727f6885d9e80e92532fefc0305e2fb5059e79869ea29e3675ae7ab36f2874fd&quot;,</span>
<span style="color:#AA5500">                &quot;LowerDir&quot;: &quot;/var/lib/docker/overlay2/0364958b3f8ddf7402ab3201d89739fdc97c3db7e720cb123fa7a2d55b6c3e87-init/diff:/var/lib/docker/overlay2/6c92a2ad0087667573f3c481bfeb5454b95998b656995e77259f66a04d075677/diff:/var/lib/docker/overlay2/e71293c59ec9118fce8cff9c1bfde7ecef2cae3063f79af16555a2f742cb9fed/diff:/var/lib/docker/overlay2/5d271a879c955ef75f1b5747ac119fe44c3c35352437fc43dd74d496f057b90b/diff:/var/lib/docker/overlay2/80a96465e569b42e2bec496078a05bd2dea33aa3225e477571e27ac2ec1b3fae/diff:/var/lib/docker/overlay2/8e9524581a3f0722c5294a054e2fb5ec60b8d0234ff9f0736f7e92eab1f5a40b/diff:/var/lib/docker/overlay2/59e596e72ab38edb757ee12311b90f96a6e7ebaa497ceb30f66d0d07ab03fc0e/diff:/var/lib/docker/overlay2/0f641d20cec488e0a9544e7f2e9bb61ac0cb0f8c03fd477b45c0b08d3ce9115b/diff:/var/lib/docker/overlay2/1657a032120bfeccce89c4ca6de69f8f09f59e4bcdb053a5aeb5647c49e41064/diff&quot;,</span>
<span style="color:#AA5500">                &quot;MergedDir&quot;: &quot;/var/lib/docker/overlay2/0364958b3f8ddf7402ab3201d89739fdc97c3db7e720cb123fa7a2d55b6c3e87/merged&quot;,</span>
<span style="color:#AA5500">                &quot;UpperDir&quot;: &quot;/var/lib/docker/overlay2/0364958b3f8ddf7402ab3201d89739fdc97c3db7e720cb123fa7a2d55b6c3e87/diff&quot;,</span>
<span style="color:#AA5500">                &quot;WorkDir&quot;: &quot;/var/lib/docker/overlay2/0364958b3f8ddf7402ab3201d89739fdc97c3db7e720cb123fa7a2d55b6c3e87/work&quot;</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            &quot;Name&quot;: &quot;overlay2&quot;</span>
<span style="color:#AA5500">        },</span>
<span style="color:#AA5500">        &quot;HostConfig&quot;: {</span>
<span style="color:#AA5500">            &quot;AutoRemove&quot;: false,</span>
<span style="color:#AA5500">            &quot;Binds&quot;: [</span>
<span style="color:#AA5500">                &quot;/mnt/Volume1/docker/freshrss/data:/var/www/FreshRSS/data:rw&quot;,</span>
<span style="color:#AA5500">                &quot;/mnt/Volume1/docker/freshrss/extensions:/var/www/FreshRSS/extensions:rw&quot;</span>
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
<span style="color:#AA5500">                &quot;80/tcp&quot;: [</span>
<span style="color:#AA5500">                    {</span>
<span style="color:#AA5500">                        &quot;HostIp&quot;: &quot;0.0.0.0&quot;,</span>
<span style="color:#AA5500">                        &quot;HostPort&quot;: &quot;8089&quot;</span>
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
<span style="color:#AA5500">        &quot;HostnamePath&quot;: &quot;/var/lib/docker/containers/727f6885d9e80e92532fefc0305e2fb5059e79869ea29e3675ae7ab36f2874fd/hostname&quot;,</span>
<span style="color:#AA5500">        &quot;HostsPath&quot;: &quot;/var/lib/docker/containers/727f6885d9e80e92532fefc0305e2fb5059e79869ea29e3675ae7ab36f2874fd/hosts&quot;,</span>
<span style="color:#AA5500">        &quot;Id&quot;: &quot;727f6885d9e80e92532fefc0305e2fb5059e79869ea29e3675ae7ab36f2874fd&quot;,</span>
<span style="color:#AA5500">        &quot;Image&quot;: &quot;sha256:2a63b3605b7a9a0fccb0dfafdd646c47f6f56feb52f64549c022ea0b13e284da&quot;,</span>
<span style="color:#AA5500">        &quot;LogPath&quot;: &quot;/var/lib/docker/containers/727f6885d9e80e92532fefc0305e2fb5059e79869ea29e3675ae7ab36f2874fd/727f6885d9e80e92532fefc0305e2fb5059e79869ea29e3675ae7ab36f2874fd-json.log&quot;,</span>
<span style="color:#AA5500">        &quot;MountLabel&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">        &quot;Mounts&quot;: [</span>
<span style="color:#AA5500">            {</span>
<span style="color:#AA5500">                &quot;Destination&quot;: &quot;/var/www/FreshRSS/data&quot;,</span>
<span style="color:#AA5500">                &quot;Mode&quot;: &quot;rw&quot;,</span>
<span style="color:#AA5500">                &quot;Propagation&quot;: &quot;rprivate&quot;,</span>
<span style="color:#AA5500">                &quot;RW&quot;: true,</span>
<span style="color:#AA5500">                &quot;Source&quot;: &quot;/mnt/Volume1/docker/freshrss/data&quot;,</span>
<span style="color:#AA5500">                &quot;Type&quot;: &quot;bind&quot;</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            {</span>
<span style="color:#AA5500">                &quot;Destination&quot;: &quot;/var/www/FreshRSS/extensions&quot;,</span>
<span style="color:#AA5500">                &quot;Mode&quot;: &quot;rw&quot;,</span>
<span style="color:#AA5500">                &quot;Propagation&quot;: &quot;rprivate&quot;,</span>
<span style="color:#AA5500">                &quot;RW&quot;: true,</span>
<span style="color:#AA5500">                &quot;Source&quot;: &quot;/mnt/Volume1/docker/freshrss/extensions&quot;,</span>
<span style="color:#AA5500">                &quot;Type&quot;: &quot;bind&quot;</span>
<span style="color:#AA5500">            }</span>
<span style="color:#AA5500">        ],</span>
<span style="color:#AA5500">        &quot;Name&quot;: &quot;/freshrss&quot;,</span>
<span style="color:#AA5500">        &quot;NetworkSettings&quot;: {</span>
<span style="color:#AA5500">            &quot;Bridge&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;EndpointID&quot;: &quot;ced803a60128bfce3398d32d8b6821d7bfa32000c39fe24c55f5b9126236ac0b&quot;,</span>
<span style="color:#AA5500">            &quot;Gateway&quot;: &quot;172.17.0.1&quot;,</span>
<span style="color:#AA5500">            &quot;GlobalIPv6Address&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;GlobalIPv6PrefixLen&quot;: 0,</span>
<span style="color:#AA5500">            &quot;HairpinMode&quot;: false,</span>
<span style="color:#AA5500">            &quot;IPAddress&quot;: &quot;172.17.0.3&quot;,</span>
<span style="color:#AA5500">            &quot;IPPrefixLen&quot;: 16,</span>
<span style="color:#AA5500">            &quot;IPv6Gateway&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;LinkLocalIPv6Address&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;LinkLocalIPv6PrefixLen&quot;: 0,</span>
<span style="color:#AA5500">            &quot;MacAddress&quot;: &quot;9a:2f:49:a7:8a:0a&quot;,</span>
<span style="color:#AA5500">            &quot;Networks&quot;: {</span>
<span style="color:#AA5500">                &quot;bridge&quot;: {</span>
<span style="color:#AA5500">                    &quot;Aliases&quot;: null,</span>
<span style="color:#AA5500">                    &quot;DNSNames&quot;: null,</span>
<span style="color:#AA5500">                    &quot;DriverOpts&quot;: null,</span>
<span style="color:#AA5500">                    &quot;EndpointID&quot;: &quot;ced803a60128bfce3398d32d8b6821d7bfa32000c39fe24c55f5b9126236ac0b&quot;,</span>
<span style="color:#AA5500">                    &quot;Gateway&quot;: &quot;172.17.0.1&quot;,</span>
<span style="color:#AA5500">                    &quot;GlobalIPv6Address&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">                    &quot;GlobalIPv6PrefixLen&quot;: 0,</span>
<span style="color:#AA5500">                    &quot;GwPriority&quot;: 0,</span>
<span style="color:#AA5500">                    &quot;IPAMConfig&quot;: null,</span>
<span style="color:#AA5500">                    &quot;IPAddress&quot;: &quot;172.17.0.3&quot;,</span>
<span style="color:#AA5500">                    &quot;IPPrefixLen&quot;: 16,</span>
<span style="color:#AA5500">                    &quot;IPv6Gateway&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">                    &quot;Links&quot;: null,</span>
<span style="color:#AA5500">                    &quot;MacAddress&quot;: &quot;9a:2f:49:a7:8a:0a&quot;,</span>
<span style="color:#AA5500">                    &quot;NetworkID&quot;: &quot;fce42755ebf1352d21e037493e0c33a917b08a8fe5d9ea19e3af1d873ab69e67&quot;</span>
<span style="color:#AA5500">                }</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            &quot;Ports&quot;: {</span>
<span style="color:#AA5500">                &quot;80/tcp&quot;: [</span>
<span style="color:#AA5500">                    {</span>
<span style="color:#AA5500">                        &quot;HostIp&quot;: &quot;0.0.0.0&quot;,</span>
<span style="color:#AA5500">                        &quot;HostPort&quot;: &quot;8089&quot;</span>
<span style="color:#AA5500">                    }</span>
<span style="color:#AA5500">                ]</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            &quot;SandboxID&quot;: &quot;17d81fa1dbbe40bb0f5b68dd8b679457f3a95da2080707bc26adfd65ebcb8ced&quot;,</span>
<span style="color:#AA5500">            &quot;SandboxKey&quot;: &quot;/var/run/docker/netns/17d81fa1dbbe&quot;,</span>
<span style="color:#AA5500">            &quot;SecondaryIPAddresses&quot;: null,</span>
<span style="color:#AA5500">            &quot;SecondaryIPv6Addresses&quot;: null</span>
<span style="color:#AA5500">        },</span>
<span style="color:#AA5500">        &quot;Path&quot;: &quot;./Docker/entrypoint.sh&quot;,</span>
<span style="color:#AA5500">        &quot;Platform&quot;: &quot;linux&quot;,</span>
<span style="color:#AA5500">        &quot;ProcessLabel&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">        &quot;ResolvConfPath&quot;: &quot;/var/lib/docker/containers/727f6885d9e80e92532fefc0305e2fb5059e79869ea29e3675ae7ab36f2874fd/resolv.conf&quot;,</span>
<span style="color:#AA5500">        &quot;RestartCount&quot;: 0,</span>
<span style="color:#AA5500">        &quot;State&quot;: {</span>
<span style="color:#AA5500">            &quot;Dead&quot;: false,</span>
<span style="color:#AA5500">            &quot;Error&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;ExitCode&quot;: 0,</span>
<span style="color:#AA5500">            &quot;FinishedAt&quot;: &quot;2025-10-10T04:02:46.251390003Z&quot;,</span>
<span style="color:#AA5500">            &quot;OOMKilled&quot;: false,</span>
<span style="color:#AA5500">            &quot;Paused&quot;: false,</span>
<span style="color:#AA5500">            &quot;Pid&quot;: 2126785,</span>
<span style="color:#AA5500">            &quot;Restarting&quot;: false,</span>
<span style="color:#AA5500">            &quot;Running&quot;: true,</span>
<span style="color:#AA5500">            &quot;StartedAt&quot;: &quot;2025-10-10T04:02:53.972734096Z&quot;,</span>
<span style="color:#AA5500">            &quot;Status&quot;: &quot;running&quot;</span>
<span style="color:#AA5500">        }</span>
<span style="color:#AA5500">    }</span>
<span style="color:#AA5500">}</span>
Freitag 10 Oktober 2025  23:17:59 +0200 (0:00:01.816)       0:01:23.817 ******* 
Freitag 10 Oktober 2025  23:17:59 +0200 (0:00:00.068)       0:01:23.885 ******* 
Freitag 10 Oktober 2025  23:17:59 +0200 (0:00:00.054)       0:01:23.940 ******* 
Freitag 10 Oktober 2025  23:17:59 +0200 (0:00:00.041)       0:01:23.981 ******* 

TASK [get_iplayer : Stop get_iplayer] *****************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/get_iplayer/tasks/main.yml:28</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:17:59 +0200 (0:00:00.665)       0:01:24.647 ******* 
Freitag 10 Oktober 2025  23:17:59 +0200 (0:00:00.057)       0:01:24.704 ******* 
Freitag 10 Oktober 2025  23:17:59 +0200 (0:00:00.050)       0:01:24.755 ******* 
Freitag 10 Oktober 2025  23:18:00 +0200 (0:00:00.057)       0:01:24.812 ******* 

TASK [gitea : Stop Gitea] *****************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/gitea/tasks/main.yml:65</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:18:00 +0200 (0:00:00.629)       0:01:25.442 ******* 

TASK [gitea : Stop Gitea Mysql] ***********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/gitea/tasks/main.yml:70</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:18:01 +0200 (0:00:00.603)       0:01:26.045 ******* 
Freitag 10 Oktober 2025  23:18:01 +0200 (0:00:00.141)       0:01:26.187 ******* 
Freitag 10 Oktober 2025  23:18:01 +0200 (0:00:00.045)       0:01:26.233 ******* 
Freitag 10 Oktober 2025  23:18:01 +0200 (0:00:00.057)       0:01:26.290 ******* 
Freitag 10 Oktober 2025  23:18:01 +0200 (0:00:00.044)       0:01:26.335 ******* 

TASK [gitlab : Stop Gitlab] ***************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/gitlab/tasks/main.yml:64</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:18:02 +0200 (0:00:00.621)       0:01:26.957 ******* 

TASK [glances : Create Glances Docker Container] ******************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/glances/tasks/main.yml:4</b></span>
<span style="color:#AA5500">changed: [ansible-nas] =&gt; {</span>
<span style="color:#AA5500">    &quot;changed&quot;: true,</span>
<span style="color:#AA5500">    &quot;container&quot;: {</span>
<span style="color:#AA5500">        &quot;AppArmorProfile&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">        &quot;Args&quot;: [</span>
<span style="color:#AA5500">            &quot;-c&quot;,</span>
<span style="color:#AA5500">            &quot;/venv/bin/python3 -m glances ${GLANCES_OPT}&quot;</span>
<span style="color:#AA5500">        ],</span>
<span style="color:#AA5500">        &quot;Config&quot;: {</span>
<span style="color:#AA5500">            &quot;AttachStderr&quot;: true,</span>
<span style="color:#AA5500">            &quot;AttachStdin&quot;: false,</span>
<span style="color:#AA5500">            &quot;AttachStdout&quot;: true,</span>
<span style="color:#AA5500">            &quot;Cmd&quot;: [</span>
<span style="color:#AA5500">                &quot;/bin/sh&quot;,</span>
<span style="color:#AA5500">                &quot;-c&quot;,</span>
<span style="color:#AA5500">                &quot;/venv/bin/python3 -m glances ${GLANCES_OPT}&quot;</span>
<span style="color:#AA5500">            ],</span>
<span style="color:#AA5500">            &quot;Domainname&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;Entrypoint&quot;: null,</span>
<span style="color:#AA5500">            &quot;Env&quot;: [</span>
<span style="color:#AA5500">                &quot;GLANCES_OPT=-w&quot;,</span>
<span style="color:#AA5500">                &quot;PATH=/venv/bin:/venv/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin&quot;</span>
<span style="color:#AA5500">            ],</span>
<span style="color:#AA5500">            &quot;ExposedPorts&quot;: {</span>
<span style="color:#AA5500">                &quot;61208/tcp&quot;: {},</span>
<span style="color:#AA5500">                &quot;61209/tcp&quot;: {}</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            &quot;Hostname&quot;: &quot;58ca8645c34f&quot;,</span>
<span style="color:#AA5500">            &quot;Image&quot;: &quot;nicolargo/glances:latest&quot;,</span>
<span style="color:#AA5500">            &quot;Labels&quot;: {</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.created&quot;: &quot;2025-07-09T15:40:20.057Z&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.description&quot;: &quot;Glances an Eye on your system. A top/htop alternative for GNU/Linux, BSD, Mac OS and Windows operating systems.&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.licenses&quot;: &quot;NOASSERTION&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.revision&quot;: &quot;73a01d4c52540bd547d478c5d9e4d4a1d38b9cbc&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.source&quot;: &quot;https://github.com/nicolargo/glances&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.title&quot;: &quot;glances&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.url&quot;: &quot;https://nicolargo.github.io/glances/&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.version&quot;: &quot;master&quot;,</span>
<span style="color:#AA5500">                &quot;traefik.enable&quot;: &quot;False&quot;,</span>
<span style="color:#AA5500">                &quot;traefik.http.routers.glances.rule&quot;: &quot;Host(`glances.Schneider.nbg`)&quot;,</span>
<span style="color:#AA5500">                &quot;traefik.http.routers.glances.tls.certresolver&quot;: &quot;letsencrypt&quot;,</span>
<span style="color:#AA5500">                &quot;traefik.http.routers.glances.tls.domains[0].main&quot;: &quot;Schneider.nbg&quot;,</span>
<span style="color:#AA5500">                &quot;traefik.http.routers.glances.tls.domains[0].sans&quot;: &quot;*.Schneider.nbg&quot;,</span>
<span style="color:#AA5500">                &quot;traefik.http.services.glances.loadbalancer.server.port&quot;: &quot;61208&quot;</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            &quot;OnBuild&quot;: null,</span>
<span style="color:#AA5500">            &quot;OpenStdin&quot;: false,</span>
<span style="color:#AA5500">            &quot;StdinOnce&quot;: false,</span>
<span style="color:#AA5500">            &quot;Tty&quot;: false,</span>
<span style="color:#AA5500">            &quot;User&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;Volumes&quot;: null,</span>
<span style="color:#AA5500">            &quot;WorkingDir&quot;: &quot;/app&quot;</span>
<span style="color:#AA5500">        },</span>
<span style="color:#AA5500">        &quot;Created&quot;: &quot;2025-10-10T03:05:36.866497248Z&quot;,</span>
<span style="color:#AA5500">        &quot;Driver&quot;: &quot;overlay2&quot;,</span>
<span style="color:#AA5500">        &quot;ExecIDs&quot;: null,</span>
<span style="color:#AA5500">        &quot;GraphDriver&quot;: {</span>
<span style="color:#AA5500">            &quot;Data&quot;: {</span>
<span style="color:#AA5500">                &quot;ID&quot;: &quot;58ca8645c34f101200091f978c8d05332586f8eada21e92f79fafacdebba2b6d&quot;,</span>
<span style="color:#AA5500">                &quot;LowerDir&quot;: &quot;/var/lib/docker/overlay2/72a13646ed564a4195c451861263bfde76baaebd426ebc5499f5ed7eed514e3f-init/diff:/var/lib/docker/overlay2/c30630e04f3c8fb91d0d239197ab9cb477224dd52abd95edca041b88482fd1e1/diff:/var/lib/docker/overlay2/98b2d4dc2f80db8c9edd8a8685cb4d38c7383ebc097e733934883e70d9e5c805/diff:/var/lib/docker/overlay2/a633aa47c8028dc84d5435d95918598d91ecb36bb0bfd79297d7067e60aa57c8/diff:/var/lib/docker/overlay2/98d25478a0dbc4b1e59ef6844ae88758c39f1634a922fd59f4467db1477f2e9c/diff:/var/lib/docker/overlay2/496cccbc35364e6a5b48d0866530a7154698ba877cfa97d10984f966ffc1574d/diff:/var/lib/docker/overlay2/b946e73fb4277d6c5b2e124561d7ebbed439cc708aeb64e106482846562238d5/diff:/var/lib/docker/overlay2/3d84e89c702522affae16dbc1204125ed165cb9823a375dacf8d68efcb7509b2/diff:/var/lib/docker/overlay2/1e0233936300ab3dd879dc6d0c0a5c785c34a04dfb5e500e262c1dc45b5457f8/diff:/var/lib/docker/overlay2/37c2e92b7f49fce432fd8b4dd2130f3e51ac936a6eb0d5562da9d339159fb24b/diff:/var/lib/docker/overlay2/cb06c6b85247bbde28c86b30d8f690b6f2a1fe091d3961fc2827658e04277ef7/diff:/var/lib/docker/overlay2/f0691f08049b90bbc43f3fb16a0ddaf37b96b32fd415a2e5a1d57801508c8825/diff&quot;,</span>
<span style="color:#AA5500">                &quot;MergedDir&quot;: &quot;/var/lib/docker/overlay2/72a13646ed564a4195c451861263bfde76baaebd426ebc5499f5ed7eed514e3f/merged&quot;,</span>
<span style="color:#AA5500">                &quot;UpperDir&quot;: &quot;/var/lib/docker/overlay2/72a13646ed564a4195c451861263bfde76baaebd426ebc5499f5ed7eed514e3f/diff&quot;,</span>
<span style="color:#AA5500">                &quot;WorkDir&quot;: &quot;/var/lib/docker/overlay2/72a13646ed564a4195c451861263bfde76baaebd426ebc5499f5ed7eed514e3f/work&quot;</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            &quot;Name&quot;: &quot;overlay2&quot;</span>
<span style="color:#AA5500">        },</span>
<span style="color:#AA5500">        &quot;HostConfig&quot;: {</span>
<span style="color:#AA5500">            &quot;AutoRemove&quot;: false,</span>
<span style="color:#AA5500">            &quot;Binds&quot;: [</span>
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
<span style="color:#AA5500">            &quot;PidMode&quot;: &quot;host&quot;,</span>
<span style="color:#AA5500">            &quot;PidsLimit&quot;: null,</span>
<span style="color:#AA5500">            &quot;PortBindings&quot;: {</span>
<span style="color:#AA5500">                &quot;61208/tcp&quot;: [</span>
<span style="color:#AA5500">                    {</span>
<span style="color:#AA5500">                        &quot;HostIp&quot;: &quot;0.0.0.0&quot;,</span>
<span style="color:#AA5500">                        &quot;HostPort&quot;: &quot;61208&quot;</span>
<span style="color:#AA5500">                    }</span>
<span style="color:#AA5500">                ],</span>
<span style="color:#AA5500">                &quot;61209/tcp&quot;: [</span>
<span style="color:#AA5500">                    {</span>
<span style="color:#AA5500">                        &quot;HostIp&quot;: &quot;0.0.0.0&quot;,</span>
<span style="color:#AA5500">                        &quot;HostPort&quot;: &quot;61209&quot;</span>
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
<span style="color:#AA5500">                &quot;apparmor=unconfined&quot;,</span>
<span style="color:#AA5500">                &quot;label=disable&quot;</span>
<span style="color:#AA5500">            ],</span>
<span style="color:#AA5500">            &quot;ShmSize&quot;: 67108864,</span>
<span style="color:#AA5500">            &quot;UTSMode&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;Ulimits&quot;: null,</span>
<span style="color:#AA5500">            &quot;UsernsMode&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;VolumeDriver&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;VolumesFrom&quot;: null</span>
<span style="color:#AA5500">        },</span>
<span style="color:#AA5500">        &quot;HostnamePath&quot;: &quot;/var/lib/docker/containers/58ca8645c34f101200091f978c8d05332586f8eada21e92f79fafacdebba2b6d/hostname&quot;,</span>
<span style="color:#AA5500">        &quot;HostsPath&quot;: &quot;/var/lib/docker/containers/58ca8645c34f101200091f978c8d05332586f8eada21e92f79fafacdebba2b6d/hosts&quot;,</span>
<span style="color:#AA5500">        &quot;Id&quot;: &quot;58ca8645c34f101200091f978c8d05332586f8eada21e92f79fafacdebba2b6d&quot;,</span>
<span style="color:#AA5500">        &quot;Image&quot;: &quot;sha256:57152ac2efc0070135d9d634d9fb8507d65bf296f4fbe206a8f263e06e91885a&quot;,</span>
<span style="color:#AA5500">        &quot;LogPath&quot;: &quot;/var/lib/docker/containers/58ca8645c34f101200091f978c8d05332586f8eada21e92f79fafacdebba2b6d/58ca8645c34f101200091f978c8d05332586f8eada21e92f79fafacdebba2b6d-json.log&quot;,</span>
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
<span style="color:#AA5500">            }</span>
<span style="color:#AA5500">        ],</span>
<span style="color:#AA5500">        &quot;Name&quot;: &quot;/glances&quot;,</span>
<span style="color:#AA5500">        &quot;NetworkSettings&quot;: {</span>
<span style="color:#AA5500">            &quot;Bridge&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;EndpointID&quot;: &quot;665ecdfb5bced153e1e7071b99f143d2c6d34d962b40c0cf9a5bf202fb1c8285&quot;,</span>
<span style="color:#AA5500">            &quot;Gateway&quot;: &quot;172.17.0.1&quot;,</span>
<span style="color:#AA5500">            &quot;GlobalIPv6Address&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;GlobalIPv6PrefixLen&quot;: 0,</span>
<span style="color:#AA5500">            &quot;HairpinMode&quot;: false,</span>
<span style="color:#AA5500">            &quot;IPAddress&quot;: &quot;172.17.0.12&quot;,</span>
<span style="color:#AA5500">            &quot;IPPrefixLen&quot;: 16,</span>
<span style="color:#AA5500">            &quot;IPv6Gateway&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;LinkLocalIPv6Address&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;LinkLocalIPv6PrefixLen&quot;: 0,</span>
<span style="color:#AA5500">            &quot;MacAddress&quot;: &quot;de:14:32:8e:63:b2&quot;,</span>
<span style="color:#AA5500">            &quot;Networks&quot;: {</span>
<span style="color:#AA5500">                &quot;bridge&quot;: {</span>
<span style="color:#AA5500">                    &quot;Aliases&quot;: null,</span>
<span style="color:#AA5500">                    &quot;DNSNames&quot;: null,</span>
<span style="color:#AA5500">                    &quot;DriverOpts&quot;: null,</span>
<span style="color:#AA5500">                    &quot;EndpointID&quot;: &quot;665ecdfb5bced153e1e7071b99f143d2c6d34d962b40c0cf9a5bf202fb1c8285&quot;,</span>
<span style="color:#AA5500">                    &quot;Gateway&quot;: &quot;172.17.0.1&quot;,</span>
<span style="color:#AA5500">                    &quot;GlobalIPv6Address&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">                    &quot;GlobalIPv6PrefixLen&quot;: 0,</span>
<span style="color:#AA5500">                    &quot;GwPriority&quot;: 0,</span>
<span style="color:#AA5500">                    &quot;IPAMConfig&quot;: null,</span>
<span style="color:#AA5500">                    &quot;IPAddress&quot;: &quot;172.17.0.12&quot;,</span>
<span style="color:#AA5500">                    &quot;IPPrefixLen&quot;: 16,</span>
<span style="color:#AA5500">                    &quot;IPv6Gateway&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">                    &quot;Links&quot;: null,</span>
<span style="color:#AA5500">                    &quot;MacAddress&quot;: &quot;de:14:32:8e:63:b2&quot;,</span>
<span style="color:#AA5500">                    &quot;NetworkID&quot;: &quot;fce42755ebf1352d21e037493e0c33a917b08a8fe5d9ea19e3af1d873ab69e67&quot;</span>
<span style="color:#AA5500">                }</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            &quot;Ports&quot;: {</span>
<span style="color:#AA5500">                &quot;61208/tcp&quot;: [</span>
<span style="color:#AA5500">                    {</span>
<span style="color:#AA5500">                        &quot;HostIp&quot;: &quot;0.0.0.0&quot;,</span>
<span style="color:#AA5500">                        &quot;HostPort&quot;: &quot;61208&quot;</span>
<span style="color:#AA5500">                    }</span>
<span style="color:#AA5500">                ],</span>
<span style="color:#AA5500">                &quot;61209/tcp&quot;: [</span>
<span style="color:#AA5500">                    {</span>
<span style="color:#AA5500">                        &quot;HostIp&quot;: &quot;0.0.0.0&quot;,</span>
<span style="color:#AA5500">                        &quot;HostPort&quot;: &quot;61209&quot;</span>
<span style="color:#AA5500">                    }</span>
<span style="color:#AA5500">                ]</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            &quot;SandboxID&quot;: &quot;9d97942181b7edc82f7dd7f590a678b01f04957d45ea7ceb62873c68aa1cc134&quot;,</span>
<span style="color:#AA5500">            &quot;SandboxKey&quot;: &quot;/var/run/docker/netns/9d97942181b7&quot;,</span>
<span style="color:#AA5500">            &quot;SecondaryIPAddresses&quot;: null,</span>
<span style="color:#AA5500">            &quot;SecondaryIPv6Addresses&quot;: null</span>
<span style="color:#AA5500">        },</span>
<span style="color:#AA5500">        &quot;Path&quot;: &quot;/bin/sh&quot;,</span>
<span style="color:#AA5500">        &quot;Platform&quot;: &quot;linux&quot;,</span>
<span style="color:#AA5500">        &quot;ProcessLabel&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">        &quot;ResolvConfPath&quot;: &quot;/var/lib/docker/containers/58ca8645c34f101200091f978c8d05332586f8eada21e92f79fafacdebba2b6d/resolv.conf&quot;,</span>
<span style="color:#AA5500">        &quot;RestartCount&quot;: 0,</span>
<span style="color:#AA5500">        &quot;State&quot;: {</span>
<span style="color:#AA5500">            &quot;Dead&quot;: false,</span>
<span style="color:#AA5500">            &quot;Error&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;ExitCode&quot;: 0,</span>
<span style="color:#AA5500">            &quot;FinishedAt&quot;: &quot;2025-10-10T04:02:46.810065182Z&quot;,</span>
<span style="color:#AA5500">            &quot;OOMKilled&quot;: false,</span>
<span style="color:#AA5500">            &quot;Paused&quot;: false,</span>
<span style="color:#AA5500">            &quot;Pid&quot;: 2127228,</span>
<span style="color:#AA5500">            &quot;Restarting&quot;: false,</span>
<span style="color:#AA5500">            &quot;Running&quot;: true,</span>
<span style="color:#AA5500">            &quot;StartedAt&quot;: &quot;2025-10-10T04:02:54.038084786Z&quot;,</span>
<span style="color:#AA5500">            &quot;Status&quot;: &quot;running&quot;</span>
<span style="color:#AA5500">        }</span>
<span style="color:#AA5500">    }</span>
<span style="color:#AA5500">}</span>
Freitag 10 Oktober 2025  23:18:03 +0200 (0:00:01.798)       0:01:28.755 ******* 
Freitag 10 Oktober 2025  23:18:04 +0200 (0:00:00.069)       0:01:28.824 ******* 
Freitag 10 Oktober 2025  23:18:04 +0200 (0:00:00.051)       0:01:28.876 ******* 
Freitag 10 Oktober 2025  23:18:04 +0200 (0:00:00.060)       0:01:28.936 ******* 

TASK [gotify : Stop Gotify] ***************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/gotify/tasks/main.yml:38</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:18:04 +0200 (0:00:00.602)       0:01:29.539 ******* 
Freitag 10 Oktober 2025  23:18:04 +0200 (0:00:00.051)       0:01:29.591 ******* 
Freitag 10 Oktober 2025  23:18:04 +0200 (0:00:00.047)       0:01:29.638 ******* 
Freitag 10 Oktober 2025  23:18:04 +0200 (0:00:00.045)       0:01:29.684 ******* 
Freitag 10 Oktober 2025  23:18:05 +0200 (0:00:00.161)       0:01:29.846 ******* 
Freitag 10 Oktober 2025  23:18:05 +0200 (0:00:00.046)       0:01:29.892 ******* 
Freitag 10 Oktober 2025  23:18:05 +0200 (0:00:00.050)       0:01:29.942 ******* 

TASK [guacamole : Stop Guacamole] *********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/guacamole/tasks/main.yml:59</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:18:05 +0200 (0:00:00.652)       0:01:30.595 ******* 
Freitag 10 Oktober 2025  23:18:05 +0200 (0:00:00.042)       0:01:30.638 ******* 

TASK [healthchecks.io : Remove healthchecks.io cronjob] ***********************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/healthchecks.io/tasks/main.yml:14</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;envs&quot;: [],</span>
<span style="color:#00AA00">    &quot;jobs&quot;: []</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:18:06 +0200 (0:00:00.506)       0:01:31.144 ******* 
Freitag 10 Oktober 2025  23:18:06 +0200 (0:00:00.047)       0:01:31.192 ******* 
Freitag 10 Oktober 2025  23:18:06 +0200 (0:00:00.043)       0:01:31.236 ******* 

TASK [heimdall : Stop Heimdall] ***********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/heimdall/tasks/main.yml:36</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:18:07 +0200 (0:00:00.613)       0:01:31.850 ******* 
Freitag 10 Oktober 2025  23:18:07 +0200 (0:00:00.068)       0:01:31.918 ******* 
Freitag 10 Oktober 2025  23:18:07 +0200 (0:00:00.044)       0:01:31.963 ******* 

TASK [hello_world : Stop Hello World] *****************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/hello_world/tasks/main.yml:33</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:18:07 +0200 (0:00:00.630)       0:01:32.593 ******* 

TASK [homeassistant : Create Home Assistant Directories] **********************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/homeassistant/tasks/main.yml:4</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; (item=/mnt/Volume1/docker/homeassistant/config) =&gt; {</span>
<span style="color:#00AA00">    &quot;ansible_loop_var&quot;: &quot;item&quot;,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;gid&quot;: 1001,</span>
<span style="color:#00AA00">    &quot;group&quot;: &quot;ansible-nas&quot;,</span>
<span style="color:#00AA00">    &quot;item&quot;: &quot;/mnt/Volume1/docker/homeassistant/config&quot;,</span>
<span style="color:#00AA00">    &quot;mode&quot;: &quot;0777&quot;,</span>
<span style="color:#00AA00">    &quot;owner&quot;: &quot;1001&quot;,</span>
<span style="color:#00AA00">    &quot;path&quot;: &quot;/mnt/Volume1/docker/homeassistant/config&quot;,</span>
<span style="color:#00AA00">    &quot;size&quot;: 4096,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;directory&quot;,</span>
<span style="color:#00AA00">    &quot;uid&quot;: 1001</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:18:08 +0200 (0:00:00.389)       0:01:32.983 ******* 

TASK [homeassistant : Home Assistant Docker Container] ************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/homeassistant/tasks/main.yml:11</b></span>
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
<span style="color:#AA5500">                &quot;PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin&quot;,</span>
<span style="color:#AA5500">                &quot;LANG=C.UTF-8&quot;,</span>
<span style="color:#AA5500">                &quot;S6_BEHAVIOUR_IF_STAGE2_FAILS=2&quot;,</span>
<span style="color:#AA5500">                &quot;S6_CMD_WAIT_FOR_SERVICES_MAXTIME=0&quot;,</span>
<span style="color:#AA5500">                &quot;S6_CMD_WAIT_FOR_SERVICES=1&quot;,</span>
<span style="color:#AA5500">                &quot;S6_SERVICES_READYTIME=50&quot;,</span>
<span style="color:#AA5500">                &quot;UV_EXTRA_INDEX_URL=https://wheels.home-assistant.io/musllinux-index/&quot;,</span>
<span style="color:#AA5500">                &quot;S6_SERVICES_GRACETIME=240000&quot;,</span>
<span style="color:#AA5500">                &quot;UV_SYSTEM_PYTHON=true&quot;,</span>
<span style="color:#AA5500">                &quot;UV_NO_CACHE=true&quot;</span>
<span style="color:#AA5500">            ],</span>
<span style="color:#AA5500">            &quot;Hostname&quot;: &quot;RaspiNAS&quot;,</span>
<span style="color:#AA5500">            &quot;Image&quot;: &quot;homeassistant/home-assistant:2025.7.3&quot;,</span>
<span style="color:#AA5500">            &quot;Labels&quot;: {</span>
<span style="color:#AA5500">                &quot;io.hass.arch&quot;: &quot;aarch64&quot;,</span>
<span style="color:#AA5500">                &quot;io.hass.base.arch&quot;: &quot;aarch64&quot;,</span>
<span style="color:#AA5500">                &quot;io.hass.base.image&quot;: &quot;ghcr.io/home-assistant/aarch64-base:3.21&quot;,</span>
<span style="color:#AA5500">                &quot;io.hass.base.name&quot;: &quot;python&quot;,</span>
<span style="color:#AA5500">                &quot;io.hass.base.version&quot;: &quot;2025.05.0&quot;,</span>
<span style="color:#AA5500">                &quot;io.hass.type&quot;: &quot;core&quot;,</span>
<span style="color:#AA5500">                &quot;io.hass.version&quot;: &quot;2025.7.3&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.authors&quot;: &quot;The Home Assistant Authors&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.created&quot;: &quot;2025-07-22 08:37:21+00:00&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.description&quot;: &quot;Open-source home automation platform running on Python 3&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.documentation&quot;: &quot;https://www.home-assistant.io/docs/&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.licenses&quot;: &quot;Apache-2.0&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.source&quot;: &quot;https://github.com/home-assistant/core&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.title&quot;: &quot;Home Assistant&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.url&quot;: &quot;https://www.home-assistant.io/&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.version&quot;: &quot;2025.7.3&quot;,</span>
<span style="color:#AA5500">                &quot;traefik.enable&quot;: &quot;True&quot;,</span>
<span style="color:#AA5500">                &quot;traefik.http.routers.homeassistant.rule&quot;: &quot;Host(`homeassistant.Schneider.nbg`)&quot;,</span>
<span style="color:#AA5500">                &quot;traefik.http.routers.homeassistant.tls.certresolver&quot;: &quot;letsencrypt&quot;,</span>
<span style="color:#AA5500">                &quot;traefik.http.routers.homeassistant.tls.domains[0].main&quot;: &quot;Schneider.nbg&quot;,</span>
<span style="color:#AA5500">                &quot;traefik.http.routers.homeassistant.tls.domains[0].sans&quot;: &quot;*.Schneider.nbg&quot;,</span>
<span style="color:#AA5500">                &quot;traefik.http.services.homeassistant.loadbalancer.server.port&quot;: &quot;8123&quot;</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            &quot;OnBuild&quot;: null,</span>
<span style="color:#AA5500">            &quot;OpenStdin&quot;: false,</span>
<span style="color:#AA5500">            &quot;StdinOnce&quot;: false,</span>
<span style="color:#AA5500">            &quot;Tty&quot;: false,</span>
<span style="color:#AA5500">            &quot;User&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;Volumes&quot;: null,</span>
<span style="color:#AA5500">            &quot;WorkingDir&quot;: &quot;/config&quot;</span>
<span style="color:#AA5500">        },</span>
<span style="color:#AA5500">        &quot;Created&quot;: &quot;2025-10-01T22:31:41.313537884Z&quot;,</span>
<span style="color:#AA5500">        &quot;Driver&quot;: &quot;overlay2&quot;,</span>
<span style="color:#AA5500">        &quot;ExecIDs&quot;: null,</span>
<span style="color:#AA5500">        &quot;GraphDriver&quot;: {</span>
<span style="color:#AA5500">            &quot;Data&quot;: {</span>
<span style="color:#AA5500">                &quot;ID&quot;: &quot;353210e441ce9ecd2d7e043a6274f7eeb325ba448ad8b45746c5538c4d4dc7a9&quot;,</span>
<span style="color:#AA5500">                &quot;LowerDir&quot;: &quot;/var/lib/docker/overlay2/3d615365956bf3e866c7041a4c4f7e4b80ec0eb91cf9efcce73d6c13c1f266ce-init/diff:/var/lib/docker/overlay2/633eb128d149d7d22c5074d6aeb1bfc3e7627e4334691912ce3d63da5df3915d/diff:/var/lib/docker/overlay2/75600d2911b872747e5cb1aea1724bac818afd59b380bd8d64ab537a5fe3a10f/diff:/var/lib/docker/overlay2/c20f1aa7896f8d5772b85b4f71dc58253e1c9a935845323641ca37ed7bce9e68/diff:/var/lib/docker/overlay2/1505bf57d493e7111570b6c7d2f73fbbeab09eca133d0ff0c00a8d21af04779d/diff:/var/lib/docker/overlay2/1eb53b46ec5e43a93ac979d3bcf1666a3785241bfaaf173fcf6cb9b4832b1fb2/diff:/var/lib/docker/overlay2/ff871a923eb49148f4d37041aebcc792c3dc726b43f2985dcbd0cc833ed7d060/diff:/var/lib/docker/overlay2/dcd4bb0583d20664e574fabc165e28550ed8148e45525ea4958c22b27b26c74d/diff:/var/lib/docker/overlay2/e86725de6e3bbc02ef347bf0aa72b4985274539f386e63ee963300b78c01fbd6/diff:/var/lib/docker/overlay2/940a5b42aca30f8abc921e26d2492fd61b0c6ed4060bd6530f7a35f18bc49175/diff:/var/lib/docker/overlay2/7ff520f5fc996fbee672a314134e970ab03221516946812d495a3ecb6f00604f/diff:/var/lib/docker/overlay2/cd2e6d3655a089ad985337bc13c7f1e938d7edc660915333764871c9ca49f882/diff:/var/lib/docker/overlay2/38bc3aab1ffdd87d008b343c5d7af1d445f7c0f1d3dc060773d58ba8c0b26509/diff:/var/lib/docker/overlay2/8ab71f47f17b95923f547289f4b16302ec3985ba582bef01ffa4042c02b52625/diff:/var/lib/docker/overlay2/4214c6f7b28ddf1353a8656ed25c87e377a5e369f35e0447e1dc69517dfc0e31/diff:/var/lib/docker/overlay2/5f6764435fc742f772b51e4ad052f283ea9aa07b3db20ff55cbce4e82eecc13a/diff:/var/lib/docker/overlay2/aff59dbe31d12cfe4b02acdf9fe8bf8578767c04c86577f2ed3d3611cff5b098/diff:/var/lib/docker/overlay2/4b91215247e686756d57526645af3b27071b06429941822962bdb1e2c0cb7c96/diff:/var/lib/docker/overlay2/9c0351321ead2390a2a07fd42391091bd99f4491f02eaf2ed6f5946f25a90bcd/diff:/var/lib/docker/overlay2/a31f5fbdcfd6f57cc69f93be3098d601df8d56fa8f284006895e8ad9711a8bf1/diff:/var/lib/docker/overlay2/65f73ba62f1e34fa69bfc25df39cbdc4f7d4e82ef0bcd81906048475010c5cfc/diff:/var/lib/docker/overlay2/69290ec0f6cc2098b76acd6931fa785c30589834405843aeef7db8a121bfc83c/diff:/var/lib/docker/overlay2/e4ca5a9238362bc2f5866de3b470b7401365b001f6538a356d048545531927a1/diff:/var/lib/docker/overlay2/6c1976458bcf08bc0d722afec2227d3195a871248c3f39d5e651091bdaf54fd4/diff:/var/lib/docker/overlay2/557fab21eb47864af61c9614e3e725b2d03cdb94b14946c6ac30ab6e32a390ba/diff:/var/lib/docker/overlay2/6eff3d617f5a5cd156d2a059ac098279b79e0ddf950b9a09049f4109f505235f/diff:/var/lib/docker/overlay2/88fd18a299d141af39e99546b52a6b70280f82fd304270687fcaadb6befccc54/diff:/var/lib/docker/overlay2/0db01d5bd20f198e45e1d20f8f82c965741da82850ed35a65d7f8a40669bf758/diff:/var/lib/docker/overlay2/97ace1cd2e71ee31a1703ea154aa74d244264d7a730262829f794d18b2f35abe/diff:/var/lib/docker/overlay2/56e264465a3b30403381a6e3d15ce40e855831c0271a96bad3894e5cd7725d1b/diff:/var/lib/docker/overlay2/cefbaa93f8dec47b3206ccf010d26be4c6c625ab0a2ebb0f81db91a8a4a5bee0/diff:/var/lib/docker/overlay2/555640fd36ae5aaf6b0ad9d78cd39a58f829c41aeed16cc923e387fb3feea757/diff:/var/lib/docker/overlay2/aaa5bf77fad85e562e3a8a5e12a054f19c1a92d5233fc96d8127523fcc9a8d74/diff:/var/lib/docker/overlay2/f2ab1e8cf9b46c862cd537dc8d31f9bd94fb1a74097e2219ed1a63928d9474b5/diff&quot;,</span>
<span style="color:#AA5500">                &quot;MergedDir&quot;: &quot;/var/lib/docker/overlay2/3d615365956bf3e866c7041a4c4f7e4b80ec0eb91cf9efcce73d6c13c1f266ce/merged&quot;,</span>
<span style="color:#AA5500">                &quot;UpperDir&quot;: &quot;/var/lib/docker/overlay2/3d615365956bf3e866c7041a4c4f7e4b80ec0eb91cf9efcce73d6c13c1f266ce/diff&quot;,</span>
<span style="color:#AA5500">                &quot;WorkDir&quot;: &quot;/var/lib/docker/overlay2/3d615365956bf3e866c7041a4c4f7e4b80ec0eb91cf9efcce73d6c13c1f266ce/work&quot;</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            &quot;Name&quot;: &quot;overlay2&quot;</span>
<span style="color:#AA5500">        },</span>
<span style="color:#AA5500">        &quot;HostConfig&quot;: {</span>
<span style="color:#AA5500">            &quot;AutoRemove&quot;: false,</span>
<span style="color:#AA5500">            &quot;Binds&quot;: [</span>
<span style="color:#AA5500">                &quot;/mnt/Volume1/docker/homeassistant/config:/config:rw&quot;</span>
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
<span style="color:#AA5500">            &quot;NetworkMode&quot;: &quot;host&quot;,</span>
<span style="color:#AA5500">            &quot;OomKillDisable&quot;: null,</span>
<span style="color:#AA5500">            &quot;OomScoreAdj&quot;: 0,</span>
<span style="color:#AA5500">            &quot;PidMode&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;PidsLimit&quot;: null,</span>
<span style="color:#AA5500">            &quot;PortBindings&quot;: null,</span>
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
<span style="color:#AA5500">        &quot;HostnamePath&quot;: &quot;/var/lib/docker/containers/353210e441ce9ecd2d7e043a6274f7eeb325ba448ad8b45746c5538c4d4dc7a9/hostname&quot;,</span>
<span style="color:#AA5500">        &quot;HostsPath&quot;: &quot;/var/lib/docker/containers/353210e441ce9ecd2d7e043a6274f7eeb325ba448ad8b45746c5538c4d4dc7a9/hosts&quot;,</span>
<span style="color:#AA5500">        &quot;Id&quot;: &quot;353210e441ce9ecd2d7e043a6274f7eeb325ba448ad8b45746c5538c4d4dc7a9&quot;,</span>
<span style="color:#AA5500">        &quot;Image&quot;: &quot;sha256:96f535c3a34fa0433d95e6c537a7fb33e0805f764fd7bf735554d7eb95d71e5f&quot;,</span>
<span style="color:#AA5500">        &quot;LogPath&quot;: &quot;/var/lib/docker/containers/353210e441ce9ecd2d7e043a6274f7eeb325ba448ad8b45746c5538c4d4dc7a9/353210e441ce9ecd2d7e043a6274f7eeb325ba448ad8b45746c5538c4d4dc7a9-json.log&quot;,</span>
<span style="color:#AA5500">        &quot;MountLabel&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">        &quot;Mounts&quot;: [</span>
<span style="color:#AA5500">            {</span>
<span style="color:#AA5500">                &quot;Destination&quot;: &quot;/config&quot;,</span>
<span style="color:#AA5500">                &quot;Mode&quot;: &quot;rw&quot;,</span>
<span style="color:#AA5500">                &quot;Propagation&quot;: &quot;rprivate&quot;,</span>
<span style="color:#AA5500">                &quot;RW&quot;: true,</span>
<span style="color:#AA5500">                &quot;Source&quot;: &quot;/mnt/Volume1/docker/homeassistant/config&quot;,</span>
<span style="color:#AA5500">                &quot;Type&quot;: &quot;bind&quot;</span>
<span style="color:#AA5500">            }</span>
<span style="color:#AA5500">        ],</span>
<span style="color:#AA5500">        &quot;Name&quot;: &quot;/homeassistant&quot;,</span>
<span style="color:#AA5500">        &quot;NetworkSettings&quot;: {</span>
<span style="color:#AA5500">            &quot;Bridge&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;EndpointID&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;Gateway&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;GlobalIPv6Address&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;GlobalIPv6PrefixLen&quot;: 0,</span>
<span style="color:#AA5500">            &quot;HairpinMode&quot;: false,</span>
<span style="color:#AA5500">            &quot;IPAddress&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;IPPrefixLen&quot;: 0,</span>
<span style="color:#AA5500">            &quot;IPv6Gateway&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;LinkLocalIPv6Address&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;LinkLocalIPv6PrefixLen&quot;: 0,</span>
<span style="color:#AA5500">            &quot;MacAddress&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;Networks&quot;: {</span>
<span style="color:#AA5500">                &quot;host&quot;: {</span>
<span style="color:#AA5500">                    &quot;Aliases&quot;: null,</span>
<span style="color:#AA5500">                    &quot;DNSNames&quot;: null,</span>
<span style="color:#AA5500">                    &quot;DriverOpts&quot;: null,</span>
<span style="color:#AA5500">                    &quot;EndpointID&quot;: &quot;f71e99df3d028cad3d2bd4c972cfef723192d17a9ccc0964d3b6ebe23576f563&quot;,</span>
<span style="color:#AA5500">                    &quot;Gateway&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">                    &quot;GlobalIPv6Address&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">                    &quot;GlobalIPv6PrefixLen&quot;: 0,</span>
<span style="color:#AA5500">                    &quot;GwPriority&quot;: 0,</span>
<span style="color:#AA5500">                    &quot;IPAMConfig&quot;: null,</span>
<span style="color:#AA5500">                    &quot;IPAddress&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">                    &quot;IPPrefixLen&quot;: 0,</span>
<span style="color:#AA5500">                    &quot;IPv6Gateway&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">                    &quot;Links&quot;: null,</span>
<span style="color:#AA5500">                    &quot;MacAddress&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">                    &quot;NetworkID&quot;: &quot;fb0b7c4943026ade3ac058dc9ffeda4029ed4c219e646fc20aea18c5b3cdbd2a&quot;</span>
<span style="color:#AA5500">                }</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            &quot;Ports&quot;: {},</span>
<span style="color:#AA5500">            &quot;SandboxID&quot;: &quot;5b077eb768b096427b3d5468c1a531a9d222852182eeec2e51323ee354033d2a&quot;,</span>
<span style="color:#AA5500">            &quot;SandboxKey&quot;: &quot;/var/run/docker/netns/default&quot;,</span>
<span style="color:#AA5500">            &quot;SecondaryIPAddresses&quot;: null,</span>
<span style="color:#AA5500">            &quot;SecondaryIPv6Addresses&quot;: null</span>
<span style="color:#AA5500">        },</span>
<span style="color:#AA5500">        &quot;Path&quot;: &quot;/init&quot;,</span>
<span style="color:#AA5500">        &quot;Platform&quot;: &quot;linux&quot;,</span>
<span style="color:#AA5500">        &quot;ProcessLabel&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">        &quot;ResolvConfPath&quot;: &quot;/var/lib/docker/containers/353210e441ce9ecd2d7e043a6274f7eeb325ba448ad8b45746c5538c4d4dc7a9/resolv.conf&quot;,</span>
<span style="color:#AA5500">        &quot;RestartCount&quot;: 0,</span>
<span style="color:#AA5500">        &quot;State&quot;: {</span>
<span style="color:#AA5500">            &quot;Dead&quot;: false,</span>
<span style="color:#AA5500">            &quot;Error&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;ExitCode&quot;: 0,</span>
<span style="color:#AA5500">            &quot;FinishedAt&quot;: &quot;2025-10-10T04:02:49.399591533Z&quot;,</span>
<span style="color:#AA5500">            &quot;OOMKilled&quot;: false,</span>
<span style="color:#AA5500">            &quot;Paused&quot;: false,</span>
<span style="color:#AA5500">            &quot;Pid&quot;: 2127240,</span>
<span style="color:#AA5500">            &quot;Restarting&quot;: false,</span>
<span style="color:#AA5500">            &quot;Running&quot;: true,</span>
<span style="color:#AA5500">            &quot;StartedAt&quot;: &quot;2025-10-10T04:02:54.029464924Z&quot;,</span>
<span style="color:#AA5500">            &quot;Status&quot;: &quot;running&quot;</span>
<span style="color:#AA5500">        }</span>
<span style="color:#AA5500">    }</span>
<span style="color:#AA5500">}</span>
Freitag 10 Oktober 2025  23:18:10 +0200 (0:00:02.040)       0:01:35.023 ******* 
Freitag 10 Oktober 2025  23:18:10 +0200 (0:00:00.065)       0:01:35.089 ******* 
Freitag 10 Oktober 2025  23:18:10 +0200 (0:00:00.048)       0:01:35.138 ******* 
Freitag 10 Oktober 2025  23:18:10 +0200 (0:00:00.052)       0:01:35.191 ******* 

TASK [homebridge : Stop Homebridge] *******************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/homebridge/tasks/main.yml:39</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:18:11 +0200 (0:00:00.645)       0:01:35.836 ******* 

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
Freitag 10 Oktober 2025  23:18:11 +0200 (0:00:00.372)       0:01:36.209 ******* 

TASK [homepage : Template config files] ***************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/homepage/tasks/main.yml:11</b></span>
<span style="color:#AA5500">changed: [ansible-nas] =&gt; (item=bookmarks.yaml) =&gt; {</span>
<span style="color:#AA5500">    &quot;ansible_loop_var&quot;: &quot;item&quot;,</span>
<span style="color:#AA5500">    &quot;changed&quot;: true,</span>
<span style="color:#AA5500">    &quot;checksum&quot;: &quot;aaf8412f7134f4dcef372e9fc4420c6d5343c735&quot;,</span>
<span style="color:#AA5500">    &quot;dest&quot;: &quot;/mnt/Volume1/docker/homepage/bookmarks.yaml&quot;,</span>
<span style="color:#AA5500">    &quot;gid&quot;: 1000,</span>
<span style="color:#AA5500">    &quot;group&quot;: &quot;dietmar&quot;,</span>
<span style="color:#AA5500">    &quot;item&quot;: &quot;bookmarks.yaml&quot;,</span>
<span style="color:#AA5500">    &quot;md5sum&quot;: &quot;3f72cffc9cca6b08caff1dd4ca5a1df4&quot;,</span>
<span style="color:#AA5500">    &quot;mode&quot;: &quot;0644&quot;,</span>
<span style="color:#AA5500">    &quot;owner&quot;: &quot;dietmar&quot;,</span>
<span style="color:#AA5500">    &quot;size&quot;: 3058,</span>
<span style="color:#AA5500">    &quot;src&quot;: &quot;/home/dietmar/.ansible/tmp/ansible-tmp-1760131091.4605513-101879-115908227526471/.source.yaml&quot;,</span>
<span style="color:#AA5500">    &quot;state&quot;: &quot;file&quot;,</span>
<span style="color:#AA5500">    &quot;uid&quot;: 1000</span>
<span style="color:#AA5500">}</span>
<span style="color:#AA5500">changed: [ansible-nas] =&gt; (item=docker.yaml) =&gt; {</span>
<span style="color:#AA5500">    &quot;ansible_loop_var&quot;: &quot;item&quot;,</span>
<span style="color:#AA5500">    &quot;changed&quot;: true,</span>
<span style="color:#AA5500">    &quot;checksum&quot;: &quot;c9c9f5d43dab59e638c885b21bba46d28f5c0509&quot;,</span>
<span style="color:#AA5500">    &quot;dest&quot;: &quot;/mnt/Volume1/docker/homepage/docker.yaml&quot;,</span>
<span style="color:#AA5500">    &quot;gid&quot;: 1000,</span>
<span style="color:#AA5500">    &quot;group&quot;: &quot;dietmar&quot;,</span>
<span style="color:#AA5500">    &quot;item&quot;: &quot;docker.yaml&quot;,</span>
<span style="color:#AA5500">    &quot;md5sum&quot;: &quot;76fb8ae78268d0ef057a633d5479d266&quot;,</span>
<span style="color:#AA5500">    &quot;mode&quot;: &quot;0644&quot;,</span>
<span style="color:#AA5500">    &quot;owner&quot;: &quot;dietmar&quot;,</span>
<span style="color:#AA5500">    &quot;size&quot;: 45,</span>
<span style="color:#AA5500">    &quot;src&quot;: &quot;/home/dietmar/.ansible/tmp/ansible-tmp-1760131092.303695-101879-253982577273541/.source.yaml&quot;,</span>
<span style="color:#AA5500">    &quot;state&quot;: &quot;file&quot;,</span>
<span style="color:#AA5500">    &quot;uid&quot;: 1000</span>
<span style="color:#AA5500">}</span>
<span style="color:#AA5500">changed: [ansible-nas] =&gt; (item=settings.yaml) =&gt; {</span>
<span style="color:#AA5500">    &quot;ansible_loop_var&quot;: &quot;item&quot;,</span>
<span style="color:#AA5500">    &quot;changed&quot;: true,</span>
<span style="color:#AA5500">    &quot;checksum&quot;: &quot;e2821d472921ed1b45268ebde46393b65eb39e65&quot;,</span>
<span style="color:#AA5500">    &quot;dest&quot;: &quot;/mnt/Volume1/docker/homepage/settings.yaml&quot;,</span>
<span style="color:#AA5500">    &quot;gid&quot;: 1000,</span>
<span style="color:#AA5500">    &quot;group&quot;: &quot;dietmar&quot;,</span>
<span style="color:#AA5500">    &quot;item&quot;: &quot;settings.yaml&quot;,</span>
<span style="color:#AA5500">    &quot;md5sum&quot;: &quot;76a99937a2be34274c7a13c51e77c74e&quot;,</span>
<span style="color:#AA5500">    &quot;mode&quot;: &quot;0644&quot;,</span>
<span style="color:#AA5500">    &quot;owner&quot;: &quot;dietmar&quot;,</span>
<span style="color:#AA5500">    &quot;size&quot;: 61,</span>
<span style="color:#AA5500">    &quot;src&quot;: &quot;/home/dietmar/.ansible/tmp/ansible-tmp-1760131092.950509-101879-120789150612470/.source.yaml&quot;,</span>
<span style="color:#AA5500">    &quot;state&quot;: &quot;file&quot;,</span>
<span style="color:#AA5500">    &quot;uid&quot;: 1000</span>
<span style="color:#AA5500">}</span>
<span style="color:#AA5500">changed: [ansible-nas] =&gt; (item=services.yaml) =&gt; {</span>
<span style="color:#AA5500">    &quot;ansible_loop_var&quot;: &quot;item&quot;,</span>
<span style="color:#AA5500">    &quot;changed&quot;: true,</span>
<span style="color:#AA5500">    &quot;checksum&quot;: &quot;643d1b2981e788261960dec10c408069b2a6de5d&quot;,</span>
<span style="color:#AA5500">    &quot;dest&quot;: &quot;/mnt/Volume1/docker/homepage/services.yaml&quot;,</span>
<span style="color:#AA5500">    &quot;gid&quot;: 1000,</span>
<span style="color:#AA5500">    &quot;group&quot;: &quot;dietmar&quot;,</span>
<span style="color:#AA5500">    &quot;item&quot;: &quot;services.yaml&quot;,</span>
<span style="color:#AA5500">    &quot;md5sum&quot;: &quot;0f0a787c08741015a3eb36b20d2eff3d&quot;,</span>
<span style="color:#AA5500">    &quot;mode&quot;: &quot;0644&quot;,</span>
<span style="color:#AA5500">    &quot;owner&quot;: &quot;dietmar&quot;,</span>
<span style="color:#AA5500">    &quot;size&quot;: 2528,</span>
<span style="color:#AA5500">    &quot;src&quot;: &quot;/home/dietmar/.ansible/tmp/ansible-tmp-1760131094.5936272-101879-158091801860120/.source.yaml&quot;,</span>
<span style="color:#AA5500">    &quot;state&quot;: &quot;file&quot;,</span>
<span style="color:#AA5500">    &quot;uid&quot;: 1000</span>
<span style="color:#AA5500">}</span>
<span style="color:#AA5500">changed: [ansible-nas] =&gt; (item=widgets.yaml) =&gt; {</span>
<span style="color:#AA5500">    &quot;ansible_loop_var&quot;: &quot;item&quot;,</span>
<span style="color:#AA5500">    &quot;changed&quot;: true,</span>
<span style="color:#AA5500">    &quot;checksum&quot;: &quot;a2e239d8c1ee2ef55af5b5d03c7f8c3fe8bc6f1c&quot;,</span>
<span style="color:#AA5500">    &quot;dest&quot;: &quot;/mnt/Volume1/docker/homepage/widgets.yaml&quot;,</span>
<span style="color:#AA5500">    &quot;gid&quot;: 1000,</span>
<span style="color:#AA5500">    &quot;group&quot;: &quot;dietmar&quot;,</span>
<span style="color:#AA5500">    &quot;item&quot;: &quot;widgets.yaml&quot;,</span>
<span style="color:#AA5500">    &quot;md5sum&quot;: &quot;37d625e7cd081cfc019af029794992d4&quot;,</span>
<span style="color:#AA5500">    &quot;mode&quot;: &quot;0644&quot;,</span>
<span style="color:#AA5500">    &quot;owner&quot;: &quot;dietmar&quot;,</span>
<span style="color:#AA5500">    &quot;size&quot;: 648,</span>
<span style="color:#AA5500">    &quot;src&quot;: &quot;/home/dietmar/.ansible/tmp/ansible-tmp-1760131095.279646-101879-12859525802780/.source.yaml&quot;,</span>
<span style="color:#AA5500">    &quot;state&quot;: &quot;file&quot;,</span>
<span style="color:#AA5500">    &quot;uid&quot;: 1000</span>
<span style="color:#AA5500">}</span>
Freitag 10 Oktober 2025  23:18:15 +0200 (0:00:04.588)       0:01:40.798 ******* 

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
<span style="color:#AA5500">            &quot;Hostname&quot;: &quot;9544640b3af2&quot;,</span>
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
<span style="color:#AA5500">        &quot;Created&quot;: &quot;2025-10-10T21:18:17.416644567Z&quot;,</span>
<span style="color:#AA5500">        &quot;Driver&quot;: &quot;overlay2&quot;,</span>
<span style="color:#AA5500">        &quot;ExecIDs&quot;: null,</span>
<span style="color:#AA5500">        &quot;GraphDriver&quot;: {</span>
<span style="color:#AA5500">            &quot;Data&quot;: {</span>
<span style="color:#AA5500">                &quot;ID&quot;: &quot;9544640b3af2a2716ce572d181f9ae52e74fec7427cb33c777a4ba7f131489c9&quot;,</span>
<span style="color:#AA5500">                &quot;LowerDir&quot;: &quot;/var/lib/docker/overlay2/384686d70d2be082725fdbd044a18b9dca9fbd93cb9ba2b7e43a728305c6faee-init/diff:/var/lib/docker/overlay2/23a9385149d0f49800ed7f1d18a7975e3e6c6cc0ddeb75551e30acbb3fe8acab/diff:/var/lib/docker/overlay2/48247c240df240adc75d0560240e5bdcea1e5b0e3421511997fbd49098c4f177/diff:/var/lib/docker/overlay2/1757a842b2db6b66f4e139af38e2a438f72effe4b9b13ef6d21e4b161e76484e/diff:/var/lib/docker/overlay2/7fbced54ce4f73d785820c4ec8bee72324553f5df29851e8e682f6a81bdacada/diff:/var/lib/docker/overlay2/a37637f159082e890f586ca87fe6b86cc7f704bb28bd9a148a16d5be78fcf3c9/diff:/var/lib/docker/overlay2/cc19d88f3f5740d1286616e33561d4bcf45479331a0103ef4bf291c2abcfee00/diff:/var/lib/docker/overlay2/3fbd10128c4266d5886821096047ca645ff55c0a76dd99e2115e24756abe8889/diff:/var/lib/docker/overlay2/d035f3715f0b05e119f1cc508d4178bc870691590ad5897c298e685f64e7e4f6/diff:/var/lib/docker/overlay2/f40b5fef4490f7de32848a38a5c19a15f50fc99f0016f98f4214304c8496b150/diff:/var/lib/docker/overlay2/502c7107094a5bb68299bb6f3d8d9b644daf0a27a5836740ac357984351c9297/diff&quot;,</span>
<span style="color:#AA5500">                &quot;MergedDir&quot;: &quot;/var/lib/docker/overlay2/384686d70d2be082725fdbd044a18b9dca9fbd93cb9ba2b7e43a728305c6faee/merged&quot;,</span>
<span style="color:#AA5500">                &quot;UpperDir&quot;: &quot;/var/lib/docker/overlay2/384686d70d2be082725fdbd044a18b9dca9fbd93cb9ba2b7e43a728305c6faee/diff&quot;,</span>
<span style="color:#AA5500">                &quot;WorkDir&quot;: &quot;/var/lib/docker/overlay2/384686d70d2be082725fdbd044a18b9dca9fbd93cb9ba2b7e43a728305c6faee/work&quot;</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            &quot;Name&quot;: &quot;overlay2&quot;</span>
<span style="color:#AA5500">        },</span>
<span style="color:#AA5500">        &quot;HostConfig&quot;: {</span>
<span style="color:#AA5500">            &quot;AutoRemove&quot;: false,</span>
<span style="color:#AA5500">            &quot;Binds&quot;: [</span>
<span style="color:#AA5500">                &quot;/mnt/Volume1/docker/homepage:/app/config:rw&quot;,</span>
<span style="color:#AA5500">                &quot;/mnt/Volume1/docker/homepage/icons:/app/public/icons:rw&quot;,</span>
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
<span style="color:#AA5500">        &quot;HostnamePath&quot;: &quot;/var/lib/docker/containers/9544640b3af2a2716ce572d181f9ae52e74fec7427cb33c777a4ba7f131489c9/hostname&quot;,</span>
<span style="color:#AA5500">        &quot;HostsPath&quot;: &quot;/var/lib/docker/containers/9544640b3af2a2716ce572d181f9ae52e74fec7427cb33c777a4ba7f131489c9/hosts&quot;,</span>
<span style="color:#AA5500">        &quot;Id&quot;: &quot;9544640b3af2a2716ce572d181f9ae52e74fec7427cb33c777a4ba7f131489c9&quot;,</span>
<span style="color:#AA5500">        &quot;Image&quot;: &quot;sha256:2833b1df3f84c40c0f35b25d7e7fac123d5d1f89883515e431c10149d7d7c6dd&quot;,</span>
<span style="color:#AA5500">        &quot;LogPath&quot;: &quot;/var/lib/docker/containers/9544640b3af2a2716ce572d181f9ae52e74fec7427cb33c777a4ba7f131489c9/9544640b3af2a2716ce572d181f9ae52e74fec7427cb33c777a4ba7f131489c9-json.log&quot;,</span>
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
<span style="color:#AA5500">                &quot;Destination&quot;: &quot;/app/public/icons&quot;,</span>
<span style="color:#AA5500">                &quot;Mode&quot;: &quot;rw&quot;,</span>
<span style="color:#AA5500">                &quot;Propagation&quot;: &quot;rprivate&quot;,</span>
<span style="color:#AA5500">                &quot;RW&quot;: true,</span>
<span style="color:#AA5500">                &quot;Source&quot;: &quot;/mnt/Volume1/docker/homepage/icons&quot;,</span>
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
<span style="color:#AA5500">            &quot;EndpointID&quot;: &quot;5e58a7cc622bcdd8e46f54fe95dcb42f8324bbf2f8900bb1ae8a63633911cd8c&quot;,</span>
<span style="color:#AA5500">            &quot;Gateway&quot;: &quot;172.17.0.1&quot;,</span>
<span style="color:#AA5500">            &quot;GlobalIPv6Address&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;GlobalIPv6PrefixLen&quot;: 0,</span>
<span style="color:#AA5500">            &quot;HairpinMode&quot;: false,</span>
<span style="color:#AA5500">            &quot;IPAddress&quot;: &quot;172.17.0.5&quot;,</span>
<span style="color:#AA5500">            &quot;IPPrefixLen&quot;: 16,</span>
<span style="color:#AA5500">            &quot;IPv6Gateway&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;LinkLocalIPv6Address&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;LinkLocalIPv6PrefixLen&quot;: 0,</span>
<span style="color:#AA5500">            &quot;MacAddress&quot;: &quot;72:d3:ae:2b:4c:6f&quot;,</span>
<span style="color:#AA5500">            &quot;Networks&quot;: {</span>
<span style="color:#AA5500">                &quot;bridge&quot;: {</span>
<span style="color:#AA5500">                    &quot;Aliases&quot;: null,</span>
<span style="color:#AA5500">                    &quot;DNSNames&quot;: null,</span>
<span style="color:#AA5500">                    &quot;DriverOpts&quot;: null,</span>
<span style="color:#AA5500">                    &quot;EndpointID&quot;: &quot;5e58a7cc622bcdd8e46f54fe95dcb42f8324bbf2f8900bb1ae8a63633911cd8c&quot;,</span>
<span style="color:#AA5500">                    &quot;Gateway&quot;: &quot;172.17.0.1&quot;,</span>
<span style="color:#AA5500">                    &quot;GlobalIPv6Address&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">                    &quot;GlobalIPv6PrefixLen&quot;: 0,</span>
<span style="color:#AA5500">                    &quot;GwPriority&quot;: 0,</span>
<span style="color:#AA5500">                    &quot;IPAMConfig&quot;: null,</span>
<span style="color:#AA5500">                    &quot;IPAddress&quot;: &quot;172.17.0.5&quot;,</span>
<span style="color:#AA5500">                    &quot;IPPrefixLen&quot;: 16,</span>
<span style="color:#AA5500">                    &quot;IPv6Gateway&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">                    &quot;Links&quot;: null,</span>
<span style="color:#AA5500">                    &quot;MacAddress&quot;: &quot;72:d3:ae:2b:4c:6f&quot;,</span>
<span style="color:#AA5500">                    &quot;NetworkID&quot;: &quot;fce42755ebf1352d21e037493e0c33a917b08a8fe5d9ea19e3af1d873ab69e67&quot;</span>
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
<span style="color:#AA5500">            &quot;SandboxID&quot;: &quot;509e011377ac810728d3459d619bacabfad115142721289084d936dc2f71b6e7&quot;,</span>
<span style="color:#AA5500">            &quot;SandboxKey&quot;: &quot;/var/run/docker/netns/509e011377ac&quot;,</span>
<span style="color:#AA5500">            &quot;SecondaryIPAddresses&quot;: null,</span>
<span style="color:#AA5500">            &quot;SecondaryIPv6Addresses&quot;: null</span>
<span style="color:#AA5500">        },</span>
<span style="color:#AA5500">        &quot;Path&quot;: &quot;docker-entrypoint.sh&quot;,</span>
<span style="color:#AA5500">        &quot;Platform&quot;: &quot;linux&quot;,</span>
<span style="color:#AA5500">        &quot;ProcessLabel&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">        &quot;ResolvConfPath&quot;: &quot;/var/lib/docker/containers/9544640b3af2a2716ce572d181f9ae52e74fec7427cb33c777a4ba7f131489c9/resolv.conf&quot;,</span>
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
<span style="color:#AA5500">            &quot;Pid&quot;: 2572732,</span>
<span style="color:#AA5500">            &quot;Restarting&quot;: false,</span>
<span style="color:#AA5500">            &quot;Running&quot;: true,</span>
<span style="color:#AA5500">            &quot;StartedAt&quot;: &quot;2025-10-10T21:18:17.482107108Z&quot;,</span>
<span style="color:#AA5500">            &quot;Status&quot;: &quot;running&quot;</span>
<span style="color:#AA5500">        }</span>
<span style="color:#AA5500">    }</span>
<span style="color:#AA5500">}</span>
Freitag 10 Oktober 2025  23:18:17 +0200 (0:00:01.733)       0:01:42.531 ******* 
Freitag 10 Oktober 2025  23:18:17 +0200 (0:00:00.067)       0:01:42.599 ******* 
Freitag 10 Oktober 2025  23:18:17 +0200 (0:00:00.045)       0:01:42.644 ******* 
Freitag 10 Oktober 2025  23:18:17 +0200 (0:00:00.051)       0:01:42.696 ******* 

TASK [ispyagentdvr : Stop iSpyAgentDVR] ***************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/ispyagentdvr/tasks/main.yml:50</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:18:18 +0200 (0:00:00.691)       0:01:43.387 ******* 
Freitag 10 Oktober 2025  23:18:18 +0200 (0:00:00.153)       0:01:43.541 ******* 
Freitag 10 Oktober 2025  23:18:18 +0200 (0:00:00.046)       0:01:43.587 ******* 

TASK [jackett : Stop Jackett] *************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/jackett/tasks/main.yml:41</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:18:19 +0200 (0:00:00.710)       0:01:44.298 ******* 

TASK [jdownloader2 : Create jdownloader2 Directories] *************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/jdownloader2/tasks/main.yml:4</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; (item=/mnt/Volume1/docker/jdownloader2/data) =&gt; {</span>
<span style="color:#00AA00">    &quot;ansible_loop_var&quot;: &quot;item&quot;,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;gid&quot;: 1000,</span>
<span style="color:#00AA00">    &quot;group&quot;: &quot;dietmar&quot;,</span>
<span style="color:#00AA00">    &quot;item&quot;: &quot;/mnt/Volume1/docker/jdownloader2/data&quot;,</span>
<span style="color:#00AA00">    &quot;mode&quot;: &quot;0755&quot;,</span>
<span style="color:#00AA00">    &quot;owner&quot;: &quot;dietmar&quot;,</span>
<span style="color:#00AA00">    &quot;path&quot;: &quot;/mnt/Volume1/docker/jdownloader2/data&quot;,</span>
<span style="color:#00AA00">    &quot;size&quot;: 4096,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;directory&quot;,</span>
<span style="color:#00AA00">    &quot;uid&quot;: 1000</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:18:19 +0200 (0:00:00.466)       0:01:44.764 ******* 

TASK [jdownloader2 : jdownloader2 Docker Container] ***************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/jdownloader2/tasks/main.yml:12</b></span>
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
<span style="color:#AA5500">                &quot;PASSWORD=&quot;,</span>
<span style="color:#AA5500">                &quot;CLI_ARGS=&quot;,</span>
<span style="color:#AA5500">                &quot;PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/opt/base/sbin:/opt/base/bin&quot;,</span>
<span style="color:#AA5500">                &quot;ENV=/root/.docker_rc&quot;,</span>
<span style="color:#AA5500">                &quot;USER_ID=1000&quot;,</span>
<span style="color:#AA5500">                &quot;GROUP_ID=1000&quot;,</span>
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
<span style="color:#AA5500">                &quot;WEB_AUTHENTICATION_USERNAME=&quot;,</span>
<span style="color:#AA5500">                &quot;WEB_AUTHENTICATION_PASSWORD=&quot;,</span>
<span style="color:#AA5500">                &quot;WEB_FILE_MANAGER=0&quot;,</span>
<span style="color:#AA5500">                &quot;WEB_FILE_MANAGER_ALLOWED_PATHS=AUTO&quot;,</span>
<span style="color:#AA5500">                &quot;WEB_FILE_MANAGER_DENIED_PATHS=&quot;,</span>
<span style="color:#AA5500">                &quot;MYJDOWNLOADER_EMAIL=&quot;,</span>
<span style="color:#AA5500">                &quot;MYJDOWNLOADER_PASSWORD=&quot;,</span>
<span style="color:#AA5500">                &quot;MYJDOWNLOADER_DEVICE_NAME=&quot;,</span>
<span style="color:#AA5500">                &quot;JDOWNLOADER_HEADLESS=0&quot;,</span>
<span style="color:#AA5500">                &quot;JDOWNLOADER_MAX_MEM=&quot;</span>
<span style="color:#AA5500">            ],</span>
<span style="color:#AA5500">            &quot;ExposedPorts&quot;: {</span>
<span style="color:#AA5500">                &quot;3129/tcp&quot;: {},</span>
<span style="color:#AA5500">                &quot;5800/tcp&quot;: {},</span>
<span style="color:#AA5500">                &quot;5900/tcp&quot;: {}</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            &quot;Hostname&quot;: &quot;a52cb1e63c49&quot;,</span>
<span style="color:#AA5500">            &quot;Image&quot;: &quot;jlesage/jdownloader-2&quot;,</span>
<span style="color:#AA5500">            &quot;Labels&quot;: {</span>
<span style="color:#AA5500">                &quot;org.label-schema.description&quot;: &quot;Docker container for JDownloader 2&quot;,</span>
<span style="color:#AA5500">                &quot;org.label-schema.name&quot;: &quot;jdownloader-2&quot;,</span>
<span style="color:#AA5500">                &quot;org.label-schema.schema-version&quot;: &quot;1.0&quot;,</span>
<span style="color:#AA5500">                &quot;org.label-schema.vcs-url&quot;: &quot;https://github.com/jlesage/docker-jdownloader-2&quot;,</span>
<span style="color:#AA5500">                &quot;org.label-schema.version&quot;: &quot;25.07.2&quot;</span>
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
<span style="color:#AA5500">        &quot;Created&quot;: &quot;2025-09-29T00:00:43.264182358Z&quot;,</span>
<span style="color:#AA5500">        &quot;Driver&quot;: &quot;overlay2&quot;,</span>
<span style="color:#AA5500">        &quot;ExecIDs&quot;: null,</span>
<span style="color:#AA5500">        &quot;GraphDriver&quot;: {</span>
<span style="color:#AA5500">            &quot;Data&quot;: {</span>
<span style="color:#AA5500">                &quot;ID&quot;: &quot;a52cb1e63c491647f36ffa34d4b8f07a36c10bc016602fc4e00a7c03eb872c8b&quot;,</span>
<span style="color:#AA5500">                &quot;LowerDir&quot;: &quot;/var/lib/docker/overlay2/394aec897b3a2333650c9f6bc60492a9cf3cfde76c4d548a7bf133dbb4850b3f-init/diff:/var/lib/docker/overlay2/7db7c3f1ba372ffedd33c4535c3f69170ae9c704c6e898cfd2a9bcc77e7f6ce4/diff:/var/lib/docker/overlay2/c92ef34c182c793e300c1036fd0284762009dae6ee69c44e9d5b8b94d3e8022f/diff:/var/lib/docker/overlay2/9b44f474bc0babb7f1475f626e185f5a0edfcfbe1a6bb60bfda8f2b844613b09/diff:/var/lib/docker/overlay2/3598e3e42b480b3db0cf2cd03cddcfb1f8f2a835ef9b7797150b5666a509735e/diff:/var/lib/docker/overlay2/8b1fafc5c5b281610debdfafb06b4d16229f9da31b55f179c01a021cdb179aa2/diff:/var/lib/docker/overlay2/b21683c93461405e0fe0083c5ec0ed66ed2e51871bd524c931741128125ac671/diff:/var/lib/docker/overlay2/a33551a139f502c062fc65fc72b13a0806e85050c97212ef832300ab5d17fc0a/diff:/var/lib/docker/overlay2/1d940ae7dcf07f6186af400268f6a70956356a5ff1b06272c0fd280e7681deae/diff:/var/lib/docker/overlay2/71c3945b10d5ec0d3b9074cf87d233805044987e7cc234629b68327f90782f80/diff:/var/lib/docker/overlay2/eaea86005b5ddb34dbf469e7ff96ab538d3af3f25c83f8884c33a3f07ac7736f/diff:/var/lib/docker/overlay2/26c1e8192ab8d8325c093e05b0fe00366159c1e10f1b5d2e17a718bdbe870365/diff:/var/lib/docker/overlay2/6e1034b872e7e9780850ea3ce367ab7b74df0c2400e39833034180621749f303/diff:/var/lib/docker/overlay2/b044e1eb447e594c2d10b959fdff4deb042a989c09aff027643a2ae3e9e43937/diff:/var/lib/docker/overlay2/34af5ccbdd6ad56bcc6cae86add101a69be164dd788d58867a6709f6edcf5b79/diff:/var/lib/docker/overlay2/e4ddb07933fc2d592fed740f421bb9a83fc6a770f34e3cdfa3df961b2c6c5c1b/diff:/var/lib/docker/overlay2/a60d5e613bbce09da83a41f76214ba64400e5c0c6c111205706347ad3757fe0a/diff:/var/lib/docker/overlay2/29cba5ce6497ba971437074abfaa9dd035a88a66792b255bd65a4f4c0e9c546f/diff&quot;,</span>
<span style="color:#AA5500">                &quot;MergedDir&quot;: &quot;/var/lib/docker/overlay2/394aec897b3a2333650c9f6bc60492a9cf3cfde76c4d548a7bf133dbb4850b3f/merged&quot;,</span>
<span style="color:#AA5500">                &quot;UpperDir&quot;: &quot;/var/lib/docker/overlay2/394aec897b3a2333650c9f6bc60492a9cf3cfde76c4d548a7bf133dbb4850b3f/diff&quot;,</span>
<span style="color:#AA5500">                &quot;WorkDir&quot;: &quot;/var/lib/docker/overlay2/394aec897b3a2333650c9f6bc60492a9cf3cfde76c4d548a7bf133dbb4850b3f/work&quot;</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            &quot;Name&quot;: &quot;overlay2&quot;</span>
<span style="color:#AA5500">        },</span>
<span style="color:#AA5500">        &quot;HostConfig&quot;: {</span>
<span style="color:#AA5500">            &quot;AutoRemove&quot;: false,</span>
<span style="color:#AA5500">            &quot;Binds&quot;: [</span>
<span style="color:#AA5500">                &quot;/mnt/Volume1/docker/jdownloader2/data:/config:rw&quot;,</span>
<span style="color:#AA5500">                &quot;/mnt/Volume1/local/Download/Production/:/output:rw&quot;</span>
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
<span style="color:#AA5500">                &quot;5800/tcp&quot;: [</span>
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
<span style="color:#AA5500">        &quot;HostnamePath&quot;: &quot;/var/lib/docker/containers/a52cb1e63c491647f36ffa34d4b8f07a36c10bc016602fc4e00a7c03eb872c8b/hostname&quot;,</span>
<span style="color:#AA5500">        &quot;HostsPath&quot;: &quot;/var/lib/docker/containers/a52cb1e63c491647f36ffa34d4b8f07a36c10bc016602fc4e00a7c03eb872c8b/hosts&quot;,</span>
<span style="color:#AA5500">        &quot;Id&quot;: &quot;a52cb1e63c491647f36ffa34d4b8f07a36c10bc016602fc4e00a7c03eb872c8b&quot;,</span>
<span style="color:#AA5500">        &quot;Image&quot;: &quot;sha256:2bc72079cf8d2db4d623f4814f15e052acd56eff67f6c15bb0c446bff70fedcf&quot;,</span>
<span style="color:#AA5500">        &quot;LogPath&quot;: &quot;/var/lib/docker/containers/a52cb1e63c491647f36ffa34d4b8f07a36c10bc016602fc4e00a7c03eb872c8b/a52cb1e63c491647f36ffa34d4b8f07a36c10bc016602fc4e00a7c03eb872c8b-json.log&quot;,</span>
<span style="color:#AA5500">        &quot;MountLabel&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">        &quot;Mounts&quot;: [</span>
<span style="color:#AA5500">            {</span>
<span style="color:#AA5500">                &quot;Destination&quot;: &quot;/config&quot;,</span>
<span style="color:#AA5500">                &quot;Mode&quot;: &quot;rw&quot;,</span>
<span style="color:#AA5500">                &quot;Propagation&quot;: &quot;rprivate&quot;,</span>
<span style="color:#AA5500">                &quot;RW&quot;: true,</span>
<span style="color:#AA5500">                &quot;Source&quot;: &quot;/mnt/Volume1/docker/jdownloader2/data&quot;,</span>
<span style="color:#AA5500">                &quot;Type&quot;: &quot;bind&quot;</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            {</span>
<span style="color:#AA5500">                &quot;Destination&quot;: &quot;/output&quot;,</span>
<span style="color:#AA5500">                &quot;Mode&quot;: &quot;rw&quot;,</span>
<span style="color:#AA5500">                &quot;Propagation&quot;: &quot;rprivate&quot;,</span>
<span style="color:#AA5500">                &quot;RW&quot;: true,</span>
<span style="color:#AA5500">                &quot;Source&quot;: &quot;/mnt/Volume1/local/Download/Production&quot;,</span>
<span style="color:#AA5500">                &quot;Type&quot;: &quot;bind&quot;</span>
<span style="color:#AA5500">            }</span>
<span style="color:#AA5500">        ],</span>
<span style="color:#AA5500">        &quot;Name&quot;: &quot;/jdownloader2&quot;,</span>
<span style="color:#AA5500">        &quot;NetworkSettings&quot;: {</span>
<span style="color:#AA5500">            &quot;Bridge&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;EndpointID&quot;: &quot;e142d129e8dc596b6322eb149e9f75acad02bfacbd97f27c3b85bb903108091c&quot;,</span>
<span style="color:#AA5500">            &quot;Gateway&quot;: &quot;172.17.0.1&quot;,</span>
<span style="color:#AA5500">            &quot;GlobalIPv6Address&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;GlobalIPv6PrefixLen&quot;: 0,</span>
<span style="color:#AA5500">            &quot;HairpinMode&quot;: false,</span>
<span style="color:#AA5500">            &quot;IPAddress&quot;: &quot;172.17.0.11&quot;,</span>
<span style="color:#AA5500">            &quot;IPPrefixLen&quot;: 16,</span>
<span style="color:#AA5500">            &quot;IPv6Gateway&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;LinkLocalIPv6Address&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;LinkLocalIPv6PrefixLen&quot;: 0,</span>
<span style="color:#AA5500">            &quot;MacAddress&quot;: &quot;b2:9a:7f:45:4f:69&quot;,</span>
<span style="color:#AA5500">            &quot;Networks&quot;: {</span>
<span style="color:#AA5500">                &quot;bridge&quot;: {</span>
<span style="color:#AA5500">                    &quot;Aliases&quot;: null,</span>
<span style="color:#AA5500">                    &quot;DNSNames&quot;: null,</span>
<span style="color:#AA5500">                    &quot;DriverOpts&quot;: null,</span>
<span style="color:#AA5500">                    &quot;EndpointID&quot;: &quot;e142d129e8dc596b6322eb149e9f75acad02bfacbd97f27c3b85bb903108091c&quot;,</span>
<span style="color:#AA5500">                    &quot;Gateway&quot;: &quot;172.17.0.1&quot;,</span>
<span style="color:#AA5500">                    &quot;GlobalIPv6Address&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">                    &quot;GlobalIPv6PrefixLen&quot;: 0,</span>
<span style="color:#AA5500">                    &quot;GwPriority&quot;: 0,</span>
<span style="color:#AA5500">                    &quot;IPAMConfig&quot;: null,</span>
<span style="color:#AA5500">                    &quot;IPAddress&quot;: &quot;172.17.0.11&quot;,</span>
<span style="color:#AA5500">                    &quot;IPPrefixLen&quot;: 16,</span>
<span style="color:#AA5500">                    &quot;IPv6Gateway&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">                    &quot;Links&quot;: null,</span>
<span style="color:#AA5500">                    &quot;MacAddress&quot;: &quot;b2:9a:7f:45:4f:69&quot;,</span>
<span style="color:#AA5500">                    &quot;NetworkID&quot;: &quot;fce42755ebf1352d21e037493e0c33a917b08a8fe5d9ea19e3af1d873ab69e67&quot;</span>
<span style="color:#AA5500">                }</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            &quot;Ports&quot;: {</span>
<span style="color:#AA5500">                &quot;3129/tcp&quot;: null,</span>
<span style="color:#AA5500">                &quot;5800/tcp&quot;: [</span>
<span style="color:#AA5500">                    {</span>
<span style="color:#AA5500">                        &quot;HostIp&quot;: &quot;0.0.0.0&quot;,</span>
<span style="color:#AA5500">                        &quot;HostPort&quot;: &quot;5800&quot;</span>
<span style="color:#AA5500">                    }</span>
<span style="color:#AA5500">                ],</span>
<span style="color:#AA5500">                &quot;5900/tcp&quot;: null</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            &quot;SandboxID&quot;: &quot;b0e92d5c017b942ac744a59d9da414fdf15d1ece4ed47d347c63b508a9da84f7&quot;,</span>
<span style="color:#AA5500">            &quot;SandboxKey&quot;: &quot;/var/run/docker/netns/b0e92d5c017b&quot;,</span>
<span style="color:#AA5500">            &quot;SecondaryIPAddresses&quot;: null,</span>
<span style="color:#AA5500">            &quot;SecondaryIPv6Addresses&quot;: null</span>
<span style="color:#AA5500">        },</span>
<span style="color:#AA5500">        &quot;Path&quot;: &quot;/init&quot;,</span>
<span style="color:#AA5500">        &quot;Platform&quot;: &quot;linux&quot;,</span>
<span style="color:#AA5500">        &quot;ProcessLabel&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">        &quot;ResolvConfPath&quot;: &quot;/var/lib/docker/containers/a52cb1e63c491647f36ffa34d4b8f07a36c10bc016602fc4e00a7c03eb872c8b/resolv.conf&quot;,</span>
<span style="color:#AA5500">        &quot;RestartCount&quot;: 0,</span>
<span style="color:#AA5500">        &quot;State&quot;: {</span>
<span style="color:#AA5500">            &quot;Dead&quot;: false,</span>
<span style="color:#AA5500">            &quot;Error&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;ExitCode&quot;: 0,</span>
<span style="color:#AA5500">            &quot;FinishedAt&quot;: &quot;2025-10-10T04:02:47.238761727Z&quot;,</span>
<span style="color:#AA5500">            &quot;OOMKilled&quot;: false,</span>
<span style="color:#AA5500">            &quot;Paused&quot;: false,</span>
<span style="color:#AA5500">            &quot;Pid&quot;: 2127155,</span>
<span style="color:#AA5500">            &quot;Restarting&quot;: false,</span>
<span style="color:#AA5500">            &quot;Running&quot;: true,</span>
<span style="color:#AA5500">            &quot;StartedAt&quot;: &quot;2025-10-10T04:02:54.038084527Z&quot;,</span>
<span style="color:#AA5500">            &quot;Status&quot;: &quot;running&quot;</span>
<span style="color:#AA5500">        }</span>
<span style="color:#AA5500">    }</span>
<span style="color:#AA5500">}</span>
Freitag 10 Oktober 2025  23:18:20 +0200 (0:00:00.704)       0:01:45.469 ******* 
Freitag 10 Oktober 2025  23:18:20 +0200 (0:00:00.062)       0:01:45.531 ******* 
Freitag 10 Oktober 2025  23:18:20 +0200 (0:00:00.051)       0:01:45.583 ******* 
Freitag 10 Oktober 2025  23:18:20 +0200 (0:00:00.050)       0:01:45.633 ******* 

TASK [jellyfin : Stop jellyfin] ***********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/jellyfin/tasks/main.yml:52</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:18:21 +0200 (0:00:00.656)       0:01:46.289 ******* 
Freitag 10 Oktober 2025  23:18:21 +0200 (0:00:00.069)       0:01:46.359 ******* 
Freitag 10 Oktober 2025  23:18:21 +0200 (0:00:00.046)       0:01:46.405 ******* 
Freitag 10 Oktober 2025  23:18:21 +0200 (0:00:00.045)       0:01:46.450 ******* 
Freitag 10 Oktober 2025  23:18:21 +0200 (0:00:00.053)       0:01:46.504 ******* 

TASK [joomla : Stop Joomla] ***************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/joomla/tasks/main.yml:62</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:18:22 +0200 (0:00:00.757)       0:01:47.261 ******* 

TASK [joomla : Stop Joomla DB] ************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/joomla/tasks/main.yml:66</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:18:23 +0200 (0:00:00.658)       0:01:47.919 ******* 
Freitag 10 Oktober 2025  23:18:23 +0200 (0:00:00.055)       0:01:47.975 ******* 
Freitag 10 Oktober 2025  23:18:23 +0200 (0:00:00.043)       0:01:48.019 ******* 

TASK [komga : Stop Komga] *****************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/komga/tasks/main.yml:42</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:18:23 +0200 (0:00:00.594)       0:01:48.614 ******* 
Freitag 10 Oktober 2025  23:18:23 +0200 (0:00:00.051)       0:01:48.665 ******* 
Freitag 10 Oktober 2025  23:18:23 +0200 (0:00:00.043)       0:01:48.708 ******* 

TASK [krusader : Stop Krusader] ***********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/krusader/tasks/main.yml:43</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:18:24 +0200 (0:00:00.653)       0:01:49.362 ******* 
Freitag 10 Oktober 2025  23:18:24 +0200 (0:00:00.042)       0:01:49.404 ******* 
Freitag 10 Oktober 2025  23:18:24 +0200 (0:00:00.045)       0:01:49.449 ******* 

TASK [lidarr : Stop Lidarr] ***************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/lidarr/tasks/main.yml:37</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:18:25 +0200 (0:00:00.653)       0:01:50.103 ******* 
Freitag 10 Oktober 2025  23:18:25 +0200 (0:00:00.049)       0:01:50.152 ******* 
Freitag 10 Oktober 2025  23:18:25 +0200 (0:00:00.042)       0:01:50.194 ******* 
Freitag 10 Oktober 2025  23:18:25 +0200 (0:00:00.240)       0:01:50.435 ******* 
Freitag 10 Oktober 2025  23:18:25 +0200 (0:00:00.049)       0:01:50.484 ******* 
Freitag 10 Oktober 2025  23:18:25 +0200 (0:00:00.054)       0:01:50.539 ******* 
Freitag 10 Oktober 2025  23:18:25 +0200 (0:00:00.048)       0:01:50.587 ******* 
Freitag 10 Oktober 2025  23:18:25 +0200 (0:00:00.054)       0:01:50.642 ******* 
Freitag 10 Oktober 2025  23:18:25 +0200 (0:00:00.049)       0:01:50.691 ******* 

TASK [loki : Stop loki] *******************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/loki/tasks/main.yml:74</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:18:26 +0200 (0:00:00.634)       0:01:51.325 ******* 
Freitag 10 Oktober 2025  23:18:26 +0200 (0:00:00.066)       0:01:51.392 ******* 
Freitag 10 Oktober 2025  23:18:26 +0200 (0:00:00.048)       0:01:51.440 ******* 

TASK [mealie : Stop Mealie] ***************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/mealie/tasks/main.yml:44</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:18:27 +0200 (0:00:00.644)       0:01:52.084 ******* 
Freitag 10 Oktober 2025  23:18:27 +0200 (0:00:00.058)       0:01:52.143 ******* 
Freitag 10 Oktober 2025  23:18:27 +0200 (0:00:00.042)       0:01:52.186 ******* 

TASK [mediathekview : Stop Mediathekview] *************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/mediathekview/tasks/main.yml:41</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:18:28 +0200 (0:00:00.644)       0:01:52.831 ******* 
Freitag 10 Oktober 2025  23:18:28 +0200 (0:00:00.174)       0:01:53.006 ******* 
Freitag 10 Oktober 2025  23:18:28 +0200 (0:00:00.044)       0:01:53.051 ******* 

TASK [minecraft-bedrock-server : Stop Minecraft Bedrock Server] ***************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/minecraft-bedrock-server/tasks/main.yml:34</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:18:28 +0200 (0:00:00.613)       0:01:53.664 ******* 
Freitag 10 Oktober 2025  23:18:28 +0200 (0:00:00.050)       0:01:53.715 ******* 
Freitag 10 Oktober 2025  23:18:28 +0200 (0:00:00.047)       0:01:53.762 ******* 

TASK [minecraft-server : Stop Minecraft Server] *******************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/minecraft-server/tasks/main.yml:27</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:18:29 +0200 (0:00:00.637)       0:01:54.399 ******* 
Freitag 10 Oktober 2025  23:18:29 +0200 (0:00:00.049)       0:01:54.448 ******* 

TASK [minidlna : Stop MiniDLNA] ***********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/minidlna/tasks/main.yml:24</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:18:30 +0200 (0:00:00.614)       0:01:55.063 ******* 
Freitag 10 Oktober 2025  23:18:30 +0200 (0:00:00.049)       0:01:55.113 ******* 
Freitag 10 Oktober 2025  23:18:30 +0200 (0:00:00.047)       0:01:55.160 ******* 
Freitag 10 Oktober 2025  23:18:30 +0200 (0:00:00.049)       0:01:55.210 ******* 
Freitag 10 Oktober 2025  23:18:30 +0200 (0:00:00.042)       0:01:55.253 ******* 

TASK [miniflux : Stop Miniflux] ***********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/miniflux/tasks/main.yml:60</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:18:31 +0200 (0:00:00.679)       0:01:55.933 ******* 
Freitag 10 Oktober 2025  23:18:31 +0200 (0:00:00.285)       0:01:56.219 ******* 
Freitag 10 Oktober 2025  23:18:31 +0200 (0:00:00.044)       0:01:56.264 ******* 

TASK [minio : Stop minio] *****************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/minio/tasks/main.yml:40</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:18:32 +0200 (0:00:00.662)       0:01:56.926 ******* 

TASK [mosquitto : Create Mosquitto Directories] *******************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/mosquitto/tasks/main.yml:4</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; (item=/mnt/Volume1/docker/mosquitto/config) =&gt; {</span>
<span style="color:#00AA00">    &quot;ansible_loop_var&quot;: &quot;item&quot;,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;gid&quot;: 1001,</span>
<span style="color:#00AA00">    &quot;group&quot;: &quot;ansible-nas&quot;,</span>
<span style="color:#00AA00">    &quot;item&quot;: &quot;/mnt/Volume1/docker/mosquitto/config&quot;,</span>
<span style="color:#00AA00">    &quot;mode&quot;: &quot;0777&quot;,</span>
<span style="color:#00AA00">    &quot;owner&quot;: &quot;1001&quot;,</span>
<span style="color:#00AA00">    &quot;path&quot;: &quot;/mnt/Volume1/docker/mosquitto/config&quot;,</span>
<span style="color:#00AA00">    &quot;size&quot;: 4096,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;directory&quot;,</span>
<span style="color:#00AA00">    &quot;uid&quot;: 1001</span>
<span style="color:#00AA00">}</span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; (item=/mnt/Volume1/docker/mosquitto/data) =&gt; {</span>
<span style="color:#00AA00">    &quot;ansible_loop_var&quot;: &quot;item&quot;,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;gid&quot;: 1883,</span>
<span style="color:#00AA00">    &quot;group&quot;: &quot;1883&quot;,</span>
<span style="color:#00AA00">    &quot;item&quot;: &quot;/mnt/Volume1/docker/mosquitto/data&quot;,</span>
<span style="color:#00AA00">    &quot;mode&quot;: &quot;0777&quot;,</span>
<span style="color:#00AA00">    &quot;owner&quot;: &quot;1883&quot;,</span>
<span style="color:#00AA00">    &quot;path&quot;: &quot;/mnt/Volume1/docker/mosquitto/data&quot;,</span>
<span style="color:#00AA00">    &quot;size&quot;: 4096,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;directory&quot;,</span>
<span style="color:#00AA00">    &quot;uid&quot;: 1883</span>
<span style="color:#00AA00">}</span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; (item=/mnt/Volume1/docker/mosquitto/log) =&gt; {</span>
<span style="color:#00AA00">    &quot;ansible_loop_var&quot;: &quot;item&quot;,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;gid&quot;: 1883,</span>
<span style="color:#00AA00">    &quot;group&quot;: &quot;1883&quot;,</span>
<span style="color:#00AA00">    &quot;item&quot;: &quot;/mnt/Volume1/docker/mosquitto/log&quot;,</span>
<span style="color:#00AA00">    &quot;mode&quot;: &quot;0777&quot;,</span>
<span style="color:#00AA00">    &quot;owner&quot;: &quot;1883&quot;,</span>
<span style="color:#00AA00">    &quot;path&quot;: &quot;/mnt/Volume1/docker/mosquitto/log&quot;,</span>
<span style="color:#00AA00">    &quot;size&quot;: 4096,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;directory&quot;,</span>
<span style="color:#00AA00">    &quot;uid&quot;: 1883</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:18:33 +0200 (0:00:01.017)       0:01:57.944 ******* 

TASK [mosquitto : Template mosquitto.conf] ************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/mosquitto/tasks/main.yml:13</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;checksum&quot;: &quot;68794448b73372a6b2b84c838da039a63c200033&quot;,</span>
<span style="color:#00AA00">    &quot;dest&quot;: &quot;/mnt/Volume1/docker/mosquitto/config/mosquitto.conf&quot;,</span>
<span style="color:#00AA00">    &quot;gid&quot;: 1883,</span>
<span style="color:#00AA00">    &quot;group&quot;: &quot;1883&quot;,</span>
<span style="color:#00AA00">    &quot;mode&quot;: &quot;0777&quot;,</span>
<span style="color:#00AA00">    &quot;owner&quot;: &quot;1883&quot;,</span>
<span style="color:#00AA00">    &quot;path&quot;: &quot;/mnt/Volume1/docker/mosquitto/config/mosquitto.conf&quot;,</span>
<span style="color:#00AA00">    &quot;size&quot;: 158,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;file&quot;,</span>
<span style="color:#00AA00">    &quot;uid&quot;: 1883</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:18:33 +0200 (0:00:00.603)       0:01:58.548 ******* 

TASK [mosquitto : Create Mosquitto container] *********************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/mosquitto/tasks/main.yml:19</b></span>
<span style="color:#AA5500">changed: [ansible-nas] =&gt; {</span>
<span style="color:#AA5500">    &quot;changed&quot;: true,</span>
<span style="color:#AA5500">    &quot;container&quot;: {</span>
<span style="color:#AA5500">        &quot;AppArmorProfile&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">        &quot;Args&quot;: [</span>
<span style="color:#AA5500">            &quot;/usr/sbin/mosquitto&quot;,</span>
<span style="color:#AA5500">            &quot;-c&quot;,</span>
<span style="color:#AA5500">            &quot;/mosquitto/config/mosquitto.conf&quot;</span>
<span style="color:#AA5500">        ],</span>
<span style="color:#AA5500">        &quot;Config&quot;: {</span>
<span style="color:#AA5500">            &quot;AttachStderr&quot;: true,</span>
<span style="color:#AA5500">            &quot;AttachStdin&quot;: false,</span>
<span style="color:#AA5500">            &quot;AttachStdout&quot;: true,</span>
<span style="color:#AA5500">            &quot;Cmd&quot;: [</span>
<span style="color:#AA5500">                &quot;/usr/sbin/mosquitto&quot;,</span>
<span style="color:#AA5500">                &quot;-c&quot;,</span>
<span style="color:#AA5500">                &quot;/mosquitto/config/mosquitto.conf&quot;</span>
<span style="color:#AA5500">            ],</span>
<span style="color:#AA5500">            &quot;Domainname&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;Entrypoint&quot;: [</span>
<span style="color:#AA5500">                &quot;/docker-entrypoint.sh&quot;</span>
<span style="color:#AA5500">            ],</span>
<span style="color:#AA5500">            &quot;Env&quot;: [</span>
<span style="color:#AA5500">                &quot;PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin&quot;,</span>
<span style="color:#AA5500">                &quot;VERSION=2.0.22&quot;,</span>
<span style="color:#AA5500">                &quot;DOWNLOAD_SHA256=2f752589ef7db40260b633fbdb536e9a04b446a315138d64a7ff3c14e2de6b68&quot;,</span>
<span style="color:#AA5500">                &quot;GPG_KEYS=A0D6EEA1DCAE49A635A3B2F0779B22DFB3E717B7&quot;,</span>
<span style="color:#AA5500">                &quot;LWS_VERSION=4.2.1&quot;,</span>
<span style="color:#AA5500">                &quot;LWS_SHA256=842da21f73ccba2be59e680de10a8cce7928313048750eb6ad73b6fa50763c51&quot;</span>
<span style="color:#AA5500">            ],</span>
<span style="color:#AA5500">            &quot;ExposedPorts&quot;: {</span>
<span style="color:#AA5500">                &quot;1883/tcp&quot;: {},</span>
<span style="color:#AA5500">                &quot;9001/tcp&quot;: {}</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            &quot;Hostname&quot;: &quot;e14ceb9cf44e&quot;,</span>
<span style="color:#AA5500">            &quot;Image&quot;: &quot;eclipse-mosquitto:latest&quot;,</span>
<span style="color:#AA5500">            &quot;Labels&quot;: {</span>
<span style="color:#AA5500">                &quot;description&quot;: &quot;Eclipse Mosquitto MQTT Broker&quot;,</span>
<span style="color:#AA5500">                &quot;maintainer&quot;: &quot;Roger Light &lt;roger@atchoo.org&gt;&quot;</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            &quot;OnBuild&quot;: null,</span>
<span style="color:#AA5500">            &quot;OpenStdin&quot;: false,</span>
<span style="color:#AA5500">            &quot;StdinOnce&quot;: false,</span>
<span style="color:#AA5500">            &quot;Tty&quot;: false,</span>
<span style="color:#AA5500">            &quot;User&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;Volumes&quot;: {</span>
<span style="color:#AA5500">                &quot;/mosquitto/data&quot;: {},</span>
<span style="color:#AA5500">                &quot;/mosquitto/log&quot;: {}</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            &quot;WorkingDir&quot;: &quot;/&quot;</span>
<span style="color:#AA5500">        },</span>
<span style="color:#AA5500">        &quot;Created&quot;: &quot;2025-10-09T16:53:20.303370084Z&quot;,</span>
<span style="color:#AA5500">        &quot;Driver&quot;: &quot;overlay2&quot;,</span>
<span style="color:#AA5500">        &quot;ExecIDs&quot;: null,</span>
<span style="color:#AA5500">        &quot;GraphDriver&quot;: {</span>
<span style="color:#AA5500">            &quot;Data&quot;: {</span>
<span style="color:#AA5500">                &quot;ID&quot;: &quot;e14ceb9cf44e7edc6c5062a35c29838155756872d7996a016efb5d99009815b5&quot;,</span>
<span style="color:#AA5500">                &quot;LowerDir&quot;: &quot;/var/lib/docker/overlay2/e9fe49a16c8d7d9b5c1cc9092c2f7ad831230c8c7ef362ae5d693964157894a6-init/diff:/var/lib/docker/overlay2/9a2beaae812d37e6f278ce8a905a11422c0bb774af7ad33849dcfd75d922059d/diff:/var/lib/docker/overlay2/d32b69d4943bdbd4fe02fb0e86e6075a5111727087dc6c8526064c44f6e099e5/diff:/var/lib/docker/overlay2/078e88580e265b928e0f4cc8b0a667035fd887eb9e6e5f614e402d30c8689360/diff&quot;,</span>
<span style="color:#AA5500">                &quot;MergedDir&quot;: &quot;/var/lib/docker/overlay2/e9fe49a16c8d7d9b5c1cc9092c2f7ad831230c8c7ef362ae5d693964157894a6/merged&quot;,</span>
<span style="color:#AA5500">                &quot;UpperDir&quot;: &quot;/var/lib/docker/overlay2/e9fe49a16c8d7d9b5c1cc9092c2f7ad831230c8c7ef362ae5d693964157894a6/diff&quot;,</span>
<span style="color:#AA5500">                &quot;WorkDir&quot;: &quot;/var/lib/docker/overlay2/e9fe49a16c8d7d9b5c1cc9092c2f7ad831230c8c7ef362ae5d693964157894a6/work&quot;</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            &quot;Name&quot;: &quot;overlay2&quot;</span>
<span style="color:#AA5500">        },</span>
<span style="color:#AA5500">        &quot;HostConfig&quot;: {</span>
<span style="color:#AA5500">            &quot;AutoRemove&quot;: false,</span>
<span style="color:#AA5500">            &quot;Binds&quot;: [</span>
<span style="color:#AA5500">                &quot;/mnt/Volume1/docker/mosquitto/config/mosquitto.conf:/mosquitto/config/mosquitto.conf:rw&quot;,</span>
<span style="color:#AA5500">                &quot;/mnt/Volume1/docker/mosquitto/data:/mosquitto/data:rw&quot;,</span>
<span style="color:#AA5500">                &quot;/mnt/Volume1/docker/mosquitto/log:/mosquitto/log:rw&quot;</span>
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
<span style="color:#AA5500">                &quot;1883/tcp&quot;: [</span>
<span style="color:#AA5500">                    {</span>
<span style="color:#AA5500">                        &quot;HostIp&quot;: &quot;0.0.0.0&quot;,</span>
<span style="color:#AA5500">                        &quot;HostPort&quot;: &quot;1883&quot;</span>
<span style="color:#AA5500">                    }</span>
<span style="color:#AA5500">                ],</span>
<span style="color:#AA5500">                &quot;9001/tcp&quot;: [</span>
<span style="color:#AA5500">                    {</span>
<span style="color:#AA5500">                        &quot;HostIp&quot;: &quot;0.0.0.0&quot;,</span>
<span style="color:#AA5500">                        &quot;HostPort&quot;: &quot;9001&quot;</span>
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
<span style="color:#AA5500">        &quot;HostnamePath&quot;: &quot;/var/lib/docker/containers/e14ceb9cf44e7edc6c5062a35c29838155756872d7996a016efb5d99009815b5/hostname&quot;,</span>
<span style="color:#AA5500">        &quot;HostsPath&quot;: &quot;/var/lib/docker/containers/e14ceb9cf44e7edc6c5062a35c29838155756872d7996a016efb5d99009815b5/hosts&quot;,</span>
<span style="color:#AA5500">        &quot;Id&quot;: &quot;e14ceb9cf44e7edc6c5062a35c29838155756872d7996a016efb5d99009815b5&quot;,</span>
<span style="color:#AA5500">        &quot;Image&quot;: &quot;sha256:1ff56399ec742b8b9f27119457381f050d5db35c501f54e9f1db5433963c7352&quot;,</span>
<span style="color:#AA5500">        &quot;LogPath&quot;: &quot;/var/lib/docker/containers/e14ceb9cf44e7edc6c5062a35c29838155756872d7996a016efb5d99009815b5/e14ceb9cf44e7edc6c5062a35c29838155756872d7996a016efb5d99009815b5-json.log&quot;,</span>
<span style="color:#AA5500">        &quot;MountLabel&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">        &quot;Mounts&quot;: [</span>
<span style="color:#AA5500">            {</span>
<span style="color:#AA5500">                &quot;Destination&quot;: &quot;/mosquitto/data&quot;,</span>
<span style="color:#AA5500">                &quot;Mode&quot;: &quot;rw&quot;,</span>
<span style="color:#AA5500">                &quot;Propagation&quot;: &quot;rprivate&quot;,</span>
<span style="color:#AA5500">                &quot;RW&quot;: true,</span>
<span style="color:#AA5500">                &quot;Source&quot;: &quot;/mnt/Volume1/docker/mosquitto/data&quot;,</span>
<span style="color:#AA5500">                &quot;Type&quot;: &quot;bind&quot;</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            {</span>
<span style="color:#AA5500">                &quot;Destination&quot;: &quot;/mosquitto/log&quot;,</span>
<span style="color:#AA5500">                &quot;Mode&quot;: &quot;rw&quot;,</span>
<span style="color:#AA5500">                &quot;Propagation&quot;: &quot;rprivate&quot;,</span>
<span style="color:#AA5500">                &quot;RW&quot;: true,</span>
<span style="color:#AA5500">                &quot;Source&quot;: &quot;/mnt/Volume1/docker/mosquitto/log&quot;,</span>
<span style="color:#AA5500">                &quot;Type&quot;: &quot;bind&quot;</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            {</span>
<span style="color:#AA5500">                &quot;Destination&quot;: &quot;/mosquitto/config/mosquitto.conf&quot;,</span>
<span style="color:#AA5500">                &quot;Mode&quot;: &quot;rw&quot;,</span>
<span style="color:#AA5500">                &quot;Propagation&quot;: &quot;rprivate&quot;,</span>
<span style="color:#AA5500">                &quot;RW&quot;: true,</span>
<span style="color:#AA5500">                &quot;Source&quot;: &quot;/mnt/Volume1/docker/mosquitto/config/mosquitto.conf&quot;,</span>
<span style="color:#AA5500">                &quot;Type&quot;: &quot;bind&quot;</span>
<span style="color:#AA5500">            }</span>
<span style="color:#AA5500">        ],</span>
<span style="color:#AA5500">        &quot;Name&quot;: &quot;/mosquitto&quot;,</span>
<span style="color:#AA5500">        &quot;NetworkSettings&quot;: {</span>
<span style="color:#AA5500">            &quot;Bridge&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;EndpointID&quot;: &quot;075b7353dd373bf72b5b1dd0cf03874d585017312278c72d8de6f406c5994069&quot;,</span>
<span style="color:#AA5500">            &quot;Gateway&quot;: &quot;172.17.0.1&quot;,</span>
<span style="color:#AA5500">            &quot;GlobalIPv6Address&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;GlobalIPv6PrefixLen&quot;: 0,</span>
<span style="color:#AA5500">            &quot;HairpinMode&quot;: false,</span>
<span style="color:#AA5500">            &quot;IPAddress&quot;: &quot;172.17.0.2&quot;,</span>
<span style="color:#AA5500">            &quot;IPPrefixLen&quot;: 16,</span>
<span style="color:#AA5500">            &quot;IPv6Gateway&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;LinkLocalIPv6Address&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;LinkLocalIPv6PrefixLen&quot;: 0,</span>
<span style="color:#AA5500">            &quot;MacAddress&quot;: &quot;7e:fe:c6:be:5f:66&quot;,</span>
<span style="color:#AA5500">            &quot;Networks&quot;: {</span>
<span style="color:#AA5500">                &quot;bridge&quot;: {</span>
<span style="color:#AA5500">                    &quot;Aliases&quot;: null,</span>
<span style="color:#AA5500">                    &quot;DNSNames&quot;: null,</span>
<span style="color:#AA5500">                    &quot;DriverOpts&quot;: null,</span>
<span style="color:#AA5500">                    &quot;EndpointID&quot;: &quot;075b7353dd373bf72b5b1dd0cf03874d585017312278c72d8de6f406c5994069&quot;,</span>
<span style="color:#AA5500">                    &quot;Gateway&quot;: &quot;172.17.0.1&quot;,</span>
<span style="color:#AA5500">                    &quot;GlobalIPv6Address&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">                    &quot;GlobalIPv6PrefixLen&quot;: 0,</span>
<span style="color:#AA5500">                    &quot;GwPriority&quot;: 0,</span>
<span style="color:#AA5500">                    &quot;IPAMConfig&quot;: null,</span>
<span style="color:#AA5500">                    &quot;IPAddress&quot;: &quot;172.17.0.2&quot;,</span>
<span style="color:#AA5500">                    &quot;IPPrefixLen&quot;: 16,</span>
<span style="color:#AA5500">                    &quot;IPv6Gateway&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">                    &quot;Links&quot;: null,</span>
<span style="color:#AA5500">                    &quot;MacAddress&quot;: &quot;7e:fe:c6:be:5f:66&quot;,</span>
<span style="color:#AA5500">                    &quot;NetworkID&quot;: &quot;fce42755ebf1352d21e037493e0c33a917b08a8fe5d9ea19e3af1d873ab69e67&quot;</span>
<span style="color:#AA5500">                }</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            &quot;Ports&quot;: {</span>
<span style="color:#AA5500">                &quot;1883/tcp&quot;: [</span>
<span style="color:#AA5500">                    {</span>
<span style="color:#AA5500">                        &quot;HostIp&quot;: &quot;0.0.0.0&quot;,</span>
<span style="color:#AA5500">                        &quot;HostPort&quot;: &quot;1883&quot;</span>
<span style="color:#AA5500">                    }</span>
<span style="color:#AA5500">                ],</span>
<span style="color:#AA5500">                &quot;9001/tcp&quot;: [</span>
<span style="color:#AA5500">                    {</span>
<span style="color:#AA5500">                        &quot;HostIp&quot;: &quot;0.0.0.0&quot;,</span>
<span style="color:#AA5500">                        &quot;HostPort&quot;: &quot;9001&quot;</span>
<span style="color:#AA5500">                    }</span>
<span style="color:#AA5500">                ]</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            &quot;SandboxID&quot;: &quot;3656e82b7165ae4621b39da45ece109b20c2615be6b74ea01b50b67928a3055a&quot;,</span>
<span style="color:#AA5500">            &quot;SandboxKey&quot;: &quot;/var/run/docker/netns/3656e82b7165&quot;,</span>
<span style="color:#AA5500">            &quot;SecondaryIPAddresses&quot;: null,</span>
<span style="color:#AA5500">            &quot;SecondaryIPv6Addresses&quot;: null</span>
<span style="color:#AA5500">        },</span>
<span style="color:#AA5500">        &quot;Path&quot;: &quot;/docker-entrypoint.sh&quot;,</span>
<span style="color:#AA5500">        &quot;Platform&quot;: &quot;linux&quot;,</span>
<span style="color:#AA5500">        &quot;ProcessLabel&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">        &quot;ResolvConfPath&quot;: &quot;/var/lib/docker/containers/e14ceb9cf44e7edc6c5062a35c29838155756872d7996a016efb5d99009815b5/resolv.conf&quot;,</span>
<span style="color:#AA5500">        &quot;RestartCount&quot;: 0,</span>
<span style="color:#AA5500">        &quot;State&quot;: {</span>
<span style="color:#AA5500">            &quot;Dead&quot;: false,</span>
<span style="color:#AA5500">            &quot;Error&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;ExitCode&quot;: 0,</span>
<span style="color:#AA5500">            &quot;FinishedAt&quot;: &quot;2025-10-10T04:02:46.145342859Z&quot;,</span>
<span style="color:#AA5500">            &quot;OOMKilled&quot;: false,</span>
<span style="color:#AA5500">            &quot;Paused&quot;: false,</span>
<span style="color:#AA5500">            &quot;Pid&quot;: 2126761,</span>
<span style="color:#AA5500">            &quot;Restarting&quot;: false,</span>
<span style="color:#AA5500">            &quot;Running&quot;: true,</span>
<span style="color:#AA5500">            &quot;StartedAt&quot;: &quot;2025-10-10T04:02:53.963239474Z&quot;,</span>
<span style="color:#AA5500">            &quot;Status&quot;: &quot;running&quot;</span>
<span style="color:#AA5500">        }</span>
<span style="color:#AA5500">    }</span>
<span style="color:#AA5500">}</span>
Freitag 10 Oktober 2025  23:18:35 +0200 (0:00:01.790)       0:02:00.339 ******* 
Freitag 10 Oktober 2025  23:18:35 +0200 (0:00:00.070)       0:02:00.410 ******* 
Freitag 10 Oktober 2025  23:18:35 +0200 (0:00:00.046)       0:02:00.457 ******* 
Freitag 10 Oktober 2025  23:18:35 +0200 (0:00:00.048)       0:02:00.505 ******* 

TASK [mumble : Stop Mumble] ***************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/mumble/tasks/main.yml:39</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:18:36 +0200 (0:00:00.622)       0:02:01.128 ******* 
Freitag 10 Oktober 2025  23:18:36 +0200 (0:00:00.054)       0:02:01.182 ******* 
Freitag 10 Oktober 2025  23:18:36 +0200 (0:00:00.043)       0:02:01.226 ******* 

TASK [mylar : Stop Mylar] *****************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/mylar/tasks/main.yml:41</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:18:37 +0200 (0:00:00.779)       0:02:02.005 ******* 
Freitag 10 Oktober 2025  23:18:37 +0200 (0:00:00.058)       0:02:02.064 ******* 
Freitag 10 Oktober 2025  23:18:37 +0200 (0:00:00.042)       0:02:02.106 ******* 

TASK [mymediaforalexa : Stop Mymediaforalexa] *********************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/mymediaforalexa/tasks/main.yml:27</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:18:37 +0200 (0:00:00.637)       0:02:02.744 ******* 
Freitag 10 Oktober 2025  23:18:37 +0200 (0:00:00.053)       0:02:02.797 ******* 
Freitag 10 Oktober 2025  23:18:38 +0200 (0:00:00.054)       0:02:02.852 ******* 

TASK [n8n : Stop n8n] *********************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/n8n/tasks/main.yml:40</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:18:38 +0200 (0:00:00.619)       0:02:03.471 ******* 
Freitag 10 Oktober 2025  23:18:38 +0200 (0:00:00.061)       0:02:03.532 ******* 
Freitag 10 Oktober 2025  23:18:38 +0200 (0:00:00.043)       0:02:03.576 ******* 

TASK [navidrome : Stop Navidrome] *********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/navidrome/tasks/main.yml:42</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:18:39 +0200 (0:00:00.631)       0:02:04.207 ******* 
Freitag 10 Oktober 2025  23:18:39 +0200 (0:00:00.058)       0:02:04.266 ******* 
Freitag 10 Oktober 2025  23:18:39 +0200 (0:00:00.041)       0:02:04.308 ******* 

TASK [netbootxyz : Stop Netbootxyz] *******************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/netbootxyz/tasks/main.yml:41</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:18:40 +0200 (0:00:00.723)       0:02:05.031 ******* 
Freitag 10 Oktober 2025  23:18:40 +0200 (0:00:00.042)       0:02:05.074 ******* 
Freitag 10 Oktober 2025  23:18:40 +0200 (0:00:00.048)       0:02:05.122 ******* 

TASK [netdata : Stop Netdata] *************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/netdata/tasks/main.yml:41</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:18:40 +0200 (0:00:00.616)       0:02:05.738 ******* 
Freitag 10 Oktober 2025  23:18:40 +0200 (0:00:00.061)       0:02:05.799 ******* 
Freitag 10 Oktober 2025  23:18:41 +0200 (0:00:00.045)       0:02:05.845 ******* 
Freitag 10 Oktober 2025  23:18:41 +0200 (0:00:00.055)       0:02:05.901 ******* 
Freitag 10 Oktober 2025  23:18:41 +0200 (0:00:00.060)       0:02:05.961 ******* 

TASK [nextcloud : Stop Nextcloud] *********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/nextcloud/tasks/main.yml:72</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:18:41 +0200 (0:00:00.603)       0:02:06.564 ******* 

TASK [nextcloud : Stop Nextcloud DB] ******************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/nextcloud/tasks/main.yml:76</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:18:42 +0200 (0:00:00.637)       0:02:07.202 ******* 
Freitag 10 Oktober 2025  23:18:42 +0200 (0:00:00.048)       0:02:07.250 ******* 
Freitag 10 Oktober 2025  23:18:42 +0200 (0:00:00.045)       0:02:07.296 ******* 
Freitag 10 Oktober 2025  23:18:42 +0200 (0:00:00.047)       0:02:07.343 ******* 
Freitag 10 Oktober 2025  23:18:42 +0200 (0:00:00.042)       0:02:07.386 ******* 
Freitag 10 Oktober 2025  23:18:42 +0200 (0:00:00.045)       0:02:07.432 ******* 

TASK [nomad : Check if Nomad is installed] ************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/nomad/tasks/main.yml:37</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;stat&quot;: {</span>
<span style="color:#00AA00">        &quot;exists&quot;: false</span>
<span style="color:#00AA00">    }</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:18:43 +0200 (0:00:00.469)       0:02:07.901 ******* 
Freitag 10 Oktober 2025  23:18:43 +0200 (0:00:00.050)       0:02:07.952 ******* 
Freitag 10 Oktober 2025  23:18:43 +0200 (0:00:00.067)       0:02:08.020 ******* 
Freitag 10 Oktober 2025  23:18:43 +0200 (0:00:00.049)       0:02:08.070 ******* 
Freitag 10 Oktober 2025  23:18:43 +0200 (0:00:00.044)       0:02:08.115 ******* 

TASK [nzbget : Stop NZBget] ***************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/nzbget/tasks/main.yml:38</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:18:43 +0200 (0:00:00.609)       0:02:08.724 ******* 
Freitag 10 Oktober 2025  23:18:43 +0200 (0:00:00.060)       0:02:08.785 ******* 
Freitag 10 Oktober 2025  23:18:44 +0200 (0:00:00.047)       0:02:08.833 ******* 

TASK [octoprint : Stop Octoprint] *********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/octoprint/tasks/main.yml:40</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:18:44 +0200 (0:00:00.628)       0:02:09.462 ******* 
Freitag 10 Oktober 2025  23:18:44 +0200 (0:00:00.049)       0:02:09.511 ******* 
Freitag 10 Oktober 2025  23:18:44 +0200 (0:00:00.043)       0:02:09.554 ******* 

TASK [ombi : Stop Ombi] *******************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/ombi/tasks/main.yml:35</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:18:45 +0200 (0:00:00.617)       0:02:10.172 ******* 
Freitag 10 Oktober 2025  23:18:45 +0200 (0:00:00.146)       0:02:10.318 ******* 
Freitag 10 Oktober 2025  23:18:45 +0200 (0:00:00.044)       0:02:10.362 ******* 
Freitag 10 Oktober 2025  23:18:45 +0200 (0:00:00.066)       0:02:10.428 ******* 
Freitag 10 Oktober 2025  23:18:45 +0200 (0:00:00.045)       0:02:10.474 ******* 

TASK [openhab : Stop openHAB] *************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/openhab/tasks/main.yml:60</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:18:46 +0200 (0:00:00.611)       0:02:11.085 ******* 
Freitag 10 Oktober 2025  23:18:46 +0200 (0:00:00.059)       0:02:11.145 ******* 
Freitag 10 Oktober 2025  23:18:46 +0200 (0:00:00.040)       0:02:11.186 ******* 

TASK [organizr : Stop Organizr] ***********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/organizr/tasks/main.yml:38</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:18:46 +0200 (0:00:00.607)       0:02:11.793 ******* 
Freitag 10 Oktober 2025  23:18:47 +0200 (0:00:00.068)       0:02:11.862 ******* 
Freitag 10 Oktober 2025  23:18:47 +0200 (0:00:00.062)       0:02:11.925 ******* 

TASK [overseerr : Stop Overseerr] *********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/overseerr/tasks/main.yml:43</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:18:47 +0200 (0:00:00.648)       0:02:12.573 ******* 
Freitag 10 Oktober 2025  23:18:47 +0200 (0:00:00.094)       0:02:12.668 ******* 
Freitag 10 Oktober 2025  23:18:47 +0200 (0:00:00.047)       0:02:12.715 ******* 
Freitag 10 Oktober 2025  23:18:47 +0200 (0:00:00.041)       0:02:12.756 ******* 
Freitag 10 Oktober 2025  23:18:48 +0200 (0:00:00.174)       0:02:12.931 ******* 
Freitag 10 Oktober 2025  23:18:48 +0200 (0:00:00.052)       0:02:12.983 ******* 

TASK [paperless_ng : Stop paperless_ng] ***************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/paperless_ng/tasks/main.yml:83</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:18:48 +0200 (0:00:00.579)       0:02:13.563 ******* 

TASK [paperless_ng : Stop paperless_ng redis] *********************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/paperless_ng/tasks/main.yml:87</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:18:49 +0200 (0:00:00.592)       0:02:14.155 ******* 

TASK [paperless_ng : Stop paperless_ng db] ************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/paperless_ng/tasks/main.yml:91</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:18:49 +0200 (0:00:00.601)       0:02:14.756 ******* 
Freitag 10 Oktober 2025  23:18:50 +0200 (0:00:00.070)       0:02:14.827 ******* 
Freitag 10 Oktober 2025  23:18:50 +0200 (0:00:00.062)       0:02:14.889 ******* 
Freitag 10 Oktober 2025  23:18:50 +0200 (0:00:00.049)       0:02:14.938 ******* 
Freitag 10 Oktober 2025  23:18:50 +0200 (0:00:00.057)       0:02:14.996 ******* 

TASK [piwigo : Stop Piwigo] ***************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/piwigo/tasks/main.yml:71</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:18:50 +0200 (0:00:00.596)       0:02:15.592 ******* 

TASK [piwigo : Stop Piwigo Db] ************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/piwigo/tasks/main.yml:75</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:18:51 +0200 (0:00:00.603)       0:02:16.196 ******* 
Freitag 10 Oktober 2025  23:18:51 +0200 (0:00:00.057)       0:02:16.253 ******* 
Freitag 10 Oktober 2025  23:18:51 +0200 (0:00:00.046)       0:02:16.300 ******* 

TASK [plex : Stop Plex] *******************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/plex/tasks/main.yml:51</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:18:52 +0200 (0:00:00.711)       0:02:17.011 ******* 
Freitag 10 Oktober 2025  23:18:52 +0200 (0:00:00.051)       0:02:17.063 ******* 

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
Freitag 10 Oktober 2025  23:18:52 +0200 (0:00:00.431)       0:02:17.495 ******* 

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
<span style="color:#AA5500">            &quot;Hostname&quot;: &quot;9e2dd406f701&quot;,</span>
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
<span style="color:#AA5500">        &quot;Created&quot;: &quot;2025-09-28T23:09:45.417956501Z&quot;,</span>
<span style="color:#AA5500">        &quot;Driver&quot;: &quot;overlay2&quot;,</span>
<span style="color:#AA5500">        &quot;ExecIDs&quot;: null,</span>
<span style="color:#AA5500">        &quot;GraphDriver&quot;: {</span>
<span style="color:#AA5500">            &quot;Data&quot;: {</span>
<span style="color:#AA5500">                &quot;ID&quot;: &quot;9e2dd406f701ba1fdf46bebb1f056f8ac0567163173c7dfe0d767498aa848597&quot;,</span>
<span style="color:#AA5500">                &quot;LowerDir&quot;: &quot;/var/lib/docker/overlay2/f0048059f37baba604b64324e99a592313f9c16476a88eab2b2e3f293d4bb577-init/diff:/var/lib/docker/overlay2/31cd9ad01add6855d89eaaff757a39ce03b4e7cb3e25298e401b77a4a035e1bc/diff:/var/lib/docker/overlay2/836a37d0634b9403b623ec0ecd176cfaf24fcfc5e159490aad55b44338ba0d40/diff:/var/lib/docker/overlay2/5bcae72c3adbc2a56f4c97a794199fd318208f73208f47ac4c17f8fccbac0435/diff:/var/lib/docker/overlay2/1e32b2747fda9795ee0b556147d8431bae46f01b36cb7838ea5545510b7662e8/diff:/var/lib/docker/overlay2/02d531b9f7ecc865be57767b872f2af3a75dce4c5bdc13380b8e7033913457c3/diff:/var/lib/docker/overlay2/b7ee2bb3c0b352ece0a920912a979ae7cdaebb9bd179a11ba4a226e23f24bca7/diff:/var/lib/docker/overlay2/32b91d3abd61218d0b8630ead4b6c03c8e805a8512920e27d9e6a61e4344521b/diff:/var/lib/docker/overlay2/7be1bdc8a767d1216aa90d30739a339f436dab2190431374582e38916a380d2e/diff&quot;,</span>
<span style="color:#AA5500">                &quot;MergedDir&quot;: &quot;/var/lib/docker/overlay2/f0048059f37baba604b64324e99a592313f9c16476a88eab2b2e3f293d4bb577/merged&quot;,</span>
<span style="color:#AA5500">                &quot;UpperDir&quot;: &quot;/var/lib/docker/overlay2/f0048059f37baba604b64324e99a592313f9c16476a88eab2b2e3f293d4bb577/diff&quot;,</span>
<span style="color:#AA5500">                &quot;WorkDir&quot;: &quot;/var/lib/docker/overlay2/f0048059f37baba604b64324e99a592313f9c16476a88eab2b2e3f293d4bb577/work&quot;</span>
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
<span style="color:#AA5500">        &quot;HostnamePath&quot;: &quot;/var/lib/docker/containers/9e2dd406f701ba1fdf46bebb1f056f8ac0567163173c7dfe0d767498aa848597/hostname&quot;,</span>
<span style="color:#AA5500">        &quot;HostsPath&quot;: &quot;/var/lib/docker/containers/9e2dd406f701ba1fdf46bebb1f056f8ac0567163173c7dfe0d767498aa848597/hosts&quot;,</span>
<span style="color:#AA5500">        &quot;Id&quot;: &quot;9e2dd406f701ba1fdf46bebb1f056f8ac0567163173c7dfe0d767498aa848597&quot;,</span>
<span style="color:#AA5500">        &quot;Image&quot;: &quot;sha256:f8f6fc245e620c66a0293093d1127256f0946d56328a516e6bc458bc5d613fce&quot;,</span>
<span style="color:#AA5500">        &quot;LogPath&quot;: &quot;/var/lib/docker/containers/9e2dd406f701ba1fdf46bebb1f056f8ac0567163173c7dfe0d767498aa848597/9e2dd406f701ba1fdf46bebb1f056f8ac0567163173c7dfe0d767498aa848597-json.log&quot;,</span>
<span style="color:#AA5500">        &quot;MountLabel&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">        &quot;Mounts&quot;: [</span>
<span style="color:#AA5500">            {</span>
<span style="color:#AA5500">                &quot;Destination&quot;: &quot;/data&quot;,</span>
<span style="color:#AA5500">                &quot;Mode&quot;: &quot;rw&quot;,</span>
<span style="color:#AA5500">                &quot;Propagation&quot;: &quot;rprivate&quot;,</span>
<span style="color:#AA5500">                &quot;RW&quot;: true,</span>
<span style="color:#AA5500">                &quot;Source&quot;: &quot;/mnt/Volume1/docker/portainer/config&quot;,</span>
<span style="color:#AA5500">                &quot;Type&quot;: &quot;bind&quot;</span>
<span style="color:#AA5500">            },</span>
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
<span style="color:#AA5500">            }</span>
<span style="color:#AA5500">        ],</span>
<span style="color:#AA5500">        &quot;Name&quot;: &quot;/portainer&quot;,</span>
<span style="color:#AA5500">        &quot;NetworkSettings&quot;: {</span>
<span style="color:#AA5500">            &quot;Bridge&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;EndpointID&quot;: &quot;639e1c0a192c9d51b9fdf3fe3fdeb77f0a533d0ee4d847dfa97bda30fbbdaa24&quot;,</span>
<span style="color:#AA5500">            &quot;Gateway&quot;: &quot;172.17.0.1&quot;,</span>
<span style="color:#AA5500">            &quot;GlobalIPv6Address&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;GlobalIPv6PrefixLen&quot;: 0,</span>
<span style="color:#AA5500">            &quot;HairpinMode&quot;: false,</span>
<span style="color:#AA5500">            &quot;IPAddress&quot;: &quot;172.17.0.8&quot;,</span>
<span style="color:#AA5500">            &quot;IPPrefixLen&quot;: 16,</span>
<span style="color:#AA5500">            &quot;IPv6Gateway&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;LinkLocalIPv6Address&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;LinkLocalIPv6PrefixLen&quot;: 0,</span>
<span style="color:#AA5500">            &quot;MacAddress&quot;: &quot;32:57:ef:4d:2f:42&quot;,</span>
<span style="color:#AA5500">            &quot;Networks&quot;: {</span>
<span style="color:#AA5500">                &quot;bridge&quot;: {</span>
<span style="color:#AA5500">                    &quot;Aliases&quot;: null,</span>
<span style="color:#AA5500">                    &quot;DNSNames&quot;: null,</span>
<span style="color:#AA5500">                    &quot;DriverOpts&quot;: null,</span>
<span style="color:#AA5500">                    &quot;EndpointID&quot;: &quot;639e1c0a192c9d51b9fdf3fe3fdeb77f0a533d0ee4d847dfa97bda30fbbdaa24&quot;,</span>
<span style="color:#AA5500">                    &quot;Gateway&quot;: &quot;172.17.0.1&quot;,</span>
<span style="color:#AA5500">                    &quot;GlobalIPv6Address&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">                    &quot;GlobalIPv6PrefixLen&quot;: 0,</span>
<span style="color:#AA5500">                    &quot;GwPriority&quot;: 0,</span>
<span style="color:#AA5500">                    &quot;IPAMConfig&quot;: null,</span>
<span style="color:#AA5500">                    &quot;IPAddress&quot;: &quot;172.17.0.8&quot;,</span>
<span style="color:#AA5500">                    &quot;IPPrefixLen&quot;: 16,</span>
<span style="color:#AA5500">                    &quot;IPv6Gateway&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">                    &quot;Links&quot;: null,</span>
<span style="color:#AA5500">                    &quot;MacAddress&quot;: &quot;32:57:ef:4d:2f:42&quot;,</span>
<span style="color:#AA5500">                    &quot;NetworkID&quot;: &quot;fce42755ebf1352d21e037493e0c33a917b08a8fe5d9ea19e3af1d873ab69e67&quot;</span>
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
<span style="color:#AA5500">            &quot;SandboxID&quot;: &quot;17beb5fc3925b1cb89d1cb4a907b104ca011dbed4d476d60286d5db95ff20a2a&quot;,</span>
<span style="color:#AA5500">            &quot;SandboxKey&quot;: &quot;/var/run/docker/netns/17beb5fc3925&quot;,</span>
<span style="color:#AA5500">            &quot;SecondaryIPAddresses&quot;: null,</span>
<span style="color:#AA5500">            &quot;SecondaryIPv6Addresses&quot;: null</span>
<span style="color:#AA5500">        },</span>
<span style="color:#AA5500">        &quot;Path&quot;: &quot;/portainer&quot;,</span>
<span style="color:#AA5500">        &quot;Platform&quot;: &quot;linux&quot;,</span>
<span style="color:#AA5500">        &quot;ProcessLabel&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">        &quot;ResolvConfPath&quot;: &quot;/var/lib/docker/containers/9e2dd406f701ba1fdf46bebb1f056f8ac0567163173c7dfe0d767498aa848597/resolv.conf&quot;,</span>
<span style="color:#AA5500">        &quot;RestartCount&quot;: 0,</span>
<span style="color:#AA5500">        &quot;State&quot;: {</span>
<span style="color:#AA5500">            &quot;Dead&quot;: false,</span>
<span style="color:#AA5500">            &quot;Error&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;ExitCode&quot;: 0,</span>
<span style="color:#AA5500">            &quot;FinishedAt&quot;: &quot;2025-10-10T04:02:46.141317984Z&quot;,</span>
<span style="color:#AA5500">            &quot;OOMKilled&quot;: false,</span>
<span style="color:#AA5500">            &quot;Paused&quot;: false,</span>
<span style="color:#AA5500">            &quot;Pid&quot;: 2127018,</span>
<span style="color:#AA5500">            &quot;Restarting&quot;: false,</span>
<span style="color:#AA5500">            &quot;Running&quot;: true,</span>
<span style="color:#AA5500">            &quot;StartedAt&quot;: &quot;2025-10-10T04:02:53.995723846Z&quot;,</span>
<span style="color:#AA5500">            &quot;Status&quot;: &quot;running&quot;</span>
<span style="color:#AA5500">        }</span>
<span style="color:#AA5500">    }</span>
<span style="color:#AA5500">}</span>
Freitag 10 Oktober 2025  23:18:54 +0200 (0:00:01.814)       0:02:19.309 ******* 
Freitag 10 Oktober 2025  23:18:54 +0200 (0:00:00.061)       0:02:19.371 ******* 
Freitag 10 Oktober 2025  23:18:54 +0200 (0:00:00.048)       0:02:19.420 ******* 
Freitag 10 Oktober 2025  23:18:54 +0200 (0:00:00.049)       0:02:19.469 ******* 

TASK [prowlarr : Stop Prowlarr] ***********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/prowlarr/tasks/main.yml:43</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:18:55 +0200 (0:00:00.598)       0:02:20.068 ******* 
Freitag 10 Oktober 2025  23:18:55 +0200 (0:00:00.044)       0:02:20.113 ******* 
Freitag 10 Oktober 2025  23:18:55 +0200 (0:00:00.039)       0:02:20.152 ******* 
Freitag 10 Oktober 2025  23:18:55 +0200 (0:00:00.057)       0:02:20.210 ******* 
Freitag 10 Oktober 2025  23:18:55 +0200 (0:00:00.049)       0:02:20.260 ******* 
Freitag 10 Oktober 2025  23:18:55 +0200 (0:00:00.041)       0:02:20.301 ******* 

TASK [promtail : Stop promtail] ***********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/promtail/tasks/main.yml:50</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:18:56 +0200 (0:00:00.722)       0:02:21.023 ******* 
Freitag 10 Oktober 2025  23:18:56 +0200 (0:00:00.047)       0:02:21.071 ******* 
Freitag 10 Oktober 2025  23:18:56 +0200 (0:00:00.050)       0:02:21.121 ******* 

TASK [pyload : Stop pyLoad] ***************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/pyload/tasks/main.yml:45</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:18:56 +0200 (0:00:00.618)       0:02:21.740 ******* 
Freitag 10 Oktober 2025  23:18:56 +0200 (0:00:00.054)       0:02:21.794 ******* 
Freitag 10 Oktober 2025  23:18:57 +0200 (0:00:00.050)       0:02:21.845 ******* 

TASK [pytivo : Stop Pytivo] ***************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/pytivo/tasks/main.yml:45</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:18:57 +0200 (0:00:00.718)       0:02:22.563 ******* 
Freitag 10 Oktober 2025  23:18:57 +0200 (0:00:00.050)       0:02:22.613 ******* 
Freitag 10 Oktober 2025  23:18:57 +0200 (0:00:00.052)       0:02:22.666 ******* 

TASK [radarr : Stop Radarr] ***************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/radarr/tasks/main.yml:44</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:18:58 +0200 (0:00:00.618)       0:02:23.284 ******* 
Freitag 10 Oktober 2025  23:18:58 +0200 (0:00:00.054)       0:02:23.338 ******* 
Freitag 10 Oktober 2025  23:18:58 +0200 (0:00:00.042)       0:02:23.381 ******* 
Freitag 10 Oktober 2025  23:18:58 +0200 (0:00:00.049)       0:02:23.430 ******* 
Freitag 10 Oktober 2025  23:18:58 +0200 (0:00:00.045)       0:02:23.475 ******* 

TASK [romm : Stop Romm] *******************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/romm/tasks/main.yml:84</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:18:59 +0200 (0:00:00.679)       0:02:24.155 ******* 

TASK [romm : Stop Romm DB] ****************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/romm/tasks/main.yml:89</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:18:59 +0200 (0:00:00.612)       0:02:24.768 ******* 
Freitag 10 Oktober 2025  23:19:00 +0200 (0:00:00.055)       0:02:24.824 ******* 
Freitag 10 Oktober 2025  23:19:00 +0200 (0:00:00.051)       0:02:24.876 ******* 
Freitag 10 Oktober 2025  23:19:00 +0200 (0:00:00.067)       0:02:24.944 ******* 
Freitag 10 Oktober 2025  23:19:00 +0200 (0:00:00.079)       0:02:25.023 ******* 
Freitag 10 Oktober 2025  23:19:00 +0200 (0:00:00.057)       0:02:25.080 ******* 
Freitag 10 Oktober 2025  23:19:00 +0200 (0:00:00.048)       0:02:25.129 ******* 

TASK [rssbridge : Stop RSSBridge] *********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/rssbridge/tasks/main.yml:34</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:19:00 +0200 (0:00:00.627)       0:02:25.756 ******* 
Freitag 10 Oktober 2025  23:19:01 +0200 (0:00:00.052)       0:02:25.809 ******* 
Freitag 10 Oktober 2025  23:19:01 +0200 (0:00:00.043)       0:02:25.852 ******* 

TASK [sabnzbd : Stop Sabnzbd] *************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/sabnzbd/tasks/main.yml:38</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:19:01 +0200 (0:00:00.614)       0:02:26.467 ******* 
Freitag 10 Oktober 2025  23:19:01 +0200 (0:00:00.046)       0:02:26.513 ******* 
Freitag 10 Oktober 2025  23:19:01 +0200 (0:00:00.149)       0:02:26.663 ******* 

TASK [sickchill : Stop Sickchill] *********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/sickchill/tasks/main.yml:40</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:19:02 +0200 (0:00:00.592)       0:02:27.255 ******* 
Freitag 10 Oktober 2025  23:19:02 +0200 (0:00:00.046)       0:02:27.302 ******* 
Freitag 10 Oktober 2025  23:19:02 +0200 (0:00:00.045)       0:02:27.348 ******* 

TASK [silverbullet : Stop silverbullet] ***************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/silverbullet/tasks/main.yml:40</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:19:03 +0200 (0:00:00.672)       0:02:28.020 ******* 
Freitag 10 Oktober 2025  23:19:03 +0200 (0:00:00.067)       0:02:28.088 ******* 
Freitag 10 Oktober 2025  23:19:03 +0200 (0:00:00.050)       0:02:28.138 ******* 

TASK [sonarr : Stop Sonarr] ***************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/sonarr/tasks/main.yml:39</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:19:03 +0200 (0:00:00.631)       0:02:28.770 ******* 
Freitag 10 Oktober 2025  23:19:04 +0200 (0:00:00.053)       0:02:28.823 ******* 
Freitag 10 Oktober 2025  23:19:04 +0200 (0:00:00.047)       0:02:28.871 ******* 
Freitag 10 Oktober 2025  23:19:04 +0200 (0:00:00.068)       0:02:28.939 ******* 
Freitag 10 Oktober 2025  23:19:04 +0200 (0:00:00.067)       0:02:29.006 ******* 
Freitag 10 Oktober 2025  23:19:04 +0200 (0:00:00.151)       0:02:29.158 ******* 
Freitag 10 Oktober 2025  23:19:04 +0200 (0:00:00.052)       0:02:29.211 ******* 
Freitag 10 Oktober 2025  23:19:04 +0200 (0:00:00.053)       0:02:29.264 ******* 
Freitag 10 Oktober 2025  23:19:04 +0200 (0:00:00.043)       0:02:29.307 ******* 

TASK [stats : Stop Prometheus] ************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/stats/tasks/prometheus.yml:60</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:19:05 +0200 (0:00:00.622)       0:02:29.930 ******* 
Freitag 10 Oktober 2025  23:19:05 +0200 (0:00:00.055)       0:02:29.985 ******* 
Freitag 10 Oktober 2025  23:19:05 +0200 (0:00:00.053)       0:02:30.039 ******* 
Freitag 10 Oktober 2025  23:19:05 +0200 (0:00:00.044)       0:02:30.083 ******* 
Freitag 10 Oktober 2025  23:19:05 +0200 (0:00:00.048)       0:02:30.132 ******* 

TASK [stats : Stop stats_telegraf] ********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/stats/tasks/telegraf.yml:56</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:19:05 +0200 (0:00:00.609)       0:02:30.741 ******* 
Freitag 10 Oktober 2025  23:19:05 +0200 (0:00:00.047)       0:02:30.789 ******* 
Freitag 10 Oktober 2025  23:19:06 +0200 (0:00:00.058)       0:02:30.848 ******* 
Freitag 10 Oktober 2025  23:19:06 +0200 (0:00:00.056)       0:02:30.904 ******* 

TASK [stats : Stop Smartctl Exporter] *****************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/stats/tasks/exporters.yml:45</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:19:06 +0200 (0:00:00.610)       0:02:31.515 ******* 

TASK [stats : Stop Speedtest Exporter] ****************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/stats/tasks/exporters.yml:49</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:19:07 +0200 (0:00:00.612)       0:02:32.127 ******* 
Freitag 10 Oktober 2025  23:19:07 +0200 (0:00:00.066)       0:02:32.194 ******* 
Freitag 10 Oktober 2025  23:19:07 +0200 (0:00:00.040)       0:02:32.234 ******* 
Freitag 10 Oktober 2025  23:19:07 +0200 (0:00:00.146)       0:02:32.380 ******* 
Freitag 10 Oktober 2025  23:19:07 +0200 (0:00:00.044)       0:02:32.425 ******* 
Freitag 10 Oktober 2025  23:19:07 +0200 (0:00:00.042)       0:02:32.468 ******* 

TASK [stats : Stop Grafana] ***************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/stats/tasks/grafana.yml:65</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:19:08 +0200 (0:00:00.659)       0:02:33.127 ******* 
Freitag 10 Oktober 2025  23:19:08 +0200 (0:00:00.054)       0:02:33.181 ******* 
Freitag 10 Oktober 2025  23:19:08 +0200 (0:00:00.052)       0:02:33.234 ******* 

TASK [syncthing : Stop Syncthing] *********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/syncthing/tasks/main.yml:38</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:19:09 +0200 (0:00:00.612)       0:02:33.847 ******* 
Freitag 10 Oktober 2025  23:19:09 +0200 (0:00:00.067)       0:02:33.914 ******* 
Freitag 10 Oktober 2025  23:19:09 +0200 (0:00:00.043)       0:02:33.957 ******* 

TASK [tautulli : Stop Tautulli] ***********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/tautulli/tasks/main.yml:40</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:19:09 +0200 (0:00:00.660)       0:02:34.618 ******* 
Freitag 10 Oktober 2025  23:19:09 +0200 (0:00:00.056)       0:02:34.674 ******* 
Freitag 10 Oktober 2025  23:19:09 +0200 (0:00:00.040)       0:02:34.715 ******* 
Freitag 10 Oktober 2025  23:19:09 +0200 (0:00:00.051)       0:02:34.767 ******* 

TASK [thelounge : Stop The Lounge] ********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/thelounge/tasks/main.yml:42</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:19:10 +0200 (0:00:00.695)       0:02:35.462 ******* 
Freitag 10 Oktober 2025  23:19:10 +0200 (0:00:00.053)       0:02:35.515 ******* 
Freitag 10 Oktober 2025  23:19:10 +0200 (0:00:00.050)       0:02:35.566 ******* 

TASK [threadfin : Stop Threadfin] *********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/threadfin/tasks/main.yml:34</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:19:11 +0200 (0:00:00.628)       0:02:36.194 ******* 
Freitag 10 Oktober 2025  23:19:11 +0200 (0:00:00.045)       0:02:36.239 ******* 
Freitag 10 Oktober 2025  23:19:11 +0200 (0:00:00.045)       0:02:36.285 ******* 

TASK [tiddlywiki : Stop Tiddlywiki] *******************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/tiddlywiki/tasks/main.yml:36</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:19:12 +0200 (0:00:00.630)       0:02:36.916 ******* 
Freitag 10 Oktober 2025  23:19:12 +0200 (0:00:00.046)       0:02:36.962 ******* 
Freitag 10 Oktober 2025  23:19:12 +0200 (0:00:00.048)       0:02:37.011 ******* 
Freitag 10 Oktober 2025  23:19:12 +0200 (0:00:00.055)       0:02:37.066 ******* 
Freitag 10 Oktober 2025  23:19:12 +0200 (0:00:00.044)       0:02:37.111 ******* 

TASK [timemachine : Stop Time Machine] ****************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/timemachine/tasks/main.yml:45</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:19:12 +0200 (0:00:00.618)       0:02:37.729 ******* 

TASK [tinymm : Create tinyMediaManager Directories] ***************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/tinymm/tasks/main.yml:7</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; (item=/mnt/Volume1/docker/tinymm/config) =&gt; {</span>
<span style="color:#00AA00">    &quot;ansible_loop_var&quot;: &quot;item&quot;,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;gid&quot;: 1001,</span>
<span style="color:#00AA00">    &quot;group&quot;: &quot;ansible-nas&quot;,</span>
<span style="color:#00AA00">    &quot;item&quot;: &quot;/mnt/Volume1/docker/tinymm/config&quot;,</span>
<span style="color:#00AA00">    &quot;mode&quot;: &quot;0777&quot;,</span>
<span style="color:#00AA00">    &quot;owner&quot;: &quot;1001&quot;,</span>
<span style="color:#00AA00">    &quot;path&quot;: &quot;/mnt/Volume1/docker/tinymm/config&quot;,</span>
<span style="color:#00AA00">    &quot;size&quot;: 4096,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;directory&quot;,</span>
<span style="color:#00AA00">    &quot;uid&quot;: 1001</span>
<span style="color:#00AA00">}</span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; (item=/mnt/Volume1/docker/tinymm/data) =&gt; {</span>
<span style="color:#00AA00">    &quot;ansible_loop_var&quot;: &quot;item&quot;,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;gid&quot;: 1001,</span>
<span style="color:#00AA00">    &quot;group&quot;: &quot;ansible-nas&quot;,</span>
<span style="color:#00AA00">    &quot;item&quot;: &quot;/mnt/Volume1/docker/tinymm/data&quot;,</span>
<span style="color:#00AA00">    &quot;mode&quot;: &quot;0777&quot;,</span>
<span style="color:#00AA00">    &quot;owner&quot;: &quot;1001&quot;,</span>
<span style="color:#00AA00">    &quot;path&quot;: &quot;/mnt/Volume1/docker/tinymm/data&quot;,</span>
<span style="color:#00AA00">    &quot;size&quot;: 4096,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;directory&quot;,</span>
<span style="color:#00AA00">    &quot;uid&quot;: 1001</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:19:13 +0200 (0:00:00.746)       0:02:38.476 ******* 

TASK [tinymm : tinyMediaManager Docker Container] *****************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/tinymm/tasks/main.yml:15</b></span>
<span style="color:#AA5500">changed: [ansible-nas] =&gt; {</span>
<span style="color:#AA5500">    &quot;changed&quot;: true,</span>
<span style="color:#AA5500">    &quot;container&quot;: {</span>
<span style="color:#AA5500">        &quot;AppArmorProfile&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">        &quot;Args&quot;: [</span>
<span style="color:#AA5500">            &quot;/app/tinyMediaManager&quot;,</span>
<span style="color:#AA5500">            &quot;-Dtmm.contentfolder=/data&quot;</span>
<span style="color:#AA5500">        ],</span>
<span style="color:#AA5500">        &quot;Config&quot;: {</span>
<span style="color:#AA5500">            &quot;AttachStderr&quot;: true,</span>
<span style="color:#AA5500">            &quot;AttachStdin&quot;: false,</span>
<span style="color:#AA5500">            &quot;AttachStdout&quot;: true,</span>
<span style="color:#AA5500">            &quot;Cmd&quot;: [</span>
<span style="color:#AA5500">                &quot;/app/tinyMediaManager&quot;,</span>
<span style="color:#AA5500">                &quot;-Dtmm.contentfolder=/data&quot;</span>
<span style="color:#AA5500">            ],</span>
<span style="color:#AA5500">            &quot;Domainname&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;Entrypoint&quot;: [</span>
<span style="color:#AA5500">                &quot;/usr/local/bin/startup.sh&quot;</span>
<span style="color:#AA5500">            ],</span>
<span style="color:#AA5500">            &quot;Env&quot;: [</span>
<span style="color:#AA5500">                &quot;TZ=Europe/Berlin&quot;,</span>
<span style="color:#AA5500">                &quot;PUID=0&quot;,</span>
<span style="color:#AA5500">                &quot;PGID=0&quot;,</span>
<span style="color:#AA5500">                &quot;PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin&quot;,</span>
<span style="color:#AA5500">                &quot;LANG=en_US.UTF-8&quot;,</span>
<span style="color:#AA5500">                &quot;LC_ALL=en_US.UTF-8&quot;,</span>
<span style="color:#AA5500">                &quot;USER_ID=1000&quot;,</span>
<span style="color:#AA5500">                &quot;GROUP_ID=1000&quot;,</span>
<span style="color:#AA5500">                &quot;APP=tinyMediaManager&quot;,</span>
<span style="color:#AA5500">                &quot;PASSWORD=&quot;,</span>
<span style="color:#AA5500">                &quot;UMASK=0022&quot;,</span>
<span style="color:#AA5500">                &quot;ALLOW_DIRECT_VNC=true&quot;,</span>
<span style="color:#AA5500">                &quot;HOME=/app&quot;,</span>
<span style="color:#AA5500">                &quot;LC_TIME=C.UTF-8&quot;</span>
<span style="color:#AA5500">            ],</span>
<span style="color:#AA5500">            &quot;ExposedPorts&quot;: {</span>
<span style="color:#AA5500">                &quot;4000/tcp&quot;: {},</span>
<span style="color:#AA5500">                &quot;5900/tcp&quot;: {}</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            &quot;Hostname&quot;: &quot;f66abc7bcadd&quot;,</span>
<span style="color:#AA5500">            &quot;Image&quot;: &quot;tinymediamanager/tinymediamanager:latest&quot;,</span>
<span style="color:#AA5500">            &quot;Labels&quot;: {</span>
<span style="color:#AA5500">                &quot;Author&quot;: &quot;max06/base-gui&quot;,</span>
<span style="color:#AA5500">                &quot;Flavor&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">                &quot;Name&quot;: &quot;base-gui&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.created&quot;: &quot;2024-12-17T11:32:40.992Z&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.description&quot;: &quot;a media management tool written in Java&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.documentation&quot;: &quot;https://www.tinymediamanager.org/docs/docker&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.licenses&quot;: &quot;Apache License, Version 2.0&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.revision&quot;: &quot;72397b1&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.source&quot;: &quot;https://github.com/max06/base-gui&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.source &quot;: &quot;https://gitlab.com/tinyMediaManager/tinyMediaManager&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.title&quot;: &quot;tinyMediaManager&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.url&quot;: &quot;https://www.tinymediamanager.org/&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.version&quot;: &quot;5.2.2&quot;</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            &quot;OnBuild&quot;: null,</span>
<span style="color:#AA5500">            &quot;OpenStdin&quot;: false,</span>
<span style="color:#AA5500">            &quot;StdinOnce&quot;: false,</span>
<span style="color:#AA5500">            &quot;Tty&quot;: false,</span>
<span style="color:#AA5500">            &quot;User&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;Volumes&quot;: null,</span>
<span style="color:#AA5500">            &quot;WorkingDir&quot;: &quot;/app&quot;</span>
<span style="color:#AA5500">        },</span>
<span style="color:#AA5500">        &quot;Created&quot;: &quot;2025-10-01T00:21:27.4683986Z&quot;,</span>
<span style="color:#AA5500">        &quot;Driver&quot;: &quot;overlay2&quot;,</span>
<span style="color:#AA5500">        &quot;ExecIDs&quot;: null,</span>
<span style="color:#AA5500">        &quot;GraphDriver&quot;: {</span>
<span style="color:#AA5500">            &quot;Data&quot;: {</span>
<span style="color:#AA5500">                &quot;ID&quot;: &quot;f66abc7bcaddfe32da83821823feee016864306fce97b1bfb6f3b011f7101fc1&quot;,</span>
<span style="color:#AA5500">                &quot;LowerDir&quot;: &quot;/var/lib/docker/overlay2/a3be5d6c233b0a1f0b7210ed4f8e73bf41024d9e243a76fa7b703f9d721de427-init/diff:/var/lib/docker/overlay2/d1bbd1cd25e31c7e47fabd7d6598af9df3dafff8558f94422c0fbc995daaa3ed/diff:/var/lib/docker/overlay2/73a31d5f5e9b4ed190b8a06bf8b09c7110d1aa796ddbef1452fb5bc013c32544/diff:/var/lib/docker/overlay2/cc51d489269cd9660de5da66f42bf7fac1679e8d75c4b156f3fb8d44769cbeeb/diff:/var/lib/docker/overlay2/f4f059d59b400eab8219b77a3b20f9fe0c3520e85b70a763f99ed6f166922c9f/diff:/var/lib/docker/overlay2/5be2307047bb6faf20d038e5937248185eb0019008053ef513dcbd2168c1d771/diff:/var/lib/docker/overlay2/824a00b267b59749d23782c6cc48145487bfd52ce5779e13bc0fcb4071e733f5/diff:/var/lib/docker/overlay2/44feafd53a80939d0eb3cf47b5d65d61aace00a59fba7a773f071ae9c8b4ba9f/diff:/var/lib/docker/overlay2/bfab7718641d0e79c9f2392f4945720edf38cc8021e58e7df7d4dccf9a7c95e5/diff:/var/lib/docker/overlay2/025f4aa59dfb58be31d5cdbc809558ca6c10480fda97e03f5b8ab25b46ffc074/diff:/var/lib/docker/overlay2/bf9f38efbc3a606c250ce82994fc646e6c7397241aa10fe96bc39ed2d01bd225/diff:/var/lib/docker/overlay2/bfc1fda2bda40615919d1f378ca1a7c5922125fe42b8bf2c082825b367082edc/diff:/var/lib/docker/overlay2/0318046056fc46e8fd583a51382b40c93d1d078ccff8d1813905c6dd5e817f02/diff:/var/lib/docker/overlay2/bb29af26330242c75c6d0587249a5afe4c9dea987f54232a5e52579d5eec8b3e/diff:/var/lib/docker/overlay2/faf38471b4c259f03cbd8d367841304031007e0c595e4fbdef0873381796cd5c/diff:/var/lib/docker/overlay2/1eab858f161780e5baa38a451566372a1c1f3df9d96a7bb023992ba0849f8781/diff:/var/lib/docker/overlay2/3a757e1200834a3f745c55816ae211da87a505e68f81be0e76219caac795ae63/diff:/var/lib/docker/overlay2/49ad0690507e2507f44999368c4fbb52c2500eafb341852fde1b7d883728f79f/diff:/var/lib/docker/overlay2/f3e11f744412bcc78a2a3aa47ecd8f49be2fde1a6481fc5f1fa6499baf4f27f5/diff:/var/lib/docker/overlay2/ede21b4a2b59da8048cfa7d9bda1bcf603865c30d647638d0cc1be9bc12a54cc/diff:/var/lib/docker/overlay2/bc5cb0e08c2e6edd11a203bf12bd7a958d4b7a65eea67d6b7df71fe0c597f616/diff:/var/lib/docker/overlay2/9540d1dcfd4d525af1b0a9572efa2141f98356903a435301d5eafd199c33b757/diff:/var/lib/docker/overlay2/b5a58e2ff079f34eca99d52b7436660c8f7aeeabeecb2dd48f9fbf02be2d451e/diff:/var/lib/docker/overlay2/29d47d1421225eb123deca8e9494dc329c0e38c0b1f30f0bf6be615c79a0d493/diff:/var/lib/docker/overlay2/3e7b4d26e46d9d8312e9b40805a364c221fa0ba8bbd0cc942d41fc82c9fdf521/diff:/var/lib/docker/overlay2/b38598dce13209bff216b99fbe30c172b71cba5d935219f794a2d2f3f4e38900/diff:/var/lib/docker/overlay2/bbcd8707130df1239f33637bbaea4e0c0dae3a35107ed28ce1a2d56f2956e84f/diff:/var/lib/docker/overlay2/d454d65b5dd46538e2e0706db28c47e6927e71be7a62cc412c512c6b2c0464be/diff:/var/lib/docker/overlay2/0373c2b49506a2fd437f5915ee3af266aa8717f47d051c16e866dee3a7db290d/diff:/var/lib/docker/overlay2/7dd4364567446f0c1d9a78a8ecdc8365fe234850689ca71007313170cce5f121/diff&quot;,</span>
<span style="color:#AA5500">                &quot;MergedDir&quot;: &quot;/var/lib/docker/overlay2/a3be5d6c233b0a1f0b7210ed4f8e73bf41024d9e243a76fa7b703f9d721de427/merged&quot;,</span>
<span style="color:#AA5500">                &quot;UpperDir&quot;: &quot;/var/lib/docker/overlay2/a3be5d6c233b0a1f0b7210ed4f8e73bf41024d9e243a76fa7b703f9d721de427/diff&quot;,</span>
<span style="color:#AA5500">                &quot;WorkDir&quot;: &quot;/var/lib/docker/overlay2/a3be5d6c233b0a1f0b7210ed4f8e73bf41024d9e243a76fa7b703f9d721de427/work&quot;</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            &quot;Name&quot;: &quot;overlay2&quot;</span>
<span style="color:#AA5500">        },</span>
<span style="color:#AA5500">        &quot;HostConfig&quot;: {</span>
<span style="color:#AA5500">            &quot;AutoRemove&quot;: false,</span>
<span style="color:#AA5500">            &quot;Binds&quot;: [</span>
<span style="color:#AA5500">                &quot;/mnt/Volume1/docker/tinymm/config:/config:rw&quot;,</span>
<span style="color:#AA5500">                &quot;/mnt/Volume1/local/Media:/media:rw&quot;,</span>
<span style="color:#AA5500">                &quot;/mnt/Volume1/local/Movies:/movies:rw&quot;,</span>
<span style="color:#AA5500">                &quot;/mnt/Volume1/local/TV:/tv:rw&quot;</span>
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
<span style="color:#AA5500">                &quot;4000/tcp&quot;: [</span>
<span style="color:#AA5500">                    {</span>
<span style="color:#AA5500">                        &quot;HostIp&quot;: &quot;0.0.0.0&quot;,</span>
<span style="color:#AA5500">                        &quot;HostPort&quot;: &quot;4000&quot;</span>
<span style="color:#AA5500">                    }</span>
<span style="color:#AA5500">                ],</span>
<span style="color:#AA5500">                &quot;5900/tcp&quot;: [</span>
<span style="color:#AA5500">                    {</span>
<span style="color:#AA5500">                        &quot;HostIp&quot;: &quot;0.0.0.0&quot;,</span>
<span style="color:#AA5500">                        &quot;HostPort&quot;: &quot;5900&quot;</span>
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
<span style="color:#AA5500">        &quot;HostnamePath&quot;: &quot;/var/lib/docker/containers/f66abc7bcaddfe32da83821823feee016864306fce97b1bfb6f3b011f7101fc1/hostname&quot;,</span>
<span style="color:#AA5500">        &quot;HostsPath&quot;: &quot;/var/lib/docker/containers/f66abc7bcaddfe32da83821823feee016864306fce97b1bfb6f3b011f7101fc1/hosts&quot;,</span>
<span style="color:#AA5500">        &quot;Id&quot;: &quot;f66abc7bcaddfe32da83821823feee016864306fce97b1bfb6f3b011f7101fc1&quot;,</span>
<span style="color:#AA5500">        &quot;Image&quot;: &quot;sha256:5e4db7cd6fa5494e1f5846475737b194b219bc4c382b6f00bff6d744e39908a4&quot;,</span>
<span style="color:#AA5500">        &quot;LogPath&quot;: &quot;/var/lib/docker/containers/f66abc7bcaddfe32da83821823feee016864306fce97b1bfb6f3b011f7101fc1/f66abc7bcaddfe32da83821823feee016864306fce97b1bfb6f3b011f7101fc1-json.log&quot;,</span>
<span style="color:#AA5500">        &quot;MountLabel&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">        &quot;Mounts&quot;: [</span>
<span style="color:#AA5500">            {</span>
<span style="color:#AA5500">                &quot;Destination&quot;: &quot;/movies&quot;,</span>
<span style="color:#AA5500">                &quot;Mode&quot;: &quot;rw&quot;,</span>
<span style="color:#AA5500">                &quot;Propagation&quot;: &quot;rprivate&quot;,</span>
<span style="color:#AA5500">                &quot;RW&quot;: true,</span>
<span style="color:#AA5500">                &quot;Source&quot;: &quot;/mnt/Volume1/local/Movies&quot;,</span>
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
<span style="color:#AA5500">                &quot;Destination&quot;: &quot;/config&quot;,</span>
<span style="color:#AA5500">                &quot;Mode&quot;: &quot;rw&quot;,</span>
<span style="color:#AA5500">                &quot;Propagation&quot;: &quot;rprivate&quot;,</span>
<span style="color:#AA5500">                &quot;RW&quot;: true,</span>
<span style="color:#AA5500">                &quot;Source&quot;: &quot;/mnt/Volume1/docker/tinymm/config&quot;,</span>
<span style="color:#AA5500">                &quot;Type&quot;: &quot;bind&quot;</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            {</span>
<span style="color:#AA5500">                &quot;Destination&quot;: &quot;/media&quot;,</span>
<span style="color:#AA5500">                &quot;Mode&quot;: &quot;rw&quot;,</span>
<span style="color:#AA5500">                &quot;Propagation&quot;: &quot;rprivate&quot;,</span>
<span style="color:#AA5500">                &quot;RW&quot;: true,</span>
<span style="color:#AA5500">                &quot;Source&quot;: &quot;/mnt/Volume1/local/Media&quot;,</span>
<span style="color:#AA5500">                &quot;Type&quot;: &quot;bind&quot;</span>
<span style="color:#AA5500">            }</span>
<span style="color:#AA5500">        ],</span>
<span style="color:#AA5500">        &quot;Name&quot;: &quot;/tinymm&quot;,</span>
<span style="color:#AA5500">        &quot;NetworkSettings&quot;: {</span>
<span style="color:#AA5500">            &quot;Bridge&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;EndpointID&quot;: &quot;f4637ef16e1f05a2d9dcf9ec4d73f80fd94628ba4a569e6421ab85a29e084c36&quot;,</span>
<span style="color:#AA5500">            &quot;Gateway&quot;: &quot;172.17.0.1&quot;,</span>
<span style="color:#AA5500">            &quot;GlobalIPv6Address&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;GlobalIPv6PrefixLen&quot;: 0,</span>
<span style="color:#AA5500">            &quot;HairpinMode&quot;: false,</span>
<span style="color:#AA5500">            &quot;IPAddress&quot;: &quot;172.17.0.7&quot;,</span>
<span style="color:#AA5500">            &quot;IPPrefixLen&quot;: 16,</span>
<span style="color:#AA5500">            &quot;IPv6Gateway&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;LinkLocalIPv6Address&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;LinkLocalIPv6PrefixLen&quot;: 0,</span>
<span style="color:#AA5500">            &quot;MacAddress&quot;: &quot;6e:b5:ad:40:fd:89&quot;,</span>
<span style="color:#AA5500">            &quot;Networks&quot;: {</span>
<span style="color:#AA5500">                &quot;bridge&quot;: {</span>
<span style="color:#AA5500">                    &quot;Aliases&quot;: null,</span>
<span style="color:#AA5500">                    &quot;DNSNames&quot;: null,</span>
<span style="color:#AA5500">                    &quot;DriverOpts&quot;: null,</span>
<span style="color:#AA5500">                    &quot;EndpointID&quot;: &quot;f4637ef16e1f05a2d9dcf9ec4d73f80fd94628ba4a569e6421ab85a29e084c36&quot;,</span>
<span style="color:#AA5500">                    &quot;Gateway&quot;: &quot;172.17.0.1&quot;,</span>
<span style="color:#AA5500">                    &quot;GlobalIPv6Address&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">                    &quot;GlobalIPv6PrefixLen&quot;: 0,</span>
<span style="color:#AA5500">                    &quot;GwPriority&quot;: 0,</span>
<span style="color:#AA5500">                    &quot;IPAMConfig&quot;: null,</span>
<span style="color:#AA5500">                    &quot;IPAddress&quot;: &quot;172.17.0.7&quot;,</span>
<span style="color:#AA5500">                    &quot;IPPrefixLen&quot;: 16,</span>
<span style="color:#AA5500">                    &quot;IPv6Gateway&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">                    &quot;Links&quot;: null,</span>
<span style="color:#AA5500">                    &quot;MacAddress&quot;: &quot;6e:b5:ad:40:fd:89&quot;,</span>
<span style="color:#AA5500">                    &quot;NetworkID&quot;: &quot;fce42755ebf1352d21e037493e0c33a917b08a8fe5d9ea19e3af1d873ab69e67&quot;</span>
<span style="color:#AA5500">                }</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            &quot;Ports&quot;: {</span>
<span style="color:#AA5500">                &quot;4000/tcp&quot;: [</span>
<span style="color:#AA5500">                    {</span>
<span style="color:#AA5500">                        &quot;HostIp&quot;: &quot;0.0.0.0&quot;,</span>
<span style="color:#AA5500">                        &quot;HostPort&quot;: &quot;4000&quot;</span>
<span style="color:#AA5500">                    }</span>
<span style="color:#AA5500">                ],</span>
<span style="color:#AA5500">                &quot;5900/tcp&quot;: [</span>
<span style="color:#AA5500">                    {</span>
<span style="color:#AA5500">                        &quot;HostIp&quot;: &quot;0.0.0.0&quot;,</span>
<span style="color:#AA5500">                        &quot;HostPort&quot;: &quot;5900&quot;</span>
<span style="color:#AA5500">                    }</span>
<span style="color:#AA5500">                ]</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            &quot;SandboxID&quot;: &quot;58be458bebfe74e0aa6e3aaab7397d7802a95f74114abd0fb16d3bd8845355c7&quot;,</span>
<span style="color:#AA5500">            &quot;SandboxKey&quot;: &quot;/var/run/docker/netns/58be458bebfe&quot;,</span>
<span style="color:#AA5500">            &quot;SecondaryIPAddresses&quot;: null,</span>
<span style="color:#AA5500">            &quot;SecondaryIPv6Addresses&quot;: null</span>
<span style="color:#AA5500">        },</span>
<span style="color:#AA5500">        &quot;Path&quot;: &quot;/usr/local/bin/startup.sh&quot;,</span>
<span style="color:#AA5500">        &quot;Platform&quot;: &quot;linux&quot;,</span>
<span style="color:#AA5500">        &quot;ProcessLabel&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">        &quot;ResolvConfPath&quot;: &quot;/var/lib/docker/containers/f66abc7bcaddfe32da83821823feee016864306fce97b1bfb6f3b011f7101fc1/resolv.conf&quot;,</span>
<span style="color:#AA5500">        &quot;RestartCount&quot;: 0,</span>
<span style="color:#AA5500">        &quot;State&quot;: {</span>
<span style="color:#AA5500">            &quot;Dead&quot;: false,</span>
<span style="color:#AA5500">            &quot;Error&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;ExitCode&quot;: 0,</span>
<span style="color:#AA5500">            &quot;FinishedAt&quot;: &quot;2025-10-10T04:02:50.116325479Z&quot;,</span>
<span style="color:#AA5500">            &quot;OOMKilled&quot;: false,</span>
<span style="color:#AA5500">            &quot;Paused&quot;: false,</span>
<span style="color:#AA5500">            &quot;Pid&quot;: 2127077,</span>
<span style="color:#AA5500">            &quot;Restarting&quot;: false,</span>
<span style="color:#AA5500">            &quot;Running&quot;: true,</span>
<span style="color:#AA5500">            &quot;StartedAt&quot;: &quot;2025-10-10T04:02:54.046276814Z&quot;,</span>
<span style="color:#AA5500">            &quot;Status&quot;: &quot;running&quot;</span>
<span style="color:#AA5500">        }</span>
<span style="color:#AA5500">    }</span>
<span style="color:#AA5500">}</span>
Freitag 10 Oktober 2025  23:19:15 +0200 (0:00:01.929)       0:02:40.405 ******* 
Freitag 10 Oktober 2025  23:19:15 +0200 (0:00:00.072)       0:02:40.477 ******* 
Freitag 10 Oktober 2025  23:19:15 +0200 (0:00:00.066)       0:02:40.544 ******* 
Freitag 10 Oktober 2025  23:19:15 +0200 (0:00:00.049)       0:02:40.593 ******* 
Freitag 10 Oktober 2025  23:19:15 +0200 (0:00:00.044)       0:02:40.638 ******* 

TASK [traefik : Stop Traefik] *************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/traefik/tasks/main.yml:44</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:19:16 +0200 (0:00:00.607)       0:02:41.245 ******* 
Freitag 10 Oktober 2025  23:19:16 +0200 (0:00:00.049)       0:02:41.295 ******* 
Freitag 10 Oktober 2025  23:19:16 +0200 (0:00:00.041)       0:02:41.337 ******* 

TASK [transmission : Stop Transmission] ***************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/transmission/tasks/main.yml:44</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:19:17 +0200 (0:00:00.636)       0:02:41.974 ******* 
Freitag 10 Oktober 2025  23:19:17 +0200 (0:00:00.046)       0:02:42.020 ******* 
Freitag 10 Oktober 2025  23:19:17 +0200 (0:00:00.045)       0:02:42.066 ******* 

TASK [transmission-with-openvpn : Stop Transmission with OpenVPM] *************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/transmission-with-openvpn/tasks/main.yml:64</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:19:17 +0200 (0:00:00.627)       0:02:42.694 ******* 
Freitag 10 Oktober 2025  23:19:18 +0200 (0:00:00.157)       0:02:42.852 ******* 
Freitag 10 Oktober 2025  23:19:18 +0200 (0:00:00.044)       0:02:42.896 ******* 

TASK [ubooquity : Stop Ubooquity] *********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/ubooquity/tasks/main.yml:42</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:19:18 +0200 (0:00:00.662)       0:02:43.559 ******* 
Freitag 10 Oktober 2025  23:19:18 +0200 (0:00:00.051)       0:02:43.610 ******* 
Freitag 10 Oktober 2025  23:19:18 +0200 (0:00:00.063)       0:02:43.673 ******* 

TASK [utorrent : Stop uTorrent] ***********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/utorrent/tasks/main.yml:46</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:19:19 +0200 (0:00:00.621)       0:02:44.294 ******* 
Freitag 10 Oktober 2025  23:19:19 +0200 (0:00:00.063)       0:02:44.357 ******* 
Freitag 10 Oktober 2025  23:19:19 +0200 (0:00:00.041)       0:02:44.399 ******* 

TASK [valheim : Stop Valheim] *************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/valheim/tasks/main.yml:44</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:19:20 +0200 (0:00:00.611)       0:02:45.011 ******* 
Freitag 10 Oktober 2025  23:19:20 +0200 (0:00:00.060)       0:02:45.072 ******* 
Freitag 10 Oktober 2025  23:19:20 +0200 (0:00:00.044)       0:02:45.116 ******* 
Freitag 10 Oktober 2025  23:19:20 +0200 (0:00:00.050)       0:02:45.166 ******* 

TASK [virtual_desktop : Stop Virtual Desktop] *********************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/virtual_desktop/tasks/main.yml:37</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:19:21 +0200 (0:00:00.649)       0:02:45.816 ******* 
Freitag 10 Oktober 2025  23:19:21 +0200 (0:00:00.184)       0:02:46.001 ******* 
Freitag 10 Oktober 2025  23:19:21 +0200 (0:00:00.043)       0:02:46.044 ******* 

TASK [wallabag : Stop Wallabag] ***********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/wallabag/tasks/main.yml:40</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:19:21 +0200 (0:00:00.650)       0:02:46.695 ******* 
Freitag 10 Oktober 2025  23:19:21 +0200 (0:00:00.101)       0:02:46.796 ******* 

TASK [watchtower : Stop Watchtower] *******************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/watchtower/tasks/main.yml:20</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:19:22 +0200 (0:00:00.626)       0:02:47.423 ******* 

TASK [wireshark : Create Wireshark Directories] *******************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/wireshark/tasks/main.yml:4</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; (item=/mnt/Volume1/docker/wireshark) =&gt; {</span>
<span style="color:#00AA00">    &quot;ansible_loop_var&quot;: &quot;item&quot;,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;gid&quot;: 0,</span>
<span style="color:#00AA00">    &quot;group&quot;: &quot;root&quot;,</span>
<span style="color:#00AA00">    &quot;item&quot;: &quot;/mnt/Volume1/docker/wireshark&quot;,</span>
<span style="color:#00AA00">    &quot;mode&quot;: &quot;0755&quot;,</span>
<span style="color:#00AA00">    &quot;owner&quot;: &quot;root&quot;,</span>
<span style="color:#00AA00">    &quot;path&quot;: &quot;/mnt/Volume1/docker/wireshark&quot;,</span>
<span style="color:#00AA00">    &quot;size&quot;: 4096,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;directory&quot;,</span>
<span style="color:#00AA00">    &quot;uid&quot;: 0</span>
<span style="color:#00AA00">}</span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; (item=/mnt/Volume1/docker/wireshark/config) =&gt; {</span>
<span style="color:#00AA00">    &quot;ansible_loop_var&quot;: &quot;item&quot;,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;gid&quot;: 1000,</span>
<span style="color:#00AA00">    &quot;group&quot;: &quot;dietmar&quot;,</span>
<span style="color:#00AA00">    &quot;item&quot;: &quot;/mnt/Volume1/docker/wireshark/config&quot;,</span>
<span style="color:#00AA00">    &quot;mode&quot;: &quot;0755&quot;,</span>
<span style="color:#00AA00">    &quot;owner&quot;: &quot;dietmar&quot;,</span>
<span style="color:#00AA00">    &quot;path&quot;: &quot;/mnt/Volume1/docker/wireshark/config&quot;,</span>
<span style="color:#00AA00">    &quot;size&quot;: 4096,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;directory&quot;,</span>
<span style="color:#00AA00">    &quot;uid&quot;: 1000</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:19:23 +0200 (0:00:00.728)       0:02:48.151 ******* 

TASK [wireshark : Create Wireshark Docker Container] **************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/wireshark/tasks/main.yml:12</b></span>
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
<span style="color:#AA5500">                &quot;PUID=1000&quot;,</span>
<span style="color:#AA5500">                &quot;PGID=1000&quot;,</span>
<span style="color:#AA5500">                &quot;PATH=/lsiopy/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin&quot;,</span>
<span style="color:#AA5500">                &quot;PS1=$(whoami)@$(hostname):$(pwd)\\$ &quot;,</span>
<span style="color:#AA5500">                &quot;HOME=/config&quot;,</span>
<span style="color:#AA5500">                &quot;TERM=xterm&quot;,</span>
<span style="color:#AA5500">                &quot;S6_CMD_WAIT_FOR_SERVICES_MAXTIME=0&quot;,</span>
<span style="color:#AA5500">                &quot;S6_VERBOSITY=1&quot;,</span>
<span style="color:#AA5500">                &quot;S6_STAGE2_HOOK=/docker-mods&quot;,</span>
<span style="color:#AA5500">                &quot;VIRTUAL_ENV=/lsiopy&quot;,</span>
<span style="color:#AA5500">                &quot;DISPLAY=:1&quot;,</span>
<span style="color:#AA5500">                &quot;PERL5LIB=/usr/local/bin&quot;,</span>
<span style="color:#AA5500">                &quot;START_DOCKER=true&quot;,</span>
<span style="color:#AA5500">                &quot;PULSE_RUNTIME_PATH=/defaults&quot;,</span>
<span style="color:#AA5500">                &quot;SELKIES_INTERPOSER=/usr/lib/selkies_joystick_interposer.so&quot;,</span>
<span style="color:#AA5500">                &quot;DISABLE_ZINK=false&quot;,</span>
<span style="color:#AA5500">                &quot;TITLE=Wireshark&quot;,</span>
<span style="color:#AA5500">                &quot;LSIO_FIRST_PARTY=true&quot;</span>
<span style="color:#AA5500">            ],</span>
<span style="color:#AA5500">            &quot;ExposedPorts&quot;: {</span>
<span style="color:#AA5500">                &quot;3000/tcp&quot;: {},</span>
<span style="color:#AA5500">                &quot;3001/tcp&quot;: {}</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            &quot;Hostname&quot;: &quot;RaspiNAS&quot;,</span>
<span style="color:#AA5500">            &quot;Image&quot;: &quot;linuxserver/wireshark:latest&quot;,</span>
<span style="color:#AA5500">            &quot;Labels&quot;: {</span>
<span style="color:#AA5500">                &quot;build_version&quot;: &quot;Linuxserver.io version:- 4.4.7-r0-ls277 Build-date:- 2025-10-06T15:34:16+00:00&quot;,</span>
<span style="color:#AA5500">                &quot;maintainer&quot;: &quot;thelamer&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.authors&quot;: &quot;linuxserver.io&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.created&quot;: &quot;2025-10-06T15:34:16+00:00&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.description&quot;: &quot;[Wireshark](https://www.wireshark.org/) is the world’s foremost and widely-used network protocol analyzer. It lets you see what’s happening on your network at a microscopic level and is the de facto (and often de jure) standard across many commercial and non-profit enterprises, government agencies, and educational institutions. Wireshark development thrives thanks to the volunteer contributions of networking experts around the globe and is the continuation of a project started by Gerald Combs in 1998. &quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.documentation&quot;: &quot;https://docs.linuxserver.io/images/docker-wireshark&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.licenses&quot;: &quot;GPL-3.0-only&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.ref.name&quot;: &quot;0db6085aa71e34467d7e9ac2fc2239daa0e6bef6&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.revision&quot;: &quot;0db6085aa71e34467d7e9ac2fc2239daa0e6bef6&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.source&quot;: &quot;https://github.com/linuxserver/docker-wireshark&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.title&quot;: &quot;Wireshark&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.url&quot;: &quot;https://github.com/linuxserver/docker-wireshark/packages&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.vendor&quot;: &quot;linuxserver.io&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.version&quot;: &quot;4.4.7-r0-ls277&quot;,</span>
<span style="color:#AA5500">                &quot;traefik.enable&quot;: &quot;False&quot;,</span>
<span style="color:#AA5500">                &quot;traefik.http.routers.wireshark.rule&quot;: &quot;Host(`wireshark.Schneider.nbg`)&quot;,</span>
<span style="color:#AA5500">                &quot;traefik.http.routers.wireshark.tls.certresolver&quot;: &quot;letsencrypt&quot;,</span>
<span style="color:#AA5500">                &quot;traefik.http.routers.wireshark.tls.domains[0].main&quot;: &quot;Schneider.nbg&quot;,</span>
<span style="color:#AA5500">                &quot;traefik.http.routers.wireshark.tls.domains[0].sans&quot;: &quot;*.Schneider.nbg&quot;,</span>
<span style="color:#AA5500">                &quot;traefik.http.services.wireshark.loadbalancer.server.port&quot;: &quot;3000&quot;</span>
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
<span style="color:#AA5500">        &quot;Created&quot;: &quot;2025-10-10T03:07:58.981890588Z&quot;,</span>
<span style="color:#AA5500">        &quot;Driver&quot;: &quot;overlay2&quot;,</span>
<span style="color:#AA5500">        &quot;ExecIDs&quot;: null,</span>
<span style="color:#AA5500">        &quot;GraphDriver&quot;: {</span>
<span style="color:#AA5500">            &quot;Data&quot;: {</span>
<span style="color:#AA5500">                &quot;ID&quot;: &quot;b5bdb3bdec2fdd0852772c1b30ed76f4f908aaeb427731c88fcf3bf488e59015&quot;,</span>
<span style="color:#AA5500">                &quot;LowerDir&quot;: &quot;/var/lib/docker/overlay2/eff91f8e33fe7d4b67e73effedbf76043629d46309181498a3adba14ef654fab-init/diff:/var/lib/docker/overlay2/752eb12022fac73e396c9e9a3edc4babb65bf1bfc16c89183f007529e4e5b7a0/diff:/var/lib/docker/overlay2/72c0ef5b1c6ceaf0bfe7bcfe6bd5fd7e7185d5ed89a52f1e603e69c983f33368/diff:/var/lib/docker/overlay2/96f841dd1bf2f49af67e69817ab6a784eab753dd06cc565baf1978bb3ec4f98d/diff:/var/lib/docker/overlay2/d86b8a6b782d7fe12ed8555f2a29782ef2168ad5c78708ed725f9ea88ba51c22/diff:/var/lib/docker/overlay2/44fab570a17ac6e92ce38208dd1cf5f65524b06f94500090754fc3915af78dad/diff:/var/lib/docker/overlay2/4c9fcb93388ea1be140e2630d81aa99e12ebf41a79693389c9793eb590c40c5c/diff:/var/lib/docker/overlay2/bae18296ac795e3a58067314bef595ea3366f7a07020299ec71dd388884abc2d/diff:/var/lib/docker/overlay2/ecace77797951c8eccd4157913f5bb7322b0fc701d2f4294ab0cc1588f51051c/diff:/var/lib/docker/overlay2/ac258b31591ebba1d54d96d51ff4782409a008f08820b09c764cd9e64fc407f9/diff:/var/lib/docker/overlay2/1cce617b0200ef640c28e8d8dd1b33ec965710057e009c06d414f647332ec1bb/diff:/var/lib/docker/overlay2/83519fb5fdd88bc64702fde4dfc35774f9565e188ec97c31618b70084205bb4a/diff:/var/lib/docker/overlay2/949f2db1051bce293a65a394dae168a5e8b02f708ebdfb1c16710a73a0955353/diff:/var/lib/docker/overlay2/f9b971f278688a9bdb00666744a95167f83d50c47ff9f940f969788efe478ca5/diff&quot;,</span>
<span style="color:#AA5500">                &quot;MergedDir&quot;: &quot;/var/lib/docker/overlay2/eff91f8e33fe7d4b67e73effedbf76043629d46309181498a3adba14ef654fab/merged&quot;,</span>
<span style="color:#AA5500">                &quot;UpperDir&quot;: &quot;/var/lib/docker/overlay2/eff91f8e33fe7d4b67e73effedbf76043629d46309181498a3adba14ef654fab/diff&quot;,</span>
<span style="color:#AA5500">                &quot;WorkDir&quot;: &quot;/var/lib/docker/overlay2/eff91f8e33fe7d4b67e73effedbf76043629d46309181498a3adba14ef654fab/work&quot;</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            &quot;Name&quot;: &quot;overlay2&quot;</span>
<span style="color:#AA5500">        },</span>
<span style="color:#AA5500">        &quot;HostConfig&quot;: {</span>
<span style="color:#AA5500">            &quot;AutoRemove&quot;: false,</span>
<span style="color:#AA5500">            &quot;Binds&quot;: [</span>
<span style="color:#AA5500">                &quot;/mnt/Volume1/docker/wireshark/config:/config:rw&quot;</span>
<span style="color:#AA5500">            ],</span>
<span style="color:#AA5500">            &quot;BlkioDeviceReadBps&quot;: null,</span>
<span style="color:#AA5500">            &quot;BlkioDeviceReadIOps&quot;: null,</span>
<span style="color:#AA5500">            &quot;BlkioDeviceWriteBps&quot;: null,</span>
<span style="color:#AA5500">            &quot;BlkioDeviceWriteIOps&quot;: null,</span>
<span style="color:#AA5500">            &quot;BlkioWeight&quot;: 0,</span>
<span style="color:#AA5500">            &quot;BlkioWeightDevice&quot;: null,</span>
<span style="color:#AA5500">            &quot;CapAdd&quot;: [</span>
<span style="color:#AA5500">                &quot;NET_ADMIN&quot;</span>
<span style="color:#AA5500">            ],</span>
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
<span style="color:#AA5500">            &quot;NetworkMode&quot;: &quot;host&quot;,</span>
<span style="color:#AA5500">            &quot;OomKillDisable&quot;: null,</span>
<span style="color:#AA5500">            &quot;OomScoreAdj&quot;: 0,</span>
<span style="color:#AA5500">            &quot;PidMode&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;PidsLimit&quot;: null,</span>
<span style="color:#AA5500">            &quot;PortBindings&quot;: null,</span>
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
<span style="color:#AA5500">        &quot;HostnamePath&quot;: &quot;/var/lib/docker/containers/b5bdb3bdec2fdd0852772c1b30ed76f4f908aaeb427731c88fcf3bf488e59015/hostname&quot;,</span>
<span style="color:#AA5500">        &quot;HostsPath&quot;: &quot;/var/lib/docker/containers/b5bdb3bdec2fdd0852772c1b30ed76f4f908aaeb427731c88fcf3bf488e59015/hosts&quot;,</span>
<span style="color:#AA5500">        &quot;Id&quot;: &quot;b5bdb3bdec2fdd0852772c1b30ed76f4f908aaeb427731c88fcf3bf488e59015&quot;,</span>
<span style="color:#AA5500">        &quot;Image&quot;: &quot;sha256:1062f101ec4a6a19d7a62634dfe42f91ac679e3c441875bd46150cbbda473c30&quot;,</span>
<span style="color:#AA5500">        &quot;LogPath&quot;: &quot;/var/lib/docker/containers/b5bdb3bdec2fdd0852772c1b30ed76f4f908aaeb427731c88fcf3bf488e59015/b5bdb3bdec2fdd0852772c1b30ed76f4f908aaeb427731c88fcf3bf488e59015-json.log&quot;,</span>
<span style="color:#AA5500">        &quot;MountLabel&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">        &quot;Mounts&quot;: [</span>
<span style="color:#AA5500">            {</span>
<span style="color:#AA5500">                &quot;Destination&quot;: &quot;/config&quot;,</span>
<span style="color:#AA5500">                &quot;Mode&quot;: &quot;rw&quot;,</span>
<span style="color:#AA5500">                &quot;Propagation&quot;: &quot;rprivate&quot;,</span>
<span style="color:#AA5500">                &quot;RW&quot;: true,</span>
<span style="color:#AA5500">                &quot;Source&quot;: &quot;/mnt/Volume1/docker/wireshark/config&quot;,</span>
<span style="color:#AA5500">                &quot;Type&quot;: &quot;bind&quot;</span>
<span style="color:#AA5500">            }</span>
<span style="color:#AA5500">        ],</span>
<span style="color:#AA5500">        &quot;Name&quot;: &quot;/wireshark&quot;,</span>
<span style="color:#AA5500">        &quot;NetworkSettings&quot;: {</span>
<span style="color:#AA5500">            &quot;Bridge&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;EndpointID&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;Gateway&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;GlobalIPv6Address&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;GlobalIPv6PrefixLen&quot;: 0,</span>
<span style="color:#AA5500">            &quot;HairpinMode&quot;: false,</span>
<span style="color:#AA5500">            &quot;IPAddress&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;IPPrefixLen&quot;: 0,</span>
<span style="color:#AA5500">            &quot;IPv6Gateway&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;LinkLocalIPv6Address&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;LinkLocalIPv6PrefixLen&quot;: 0,</span>
<span style="color:#AA5500">            &quot;MacAddress&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;Networks&quot;: {</span>
<span style="color:#AA5500">                &quot;host&quot;: {</span>
<span style="color:#AA5500">                    &quot;Aliases&quot;: null,</span>
<span style="color:#AA5500">                    &quot;DNSNames&quot;: null,</span>
<span style="color:#AA5500">                    &quot;DriverOpts&quot;: null,</span>
<span style="color:#AA5500">                    &quot;EndpointID&quot;: &quot;a7c59fa37b61e491ccb7aa482fbbe19c4b2cecc85b49636cb782fb1257cf9c62&quot;,</span>
<span style="color:#AA5500">                    &quot;Gateway&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">                    &quot;GlobalIPv6Address&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">                    &quot;GlobalIPv6PrefixLen&quot;: 0,</span>
<span style="color:#AA5500">                    &quot;GwPriority&quot;: 0,</span>
<span style="color:#AA5500">                    &quot;IPAMConfig&quot;: null,</span>
<span style="color:#AA5500">                    &quot;IPAddress&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">                    &quot;IPPrefixLen&quot;: 0,</span>
<span style="color:#AA5500">                    &quot;IPv6Gateway&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">                    &quot;Links&quot;: null,</span>
<span style="color:#AA5500">                    &quot;MacAddress&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">                    &quot;NetworkID&quot;: &quot;fb0b7c4943026ade3ac058dc9ffeda4029ed4c219e646fc20aea18c5b3cdbd2a&quot;</span>
<span style="color:#AA5500">                }</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            &quot;Ports&quot;: {},</span>
<span style="color:#AA5500">            &quot;SandboxID&quot;: &quot;442493a7c9546b7660f6a83c9cf9f12ed7dfc82e7e8edffde3cae200bd084259&quot;,</span>
<span style="color:#AA5500">            &quot;SandboxKey&quot;: &quot;/var/run/docker/netns/default&quot;,</span>
<span style="color:#AA5500">            &quot;SecondaryIPAddresses&quot;: null,</span>
<span style="color:#AA5500">            &quot;SecondaryIPv6Addresses&quot;: null</span>
<span style="color:#AA5500">        },</span>
<span style="color:#AA5500">        &quot;Path&quot;: &quot;/init&quot;,</span>
<span style="color:#AA5500">        &quot;Platform&quot;: &quot;linux&quot;,</span>
<span style="color:#AA5500">        &quot;ProcessLabel&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">        &quot;ResolvConfPath&quot;: &quot;/var/lib/docker/containers/b5bdb3bdec2fdd0852772c1b30ed76f4f908aaeb427731c88fcf3bf488e59015/resolv.conf&quot;,</span>
<span style="color:#AA5500">        &quot;RestartCount&quot;: 0,</span>
<span style="color:#AA5500">        &quot;State&quot;: {</span>
<span style="color:#AA5500">            &quot;Dead&quot;: false,</span>
<span style="color:#AA5500">            &quot;Error&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;ExitCode&quot;: 0,</span>
<span style="color:#AA5500">            &quot;FinishedAt&quot;: &quot;2025-10-10T04:02:50.014607673Z&quot;,</span>
<span style="color:#AA5500">            &quot;OOMKilled&quot;: false,</span>
<span style="color:#AA5500">            &quot;Paused&quot;: false,</span>
<span style="color:#AA5500">            &quot;Pid&quot;: 2127108,</span>
<span style="color:#AA5500">            &quot;Restarting&quot;: false,</span>
<span style="color:#AA5500">            &quot;Running&quot;: true,</span>
<span style="color:#AA5500">            &quot;StartedAt&quot;: &quot;2025-10-10T04:02:54.020295728Z&quot;,</span>
<span style="color:#AA5500">            &quot;Status&quot;: &quot;running&quot;</span>
<span style="color:#AA5500">        }</span>
<span style="color:#AA5500">    }</span>
<span style="color:#AA5500">}</span>
Freitag 10 Oktober 2025  23:19:25 +0200 (0:00:01.869)       0:02:50.021 ******* 
Freitag 10 Oktober 2025  23:19:25 +0200 (0:00:00.063)       0:02:50.085 ******* 
Freitag 10 Oktober 2025  23:19:25 +0200 (0:00:00.044)       0:02:50.129 ******* 
Freitag 10 Oktober 2025  23:19:25 +0200 (0:00:00.050)       0:02:50.179 ******* 
Freitag 10 Oktober 2025  23:19:25 +0200 (0:00:00.051)       0:02:50.231 ******* 
Freitag 10 Oktober 2025  23:19:25 +0200 (0:00:00.043)       0:02:50.274 ******* 
Freitag 10 Oktober 2025  23:19:25 +0200 (0:00:00.047)       0:02:50.321 ******* 
Freitag 10 Oktober 2025  23:19:25 +0200 (0:00:00.140)       0:02:50.462 ******* 

TASK [woodpecker-ci : Stop Woodpecker-CI] *************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/woodpecker-ci/tasks/main.yml:78</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:19:26 +0200 (0:00:00.624)       0:02:51.087 ******* 
Freitag 10 Oktober 2025  23:19:26 +0200 (0:00:00.066)       0:02:51.153 ******* 
Freitag 10 Oktober 2025  23:19:26 +0200 (0:00:00.047)       0:02:51.201 ******* 

TASK [youtubedlmaterial : Stop Youtubedlmaterial] *****************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/youtubedlmaterial/tasks/main.yml:52</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Freitag 10 Oktober 2025  23:19:26 +0200 (0:00:00.595)       0:02:51.796 ******* 
Freitag 10 Oktober 2025  23:19:27 +0200 (0:00:00.061)       0:02:51.858 ******* 
Freitag 10 Oktober 2025  23:19:27 +0200 (0:00:00.047)       0:02:51.905 ******* 
Freitag 10 Oktober 2025  23:19:27 +0200 (0:00:00.052)       0:02:51.958 ******* 

TASK [znc : Stop ZNC] *********************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/znc/tasks/main.yml:45</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>

PLAY RECAP ********************************************************************************************************************************************************************************************************
<span style="color:#AA5500">ansible-nas</span>                : <span style="color:#00AA00">ok=172 </span> <span style="color:#AA5500">changed=15  </span> unreachable=0    failed=0    <span style="color:#00AAAA">skipped=304 </span> rescued=0    ignored=0   

Freitag 10 Oktober 2025  23:19:27 +0200 (0:00:00.621)       0:02:52.579 ******* 
=============================================================================== 
dokuwiki : DokuWiki Docker Container ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- 10.98s
/media/IT/repos/github/forked/ansible-nas/roles/dokuwiki/tasks/main.yml:11 ---------------------------------------------------------------------------------------------------------------------------------------
geerlingguy.nfs : Ensure directories to export exist ------------------------------------------------------------------------------------------------------------------------------------------------------- 6.08s
/home/dietmar/.ansible/roles/geerlingguy.nfs/tasks/main.yml:19 ---------------------------------------------------------------------------------------------------------------------------------------------------
homepage : Template config files --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 4.59s
/media/IT/repos/github/forked/ansible-nas/roles/homepage/tasks/main.yml:11 ---------------------------------------------------------------------------------------------------------------------------------------
ansible-nas-general : Update apt-cache --------------------------------------------------------------------------------------------------------------------------------------------------------------------- 4.14s
/media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-general/tasks/main.yml:7 -----------------------------------------------------------------------------------------------------------------------------
homeassistant : Home Assistant Docker Container ------------------------------------------------------------------------------------------------------------------------------------------------------------ 2.04s
/media/IT/repos/github/forked/ansible-nas/roles/homeassistant/tasks/main.yml:11 ----------------------------------------------------------------------------------------------------------------------------------
tinymm : tinyMediaManager Docker Container ----------------------------------------------------------------------------------------------------------------------------------------------------------------- 1.93s
/media/IT/repos/github/forked/ansible-nas/roles/tinymm/tasks/main.yml:15 -----------------------------------------------------------------------------------------------------------------------------------------
calibre : Calibre Docker Container ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 1.92s
/media/IT/repos/github/forked/ansible-nas/roles/calibre/tasks/main.yml:12 ----------------------------------------------------------------------------------------------------------------------------------------
dupeguru : dupeGuru Docker Container ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- 1.91s
/media/IT/repos/github/forked/ansible-nas/roles/dupeguru/tasks/main.yml:13 ---------------------------------------------------------------------------------------------------------------------------------------
wireshark : Create Wireshark Docker Container -------------------------------------------------------------------------------------------------------------------------------------------------------------- 1.87s
/media/IT/repos/github/forked/ansible-nas/roles/wireshark/tasks/main.yml:12 --------------------------------------------------------------------------------------------------------------------------------------
freshrss : FreshRSS Docker Container ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- 1.82s
/media/IT/repos/github/forked/ansible-nas/roles/freshrss/tasks/main.yml:12 ---------------------------------------------------------------------------------------------------------------------------------------
portainer : Portainer Docker Container --------------------------------------------------------------------------------------------------------------------------------------------------------------------- 1.81s
/media/IT/repos/github/forked/ansible-nas/roles/portainer/tasks/main.yml:16 --------------------------------------------------------------------------------------------------------------------------------------
glances : Create Glances Docker Container ------------------------------------------------------------------------------------------------------------------------------------------------------------------ 1.80s
/media/IT/repos/github/forked/ansible-nas/roles/glances/tasks/main.yml:4 -----------------------------------------------------------------------------------------------------------------------------------------
mosquitto : Create Mosquitto container --------------------------------------------------------------------------------------------------------------------------------------------------------------------- 1.79s
/media/IT/repos/github/forked/ansible-nas/roles/mosquitto/tasks/main.yml:19 --------------------------------------------------------------------------------------------------------------------------------------
ansible-nas-users : Create ansible-nas group --------------------------------------------------------------------------------------------------------------------------------------------------------------- 1.77s
/media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-users/tasks/main.yml:2 -------------------------------------------------------------------------------------------------------------------------------
calibreweb : Calibre-web Docker Container ------------------------------------------------------------------------------------------------------------------------------------------------------------------ 1.76s
/media/IT/repos/github/forked/ansible-nas/roles/calibreweb/tasks/main.yml:12 -------------------------------------------------------------------------------------------------------------------------------------
homepage : Create Homepage Docker Container ---------------------------------------------------------------------------------------------------------------------------------------------------------------- 1.73s
/media/IT/repos/github/forked/ansible-nas/roles/homepage/tasks/main.yml:23 ---------------------------------------------------------------------------------------------------------------------------------------
vladgh.samba.server : Install Samba packages --------------------------------------------------------------------------------------------------------------------------------------------------------------- 1.69s
/home/dietmar/.ansible/collections/ansible_collections/vladgh/samba/roles/server/tasks/main.yml:12 ---------------------------------------------------------------------------------------------------------------
ansible-nas-docker : Install docker python module ---------------------------------------------------------------------------------------------------------------------------------------------------------- 1.68s
/media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-docker/tasks/main.yml:26 -----------------------------------------------------------------------------------------------------------------------------
geerlingguy.docker : Ensure additional dependencies are installed (on Ubuntu &lt; 20.04 and any other systems). ----------------------------------------------------------------------------------------------- 1.51s
/home/dietmar/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml:18 ----------------------------------------------------------------------------------------------------------------------------------------
geerlingguy.docker : Install Docker packages (with downgrade option). -------------------------------------------------------------------------------------------------------------------------------------- 1.50s
/home/dietmar/.ansible/roles/geerlingguy.docker/tasks/main.yml:27 ------------------------------------------------------------------------------------------------------------------------------------------------
[<span style="color:#00AA00">2025-10-10 23:19:28</span>] (Venv) [<span style="color:#55FF55"><b>dietmar@MiraPi</b></span>] [<span style="color:#5555FF"><b>.../forked/ansible-nas</b></span>] $ 
</pre>