<pre>[<span style="color:#00AA00">2025-10-09 18:50:37</span>] (Venv) [<span style="color:#55FF55"><b>dietmar@MiraPi</b></span>] [<span style="color:#5555FF"><b>.../forked/ansible-nas</b></span>] $ ansible-playbook -i inventories/RaspiNAS/inventory nas.yml -b 
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
Donnerstag 09 Oktober 2025  18:50:41 +0200 (0:00:00.152)       0:00:00.153 **** 

TASK [Gathering Facts] ********************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/nas.yml:2</b></span>
<span style="color:#00AA00">ok: [ansible-nas]</span>
Donnerstag 09 Oktober 2025  18:50:44 +0200 (0:00:02.817)       0:00:02.970 **** 

TASK [ansible-nas-users : Create ansible-nas group] ***************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-users/tasks/main.yml:2</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;gid&quot;: 1001,</span>
<span style="color:#00AA00">    &quot;name&quot;: &quot;ansible-nas&quot;,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;present&quot;,</span>
<span style="color:#00AA00">    &quot;system&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:50:45 +0200 (0:00:00.522)       0:00:03.493 **** 

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
Donnerstag 09 Oktober 2025  18:50:45 +0200 (0:00:00.620)       0:00:04.113 **** 

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
Donnerstag 09 Oktober 2025  18:50:45 +0200 (0:00:00.045)       0:00:04.159 **** 

TASK [vladgh.samba.server : Install Samba packages] ***************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/collections/ansible_collections/vladgh/samba/roles/server/tasks/main.yml:12</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;cache_update_time&quot;: 1760005148,</span>
<span style="color:#00AA00">    &quot;cache_updated&quot;: false,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:50:47 +0200 (0:00:01.639)       0:00:05.798 **** 

TASK [vladgh.samba.server : Install Samba VFS extensions packages] ************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/collections/ansible_collections/vladgh/samba/roles/server/tasks/main.yml:19</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;cache_update_time&quot;: 1760005148,</span>
<span style="color:#00AA00">    &quot;cache_updated&quot;: false,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:50:49 +0200 (0:00:01.446)       0:00:07.244 **** 

TASK [vladgh.samba.server : Register Samba version] ***************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/collections/ansible_collections/vladgh/samba/roles/server/tasks/main.yml:26</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;cmd&quot;: &quot;set -o nounset -o pipefail -o errexit &amp;&amp; smbd --version | sed &apos;s/Version //&apos;\n&quot;,</span>
<span style="color:#00AA00">    &quot;delta&quot;: &quot;0:00:00.043944&quot;,</span>
<span style="color:#00AA00">    &quot;end&quot;: &quot;2025-10-09 18:50:49.598905&quot;,</span>
<span style="color:#00AA00">    &quot;rc&quot;: 0,</span>
<span style="color:#00AA00">    &quot;start&quot;: &quot;2025-10-09 18:50:49.554961&quot;</span>
<span style="color:#00AA00">}</span>

<span style="color:#00AA00">STDOUT:</span>

<span style="color:#00AA00">4.17.12-Debian</span>
Donnerstag 09 Oktober 2025  18:50:49 +0200 (0:00:00.590)       0:00:07.835 **** 
Donnerstag 09 Oktober 2025  18:50:49 +0200 (0:00:00.055)       0:00:07.891 **** 
Donnerstag 09 Oktober 2025  18:50:49 +0200 (0:00:00.032)       0:00:07.923 **** 
Donnerstag 09 Oktober 2025  18:50:49 +0200 (0:00:00.055)       0:00:07.979 **** 
Donnerstag 09 Oktober 2025  18:50:49 +0200 (0:00:00.038)       0:00:08.017 **** 

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
Donnerstag 09 Oktober 2025  18:50:50 +0200 (0:00:00.914)       0:00:08.932 **** 
Donnerstag 09 Oktober 2025  18:50:50 +0200 (0:00:00.037)       0:00:08.969 **** 
Donnerstag 09 Oktober 2025  18:50:50 +0200 (0:00:00.036)       0:00:09.007 **** 
Donnerstag 09 Oktober 2025  18:50:50 +0200 (0:00:00.032)       0:00:09.039 **** 
Donnerstag 09 Oktober 2025  18:50:50 +0200 (0:00:00.037)       0:00:09.077 **** 

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
<span style="color:#00AA00">        &quot;After&quot;: &quot;network.target system.slice nmbd.service network-online.target winbind.service systemd-journald.socket sysinit.target basic.target&quot;,</span>
<span style="color:#00AA00">        &quot;AllowIsolate&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;AssertResult&quot;: &quot;yes&quot;,</span>
<span style="color:#00AA00">        &quot;AssertTimestamp&quot;: &quot;Sun 2025-10-05 14:54:06 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;AssertTimestampMonotonic&quot;: &quot;15341479&quot;,</span>
<span style="color:#00AA00">        &quot;Before&quot;: &quot;multi-user.target zfs-share.service shutdown.target&quot;,</span>
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
<span style="color:#00AA00">        &quot;CPUUsageNSec&quot;: &quot;1675602000&quot;,</span>
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
Donnerstag 09 Oktober 2025  18:50:51 +0200 (0:00:00.932)       0:00:10.009 **** 

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
<span style="color:#00AA00">        &quot;After&quot;: &quot;system.slice network-online.target network.target sysinit.target systemd-journald.socket basic.target&quot;,</span>
<span style="color:#00AA00">        &quot;AllowIsolate&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;AssertResult&quot;: &quot;yes&quot;,</span>
<span style="color:#00AA00">        &quot;AssertTimestamp&quot;: &quot;Sun 2025-10-05 14:54:06 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;AssertTimestampMonotonic&quot;: &quot;15042627&quot;,</span>
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
<span style="color:#00AA00">        &quot;CPUUsageNSec&quot;: &quot;41370384000&quot;,</span>
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
Donnerstag 09 Oktober 2025  18:50:52 +0200 (0:00:00.553)       0:00:10.563 **** 
Donnerstag 09 Oktober 2025  18:50:52 +0200 (0:00:00.042)       0:00:10.606 **** 

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
Donnerstag 09 Oktober 2025  18:50:52 +0200 (0:00:00.041)       0:00:10.647 **** 
Donnerstag 09 Oktober 2025  18:50:52 +0200 (0:00:00.034)       0:00:10.682 **** 
Donnerstag 09 Oktober 2025  18:50:52 +0200 (0:00:00.034)       0:00:10.716 **** 

TASK [geerlingguy.nfs : include_tasks] ****************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.nfs/tasks/main.yml:16</b></span>
<span style="color:#00AAAA">included: /home/dietmar/.ansible/roles/geerlingguy.nfs/tasks/setup-Debian.yml for ansible-nas</span>
Donnerstag 09 Oktober 2025  18:50:52 +0200 (0:00:00.050)       0:00:10.767 **** 

TASK [geerlingguy.nfs : Ensure NFS utilities are installed.] ******************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.nfs/tasks/setup-Debian.yml:2</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;cache_update_time&quot;: 1760005148,</span>
<span style="color:#00AA00">    &quot;cache_updated&quot;: false,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:50:53 +0200 (0:00:01.409)       0:00:12.176 **** 

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
Donnerstag 09 Oktober 2025  18:51:00 +0200 (0:00:06.015)       0:00:18.191 **** 

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
Donnerstag 09 Oktober 2025  18:51:00 +0200 (0:00:00.648)       0:00:18.839 **** 

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
<span style="color:#00AA00">        &quot;After&quot;: &quot;nfsdcld.service network-online.target rpc-svcgssd.service zfs-share.service mnt-Volume1.mount gssproxy.service nfs-mountd.service local-fs.target systemd-journald.socket rpc-statd.service system.slice -.mount nfs-idmapd.service rpcbind.socket proc-fs-nfsd.mount rpc-gssd.service&quot;,</span>
<span style="color:#00AA00">        &quot;AllowIsolate&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;AssertResult&quot;: &quot;yes&quot;,</span>
<span style="color:#00AA00">        &quot;AssertTimestamp&quot;: &quot;Sun 2025-10-05 14:54:06 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;AssertTimestampMonotonic&quot;: &quot;15580387&quot;,</span>
<span style="color:#00AA00">        &quot;Before&quot;: &quot;media-web.mount media-Produktion.mount rpc-statd-notify.service media-Medien.mount media-Dokumente.mount&quot;,</span>
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
<span style="color:#00AA00">        &quot;ConsistsOf&quot;: &quot;zfs-share.service rpc-svcgssd.service&quot;,</span>
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
<span style="color:#00AA00">        &quot;Requires&quot;: &quot;system.slice proc-fs-nfsd.mount nfs-mountd.service network.target mnt-Volume1.mount -.mount&quot;,</span>
<span style="color:#00AA00">        &quot;RequiresMountsFor&quot;: &quot;/mnt/Volume1/local/Podcasts /mnt/Volume1/local/TV /mnt/Volume1/local/Download /mnt/Volume1/local/Audiobooks /mnt/Volume1/docker /mnt/Volume1/local/Music /mnt/Volume1/local/Web /mnt/Volume1/local/Comics /mnt/Volume1/local/Media /mnt/Volume1/local/Persönliches /mnt/Volume1/local/Organisation /mnt/Volume1/local/Versorgung /mnt/Volume1/local/Movies /mnt/Volume1/local/Ägyptologie /mnt/Volume1/local/Documents /mnt/Volume1/local/Books /mnt/Volume1/local/Inventar /mnt/Volume1/local/IT /mnt/Volume1/local/Photos&quot;,</span>
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
<span style="color:#00AA00">        &quot;Wants&quot;: &quot;nfs-idmapd.service rpc-statd-notify.service nfsdcld.service rpcbind.socket network-online.target rpc-svcgssd.service auth-rpcgss-module.service rpc-statd.service&quot;,</span>
<span style="color:#00AA00">        &quot;WatchdogSignal&quot;: &quot;6&quot;,</span>
<span style="color:#00AA00">        &quot;WatchdogTimestampMonotonic&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;WatchdogUSec&quot;: &quot;0&quot;</span>
<span style="color:#00AA00">    }</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:51:01 +0200 (0:00:00.619)       0:00:19.459 **** 

TASK [geerlingguy.docker : Load OS-specific vars.] ****************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.docker/tasks/main.yml:2</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;ansible_facts&quot;: {},</span>
<span style="color:#00AA00">    &quot;ansible_included_var_files&quot;: [</span>
<span style="color:#00AA00">        &quot;/home/dietmar/.ansible/roles/geerlingguy.docker/vars/main.yml&quot;</span>
<span style="color:#00AA00">    ],</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:51:01 +0200 (0:00:00.047)       0:00:19.506 **** 
Donnerstag 09 Oktober 2025  18:51:01 +0200 (0:00:00.035)       0:00:19.542 **** 

TASK [geerlingguy.docker : include_tasks] *************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.docker/tasks/main.yml:16</b></span>
<span style="color:#00AAAA">included: /home/dietmar/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml for ansible-nas</span>
Donnerstag 09 Oktober 2025  18:51:01 +0200 (0:00:00.057)       0:00:19.600 **** 

TASK [geerlingguy.docker : Ensure old versions of Docker are not installed.] **************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml:2</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:51:02 +0200 (0:00:00.985)       0:00:20.585 **** 

TASK [geerlingguy.docker : Ensure dependencies are installed.] ****************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml:10</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;cache_update_time&quot;: 1760005148,</span>
<span style="color:#00AA00">    &quot;cache_updated&quot;: false,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:51:03 +0200 (0:00:01.400)       0:00:21.986 **** 

TASK [geerlingguy.docker : Ensure additional dependencies are installed (on Ubuntu &lt; 20.04 and any other systems).] ***********************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml:18</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;cache_update_time&quot;: 1760005148,</span>
<span style="color:#00AA00">    &quot;cache_updated&quot;: false,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:51:05 +0200 (0:00:01.428)       0:00:23.415 **** 
Donnerstag 09 Oktober 2025  18:51:05 +0200 (0:00:00.044)       0:00:23.460 **** 

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
Donnerstag 09 Oktober 2025  18:51:05 +0200 (0:00:00.581)       0:00:24.041 **** 
Donnerstag 09 Oktober 2025  18:51:05 +0200 (0:00:00.059)       0:00:24.101 **** 
Donnerstag 09 Oktober 2025  18:51:05 +0200 (0:00:00.069)       0:00:24.170 **** 

TASK [geerlingguy.docker : Add Docker repository.] ****************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml:50</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;repo&quot;: &quot;deb [arch=arm64 signed-by=/etc/apt/trusted.gpg.d/docker.asc] https://download.docker.com/linux/debian bookworm stable&quot;,</span>
<span style="color:#00AA00">    &quot;sources_added&quot;: [],</span>
<span style="color:#00AA00">    &quot;sources_removed&quot;: [],</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;present&quot;</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:51:06 +0200 (0:00:00.724)       0:00:24.895 **** 
Donnerstag 09 Oktober 2025  18:51:06 +0200 (0:00:00.037)       0:00:24.932 **** 

TASK [geerlingguy.docker : Install Docker packages (with downgrade option).] **************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.docker/tasks/main.yml:27</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;cache_update_time&quot;: 1760005148,</span>
<span style="color:#00AA00">    &quot;cache_updated&quot;: false,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:51:08 +0200 (0:00:01.430)       0:00:26.362 **** 
Donnerstag 09 Oktober 2025  18:51:08 +0200 (0:00:00.055)       0:00:26.417 **** 

TASK [geerlingguy.docker : Install docker-compose-plugin (with downgrade option).] ********************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.docker/tasks/main.yml:44</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;cache_update_time&quot;: 1760005148,</span>
<span style="color:#00AA00">    &quot;cache_updated&quot;: false,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:51:09 +0200 (0:00:01.422)       0:00:27.839 **** 
Donnerstag 09 Oktober 2025  18:51:09 +0200 (0:00:00.069)       0:00:27.909 **** 
Donnerstag 09 Oktober 2025  18:51:09 +0200 (0:00:00.056)       0:00:27.966 **** 

TASK [geerlingguy.docker : Ensure Docker is started and enabled at boot.] *****************************************************************************************************************************************
<span style="color:#555555"><b>task path: /home/dietmar/.ansible/roles/geerlingguy.docker/tasks/main.yml:68</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;enabled&quot;: true,</span>
<span style="color:#00AA00">    &quot;name&quot;: &quot;docker&quot;,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;started&quot;,</span>
<span style="color:#00AA00">    &quot;status&quot;: {</span>
<span style="color:#00AA00">        &quot;ActiveEnterTimestamp&quot;: &quot;Sun 2025-10-05 14:54:08 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;ActiveEnterTimestampMonotonic&quot;: &quot;17142072&quot;,</span>
<span style="color:#00AA00">        &quot;ActiveExitTimestampMonotonic&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;ActiveState&quot;: &quot;active&quot;,</span>
<span style="color:#00AA00">        &quot;After&quot;: &quot;docker.socket network-online.target systemd-journald.socket time-set.target containerd.service nss-lookup.target sysinit.target basic.target system.slice firewalld.service&quot;,</span>
<span style="color:#00AA00">        &quot;AllowIsolate&quot;: &quot;no&quot;,</span>
<span style="color:#00AA00">        &quot;AssertResult&quot;: &quot;yes&quot;,</span>
<span style="color:#00AA00">        &quot;AssertTimestamp&quot;: &quot;Sun 2025-10-05 14:54:06 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;AssertTimestampMonotonic&quot;: &quot;15037107&quot;,</span>
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
<span style="color:#00AA00">        &quot;CPUUsageNSec&quot;: &quot;242007162000&quot;,</span>
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
<span style="color:#00AA00">        &quot;ConditionTimestampMonotonic&quot;: &quot;15037105&quot;,</span>
<span style="color:#00AA00">        &quot;ConfigurationDirectoryMode&quot;: &quot;0755&quot;,</span>
<span style="color:#00AA00">        &quot;Conflicts&quot;: &quot;shutdown.target&quot;,</span>
<span style="color:#00AA00">        &quot;ControlGroup&quot;: &quot;/system.slice/docker.service&quot;,</span>
<span style="color:#00AA00">        &quot;ControlGroupId&quot;: &quot;3042&quot;,</span>
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
<span style="color:#00AA00">        &quot;ExecMainPID&quot;: &quot;1010&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainStartTimestamp&quot;: &quot;Sun 2025-10-05 14:54:06 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;ExecMainStartTimestampMonotonic&quot;: &quot;15038695&quot;,</span>
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
<span style="color:#00AA00">        &quot;InactiveEnterTimestampMonotonic&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;InactiveExitTimestamp&quot;: &quot;Sun 2025-10-05 14:54:06 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;InactiveExitTimestampMonotonic&quot;: &quot;15038998&quot;,</span>
<span style="color:#00AA00">        &quot;InvocationID&quot;: &quot;42fa14ab75744ffab966b5cd2ff40c80&quot;,</span>
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
<span style="color:#00AA00">        &quot;MainPID&quot;: &quot;1010&quot;,</span>
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
<span style="color:#00AA00">        &quot;StateChangeTimestamp&quot;: &quot;Sun 2025-10-05 14:54:08 CEST&quot;,</span>
<span style="color:#00AA00">        &quot;StateChangeTimestampMonotonic&quot;: &quot;17142072&quot;,</span>
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
<span style="color:#00AA00">        &quot;TasksCurrent&quot;: &quot;137&quot;,</span>
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
<span style="color:#00AA00">        &quot;Wants&quot;: &quot;containerd.service network-online.target&quot;,</span>
<span style="color:#00AA00">        &quot;WatchdogSignal&quot;: &quot;6&quot;,</span>
<span style="color:#00AA00">        &quot;WatchdogTimestampMonotonic&quot;: &quot;0&quot;,</span>
<span style="color:#00AA00">        &quot;WatchdogUSec&quot;: &quot;0&quot;</span>
<span style="color:#00AA00">    }</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:51:10 +0200 (0:00:00.557)       0:00:28.524 **** 
<span style="color:#0000AA">META: triggered running handlers for ansible-nas</span>
Donnerstag 09 Oktober 2025  18:51:10 +0200 (0:00:00.015)       0:00:28.539 **** 
Donnerstag 09 Oktober 2025  18:51:10 +0200 (0:00:00.063)       0:00:28.602 **** 
Donnerstag 09 Oktober 2025  18:51:10 +0200 (0:00:00.079)       0:00:28.682 **** 
Donnerstag 09 Oktober 2025  18:51:10 +0200 (0:00:00.037)       0:00:28.719 **** 
Donnerstag 09 Oktober 2025  18:51:10 +0200 (0:00:00.055)       0:00:28.775 **** 

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
Donnerstag 09 Oktober 2025  18:51:11 +0200 (0:00:00.619)       0:00:29.394 **** 

TASK [ansible-nas-general : Update apt-cache] *********************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-general/tasks/main.yml:7</b></span>
<span style="color:#AA5500">changed: [ansible-nas] =&gt; {</span>
<span style="color:#AA5500">    &quot;attempts&quot;: 1,</span>
<span style="color:#AA5500">    &quot;cache_update_time&quot;: 1760028676,</span>
<span style="color:#AA5500">    &quot;cache_updated&quot;: true,</span>
<span style="color:#AA5500">    &quot;changed&quot;: true</span>
<span style="color:#AA5500">}</span>
Donnerstag 09 Oktober 2025  18:51:18 +0200 (0:00:07.513)       0:00:36.908 **** 
Donnerstag 09 Oktober 2025  18:51:18 +0200 (0:00:00.051)       0:00:36.960 **** 

TASK [ansible-nas-general : Install some packages] ****************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-general/tasks/main.yml:22</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;attempts&quot;: 1,</span>
<span style="color:#00AA00">    &quot;cache_update_time&quot;: 1760028676,</span>
<span style="color:#00AA00">    &quot;cache_updated&quot;: false,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:51:20 +0200 (0:00:01.428)       0:00:38.388 **** 

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
Donnerstag 09 Oktober 2025  18:51:21 +0200 (0:00:01.011)       0:00:39.400 **** 

TASK [ansible-nas-general : Set timezone to Europe/Berlin] ********************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-general/tasks/main.yml:33</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:51:21 +0200 (0:00:00.739)       0:00:40.139 **** 
Donnerstag 09 Oktober 2025  18:51:22 +0200 (0:00:00.043)       0:00:40.183 **** 

TASK [ansible-nas-docker : Install python3-pip] *******************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-docker/tasks/main.yml:2</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;attempts&quot;: 1,</span>
<span style="color:#00AA00">    &quot;cache_update_time&quot;: 1760028676,</span>
<span style="color:#00AA00">    &quot;cache_updated&quot;: false,</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:51:23 +0200 (0:00:01.412)       0:00:41.596 **** 

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
Donnerstag 09 Oktober 2025  18:51:24 +0200 (0:00:00.627)       0:00:42.224 **** 

TASK [ansible-nas-docker : Remove &quot;ext-managed&quot;] ******************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-docker/tasks/main.yml:14</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;path&quot;: &quot;/usr/lib/python3.11/EXTERNALLY-MANAGED&quot;,</span>
<span style="color:#00AA00">    &quot;state&quot;: &quot;absent&quot;</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:51:24 +0200 (0:00:00.379)       0:00:42.603 **** 

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

Donnerstag 09 Oktober 2025  18:51:25 +0200 (0:00:01.319)       0:00:43.922 **** 

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

Donnerstag 09 Oktober 2025  18:51:27 +0200 (0:00:01.575)       0:00:45.498 **** 

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
Donnerstag 09 Oktober 2025  18:51:27 +0200 (0:00:00.343)       0:00:45.841 **** 

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
Donnerstag 09 Oktober 2025  18:51:28 +0200 (0:00:00.412)       0:00:46.253 **** 

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
Donnerstag 09 Oktober 2025  18:51:28 +0200 (0:00:00.620)       0:00:46.874 **** 
Donnerstag 09 Oktober 2025  18:51:28 +0200 (0:00:00.045)       0:00:46.919 **** 
Donnerstag 09 Oktober 2025  18:51:28 +0200 (0:00:00.039)       0:00:46.959 **** 

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
Donnerstag 09 Oktober 2025  18:51:28 +0200 (0:00:00.059)       0:00:47.019 **** 
Donnerstag 09 Oktober 2025  18:51:28 +0200 (0:00:00.049)       0:00:47.068 **** 
Donnerstag 09 Oktober 2025  18:51:28 +0200 (0:00:00.037)       0:00:47.106 **** 

TASK [airsonic : Stop Airsonic] ***********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/airsonic/tasks/main.yml:37</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:51:30 +0200 (0:00:01.072)       0:00:48.178 **** 
Donnerstag 09 Oktober 2025  18:51:30 +0200 (0:00:00.046)       0:00:48.224 **** 
Donnerstag 09 Oktober 2025  18:51:30 +0200 (0:00:00.044)       0:00:48.269 **** 
Donnerstag 09 Oktober 2025  18:51:30 +0200 (0:00:00.040)       0:00:48.310 **** 
Donnerstag 09 Oktober 2025  18:51:30 +0200 (0:00:00.048)       0:00:48.359 **** 

TASK [apcupsd : Stop Apcupsd] *************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/apcupsd/tasks/main.yml:44</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:51:30 +0200 (0:00:00.568)       0:00:48.927 **** 
Donnerstag 09 Oktober 2025  18:51:30 +0200 (0:00:00.118)       0:00:49.046 **** 
Donnerstag 09 Oktober 2025  18:51:30 +0200 (0:00:00.039)       0:00:49.086 **** 

TASK [bazarr : Stop Bazarr] ***************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/bazarr/tasks/main.yml:46</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:51:31 +0200 (0:00:00.591)       0:00:49.677 **** 
Donnerstag 09 Oktober 2025  18:51:31 +0200 (0:00:00.035)       0:00:49.713 **** 
Donnerstag 09 Oktober 2025  18:51:31 +0200 (0:00:00.051)       0:00:49.764 **** 
Donnerstag 09 Oktober 2025  18:51:31 +0200 (0:00:00.035)       0:00:49.799 **** 
Donnerstag 09 Oktober 2025  18:51:31 +0200 (0:00:00.045)       0:00:49.845 **** 

TASK [bitwarden : Stop Bitwarden] *********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/bitwarden/tasks/main.yml:64</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:51:32 +0200 (0:00:00.595)       0:00:50.441 **** 

TASK [bitwarden : Stop Bitwarden Backup] **************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/bitwarden/tasks/main.yml:69</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:51:32 +0200 (0:00:00.584)       0:00:51.026 **** 
Donnerstag 09 Oktober 2025  18:51:32 +0200 (0:00:00.045)       0:00:51.071 **** 
Donnerstag 09 Oktober 2025  18:51:32 +0200 (0:00:00.039)       0:00:51.110 **** 

TASK [booksonic : Stop Booksonic] *********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/booksonic/tasks/main.yml:42</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:51:33 +0200 (0:00:00.591)       0:00:51.702 **** 

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
Donnerstag 09 Oktober 2025  18:51:33 +0200 (0:00:00.361)       0:00:52.063 **** 

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
<span style="color:#AA5500">            &quot;EndpointID&quot;: &quot;b5f3edb3ffc9483084c474e92ccc62d918af07c28d3757bc2c77b77cf91736b9&quot;,</span>
<span style="color:#AA5500">            &quot;Gateway&quot;: &quot;172.17.0.1&quot;,</span>
<span style="color:#AA5500">            &quot;GlobalIPv6Address&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;GlobalIPv6PrefixLen&quot;: 0,</span>
<span style="color:#AA5500">            &quot;HairpinMode&quot;: false,</span>
<span style="color:#AA5500">            &quot;IPAddress&quot;: &quot;172.17.0.3&quot;,</span>
<span style="color:#AA5500">            &quot;IPPrefixLen&quot;: 16,</span>
<span style="color:#AA5500">            &quot;IPv6Gateway&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;LinkLocalIPv6Address&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;LinkLocalIPv6PrefixLen&quot;: 0,</span>
<span style="color:#AA5500">            &quot;MacAddress&quot;: &quot;8a:28:dd:88:1b:5b&quot;,</span>
<span style="color:#AA5500">            &quot;Networks&quot;: {</span>
<span style="color:#AA5500">                &quot;bridge&quot;: {</span>
<span style="color:#AA5500">                    &quot;Aliases&quot;: null,</span>
<span style="color:#AA5500">                    &quot;DNSNames&quot;: null,</span>
<span style="color:#AA5500">                    &quot;DriverOpts&quot;: null,</span>
<span style="color:#AA5500">                    &quot;EndpointID&quot;: &quot;b5f3edb3ffc9483084c474e92ccc62d918af07c28d3757bc2c77b77cf91736b9&quot;,</span>
<span style="color:#AA5500">                    &quot;Gateway&quot;: &quot;172.17.0.1&quot;,</span>
<span style="color:#AA5500">                    &quot;GlobalIPv6Address&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">                    &quot;GlobalIPv6PrefixLen&quot;: 0,</span>
<span style="color:#AA5500">                    &quot;GwPriority&quot;: 0,</span>
<span style="color:#AA5500">                    &quot;IPAMConfig&quot;: null,</span>
<span style="color:#AA5500">                    &quot;IPAddress&quot;: &quot;172.17.0.3&quot;,</span>
<span style="color:#AA5500">                    &quot;IPPrefixLen&quot;: 16,</span>
<span style="color:#AA5500">                    &quot;IPv6Gateway&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">                    &quot;Links&quot;: null,</span>
<span style="color:#AA5500">                    &quot;MacAddress&quot;: &quot;8a:28:dd:88:1b:5b&quot;,</span>
<span style="color:#AA5500">                    &quot;NetworkID&quot;: &quot;ec2adf010135e4885496c9e97e12dbc6ddfe52e3d312d8ae75261b7c475789e6&quot;</span>
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
<span style="color:#AA5500">            &quot;SandboxID&quot;: &quot;502d05d76d6d5814104bc6e983990715f8550c61f9dd4e814e19dc3126194b57&quot;,</span>
<span style="color:#AA5500">            &quot;SandboxKey&quot;: &quot;/var/run/docker/netns/502d05d76d6d&quot;,</span>
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
<span style="color:#AA5500">            &quot;FinishedAt&quot;: &quot;2025-10-05T12:53:08.635752729Z&quot;,</span>
<span style="color:#AA5500">            &quot;OOMKilled&quot;: false,</span>
<span style="color:#AA5500">            &quot;Paused&quot;: false,</span>
<span style="color:#AA5500">            &quot;Pid&quot;: 2667,</span>
<span style="color:#AA5500">            &quot;Restarting&quot;: false,</span>
<span style="color:#AA5500">            &quot;Running&quot;: true,</span>
<span style="color:#AA5500">            &quot;StartedAt&quot;: &quot;2025-10-05T12:54:07.697173453Z&quot;,</span>
<span style="color:#AA5500">            &quot;Status&quot;: &quot;running&quot;</span>
<span style="color:#AA5500">        }</span>
<span style="color:#AA5500">    }</span>
<span style="color:#AA5500">}</span>
Donnerstag 09 Oktober 2025  18:51:35 +0200 (0:00:01.898)       0:00:53.962 **** 
Donnerstag 09 Oktober 2025  18:51:35 +0200 (0:00:00.062)       0:00:54.024 **** 

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
Donnerstag 09 Oktober 2025  18:51:36 +0200 (0:00:00.682)       0:00:54.707 **** 

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
<span style="color:#AA5500">                &quot;Destination&quot;: &quot;/config&quot;,</span>
<span style="color:#AA5500">                &quot;Mode&quot;: &quot;rw&quot;,</span>
<span style="color:#AA5500">                &quot;Propagation&quot;: &quot;rprivate&quot;,</span>
<span style="color:#AA5500">                &quot;RW&quot;: true,</span>
<span style="color:#AA5500">                &quot;Source&quot;: &quot;/mnt/Volume1/docker/calibreweb/config&quot;,</span>
<span style="color:#AA5500">                &quot;Type&quot;: &quot;bind&quot;</span>
<span style="color:#AA5500">            },</span>
<span style="color:#AA5500">            {</span>
<span style="color:#AA5500">                &quot;Destination&quot;: &quot;/books&quot;,</span>
<span style="color:#AA5500">                &quot;Mode&quot;: &quot;rw&quot;,</span>
<span style="color:#AA5500">                &quot;Propagation&quot;: &quot;rprivate&quot;,</span>
<span style="color:#AA5500">                &quot;RW&quot;: true,</span>
<span style="color:#AA5500">                &quot;Source&quot;: &quot;/mnt/Volume1/local/Books&quot;,</span>
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
<span style="color:#AA5500">            &quot;EndpointID&quot;: &quot;35c6417c91969854442f3eb846a6b2cfa94f64a748500907dae51faeb86fb472&quot;,</span>
<span style="color:#AA5500">            &quot;Gateway&quot;: &quot;172.17.0.1&quot;,</span>
<span style="color:#AA5500">            &quot;GlobalIPv6Address&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;GlobalIPv6PrefixLen&quot;: 0,</span>
<span style="color:#AA5500">            &quot;HairpinMode&quot;: false,</span>
<span style="color:#AA5500">            &quot;IPAddress&quot;: &quot;172.17.0.8&quot;,</span>
<span style="color:#AA5500">            &quot;IPPrefixLen&quot;: 16,</span>
<span style="color:#AA5500">            &quot;IPv6Gateway&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;LinkLocalIPv6Address&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;LinkLocalIPv6PrefixLen&quot;: 0,</span>
<span style="color:#AA5500">            &quot;MacAddress&quot;: &quot;42:37:92:02:8f:31&quot;,</span>
<span style="color:#AA5500">            &quot;Networks&quot;: {</span>
<span style="color:#AA5500">                &quot;bridge&quot;: {</span>
<span style="color:#AA5500">                    &quot;Aliases&quot;: null,</span>
<span style="color:#AA5500">                    &quot;DNSNames&quot;: null,</span>
<span style="color:#AA5500">                    &quot;DriverOpts&quot;: null,</span>
<span style="color:#AA5500">                    &quot;EndpointID&quot;: &quot;35c6417c91969854442f3eb846a6b2cfa94f64a748500907dae51faeb86fb472&quot;,</span>
<span style="color:#AA5500">                    &quot;Gateway&quot;: &quot;172.17.0.1&quot;,</span>
<span style="color:#AA5500">                    &quot;GlobalIPv6Address&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">                    &quot;GlobalIPv6PrefixLen&quot;: 0,</span>
<span style="color:#AA5500">                    &quot;GwPriority&quot;: 0,</span>
<span style="color:#AA5500">                    &quot;IPAMConfig&quot;: null,</span>
<span style="color:#AA5500">                    &quot;IPAddress&quot;: &quot;172.17.0.8&quot;,</span>
<span style="color:#AA5500">                    &quot;IPPrefixLen&quot;: 16,</span>
<span style="color:#AA5500">                    &quot;IPv6Gateway&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">                    &quot;Links&quot;: null,</span>
<span style="color:#AA5500">                    &quot;MacAddress&quot;: &quot;42:37:92:02:8f:31&quot;,</span>
<span style="color:#AA5500">                    &quot;NetworkID&quot;: &quot;ec2adf010135e4885496c9e97e12dbc6ddfe52e3d312d8ae75261b7c475789e6&quot;</span>
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
<span style="color:#AA5500">            &quot;SandboxID&quot;: &quot;fe86ce0072543b9a0fa5681342f0bf79a873f5f8fc6a59601e9197f2f96597db&quot;,</span>
<span style="color:#AA5500">            &quot;SandboxKey&quot;: &quot;/var/run/docker/netns/fe86ce007254&quot;,</span>
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
<span style="color:#AA5500">            &quot;FinishedAt&quot;: &quot;0001-01-01T00:00:00Z&quot;,</span>
<span style="color:#AA5500">            &quot;OOMKilled&quot;: false,</span>
<span style="color:#AA5500">            &quot;Paused&quot;: false,</span>
<span style="color:#AA5500">            &quot;Pid&quot;: 1789980,</span>
<span style="color:#AA5500">            &quot;Restarting&quot;: false,</span>
<span style="color:#AA5500">            &quot;Running&quot;: true,</span>
<span style="color:#AA5500">            &quot;StartedAt&quot;: &quot;2025-10-09T16:52:13.015918916Z&quot;,</span>
<span style="color:#AA5500">            &quot;Status&quot;: &quot;running&quot;</span>
<span style="color:#AA5500">        }</span>
<span style="color:#AA5500">    }</span>
<span style="color:#AA5500">}</span>
Donnerstag 09 Oktober 2025  18:52:13 +0200 (0:00:36.739)       0:01:31.446 **** 
Donnerstag 09 Oktober 2025  18:52:13 +0200 (0:00:00.056)       0:01:31.502 **** 
Donnerstag 09 Oktober 2025  18:52:13 +0200 (0:00:00.048)       0:01:31.551 **** 
Donnerstag 09 Oktober 2025  18:52:13 +0200 (0:00:00.039)       0:01:31.590 **** 

TASK [cloudcmd : Stop Cloudcmd] ***********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/cloudcmd/tasks/main.yml:38</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:52:14 +0200 (0:00:00.626)       0:01:32.217 **** 
Donnerstag 09 Oktober 2025  18:52:14 +0200 (0:00:00.036)       0:01:32.253 **** 
Donnerstag 09 Oktober 2025  18:52:14 +0200 (0:00:00.050)       0:01:32.304 **** 
Donnerstag 09 Oktober 2025  18:52:14 +0200 (0:00:00.042)       0:01:32.346 **** 
Donnerstag 09 Oktober 2025  18:52:14 +0200 (0:00:00.039)       0:01:32.386 **** 

TASK [cloudflare_ddns : Stop Cloudflare DDNS] *********************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/cloudflare_ddns/tasks/main.yml:34</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:52:14 +0200 (0:00:00.592)       0:01:32.978 **** 
Donnerstag 09 Oktober 2025  18:52:14 +0200 (0:00:00.044)       0:01:33.023 **** 
Donnerstag 09 Oktober 2025  18:52:14 +0200 (0:00:00.039)       0:01:33.063 **** 

TASK [couchdb : Stop CouchDB] *************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/couchdb/tasks/main.yml:38</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:52:15 +0200 (0:00:00.639)       0:01:33.703 **** 
Donnerstag 09 Oktober 2025  18:52:15 +0200 (0:00:00.046)       0:01:33.750 **** 

TASK [code-server : Stop Code Server] *****************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/code-server/tasks/main.yml:32</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:52:16 +0200 (0:00:00.618)       0:01:34.368 **** 
Donnerstag 09 Oktober 2025  18:52:16 +0200 (0:00:00.038)       0:01:34.407 **** 
Donnerstag 09 Oktober 2025  18:52:16 +0200 (0:00:00.041)       0:01:34.448 **** 

TASK [couchpotato : Stop Couchpotato] *****************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/couchpotato/tasks/main.yml:41</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:52:16 +0200 (0:00:00.718)       0:01:35.167 **** 
Donnerstag 09 Oktober 2025  18:52:17 +0200 (0:00:00.048)       0:01:35.215 **** 
Donnerstag 09 Oktober 2025  18:52:17 +0200 (0:00:00.041)       0:01:35.256 **** 
Donnerstag 09 Oktober 2025  18:52:17 +0200 (0:00:00.038)       0:01:35.295 **** 

TASK [dashy : Stop Dashy] *****************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/dashy/tasks/main.yml:39</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:52:17 +0200 (0:00:00.611)       0:01:35.906 **** 
Donnerstag 09 Oktober 2025  18:52:17 +0200 (0:00:00.034)       0:01:35.941 **** 
Donnerstag 09 Oktober 2025  18:52:17 +0200 (0:00:00.043)       0:01:35.984 **** 
Donnerstag 09 Oktober 2025  18:52:17 +0200 (0:00:00.034)       0:01:36.019 **** 
Donnerstag 09 Oktober 2025  18:52:17 +0200 (0:00:00.042)       0:01:36.061 **** 

TASK [ddns_updater : Stop DDNS Updater] ***************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/ddns_updater/tasks/main.yml:54</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:52:18 +0200 (0:00:00.746)       0:01:36.807 **** 
Donnerstag 09 Oktober 2025  18:52:18 +0200 (0:00:00.038)       0:01:36.846 **** 
Donnerstag 09 Oktober 2025  18:52:18 +0200 (0:00:00.041)       0:01:36.888 **** 

TASK [deluge : Stop Deluge] ***************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/deluge/tasks/main.yml:46</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:52:19 +0200 (0:00:00.617)       0:01:37.505 **** 

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
Donnerstag 09 Oktober 2025  18:52:19 +0200 (0:00:00.398)       0:01:37.904 **** 

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
<span style="color:#AA5500">            &quot;Hostname&quot;: &quot;67bff9f63b20&quot;,</span>
<span style="color:#AA5500">            &quot;Image&quot;: &quot;linuxserver/dokuwiki:latest&quot;,</span>
<span style="color:#AA5500">            &quot;Labels&quot;: {</span>
<span style="color:#AA5500">                &quot;build_version&quot;: &quot;Linuxserver.io version:- 2025-05-14b-ls280 Build-date:- 2025-10-03T15:46:31+00:00&quot;,</span>
<span style="color:#AA5500">                &quot;maintainer&quot;: &quot;chbmb&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.authors&quot;: &quot;linuxserver.io&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.created&quot;: &quot;2025-10-03T15:46:31+00:00&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.description&quot;: &quot;[Dokuwiki](https://www.dokuwiki.org/dokuwiki/) is a simple to use and highly versatile Open Source wiki software that doesn&apos;t require a database. It is loved by users for its clean and readable syntax. The ease of maintenance, backup and integration makes it an administrator&apos;s favorite. Built in access controls and authentication connectors make DokuWiki especially useful in the enterprise context and the large number of plugins contributed by its vibrant community allow for a broad range of use cases beyond a traditional wiki.  &quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.documentation&quot;: &quot;https://docs.linuxserver.io/images/docker-dokuwiki&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.licenses&quot;: &quot;GPL-3.0-only&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.ref.name&quot;: &quot;5ad13fa2e5c58028bbec7b6fd61d25a236acd769&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.revision&quot;: &quot;5ad13fa2e5c58028bbec7b6fd61d25a236acd769&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.source&quot;: &quot;https://github.com/linuxserver/docker-dokuwiki&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.title&quot;: &quot;Dokuwiki&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.url&quot;: &quot;https://github.com/linuxserver/docker-dokuwiki/packages&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.vendor&quot;: &quot;linuxserver.io&quot;,</span>
<span style="color:#AA5500">                &quot;org.opencontainers.image.version&quot;: &quot;2025-05-14b-ls280&quot;,</span>
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
<span style="color:#AA5500">        &quot;Created&quot;: &quot;2025-10-09T16:52:33.194848802Z&quot;,</span>
<span style="color:#AA5500">        &quot;Driver&quot;: &quot;overlay2&quot;,</span>
<span style="color:#AA5500">        &quot;ExecIDs&quot;: null,</span>
<span style="color:#AA5500">        &quot;GraphDriver&quot;: {</span>
<span style="color:#AA5500">            &quot;Data&quot;: {</span>
<span style="color:#AA5500">                &quot;ID&quot;: &quot;67bff9f63b204272f68f5b9f3694a2e719622b40c52637b220cb0d0827ffa08e&quot;,</span>
<span style="color:#AA5500">                &quot;LowerDir&quot;: &quot;/var/lib/docker/overlay2/f76d5250b2714a469a78dd9572ecbe2679e4c28346944ebcf77d3d58a9fcc881-init/diff:/var/lib/docker/overlay2/4a2c075506c5ba94fe288dafd132594d9a0c846bb3662a72aa99b405da401f8e/diff:/var/lib/docker/overlay2/6ba4333a6a76e395f4567d6d0a5ba5c0ba5dcd8c45afb1acf6a0fdc1911a9914/diff:/var/lib/docker/overlay2/17c9527814985a16a9599efb50af89692071c31b274e790c880a0b06b77c1ae0/diff:/var/lib/docker/overlay2/52d5130bf8344bf3d1a66eb24555e42f8433faf2f501187c3cc95337a12bafb0/diff:/var/lib/docker/overlay2/32b10de10b3dd033bd315839285b4518ecb2e608688acb47137105de510790c5/diff:/var/lib/docker/overlay2/41b4593929534f90aa9ced37fdd73cfd2e519c9390c0ba81f897c6f02bf826bb/diff:/var/lib/docker/overlay2/caf9534c8358c1a3f2717f8c3dd770836cc45da0a9253d6c71b40574f85af385/diff:/var/lib/docker/overlay2/fcbe3c516762ccd9b79f7e9e8be35f3521fe12c4fb42acc0cd72443174dd6c68/diff:/var/lib/docker/overlay2/4dd7c6b255420ef624904a30d593327a3b1f58e9dabf95a9002c5e9f8c3b0b35/diff:/var/lib/docker/overlay2/d342fb36040ace412f24373923afa2d0b10844f812ce82c8cd4b596810cf0c25/diff:/var/lib/docker/overlay2/30087692b526bf2201ee82c518dcbaec86bda480c14a1e69bef7022e2f7fa42a/diff&quot;,</span>
<span style="color:#AA5500">                &quot;MergedDir&quot;: &quot;/var/lib/docker/overlay2/f76d5250b2714a469a78dd9572ecbe2679e4c28346944ebcf77d3d58a9fcc881/merged&quot;,</span>
<span style="color:#AA5500">                &quot;UpperDir&quot;: &quot;/var/lib/docker/overlay2/f76d5250b2714a469a78dd9572ecbe2679e4c28346944ebcf77d3d58a9fcc881/diff&quot;,</span>
<span style="color:#AA5500">                &quot;WorkDir&quot;: &quot;/var/lib/docker/overlay2/f76d5250b2714a469a78dd9572ecbe2679e4c28346944ebcf77d3d58a9fcc881/work&quot;</span>
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
<span style="color:#AA5500">        &quot;HostnamePath&quot;: &quot;/var/lib/docker/containers/67bff9f63b204272f68f5b9f3694a2e719622b40c52637b220cb0d0827ffa08e/hostname&quot;,</span>
<span style="color:#AA5500">        &quot;HostsPath&quot;: &quot;/var/lib/docker/containers/67bff9f63b204272f68f5b9f3694a2e719622b40c52637b220cb0d0827ffa08e/hosts&quot;,</span>
<span style="color:#AA5500">        &quot;Id&quot;: &quot;67bff9f63b204272f68f5b9f3694a2e719622b40c52637b220cb0d0827ffa08e&quot;,</span>
<span style="color:#AA5500">        &quot;Image&quot;: &quot;sha256:d774d431611cda52228b9472f465e98fa595978fdcbf931e860068ee07e7c62f&quot;,</span>
<span style="color:#AA5500">        &quot;LogPath&quot;: &quot;/var/lib/docker/containers/67bff9f63b204272f68f5b9f3694a2e719622b40c52637b220cb0d0827ffa08e/67bff9f63b204272f68f5b9f3694a2e719622b40c52637b220cb0d0827ffa08e-json.log&quot;,</span>
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
<span style="color:#AA5500">                &quot;Name&quot;: &quot;576462412c54610c69f9db42a78f6660f4230470307c8702922ad0d12bc54059&quot;,</span>
<span style="color:#AA5500">                &quot;Propagation&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">                &quot;RW&quot;: true,</span>
<span style="color:#AA5500">                &quot;Source&quot;: &quot;/var/lib/docker/volumes/576462412c54610c69f9db42a78f6660f4230470307c8702922ad0d12bc54059/_data&quot;,</span>
<span style="color:#AA5500">                &quot;Type&quot;: &quot;volume&quot;</span>
<span style="color:#AA5500">            }</span>
<span style="color:#AA5500">        ],</span>
<span style="color:#AA5500">        &quot;Name&quot;: &quot;/dokuwiki&quot;,</span>
<span style="color:#AA5500">        &quot;NetworkSettings&quot;: {</span>
<span style="color:#AA5500">            &quot;Bridge&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;EndpointID&quot;: &quot;6f68e8afa75f2807d7f7d450a46483e389674898edfce2d8c3bed5ed1ec13484&quot;,</span>
<span style="color:#AA5500">            &quot;Gateway&quot;: &quot;172.17.0.1&quot;,</span>
<span style="color:#AA5500">            &quot;GlobalIPv6Address&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;GlobalIPv6PrefixLen&quot;: 0,</span>
<span style="color:#AA5500">            &quot;HairpinMode&quot;: false,</span>
<span style="color:#AA5500">            &quot;IPAddress&quot;: &quot;172.17.0.10&quot;,</span>
<span style="color:#AA5500">            &quot;IPPrefixLen&quot;: 16,</span>
<span style="color:#AA5500">            &quot;IPv6Gateway&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;LinkLocalIPv6Address&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;LinkLocalIPv6PrefixLen&quot;: 0,</span>
<span style="color:#AA5500">            &quot;MacAddress&quot;: &quot;1a:09:a5:b7:fd:ba&quot;,</span>
<span style="color:#AA5500">            &quot;Networks&quot;: {</span>
<span style="color:#AA5500">                &quot;bridge&quot;: {</span>
<span style="color:#AA5500">                    &quot;Aliases&quot;: null,</span>
<span style="color:#AA5500">                    &quot;DNSNames&quot;: null,</span>
<span style="color:#AA5500">                    &quot;DriverOpts&quot;: null,</span>
<span style="color:#AA5500">                    &quot;EndpointID&quot;: &quot;6f68e8afa75f2807d7f7d450a46483e389674898edfce2d8c3bed5ed1ec13484&quot;,</span>
<span style="color:#AA5500">                    &quot;Gateway&quot;: &quot;172.17.0.1&quot;,</span>
<span style="color:#AA5500">                    &quot;GlobalIPv6Address&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">                    &quot;GlobalIPv6PrefixLen&quot;: 0,</span>
<span style="color:#AA5500">                    &quot;GwPriority&quot;: 0,</span>
<span style="color:#AA5500">                    &quot;IPAMConfig&quot;: null,</span>
<span style="color:#AA5500">                    &quot;IPAddress&quot;: &quot;172.17.0.10&quot;,</span>
<span style="color:#AA5500">                    &quot;IPPrefixLen&quot;: 16,</span>
<span style="color:#AA5500">                    &quot;IPv6Gateway&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">                    &quot;Links&quot;: null,</span>
<span style="color:#AA5500">                    &quot;MacAddress&quot;: &quot;1a:09:a5:b7:fd:ba&quot;,</span>
<span style="color:#AA5500">                    &quot;NetworkID&quot;: &quot;ec2adf010135e4885496c9e97e12dbc6ddfe52e3d312d8ae75261b7c475789e6&quot;</span>
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
<span style="color:#AA5500">            &quot;SandboxID&quot;: &quot;5b45d8e99d19d53faf24314d963c1425a3d1cfc99b63558f558007dd7493b843&quot;,</span>
<span style="color:#AA5500">            &quot;SandboxKey&quot;: &quot;/var/run/docker/netns/5b45d8e99d19&quot;,</span>
<span style="color:#AA5500">            &quot;SecondaryIPAddresses&quot;: null,</span>
<span style="color:#AA5500">            &quot;SecondaryIPv6Addresses&quot;: null</span>
<span style="color:#AA5500">        },</span>
<span style="color:#AA5500">        &quot;Path&quot;: &quot;/init&quot;,</span>
<span style="color:#AA5500">        &quot;Platform&quot;: &quot;linux&quot;,</span>
<span style="color:#AA5500">        &quot;ProcessLabel&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">        &quot;ResolvConfPath&quot;: &quot;/var/lib/docker/containers/67bff9f63b204272f68f5b9f3694a2e719622b40c52637b220cb0d0827ffa08e/resolv.conf&quot;,</span>
<span style="color:#AA5500">        &quot;RestartCount&quot;: 0,</span>
<span style="color:#AA5500">        &quot;State&quot;: {</span>
<span style="color:#AA5500">            &quot;Dead&quot;: false,</span>
<span style="color:#AA5500">            &quot;Error&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;ExitCode&quot;: 0,</span>
<span style="color:#AA5500">            &quot;FinishedAt&quot;: &quot;0001-01-01T00:00:00Z&quot;,</span>
<span style="color:#AA5500">            &quot;OOMKilled&quot;: false,</span>
<span style="color:#AA5500">            &quot;Paused&quot;: false,</span>
<span style="color:#AA5500">            &quot;Pid&quot;: 1790816,</span>
<span style="color:#AA5500">            &quot;Restarting&quot;: false,</span>
<span style="color:#AA5500">            &quot;Running&quot;: true,</span>
<span style="color:#AA5500">            &quot;StartedAt&quot;: &quot;2025-10-09T16:52:33.273985921Z&quot;,</span>
<span style="color:#AA5500">            &quot;Status&quot;: &quot;running&quot;</span>
<span style="color:#AA5500">        }</span>
<span style="color:#AA5500">    }</span>
<span style="color:#AA5500">}</span>
Donnerstag 09 Oktober 2025  18:52:33 +0200 (0:00:13.860)       0:01:51.765 **** 
Donnerstag 09 Oktober 2025  18:52:33 +0200 (0:00:00.058)       0:01:51.823 **** 
Donnerstag 09 Oktober 2025  18:52:33 +0200 (0:00:00.036)       0:01:51.859 **** 
Donnerstag 09 Oktober 2025  18:52:33 +0200 (0:00:00.041)       0:01:51.901 **** 
Donnerstag 09 Oktober 2025  18:52:33 +0200 (0:00:00.046)       0:01:51.948 **** 
Donnerstag 09 Oktober 2025  18:52:33 +0200 (0:00:00.039)       0:01:51.988 **** 
Donnerstag 09 Oktober 2025  18:52:33 +0200 (0:00:00.036)       0:01:52.024 **** 
Donnerstag 09 Oktober 2025  18:52:33 +0200 (0:00:00.040)       0:01:52.065 **** 

TASK [drone-ci : Stop Drone-CI] ***********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/drone-ci/tasks/main.yml:79</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:52:34 +0200 (0:00:00.638)       0:01:52.703 **** 

TASK [drone-ci : Stop Drone-CI Runner] ****************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/drone-ci/tasks/main.yml:84</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:52:35 +0200 (0:00:00.720)       0:01:53.424 **** 
Donnerstag 09 Oktober 2025  18:52:35 +0200 (0:00:00.040)       0:01:53.465 **** 
Donnerstag 09 Oktober 2025  18:52:35 +0200 (0:00:00.041)       0:01:53.506 **** 

TASK [dupeguru : Stop dupeGuru] ***********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/dupeguru/tasks/main.yml:33</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:52:36 +0200 (0:00:00.673)       0:01:54.179 **** 
Donnerstag 09 Oktober 2025  18:52:36 +0200 (0:00:00.074)       0:01:54.253 **** 
Donnerstag 09 Oktober 2025  18:52:36 +0200 (0:00:00.042)       0:01:54.296 **** 

TASK [duplicacy : Stop Duplicacy] *********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/duplicacy/tasks/main.yml:44</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:52:36 +0200 (0:00:00.667)       0:01:54.964 **** 
Donnerstag 09 Oktober 2025  18:52:36 +0200 (0:00:00.040)       0:01:55.004 **** 
Donnerstag 09 Oktober 2025  18:52:36 +0200 (0:00:00.041)       0:01:55.045 **** 

TASK [duplicati : Stop Duplicati] *********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/duplicati/tasks/main.yml:40</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:52:37 +0200 (0:00:00.781)       0:01:55.827 **** 
Donnerstag 09 Oktober 2025  18:52:37 +0200 (0:00:00.039)       0:01:55.867 **** 
Donnerstag 09 Oktober 2025  18:52:37 +0200 (0:00:00.043)       0:01:55.910 **** 

TASK [emby : Stop Emby] *******************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/emby/tasks/main.yml:41</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:52:38 +0200 (0:00:00.704)       0:01:56.615 **** 
Donnerstag 09 Oktober 2025  18:52:38 +0200 (0:00:00.083)       0:01:56.699 **** 
Donnerstag 09 Oktober 2025  18:52:38 +0200 (0:00:00.052)       0:01:56.751 **** 

TASK [esphome : Stop EspHome] *************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/esphome/tasks/main.yml:38</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:52:39 +0200 (0:00:00.672)       0:01:57.424 **** 
Donnerstag 09 Oktober 2025  18:52:39 +0200 (0:00:00.077)       0:01:57.502 **** 
Donnerstag 09 Oktober 2025  18:52:39 +0200 (0:00:00.056)       0:01:57.558 **** 
Donnerstag 09 Oktober 2025  18:52:39 +0200 (0:00:00.046)       0:01:57.605 **** 
Donnerstag 09 Oktober 2025  18:52:39 +0200 (0:00:00.046)       0:01:57.651 **** 

TASK [firefly : Stop Firefly] *************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/firefly/tasks/main.yml:68</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:52:40 +0200 (0:00:00.614)       0:01:58.265 **** 

TASK [firefly : Stop Firefly MySQL] *******************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/firefly/tasks/main.yml:73</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:52:40 +0200 (0:00:00.624)       0:01:58.890 **** 
Donnerstag 09 Oktober 2025  18:52:40 +0200 (0:00:00.052)       0:01:58.942 **** 
Donnerstag 09 Oktober 2025  18:52:40 +0200 (0:00:00.042)       0:01:58.985 **** 

TASK [flaresolverr : Stop FlareSolverr] ***************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/flaresolverr/tasks/main.yml:35</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:52:41 +0200 (0:00:00.643)       0:01:59.628 **** 

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
Donnerstag 09 Oktober 2025  18:52:42 +0200 (0:00:00.735)       0:02:00.364 **** 

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
<span style="color:#AA5500">            &quot;EndpointID&quot;: &quot;47235c92ff6f657c2619c74dd6da7c503e4d6479cb5ad4246039539bad69db1b&quot;,</span>
<span style="color:#AA5500">            &quot;Gateway&quot;: &quot;172.17.0.1&quot;,</span>
<span style="color:#AA5500">            &quot;GlobalIPv6Address&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;GlobalIPv6PrefixLen&quot;: 0,</span>
<span style="color:#AA5500">            &quot;HairpinMode&quot;: false,</span>
<span style="color:#AA5500">            &quot;IPAddress&quot;: &quot;172.17.0.6&quot;,</span>
<span style="color:#AA5500">            &quot;IPPrefixLen&quot;: 16,</span>
<span style="color:#AA5500">            &quot;IPv6Gateway&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;LinkLocalIPv6Address&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;LinkLocalIPv6PrefixLen&quot;: 0,</span>
<span style="color:#AA5500">            &quot;MacAddress&quot;: &quot;fa:48:e3:fb:11:f3&quot;,</span>
<span style="color:#AA5500">            &quot;Networks&quot;: {</span>
<span style="color:#AA5500">                &quot;bridge&quot;: {</span>
<span style="color:#AA5500">                    &quot;Aliases&quot;: null,</span>
<span style="color:#AA5500">                    &quot;DNSNames&quot;: null,</span>
<span style="color:#AA5500">                    &quot;DriverOpts&quot;: null,</span>
<span style="color:#AA5500">                    &quot;EndpointID&quot;: &quot;47235c92ff6f657c2619c74dd6da7c503e4d6479cb5ad4246039539bad69db1b&quot;,</span>
<span style="color:#AA5500">                    &quot;Gateway&quot;: &quot;172.17.0.1&quot;,</span>
<span style="color:#AA5500">                    &quot;GlobalIPv6Address&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">                    &quot;GlobalIPv6PrefixLen&quot;: 0,</span>
<span style="color:#AA5500">                    &quot;GwPriority&quot;: 0,</span>
<span style="color:#AA5500">                    &quot;IPAMConfig&quot;: null,</span>
<span style="color:#AA5500">                    &quot;IPAddress&quot;: &quot;172.17.0.6&quot;,</span>
<span style="color:#AA5500">                    &quot;IPPrefixLen&quot;: 16,</span>
<span style="color:#AA5500">                    &quot;IPv6Gateway&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">                    &quot;Links&quot;: null,</span>
<span style="color:#AA5500">                    &quot;MacAddress&quot;: &quot;fa:48:e3:fb:11:f3&quot;,</span>
<span style="color:#AA5500">                    &quot;NetworkID&quot;: &quot;ec2adf010135e4885496c9e97e12dbc6ddfe52e3d312d8ae75261b7c475789e6&quot;</span>
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
<span style="color:#AA5500">            &quot;SandboxID&quot;: &quot;f1e3117a5355407b46a1c9217f0b1d26564c0049e4f5d5bbb69869bc840813e5&quot;,</span>
<span style="color:#AA5500">            &quot;SandboxKey&quot;: &quot;/var/run/docker/netns/f1e3117a5355&quot;,</span>
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
<span style="color:#AA5500">            &quot;FinishedAt&quot;: &quot;2025-10-05T12:53:05.287323517Z&quot;,</span>
<span style="color:#AA5500">            &quot;OOMKilled&quot;: false,</span>
<span style="color:#AA5500">            &quot;Paused&quot;: false,</span>
<span style="color:#AA5500">            &quot;Pid&quot;: 2670,</span>
<span style="color:#AA5500">            &quot;Restarting&quot;: false,</span>
<span style="color:#AA5500">            &quot;Running&quot;: true,</span>
<span style="color:#AA5500">            &quot;StartedAt&quot;: &quot;2025-10-05T12:54:07.678255176Z&quot;,</span>
<span style="color:#AA5500">            &quot;Status&quot;: &quot;running&quot;</span>
<span style="color:#AA5500">        }</span>
<span style="color:#AA5500">    }</span>
<span style="color:#AA5500">}</span>
Donnerstag 09 Oktober 2025  18:52:44 +0200 (0:00:01.827)       0:02:02.191 **** 
Donnerstag 09 Oktober 2025  18:52:44 +0200 (0:00:00.052)       0:02:02.243 **** 
Donnerstag 09 Oktober 2025  18:52:44 +0200 (0:00:00.057)       0:02:02.301 **** 
Donnerstag 09 Oktober 2025  18:52:44 +0200 (0:00:00.036)       0:02:02.337 **** 

TASK [get_iplayer : Stop get_iplayer] *****************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/get_iplayer/tasks/main.yml:28</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:52:44 +0200 (0:00:00.646)       0:02:02.984 **** 
Donnerstag 09 Oktober 2025  18:52:44 +0200 (0:00:00.046)       0:02:03.030 **** 
Donnerstag 09 Oktober 2025  18:52:44 +0200 (0:00:00.040)       0:02:03.071 **** 
Donnerstag 09 Oktober 2025  18:52:44 +0200 (0:00:00.036)       0:02:03.107 **** 

TASK [gitea : Stop Gitea] *****************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/gitea/tasks/main.yml:65</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:52:45 +0200 (0:00:00.631)       0:02:03.739 **** 

TASK [gitea : Stop Gitea Mysql] ***********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/gitea/tasks/main.yml:70</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:52:46 +0200 (0:00:00.657)       0:02:04.396 **** 
Donnerstag 09 Oktober 2025  18:52:46 +0200 (0:00:00.036)       0:02:04.432 **** 
Donnerstag 09 Oktober 2025  18:52:46 +0200 (0:00:00.043)       0:02:04.475 **** 
Donnerstag 09 Oktober 2025  18:52:46 +0200 (0:00:00.047)       0:02:04.523 **** 
Donnerstag 09 Oktober 2025  18:52:46 +0200 (0:00:00.045)       0:02:04.569 **** 

TASK [gitlab : Stop Gitlab] ***************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/gitlab/tasks/main.yml:64</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:52:47 +0200 (0:00:01.132)       0:02:05.701 **** 
Donnerstag 09 Oktober 2025  18:52:47 +0200 (0:00:00.036)       0:02:05.737 **** 

TASK [glances : Stop Glances] *************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/glances/tasks/main.yml:32</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:52:48 +0200 (0:00:00.721)       0:02:06.459 **** 
Donnerstag 09 Oktober 2025  18:52:48 +0200 (0:00:00.049)       0:02:06.508 **** 
Donnerstag 09 Oktober 2025  18:52:48 +0200 (0:00:00.043)       0:02:06.552 **** 

TASK [gotify : Stop Gotify] ***************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/gotify/tasks/main.yml:38</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:52:49 +0200 (0:00:00.635)       0:02:07.187 **** 
Donnerstag 09 Oktober 2025  18:52:49 +0200 (0:00:00.038)       0:02:07.226 **** 
Donnerstag 09 Oktober 2025  18:52:49 +0200 (0:00:00.047)       0:02:07.274 **** 
Donnerstag 09 Oktober 2025  18:52:49 +0200 (0:00:00.044)       0:02:07.319 **** 
Donnerstag 09 Oktober 2025  18:52:49 +0200 (0:00:00.050)       0:02:07.369 **** 
Donnerstag 09 Oktober 2025  18:52:49 +0200 (0:00:00.040)       0:02:07.410 **** 
Donnerstag 09 Oktober 2025  18:52:49 +0200 (0:00:00.037)       0:02:07.447 **** 

TASK [guacamole : Stop Guacamole] *********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/guacamole/tasks/main.yml:59</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:52:49 +0200 (0:00:00.634)       0:02:08.082 **** 
Donnerstag 09 Oktober 2025  18:52:49 +0200 (0:00:00.035)       0:02:08.117 **** 

TASK [healthchecks.io : Remove healthchecks.io cronjob] ***********************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/healthchecks.io/tasks/main.yml:14</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;envs&quot;: [],</span>
<span style="color:#00AA00">    &quot;jobs&quot;: []</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:52:50 +0200 (0:00:00.509)       0:02:08.627 **** 
Donnerstag 09 Oktober 2025  18:52:50 +0200 (0:00:00.041)       0:02:08.668 **** 
Donnerstag 09 Oktober 2025  18:52:50 +0200 (0:00:00.040)       0:02:08.709 **** 

TASK [heimdall : Stop Heimdall] ***********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/heimdall/tasks/main.yml:36</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:52:51 +0200 (0:00:00.670)       0:02:09.379 **** 
Donnerstag 09 Oktober 2025  18:52:51 +0200 (0:00:00.041)       0:02:09.421 **** 
Donnerstag 09 Oktober 2025  18:52:51 +0200 (0:00:00.044)       0:02:09.466 **** 

TASK [hello_world : Stop Hello World] *****************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/hello_world/tasks/main.yml:33</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:52:51 +0200 (0:00:00.595)       0:02:10.061 **** 

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
Donnerstag 09 Oktober 2025  18:52:52 +0200 (0:00:00.353)       0:02:10.415 **** 

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
<span style="color:#AA5500">                    &quot;EndpointID&quot;: &quot;73af867c654951316db2033c57283c539d5b0844d99d3230f660ba49e103496c&quot;,</span>
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
<span style="color:#AA5500">            &quot;SandboxID&quot;: &quot;ad800f0a1808a87bfe6f0995632a5180515d963b7848979c59c77a5729031a2a&quot;,</span>
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
<span style="color:#AA5500">            &quot;FinishedAt&quot;: &quot;2025-10-05T12:53:15.592537328Z&quot;,</span>
<span style="color:#AA5500">            &quot;OOMKilled&quot;: false,</span>
<span style="color:#AA5500">            &quot;Paused&quot;: false,</span>
<span style="color:#AA5500">            &quot;Pid&quot;: 2699,</span>
<span style="color:#AA5500">            &quot;Restarting&quot;: false,</span>
<span style="color:#AA5500">            &quot;Running&quot;: true,</span>
<span style="color:#AA5500">            &quot;StartedAt&quot;: &quot;2025-10-05T12:54:07.734918213Z&quot;,</span>
<span style="color:#AA5500">            &quot;Status&quot;: &quot;running&quot;</span>
<span style="color:#AA5500">        }</span>
<span style="color:#AA5500">    }</span>
<span style="color:#AA5500">}</span>
Donnerstag 09 Oktober 2025  18:52:53 +0200 (0:00:01.739)       0:02:12.154 **** 
Donnerstag 09 Oktober 2025  18:52:54 +0200 (0:00:00.066)       0:02:12.221 **** 
Donnerstag 09 Oktober 2025  18:52:54 +0200 (0:00:00.063)       0:02:12.284 **** 
Donnerstag 09 Oktober 2025  18:52:54 +0200 (0:00:00.054)       0:02:12.339 **** 

TASK [homebridge : Stop Homebridge] *******************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/homebridge/tasks/main.yml:39</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:52:54 +0200 (0:00:00.598)       0:02:12.937 **** 

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
Donnerstag 09 Oktober 2025  18:52:55 +0200 (0:00:00.366)       0:02:13.304 **** 

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
<span style="color:#AA5500">    &quot;src&quot;: &quot;/home/dietmar/.ansible/tmp/ansible-tmp-1760028775.181908-194096-155478757161688/.source.yaml&quot;,</span>
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
<span style="color:#AA5500">    &quot;src&quot;: &quot;/home/dietmar/.ansible/tmp/ansible-tmp-1760028775.9920425-194096-2512214481947/.source.yaml&quot;,</span>
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
<span style="color:#AA5500">    &quot;src&quot;: &quot;/home/dietmar/.ansible/tmp/ansible-tmp-1760028776.5739143-194096-39241394453498/.source.yaml&quot;,</span>
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
<span style="color:#AA5500">    &quot;src&quot;: &quot;/home/dietmar/.ansible/tmp/ansible-tmp-1760028777.1876156-194096-183914195171968/.source.yaml&quot;,</span>
<span style="color:#AA5500">    &quot;state&quot;: &quot;file&quot;,</span>
<span style="color:#AA5500">    &quot;uid&quot;: 0</span>
<span style="color:#AA5500">}</span>
<span style="color:#AA5500">changed: [ansible-nas] =&gt; (item=widgets.yaml) =&gt; {</span>
<span style="color:#AA5500">    &quot;ansible_loop_var&quot;: &quot;item&quot;,</span>
<span style="color:#AA5500">    &quot;changed&quot;: true,</span>
<span style="color:#AA5500">    &quot;checksum&quot;: &quot;7c716bdbcc8065135fbe8f1a314a3dae569cedb2&quot;,</span>
<span style="color:#AA5500">    &quot;dest&quot;: &quot;/mnt/Volume1/docker/homepage/widgets.yaml&quot;,</span>
<span style="color:#AA5500">    &quot;gid&quot;: 0,</span>
<span style="color:#AA5500">    &quot;group&quot;: &quot;root&quot;,</span>
<span style="color:#AA5500">    &quot;item&quot;: &quot;widgets.yaml&quot;,</span>
<span style="color:#AA5500">    &quot;md5sum&quot;: &quot;398254b32a7cb1d1b2e4fa7be28ab613&quot;,</span>
<span style="color:#AA5500">    &quot;mode&quot;: &quot;0777&quot;,</span>
<span style="color:#AA5500">    &quot;owner&quot;: &quot;root&quot;,</span>
<span style="color:#AA5500">    &quot;size&quot;: 288,</span>
<span style="color:#AA5500">    &quot;src&quot;: &quot;/home/dietmar/.ansible/tmp/ansible-tmp-1760028777.7711186-194096-160097149271838/.source.yaml&quot;,</span>
<span style="color:#AA5500">    &quot;state&quot;: &quot;file&quot;,</span>
<span style="color:#AA5500">    &quot;uid&quot;: 0</span>
<span style="color:#AA5500">}</span>
Donnerstag 09 Oktober 2025  18:52:58 +0200 (0:00:03.253)       0:02:16.557 **** 

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
<span style="color:#AA5500">            &quot;Hostname&quot;: &quot;d16b59410874&quot;,</span>
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
<span style="color:#AA5500">        &quot;Created&quot;: &quot;2025-10-09T16:53:00.727859087Z&quot;,</span>
<span style="color:#AA5500">        &quot;Driver&quot;: &quot;overlay2&quot;,</span>
<span style="color:#AA5500">        &quot;ExecIDs&quot;: null,</span>
<span style="color:#AA5500">        &quot;GraphDriver&quot;: {</span>
<span style="color:#AA5500">            &quot;Data&quot;: {</span>
<span style="color:#AA5500">                &quot;ID&quot;: &quot;d16b594108749fd2fac6f3d6925bc1bdb7ba5fd10b07992b2eb331284928e171&quot;,</span>
<span style="color:#AA5500">                &quot;LowerDir&quot;: &quot;/var/lib/docker/overlay2/a3ee36fe3cc745e8be2d0a091b5af6342c5684266a6f6b734e81f8af2119d9bc-init/diff:/var/lib/docker/overlay2/23a9385149d0f49800ed7f1d18a7975e3e6c6cc0ddeb75551e30acbb3fe8acab/diff:/var/lib/docker/overlay2/48247c240df240adc75d0560240e5bdcea1e5b0e3421511997fbd49098c4f177/diff:/var/lib/docker/overlay2/1757a842b2db6b66f4e139af38e2a438f72effe4b9b13ef6d21e4b161e76484e/diff:/var/lib/docker/overlay2/7fbced54ce4f73d785820c4ec8bee72324553f5df29851e8e682f6a81bdacada/diff:/var/lib/docker/overlay2/a37637f159082e890f586ca87fe6b86cc7f704bb28bd9a148a16d5be78fcf3c9/diff:/var/lib/docker/overlay2/cc19d88f3f5740d1286616e33561d4bcf45479331a0103ef4bf291c2abcfee00/diff:/var/lib/docker/overlay2/3fbd10128c4266d5886821096047ca645ff55c0a76dd99e2115e24756abe8889/diff:/var/lib/docker/overlay2/d035f3715f0b05e119f1cc508d4178bc870691590ad5897c298e685f64e7e4f6/diff:/var/lib/docker/overlay2/f40b5fef4490f7de32848a38a5c19a15f50fc99f0016f98f4214304c8496b150/diff:/var/lib/docker/overlay2/502c7107094a5bb68299bb6f3d8d9b644daf0a27a5836740ac357984351c9297/diff&quot;,</span>
<span style="color:#AA5500">                &quot;MergedDir&quot;: &quot;/var/lib/docker/overlay2/a3ee36fe3cc745e8be2d0a091b5af6342c5684266a6f6b734e81f8af2119d9bc/merged&quot;,</span>
<span style="color:#AA5500">                &quot;UpperDir&quot;: &quot;/var/lib/docker/overlay2/a3ee36fe3cc745e8be2d0a091b5af6342c5684266a6f6b734e81f8af2119d9bc/diff&quot;,</span>
<span style="color:#AA5500">                &quot;WorkDir&quot;: &quot;/var/lib/docker/overlay2/a3ee36fe3cc745e8be2d0a091b5af6342c5684266a6f6b734e81f8af2119d9bc/work&quot;</span>
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
<span style="color:#AA5500">        &quot;HostnamePath&quot;: &quot;/var/lib/docker/containers/d16b594108749fd2fac6f3d6925bc1bdb7ba5fd10b07992b2eb331284928e171/hostname&quot;,</span>
<span style="color:#AA5500">        &quot;HostsPath&quot;: &quot;/var/lib/docker/containers/d16b594108749fd2fac6f3d6925bc1bdb7ba5fd10b07992b2eb331284928e171/hosts&quot;,</span>
<span style="color:#AA5500">        &quot;Id&quot;: &quot;d16b594108749fd2fac6f3d6925bc1bdb7ba5fd10b07992b2eb331284928e171&quot;,</span>
<span style="color:#AA5500">        &quot;Image&quot;: &quot;sha256:2833b1df3f84c40c0f35b25d7e7fac123d5d1f89883515e431c10149d7d7c6dd&quot;,</span>
<span style="color:#AA5500">        &quot;LogPath&quot;: &quot;/var/lib/docker/containers/d16b594108749fd2fac6f3d6925bc1bdb7ba5fd10b07992b2eb331284928e171/d16b594108749fd2fac6f3d6925bc1bdb7ba5fd10b07992b2eb331284928e171-json.log&quot;,</span>
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
<span style="color:#AA5500">            &quot;EndpointID&quot;: &quot;68dca3904c6d478daddc235617f678ec2e46b150afd3b09ac15af6a0a34de2df&quot;,</span>
<span style="color:#AA5500">            &quot;Gateway&quot;: &quot;172.17.0.1&quot;,</span>
<span style="color:#AA5500">            &quot;GlobalIPv6Address&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;GlobalIPv6PrefixLen&quot;: 0,</span>
<span style="color:#AA5500">            &quot;HairpinMode&quot;: false,</span>
<span style="color:#AA5500">            &quot;IPAddress&quot;: &quot;172.17.0.7&quot;,</span>
<span style="color:#AA5500">            &quot;IPPrefixLen&quot;: 16,</span>
<span style="color:#AA5500">            &quot;IPv6Gateway&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;LinkLocalIPv6Address&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;LinkLocalIPv6PrefixLen&quot;: 0,</span>
<span style="color:#AA5500">            &quot;MacAddress&quot;: &quot;0e:fd:e9:bd:fc:d8&quot;,</span>
<span style="color:#AA5500">            &quot;Networks&quot;: {</span>
<span style="color:#AA5500">                &quot;bridge&quot;: {</span>
<span style="color:#AA5500">                    &quot;Aliases&quot;: null,</span>
<span style="color:#AA5500">                    &quot;DNSNames&quot;: null,</span>
<span style="color:#AA5500">                    &quot;DriverOpts&quot;: null,</span>
<span style="color:#AA5500">                    &quot;EndpointID&quot;: &quot;68dca3904c6d478daddc235617f678ec2e46b150afd3b09ac15af6a0a34de2df&quot;,</span>
<span style="color:#AA5500">                    &quot;Gateway&quot;: &quot;172.17.0.1&quot;,</span>
<span style="color:#AA5500">                    &quot;GlobalIPv6Address&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">                    &quot;GlobalIPv6PrefixLen&quot;: 0,</span>
<span style="color:#AA5500">                    &quot;GwPriority&quot;: 0,</span>
<span style="color:#AA5500">                    &quot;IPAMConfig&quot;: null,</span>
<span style="color:#AA5500">                    &quot;IPAddress&quot;: &quot;172.17.0.7&quot;,</span>
<span style="color:#AA5500">                    &quot;IPPrefixLen&quot;: 16,</span>
<span style="color:#AA5500">                    &quot;IPv6Gateway&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">                    &quot;Links&quot;: null,</span>
<span style="color:#AA5500">                    &quot;MacAddress&quot;: &quot;0e:fd:e9:bd:fc:d8&quot;,</span>
<span style="color:#AA5500">                    &quot;NetworkID&quot;: &quot;ec2adf010135e4885496c9e97e12dbc6ddfe52e3d312d8ae75261b7c475789e6&quot;</span>
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
<span style="color:#AA5500">            &quot;SandboxID&quot;: &quot;752f53e608f4136143ee37ddb668a79adcc16abc8db56d887121a688f6da54e6&quot;,</span>
<span style="color:#AA5500">            &quot;SandboxKey&quot;: &quot;/var/run/docker/netns/752f53e608f4&quot;,</span>
<span style="color:#AA5500">            &quot;SecondaryIPAddresses&quot;: null,</span>
<span style="color:#AA5500">            &quot;SecondaryIPv6Addresses&quot;: null</span>
<span style="color:#AA5500">        },</span>
<span style="color:#AA5500">        &quot;Path&quot;: &quot;docker-entrypoint.sh&quot;,</span>
<span style="color:#AA5500">        &quot;Platform&quot;: &quot;linux&quot;,</span>
<span style="color:#AA5500">        &quot;ProcessLabel&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">        &quot;ResolvConfPath&quot;: &quot;/var/lib/docker/containers/d16b594108749fd2fac6f3d6925bc1bdb7ba5fd10b07992b2eb331284928e171/resolv.conf&quot;,</span>
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
<span style="color:#AA5500">            &quot;Pid&quot;: 1793023,</span>
<span style="color:#AA5500">            &quot;Restarting&quot;: false,</span>
<span style="color:#AA5500">            &quot;Running&quot;: true,</span>
<span style="color:#AA5500">            &quot;StartedAt&quot;: &quot;2025-10-09T16:53:00.801446251Z&quot;,</span>
<span style="color:#AA5500">            &quot;Status&quot;: &quot;running&quot;</span>
<span style="color:#AA5500">        }</span>
<span style="color:#AA5500">    }</span>
<span style="color:#AA5500">}</span>
Donnerstag 09 Oktober 2025  18:53:01 +0200 (0:00:02.688)       0:02:19.246 **** 
Donnerstag 09 Oktober 2025  18:53:01 +0200 (0:00:00.056)       0:02:19.303 **** 
Donnerstag 09 Oktober 2025  18:53:01 +0200 (0:00:00.047)       0:02:19.351 **** 
Donnerstag 09 Oktober 2025  18:53:01 +0200 (0:00:00.046)       0:02:19.398 **** 

TASK [ispyagentdvr : Stop iSpyAgentDVR] ***************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/ispyagentdvr/tasks/main.yml:50</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:53:01 +0200 (0:00:00.674)       0:02:20.073 **** 
Donnerstag 09 Oktober 2025  18:53:01 +0200 (0:00:00.039)       0:02:20.112 **** 
Donnerstag 09 Oktober 2025  18:53:01 +0200 (0:00:00.041)       0:02:20.154 **** 

TASK [jackett : Stop Jackett] *************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/jackett/tasks/main.yml:41</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:53:02 +0200 (0:00:00.707)       0:02:20.862 **** 

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
Donnerstag 09 Oktober 2025  18:53:03 +0200 (0:00:00.420)       0:02:21.282 **** 

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
<span style="color:#AA5500">            &quot;EndpointID&quot;: &quot;f924349158a6780b7628c0df2804a79d790068839ef23f625c71874c323ab225&quot;,</span>
<span style="color:#AA5500">            &quot;Gateway&quot;: &quot;172.17.0.1&quot;,</span>
<span style="color:#AA5500">            &quot;GlobalIPv6Address&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;GlobalIPv6PrefixLen&quot;: 0,</span>
<span style="color:#AA5500">            &quot;HairpinMode&quot;: false,</span>
<span style="color:#AA5500">            &quot;IPAddress&quot;: &quot;172.17.0.4&quot;,</span>
<span style="color:#AA5500">            &quot;IPPrefixLen&quot;: 16,</span>
<span style="color:#AA5500">            &quot;IPv6Gateway&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;LinkLocalIPv6Address&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;LinkLocalIPv6PrefixLen&quot;: 0,</span>
<span style="color:#AA5500">            &quot;MacAddress&quot;: &quot;a6:15:45:97:92:f8&quot;,</span>
<span style="color:#AA5500">            &quot;Networks&quot;: {</span>
<span style="color:#AA5500">                &quot;bridge&quot;: {</span>
<span style="color:#AA5500">                    &quot;Aliases&quot;: null,</span>
<span style="color:#AA5500">                    &quot;DNSNames&quot;: null,</span>
<span style="color:#AA5500">                    &quot;DriverOpts&quot;: null,</span>
<span style="color:#AA5500">                    &quot;EndpointID&quot;: &quot;f924349158a6780b7628c0df2804a79d790068839ef23f625c71874c323ab225&quot;,</span>
<span style="color:#AA5500">                    &quot;Gateway&quot;: &quot;172.17.0.1&quot;,</span>
<span style="color:#AA5500">                    &quot;GlobalIPv6Address&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">                    &quot;GlobalIPv6PrefixLen&quot;: 0,</span>
<span style="color:#AA5500">                    &quot;GwPriority&quot;: 0,</span>
<span style="color:#AA5500">                    &quot;IPAMConfig&quot;: null,</span>
<span style="color:#AA5500">                    &quot;IPAddress&quot;: &quot;172.17.0.4&quot;,</span>
<span style="color:#AA5500">                    &quot;IPPrefixLen&quot;: 16,</span>
<span style="color:#AA5500">                    &quot;IPv6Gateway&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">                    &quot;Links&quot;: null,</span>
<span style="color:#AA5500">                    &quot;MacAddress&quot;: &quot;a6:15:45:97:92:f8&quot;,</span>
<span style="color:#AA5500">                    &quot;NetworkID&quot;: &quot;ec2adf010135e4885496c9e97e12dbc6ddfe52e3d312d8ae75261b7c475789e6&quot;</span>
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
<span style="color:#AA5500">            &quot;SandboxID&quot;: &quot;2e2f00f84e97c6b6f28df447171989b90ac414d3dbbbd406f28089d2931de004&quot;,</span>
<span style="color:#AA5500">            &quot;SandboxKey&quot;: &quot;/var/run/docker/netns/2e2f00f84e97&quot;,</span>
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
<span style="color:#AA5500">            &quot;FinishedAt&quot;: &quot;2025-10-05T12:53:06.331229149Z&quot;,</span>
<span style="color:#AA5500">            &quot;OOMKilled&quot;: false,</span>
<span style="color:#AA5500">            &quot;Paused&quot;: false,</span>
<span style="color:#AA5500">            &quot;Pid&quot;: 2650,</span>
<span style="color:#AA5500">            &quot;Restarting&quot;: false,</span>
<span style="color:#AA5500">            &quot;Running&quot;: true,</span>
<span style="color:#AA5500">            &quot;StartedAt&quot;: &quot;2025-10-05T12:54:07.701242361Z&quot;,</span>
<span style="color:#AA5500">            &quot;Status&quot;: &quot;running&quot;</span>
<span style="color:#AA5500">        }</span>
<span style="color:#AA5500">    }</span>
<span style="color:#AA5500">}</span>
Donnerstag 09 Oktober 2025  18:53:03 +0200 (0:00:00.702)       0:02:21.984 **** 
Donnerstag 09 Oktober 2025  18:53:03 +0200 (0:00:00.050)       0:02:22.035 **** 
Donnerstag 09 Oktober 2025  18:53:03 +0200 (0:00:00.046)       0:02:22.082 **** 
Donnerstag 09 Oktober 2025  18:53:03 +0200 (0:00:00.040)       0:02:22.123 **** 

TASK [jellyfin : Stop jellyfin] ***********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/jellyfin/tasks/main.yml:52</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:53:04 +0200 (0:00:00.600)       0:02:22.723 **** 
Donnerstag 09 Oktober 2025  18:53:04 +0200 (0:00:00.061)       0:02:22.785 **** 
Donnerstag 09 Oktober 2025  18:53:04 +0200 (0:00:00.036)       0:02:22.821 **** 
Donnerstag 09 Oktober 2025  18:53:04 +0200 (0:00:00.046)       0:02:22.868 **** 
Donnerstag 09 Oktober 2025  18:53:04 +0200 (0:00:00.102)       0:02:22.971 **** 

TASK [joomla : Stop Joomla] ***************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/joomla/tasks/main.yml:62</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:53:05 +0200 (0:00:00.569)       0:02:23.541 **** 

TASK [joomla : Stop Joomla DB] ************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/joomla/tasks/main.yml:66</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:53:05 +0200 (0:00:00.585)       0:02:24.126 **** 
Donnerstag 09 Oktober 2025  18:53:05 +0200 (0:00:00.044)       0:02:24.170 **** 
Donnerstag 09 Oktober 2025  18:53:06 +0200 (0:00:00.051)       0:02:24.222 **** 

TASK [komga : Stop Komga] *****************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/komga/tasks/main.yml:42</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:53:06 +0200 (0:00:00.595)       0:02:24.817 **** 
Donnerstag 09 Oktober 2025  18:53:06 +0200 (0:00:00.039)       0:02:24.856 **** 
Donnerstag 09 Oktober 2025  18:53:06 +0200 (0:00:00.043)       0:02:24.900 **** 

TASK [krusader : Stop Krusader] ***********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/krusader/tasks/main.yml:43</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:53:07 +0200 (0:00:00.589)       0:02:25.489 **** 
Donnerstag 09 Oktober 2025  18:53:07 +0200 (0:00:00.039)       0:02:25.529 **** 
Donnerstag 09 Oktober 2025  18:53:07 +0200 (0:00:00.038)       0:02:25.568 **** 

TASK [lidarr : Stop Lidarr] ***************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/lidarr/tasks/main.yml:37</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:53:07 +0200 (0:00:00.601)       0:02:26.169 **** 
Donnerstag 09 Oktober 2025  18:53:08 +0200 (0:00:00.037)       0:02:26.206 **** 
Donnerstag 09 Oktober 2025  18:53:08 +0200 (0:00:00.054)       0:02:26.261 **** 
Donnerstag 09 Oktober 2025  18:53:08 +0200 (0:00:00.039)       0:02:26.300 **** 
Donnerstag 09 Oktober 2025  18:53:08 +0200 (0:00:00.054)       0:02:26.355 **** 
Donnerstag 09 Oktober 2025  18:53:08 +0200 (0:00:00.050)       0:02:26.405 **** 
Donnerstag 09 Oktober 2025  18:53:08 +0200 (0:00:00.035)       0:02:26.440 **** 
Donnerstag 09 Oktober 2025  18:53:08 +0200 (0:00:00.045)       0:02:26.486 **** 
Donnerstag 09 Oktober 2025  18:53:08 +0200 (0:00:00.045)       0:02:26.531 **** 

TASK [loki : Stop loki] *******************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/loki/tasks/main.yml:74</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:53:08 +0200 (0:00:00.610)       0:02:27.141 **** 
Donnerstag 09 Oktober 2025  18:53:09 +0200 (0:00:00.040)       0:02:27.182 **** 
Donnerstag 09 Oktober 2025  18:53:09 +0200 (0:00:00.053)       0:02:27.236 **** 

TASK [mealie : Stop Mealie] ***************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/mealie/tasks/main.yml:44</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:53:09 +0200 (0:00:00.641)       0:02:27.877 **** 
Donnerstag 09 Oktober 2025  18:53:09 +0200 (0:00:00.053)       0:02:27.930 **** 
Donnerstag 09 Oktober 2025  18:53:09 +0200 (0:00:00.037)       0:02:27.968 **** 

TASK [mediathekview : Stop Mediathekview] *************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/mediathekview/tasks/main.yml:41</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:53:10 +0200 (0:00:00.586)       0:02:28.555 **** 
Donnerstag 09 Oktober 2025  18:53:10 +0200 (0:00:00.052)       0:02:28.607 **** 
Donnerstag 09 Oktober 2025  18:53:10 +0200 (0:00:00.042)       0:02:28.649 **** 

TASK [minecraft-bedrock-server : Stop Minecraft Bedrock Server] ***************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/minecraft-bedrock-server/tasks/main.yml:34</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:53:11 +0200 (0:00:00.589)       0:02:29.239 **** 
Donnerstag 09 Oktober 2025  18:53:11 +0200 (0:00:00.039)       0:02:29.278 **** 
Donnerstag 09 Oktober 2025  18:53:11 +0200 (0:00:00.056)       0:02:29.334 **** 

TASK [minecraft-server : Stop Minecraft Server] *******************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/minecraft-server/tasks/main.yml:27</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:53:11 +0200 (0:00:00.621)       0:02:29.956 **** 
Donnerstag 09 Oktober 2025  18:53:11 +0200 (0:00:00.034)       0:02:29.991 **** 

TASK [minidlna : Stop MiniDLNA] ***********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/minidlna/tasks/main.yml:24</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:53:12 +0200 (0:00:00.594)       0:02:30.585 **** 
Donnerstag 09 Oktober 2025  18:53:12 +0200 (0:00:00.042)       0:02:30.627 **** 
Donnerstag 09 Oktober 2025  18:53:12 +0200 (0:00:00.040)       0:02:30.668 **** 
Donnerstag 09 Oktober 2025  18:53:12 +0200 (0:00:00.039)       0:02:30.707 **** 
Donnerstag 09 Oktober 2025  18:53:12 +0200 (0:00:00.037)       0:02:30.745 **** 

TASK [miniflux : Stop Miniflux] ***********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/miniflux/tasks/main.yml:60</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:53:13 +0200 (0:00:00.625)       0:02:31.371 **** 
Donnerstag 09 Oktober 2025  18:53:13 +0200 (0:00:00.041)       0:02:31.412 **** 
Donnerstag 09 Oktober 2025  18:53:13 +0200 (0:00:00.046)       0:02:31.458 **** 

TASK [minio : Stop minio] *****************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/minio/tasks/main.yml:40</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:53:13 +0200 (0:00:00.570)       0:02:32.029 **** 

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
Donnerstag 09 Oktober 2025  18:53:14 +0200 (0:00:01.002)       0:02:33.032 **** 

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
Donnerstag 09 Oktober 2025  18:53:15 +0200 (0:00:00.633)       0:02:33.665 **** 

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
<span style="color:#AA5500">                &quot;Destination&quot;: &quot;/mosquitto/config/mosquitto.conf&quot;,</span>
<span style="color:#AA5500">                &quot;Mode&quot;: &quot;rw&quot;,</span>
<span style="color:#AA5500">                &quot;Propagation&quot;: &quot;rprivate&quot;,</span>
<span style="color:#AA5500">                &quot;RW&quot;: true,</span>
<span style="color:#AA5500">                &quot;Source&quot;: &quot;/mnt/Volume1/docker/mosquitto/config/mosquitto.conf&quot;,</span>
<span style="color:#AA5500">                &quot;Type&quot;: &quot;bind&quot;</span>
<span style="color:#AA5500">            },</span>
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
<span style="color:#AA5500">            }</span>
<span style="color:#AA5500">        ],</span>
<span style="color:#AA5500">        &quot;Name&quot;: &quot;/mosquitto&quot;,</span>
<span style="color:#AA5500">        &quot;NetworkSettings&quot;: {</span>
<span style="color:#AA5500">            &quot;Bridge&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;EndpointID&quot;: &quot;c46f72cd8a0ae6182051e01687f9d5b1d0ae8d7d718d4193aa772edba53fc0f0&quot;,</span>
<span style="color:#AA5500">            &quot;Gateway&quot;: &quot;172.17.0.1&quot;,</span>
<span style="color:#AA5500">            &quot;GlobalIPv6Address&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;GlobalIPv6PrefixLen&quot;: 0,</span>
<span style="color:#AA5500">            &quot;HairpinMode&quot;: false,</span>
<span style="color:#AA5500">            &quot;IPAddress&quot;: &quot;172.17.0.5&quot;,</span>
<span style="color:#AA5500">            &quot;IPPrefixLen&quot;: 16,</span>
<span style="color:#AA5500">            &quot;IPv6Gateway&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;LinkLocalIPv6Address&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;LinkLocalIPv6PrefixLen&quot;: 0,</span>
<span style="color:#AA5500">            &quot;MacAddress&quot;: &quot;3e:b4:64:a3:e4:20&quot;,</span>
<span style="color:#AA5500">            &quot;Networks&quot;: {</span>
<span style="color:#AA5500">                &quot;bridge&quot;: {</span>
<span style="color:#AA5500">                    &quot;Aliases&quot;: null,</span>
<span style="color:#AA5500">                    &quot;DNSNames&quot;: null,</span>
<span style="color:#AA5500">                    &quot;DriverOpts&quot;: null,</span>
<span style="color:#AA5500">                    &quot;EndpointID&quot;: &quot;c46f72cd8a0ae6182051e01687f9d5b1d0ae8d7d718d4193aa772edba53fc0f0&quot;,</span>
<span style="color:#AA5500">                    &quot;Gateway&quot;: &quot;172.17.0.1&quot;,</span>
<span style="color:#AA5500">                    &quot;GlobalIPv6Address&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">                    &quot;GlobalIPv6PrefixLen&quot;: 0,</span>
<span style="color:#AA5500">                    &quot;GwPriority&quot;: 0,</span>
<span style="color:#AA5500">                    &quot;IPAMConfig&quot;: null,</span>
<span style="color:#AA5500">                    &quot;IPAddress&quot;: &quot;172.17.0.5&quot;,</span>
<span style="color:#AA5500">                    &quot;IPPrefixLen&quot;: 16,</span>
<span style="color:#AA5500">                    &quot;IPv6Gateway&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">                    &quot;Links&quot;: null,</span>
<span style="color:#AA5500">                    &quot;MacAddress&quot;: &quot;3e:b4:64:a3:e4:20&quot;,</span>
<span style="color:#AA5500">                    &quot;NetworkID&quot;: &quot;ec2adf010135e4885496c9e97e12dbc6ddfe52e3d312d8ae75261b7c475789e6&quot;</span>
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
<span style="color:#AA5500">            &quot;SandboxID&quot;: &quot;168346a4c47f3f3fbbd1f59cd774d0e60cad289255ae331663501748bd1839bc&quot;,</span>
<span style="color:#AA5500">            &quot;SandboxKey&quot;: &quot;/var/run/docker/netns/168346a4c47f&quot;,</span>
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
<span style="color:#AA5500">            &quot;FinishedAt&quot;: &quot;0001-01-01T00:00:00Z&quot;,</span>
<span style="color:#AA5500">            &quot;OOMKilled&quot;: false,</span>
<span style="color:#AA5500">            &quot;Paused&quot;: false,</span>
<span style="color:#AA5500">            &quot;Pid&quot;: 1794196,</span>
<span style="color:#AA5500">            &quot;Restarting&quot;: false,</span>
<span style="color:#AA5500">            &quot;Running&quot;: true,</span>
<span style="color:#AA5500">            &quot;StartedAt&quot;: &quot;2025-10-09T16:53:20.359607655Z&quot;,</span>
<span style="color:#AA5500">            &quot;Status&quot;: &quot;running&quot;</span>
<span style="color:#AA5500">        }</span>
<span style="color:#AA5500">    }</span>
<span style="color:#AA5500">}</span>
Donnerstag 09 Oktober 2025  18:53:20 +0200 (0:00:05.096)       0:02:38.762 **** 
Donnerstag 09 Oktober 2025  18:53:20 +0200 (0:00:00.067)       0:02:38.829 **** 
Donnerstag 09 Oktober 2025  18:53:20 +0200 (0:00:00.061)       0:02:38.891 **** 
Donnerstag 09 Oktober 2025  18:53:20 +0200 (0:00:00.112)       0:02:39.003 **** 

TASK [mumble : Stop Mumble] ***************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/mumble/tasks/main.yml:39</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:53:21 +0200 (0:00:00.607)       0:02:39.611 **** 
Donnerstag 09 Oktober 2025  18:53:21 +0200 (0:00:00.039)       0:02:39.651 **** 
Donnerstag 09 Oktober 2025  18:53:21 +0200 (0:00:00.044)       0:02:39.695 **** 

TASK [mylar : Stop Mylar] *****************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/mylar/tasks/main.yml:41</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:53:22 +0200 (0:00:00.609)       0:02:40.305 **** 
Donnerstag 09 Oktober 2025  18:53:22 +0200 (0:00:00.054)       0:02:40.359 **** 
Donnerstag 09 Oktober 2025  18:53:22 +0200 (0:00:00.040)       0:02:40.399 **** 

TASK [mymediaforalexa : Stop Mymediaforalexa] *********************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/mymediaforalexa/tasks/main.yml:27</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:53:22 +0200 (0:00:00.607)       0:02:41.007 **** 
Donnerstag 09 Oktober 2025  18:53:22 +0200 (0:00:00.057)       0:02:41.064 **** 
Donnerstag 09 Oktober 2025  18:53:22 +0200 (0:00:00.041)       0:02:41.106 **** 

TASK [n8n : Stop n8n] *********************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/n8n/tasks/main.yml:40</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:53:23 +0200 (0:00:00.586)       0:02:41.692 **** 
Donnerstag 09 Oktober 2025  18:53:23 +0200 (0:00:00.044)       0:02:41.736 **** 
Donnerstag 09 Oktober 2025  18:53:23 +0200 (0:00:00.047)       0:02:41.784 **** 

TASK [navidrome : Stop Navidrome] *********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/navidrome/tasks/main.yml:42</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:53:24 +0200 (0:00:00.594)       0:02:42.379 **** 
Donnerstag 09 Oktober 2025  18:53:24 +0200 (0:00:00.044)       0:02:42.424 **** 
Donnerstag 09 Oktober 2025  18:53:24 +0200 (0:00:00.042)       0:02:42.466 **** 

TASK [netbootxyz : Stop Netbootxyz] *******************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/netbootxyz/tasks/main.yml:41</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:53:24 +0200 (0:00:00.592)       0:02:43.059 **** 
Donnerstag 09 Oktober 2025  18:53:24 +0200 (0:00:00.043)       0:02:43.103 **** 
Donnerstag 09 Oktober 2025  18:53:24 +0200 (0:00:00.035)       0:02:43.139 **** 

TASK [netdata : Stop Netdata] *************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/netdata/tasks/main.yml:41</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:53:25 +0200 (0:00:00.588)       0:02:43.727 **** 
Donnerstag 09 Oktober 2025  18:53:25 +0200 (0:00:00.053)       0:02:43.780 **** 
Donnerstag 09 Oktober 2025  18:53:25 +0200 (0:00:00.050)       0:02:43.831 **** 
Donnerstag 09 Oktober 2025  18:53:25 +0200 (0:00:00.038)       0:02:43.869 **** 
Donnerstag 09 Oktober 2025  18:53:25 +0200 (0:00:00.042)       0:02:43.911 **** 

TASK [nextcloud : Stop Nextcloud] *********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/nextcloud/tasks/main.yml:72</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:53:26 +0200 (0:00:00.640)       0:02:44.552 **** 

TASK [nextcloud : Stop Nextcloud DB] ******************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/nextcloud/tasks/main.yml:76</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:53:26 +0200 (0:00:00.595)       0:02:45.147 **** 
Donnerstag 09 Oktober 2025  18:53:27 +0200 (0:00:00.049)       0:02:45.197 **** 
Donnerstag 09 Oktober 2025  18:53:27 +0200 (0:00:00.044)       0:02:45.242 **** 
Donnerstag 09 Oktober 2025  18:53:27 +0200 (0:00:00.040)       0:02:45.282 **** 
Donnerstag 09 Oktober 2025  18:53:27 +0200 (0:00:00.048)       0:02:45.331 **** 
Donnerstag 09 Oktober 2025  18:53:27 +0200 (0:00:00.046)       0:02:45.377 **** 

TASK [nomad : Check if Nomad is installed] ************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/nomad/tasks/main.yml:37</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false,</span>
<span style="color:#00AA00">    &quot;stat&quot;: {</span>
<span style="color:#00AA00">        &quot;exists&quot;: false</span>
<span style="color:#00AA00">    }</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:53:27 +0200 (0:00:00.335)       0:02:45.713 **** 
Donnerstag 09 Oktober 2025  18:53:27 +0200 (0:00:00.059)       0:02:45.772 **** 
Donnerstag 09 Oktober 2025  18:53:27 +0200 (0:00:00.056)       0:02:45.828 **** 
Donnerstag 09 Oktober 2025  18:53:27 +0200 (0:00:00.041)       0:02:45.870 **** 
Donnerstag 09 Oktober 2025  18:53:27 +0200 (0:00:00.042)       0:02:45.912 **** 

TASK [nzbget : Stop NZBget] ***************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/nzbget/tasks/main.yml:38</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:53:28 +0200 (0:00:00.610)       0:02:46.522 **** 
Donnerstag 09 Oktober 2025  18:53:28 +0200 (0:00:00.042)       0:02:46.565 **** 
Donnerstag 09 Oktober 2025  18:53:28 +0200 (0:00:00.044)       0:02:46.610 **** 

TASK [octoprint : Stop Octoprint] *********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/octoprint/tasks/main.yml:40</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:53:29 +0200 (0:00:00.585)       0:02:47.195 **** 
Donnerstag 09 Oktober 2025  18:53:29 +0200 (0:00:00.048)       0:02:47.244 **** 
Donnerstag 09 Oktober 2025  18:53:29 +0200 (0:00:00.046)       0:02:47.291 **** 

TASK [ombi : Stop Ombi] *******************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/ombi/tasks/main.yml:35</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:53:29 +0200 (0:00:00.582)       0:02:47.873 **** 
Donnerstag 09 Oktober 2025  18:53:29 +0200 (0:00:00.035)       0:02:47.909 **** 
Donnerstag 09 Oktober 2025  18:53:29 +0200 (0:00:00.046)       0:02:47.955 **** 
Donnerstag 09 Oktober 2025  18:53:29 +0200 (0:00:00.059)       0:02:48.014 **** 
Donnerstag 09 Oktober 2025  18:53:29 +0200 (0:00:00.041)       0:02:48.056 **** 

TASK [openhab : Stop openHAB] *************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/openhab/tasks/main.yml:60</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:53:30 +0200 (0:00:00.580)       0:02:48.637 **** 
Donnerstag 09 Oktober 2025  18:53:30 +0200 (0:00:00.039)       0:02:48.676 **** 
Donnerstag 09 Oktober 2025  18:53:30 +0200 (0:00:00.123)       0:02:48.800 **** 

TASK [organizr : Stop Organizr] ***********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/organizr/tasks/main.yml:38</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:53:31 +0200 (0:00:00.592)       0:02:49.392 **** 
Donnerstag 09 Oktober 2025  18:53:31 +0200 (0:00:00.053)       0:02:49.446 **** 
Donnerstag 09 Oktober 2025  18:53:31 +0200 (0:00:00.040)       0:02:49.486 **** 

TASK [overseerr : Stop Overseerr] *********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/overseerr/tasks/main.yml:43</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:53:32 +0200 (0:00:00.753)       0:02:50.240 **** 
Donnerstag 09 Oktober 2025  18:53:32 +0200 (0:00:00.082)       0:02:50.323 **** 
Donnerstag 09 Oktober 2025  18:53:32 +0200 (0:00:00.060)       0:02:50.383 **** 
Donnerstag 09 Oktober 2025  18:53:32 +0200 (0:00:00.120)       0:02:50.503 **** 
Donnerstag 09 Oktober 2025  18:53:32 +0200 (0:00:00.052)       0:02:50.556 **** 
Donnerstag 09 Oktober 2025  18:53:32 +0200 (0:00:00.103)       0:02:50.661 **** 

TASK [paperless_ng : Stop paperless_ng] ***************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/paperless_ng/tasks/main.yml:83</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:53:33 +0200 (0:00:00.906)       0:02:51.568 **** 

TASK [paperless_ng : Stop paperless_ng redis] *********************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/paperless_ng/tasks/main.yml:87</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:53:34 +0200 (0:00:00.806)       0:02:52.374 **** 

TASK [paperless_ng : Stop paperless_ng db] ************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/paperless_ng/tasks/main.yml:91</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:53:34 +0200 (0:00:00.629)       0:02:53.004 **** 
Donnerstag 09 Oktober 2025  18:53:34 +0200 (0:00:00.083)       0:02:53.088 **** 
Donnerstag 09 Oktober 2025  18:53:34 +0200 (0:00:00.061)       0:02:53.149 **** 
Donnerstag 09 Oktober 2025  18:53:35 +0200 (0:00:00.077)       0:02:53.227 **** 
Donnerstag 09 Oktober 2025  18:53:35 +0200 (0:00:00.054)       0:02:53.281 **** 

TASK [piwigo : Stop Piwigo] ***************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/piwigo/tasks/main.yml:71</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:53:35 +0200 (0:00:00.638)       0:02:53.920 **** 

TASK [piwigo : Stop Piwigo Db] ************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/piwigo/tasks/main.yml:75</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:53:36 +0200 (0:00:00.616)       0:02:54.537 **** 
Donnerstag 09 Oktober 2025  18:53:36 +0200 (0:00:00.046)       0:02:54.584 **** 
Donnerstag 09 Oktober 2025  18:53:36 +0200 (0:00:00.060)       0:02:54.644 **** 

TASK [plex : Stop Plex] *******************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/plex/tasks/main.yml:51</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:53:37 +0200 (0:00:00.593)       0:02:55.238 **** 
Donnerstag 09 Oktober 2025  18:53:37 +0200 (0:00:00.044)       0:02:55.282 **** 

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
Donnerstag 09 Oktober 2025  18:53:37 +0200 (0:00:00.369)       0:02:55.652 **** 

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
<span style="color:#AA5500">            &quot;EndpointID&quot;: &quot;4ebb832082e1d421387d96cbf52c8ce805841279b018eeb0fb6c6d364b859818&quot;,</span>
<span style="color:#AA5500">            &quot;Gateway&quot;: &quot;172.17.0.1&quot;,</span>
<span style="color:#AA5500">            &quot;GlobalIPv6Address&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;GlobalIPv6PrefixLen&quot;: 0,</span>
<span style="color:#AA5500">            &quot;HairpinMode&quot;: false,</span>
<span style="color:#AA5500">            &quot;IPAddress&quot;: &quot;172.17.0.2&quot;,</span>
<span style="color:#AA5500">            &quot;IPPrefixLen&quot;: 16,</span>
<span style="color:#AA5500">            &quot;IPv6Gateway&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;LinkLocalIPv6Address&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;LinkLocalIPv6PrefixLen&quot;: 0,</span>
<span style="color:#AA5500">            &quot;MacAddress&quot;: &quot;86:b3:19:6b:43:e3&quot;,</span>
<span style="color:#AA5500">            &quot;Networks&quot;: {</span>
<span style="color:#AA5500">                &quot;bridge&quot;: {</span>
<span style="color:#AA5500">                    &quot;Aliases&quot;: null,</span>
<span style="color:#AA5500">                    &quot;DNSNames&quot;: null,</span>
<span style="color:#AA5500">                    &quot;DriverOpts&quot;: null,</span>
<span style="color:#AA5500">                    &quot;EndpointID&quot;: &quot;4ebb832082e1d421387d96cbf52c8ce805841279b018eeb0fb6c6d364b859818&quot;,</span>
<span style="color:#AA5500">                    &quot;Gateway&quot;: &quot;172.17.0.1&quot;,</span>
<span style="color:#AA5500">                    &quot;GlobalIPv6Address&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">                    &quot;GlobalIPv6PrefixLen&quot;: 0,</span>
<span style="color:#AA5500">                    &quot;GwPriority&quot;: 0,</span>
<span style="color:#AA5500">                    &quot;IPAMConfig&quot;: null,</span>
<span style="color:#AA5500">                    &quot;IPAddress&quot;: &quot;172.17.0.2&quot;,</span>
<span style="color:#AA5500">                    &quot;IPPrefixLen&quot;: 16,</span>
<span style="color:#AA5500">                    &quot;IPv6Gateway&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">                    &quot;Links&quot;: null,</span>
<span style="color:#AA5500">                    &quot;MacAddress&quot;: &quot;86:b3:19:6b:43:e3&quot;,</span>
<span style="color:#AA5500">                    &quot;NetworkID&quot;: &quot;ec2adf010135e4885496c9e97e12dbc6ddfe52e3d312d8ae75261b7c475789e6&quot;</span>
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
<span style="color:#AA5500">            &quot;SandboxID&quot;: &quot;a04a77644ed8a5bc8dcc4dcf2b64f6f41ab48f681253243cc2d91d7f1afc6b8d&quot;,</span>
<span style="color:#AA5500">            &quot;SandboxKey&quot;: &quot;/var/run/docker/netns/a04a77644ed8&quot;,</span>
<span style="color:#AA5500">            &quot;SecondaryIPAddresses&quot;: null,</span>
<span style="color:#AA5500">            &quot;SecondaryIPv6Addresses&quot;: null</span>
<span style="color:#AA5500">        },</span>
<span style="color:#AA5500">        &quot;Path&quot;: &quot;/portainer&quot;,</span>
<span style="color:#AA5500">        &quot;Platform&quot;: &quot;linux&quot;,</span>
<span style="color:#AA5500">        &quot;ProcessLabel&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">        &quot;ResolvConfPath&quot;: &quot;/var/lib/docker/containers/9e2dd406f701ba1fdf46bebb1f056f8ac0567163173c7dfe0d767498aa848597/resolv.conf&quot;,</span>
<span style="color:#AA5500">        &quot;RestartCount&quot;: 1,</span>
<span style="color:#AA5500">        &quot;State&quot;: {</span>
<span style="color:#AA5500">            &quot;Dead&quot;: false,</span>
<span style="color:#AA5500">            &quot;Error&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;ExitCode&quot;: 0,</span>
<span style="color:#AA5500">            &quot;FinishedAt&quot;: &quot;2025-10-06T03:56:39.811369875Z&quot;,</span>
<span style="color:#AA5500">            &quot;OOMKilled&quot;: false,</span>
<span style="color:#AA5500">            &quot;Paused&quot;: false,</span>
<span style="color:#AA5500">            &quot;Pid&quot;: 233915,</span>
<span style="color:#AA5500">            &quot;Restarting&quot;: false,</span>
<span style="color:#AA5500">            &quot;Running&quot;: true,</span>
<span style="color:#AA5500">            &quot;StartedAt&quot;: &quot;2025-10-06T03:56:39.828525711Z&quot;,</span>
<span style="color:#AA5500">            &quot;Status&quot;: &quot;running&quot;</span>
<span style="color:#AA5500">        }</span>
<span style="color:#AA5500">    }</span>
<span style="color:#AA5500">}</span>
Donnerstag 09 Oktober 2025  18:53:39 +0200 (0:00:01.825)       0:02:57.478 **** 
Donnerstag 09 Oktober 2025  18:53:39 +0200 (0:00:00.051)       0:02:57.529 **** 
Donnerstag 09 Oktober 2025  18:53:39 +0200 (0:00:00.043)       0:02:57.572 **** 
Donnerstag 09 Oktober 2025  18:53:39 +0200 (0:00:00.044)       0:02:57.617 **** 

TASK [prowlarr : Stop Prowlarr] ***********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/prowlarr/tasks/main.yml:43</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:53:40 +0200 (0:00:00.604)       0:02:58.221 **** 
Donnerstag 09 Oktober 2025  18:53:40 +0200 (0:00:00.035)       0:02:58.256 **** 
Donnerstag 09 Oktober 2025  18:53:40 +0200 (0:00:00.047)       0:02:58.304 **** 
Donnerstag 09 Oktober 2025  18:53:40 +0200 (0:00:00.058)       0:02:58.362 **** 
Donnerstag 09 Oktober 2025  18:53:40 +0200 (0:00:00.041)       0:02:58.403 **** 
Donnerstag 09 Oktober 2025  18:53:40 +0200 (0:00:00.047)       0:02:58.452 **** 

TASK [promtail : Stop promtail] ***********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/promtail/tasks/main.yml:50</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:53:40 +0200 (0:00:00.600)       0:02:59.052 **** 
Donnerstag 09 Oktober 2025  18:53:40 +0200 (0:00:00.038)       0:02:59.090 **** 
Donnerstag 09 Oktober 2025  18:53:40 +0200 (0:00:00.045)       0:02:59.136 **** 

TASK [pyload : Stop pyLoad] ***************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/pyload/tasks/main.yml:45</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:53:41 +0200 (0:00:00.575)       0:02:59.711 **** 
Donnerstag 09 Oktober 2025  18:53:41 +0200 (0:00:00.052)       0:02:59.764 **** 
Donnerstag 09 Oktober 2025  18:53:41 +0200 (0:00:00.053)       0:02:59.818 **** 

TASK [pytivo : Stop Pytivo] ***************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/pytivo/tasks/main.yml:45</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:53:42 +0200 (0:00:00.583)       0:03:00.401 **** 
Donnerstag 09 Oktober 2025  18:53:42 +0200 (0:00:00.041)       0:03:00.443 **** 
Donnerstag 09 Oktober 2025  18:53:42 +0200 (0:00:00.050)       0:03:00.493 **** 

TASK [radarr : Stop Radarr] ***************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/radarr/tasks/main.yml:44</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:53:42 +0200 (0:00:00.573)       0:03:01.067 **** 
Donnerstag 09 Oktober 2025  18:53:42 +0200 (0:00:00.048)       0:03:01.115 **** 
Donnerstag 09 Oktober 2025  18:53:42 +0200 (0:00:00.043)       0:03:01.159 **** 
Donnerstag 09 Oktober 2025  18:53:43 +0200 (0:00:00.035)       0:03:01.195 **** 
Donnerstag 09 Oktober 2025  18:53:43 +0200 (0:00:00.050)       0:03:01.245 **** 

TASK [romm : Stop Romm] *******************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/romm/tasks/main.yml:84</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:53:43 +0200 (0:00:00.597)       0:03:01.843 **** 

TASK [romm : Stop Romm DB] ****************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/romm/tasks/main.yml:89</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:53:44 +0200 (0:00:00.584)       0:03:02.428 **** 
Donnerstag 09 Oktober 2025  18:53:44 +0200 (0:00:00.035)       0:03:02.463 **** 
Donnerstag 09 Oktober 2025  18:53:44 +0200 (0:00:00.052)       0:03:02.516 **** 
Donnerstag 09 Oktober 2025  18:53:44 +0200 (0:00:00.120)       0:03:02.637 **** 
Donnerstag 09 Oktober 2025  18:53:44 +0200 (0:00:00.052)       0:03:02.690 **** 
Donnerstag 09 Oktober 2025  18:53:44 +0200 (0:00:00.049)       0:03:02.739 **** 
Donnerstag 09 Oktober 2025  18:53:44 +0200 (0:00:00.044)       0:03:02.784 **** 

TASK [rssbridge : Stop RSSBridge] *********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/rssbridge/tasks/main.yml:34</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:53:45 +0200 (0:00:00.598)       0:03:03.383 **** 
Donnerstag 09 Oktober 2025  18:53:45 +0200 (0:00:00.042)       0:03:03.425 **** 
Donnerstag 09 Oktober 2025  18:53:45 +0200 (0:00:00.044)       0:03:03.470 **** 

TASK [sabnzbd : Stop Sabnzbd] *************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/sabnzbd/tasks/main.yml:38</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:53:45 +0200 (0:00:00.579)       0:03:04.050 **** 
Donnerstag 09 Oktober 2025  18:53:45 +0200 (0:00:00.055)       0:03:04.105 **** 
Donnerstag 09 Oktober 2025  18:53:45 +0200 (0:00:00.044)       0:03:04.150 **** 

TASK [sickchill : Stop Sickchill] *********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/sickchill/tasks/main.yml:40</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:53:46 +0200 (0:00:00.587)       0:03:04.738 **** 
Donnerstag 09 Oktober 2025  18:53:46 +0200 (0:00:00.040)       0:03:04.779 **** 
Donnerstag 09 Oktober 2025  18:53:46 +0200 (0:00:00.052)       0:03:04.831 **** 

TASK [silverbullet : Stop silverbullet] ***************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/silverbullet/tasks/main.yml:40</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:53:47 +0200 (0:00:00.613)       0:03:05.445 **** 
Donnerstag 09 Oktober 2025  18:53:47 +0200 (0:00:00.049)       0:03:05.495 **** 
Donnerstag 09 Oktober 2025  18:53:47 +0200 (0:00:00.046)       0:03:05.541 **** 

TASK [sonarr : Stop Sonarr] ***************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/sonarr/tasks/main.yml:39</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:53:47 +0200 (0:00:00.589)       0:03:06.130 **** 
Donnerstag 09 Oktober 2025  18:53:47 +0200 (0:00:00.040)       0:03:06.171 **** 
Donnerstag 09 Oktober 2025  18:53:48 +0200 (0:00:00.050)       0:03:06.221 **** 
Donnerstag 09 Oktober 2025  18:53:48 +0200 (0:00:00.036)       0:03:06.258 **** 
Donnerstag 09 Oktober 2025  18:53:48 +0200 (0:00:00.064)       0:03:06.322 **** 
Donnerstag 09 Oktober 2025  18:53:48 +0200 (0:00:00.076)       0:03:06.399 **** 
Donnerstag 09 Oktober 2025  18:53:48 +0200 (0:00:00.054)       0:03:06.453 **** 
Donnerstag 09 Oktober 2025  18:53:48 +0200 (0:00:00.036)       0:03:06.489 **** 
Donnerstag 09 Oktober 2025  18:53:48 +0200 (0:00:00.046)       0:03:06.536 **** 

TASK [stats : Stop Prometheus] ************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/stats/tasks/prometheus.yml:60</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:53:48 +0200 (0:00:00.598)       0:03:07.135 **** 
Donnerstag 09 Oktober 2025  18:53:49 +0200 (0:00:00.049)       0:03:07.184 **** 
Donnerstag 09 Oktober 2025  18:53:49 +0200 (0:00:00.051)       0:03:07.235 **** 
Donnerstag 09 Oktober 2025  18:53:49 +0200 (0:00:00.052)       0:03:07.288 **** 
Donnerstag 09 Oktober 2025  18:53:49 +0200 (0:00:00.060)       0:03:07.349 **** 

TASK [stats : Stop stats_telegraf] ********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/stats/tasks/telegraf.yml:56</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:53:49 +0200 (0:00:00.571)       0:03:07.920 **** 
Donnerstag 09 Oktober 2025  18:53:49 +0200 (0:00:00.040)       0:03:07.961 **** 
Donnerstag 09 Oktober 2025  18:53:49 +0200 (0:00:00.048)       0:03:08.009 **** 
Donnerstag 09 Oktober 2025  18:53:49 +0200 (0:00:00.037)       0:03:08.047 **** 

TASK [stats : Stop Smartctl Exporter] *****************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/stats/tasks/exporters.yml:45</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:53:50 +0200 (0:00:00.576)       0:03:08.623 **** 

TASK [stats : Stop Speedtest Exporter] ****************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/stats/tasks/exporters.yml:49</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:53:51 +0200 (0:00:00.589)       0:03:09.213 **** 
Donnerstag 09 Oktober 2025  18:53:51 +0200 (0:00:00.061)       0:03:09.274 **** 
Donnerstag 09 Oktober 2025  18:53:51 +0200 (0:00:00.053)       0:03:09.328 **** 
Donnerstag 09 Oktober 2025  18:53:51 +0200 (0:00:00.061)       0:03:09.390 **** 
Donnerstag 09 Oktober 2025  18:53:51 +0200 (0:00:00.036)       0:03:09.426 **** 
Donnerstag 09 Oktober 2025  18:53:51 +0200 (0:00:00.046)       0:03:09.472 **** 

TASK [stats : Stop Grafana] ***************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/stats/tasks/grafana.yml:65</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:53:51 +0200 (0:00:00.590)       0:03:10.063 **** 
Donnerstag 09 Oktober 2025  18:53:51 +0200 (0:00:00.042)       0:03:10.105 **** 
Donnerstag 09 Oktober 2025  18:53:51 +0200 (0:00:00.059)       0:03:10.165 **** 

TASK [syncthing : Stop Syncthing] *********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/syncthing/tasks/main.yml:38</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:53:52 +0200 (0:00:00.609)       0:03:10.774 **** 
Donnerstag 09 Oktober 2025  18:53:52 +0200 (0:00:00.056)       0:03:10.831 **** 
Donnerstag 09 Oktober 2025  18:53:52 +0200 (0:00:00.044)       0:03:10.876 **** 

TASK [tautulli : Stop Tautulli] ***********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/tautulli/tasks/main.yml:40</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:53:53 +0200 (0:00:00.596)       0:03:11.473 **** 
Donnerstag 09 Oktober 2025  18:53:53 +0200 (0:00:00.043)       0:03:11.516 **** 
Donnerstag 09 Oktober 2025  18:53:53 +0200 (0:00:00.035)       0:03:11.552 **** 
Donnerstag 09 Oktober 2025  18:53:53 +0200 (0:00:00.043)       0:03:11.595 **** 

TASK [thelounge : Stop The Lounge] ********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/thelounge/tasks/main.yml:42</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:53:54 +0200 (0:00:00.692)       0:03:12.288 **** 
Donnerstag 09 Oktober 2025  18:53:54 +0200 (0:00:00.051)       0:03:12.340 **** 
Donnerstag 09 Oktober 2025  18:53:54 +0200 (0:00:00.050)       0:03:12.390 **** 

TASK [threadfin : Stop Threadfin] *********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/threadfin/tasks/main.yml:34</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:53:54 +0200 (0:00:00.579)       0:03:12.969 **** 
Donnerstag 09 Oktober 2025  18:53:54 +0200 (0:00:00.040)       0:03:13.010 **** 
Donnerstag 09 Oktober 2025  18:53:54 +0200 (0:00:00.056)       0:03:13.067 **** 

TASK [tiddlywiki : Stop Tiddlywiki] *******************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/tiddlywiki/tasks/main.yml:36</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:53:55 +0200 (0:00:00.582)       0:03:13.649 **** 
Donnerstag 09 Oktober 2025  18:53:55 +0200 (0:00:00.034)       0:03:13.684 **** 
Donnerstag 09 Oktober 2025  18:53:55 +0200 (0:00:00.043)       0:03:13.727 **** 
Donnerstag 09 Oktober 2025  18:53:55 +0200 (0:00:00.040)       0:03:13.768 **** 
Donnerstag 09 Oktober 2025  18:53:55 +0200 (0:00:00.043)       0:03:13.812 **** 

TASK [timemachine : Stop Time Machine] ****************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/timemachine/tasks/main.yml:45</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:53:56 +0200 (0:00:00.590)       0:03:14.402 **** 

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
Donnerstag 09 Oktober 2025  18:53:56 +0200 (0:00:00.683)       0:03:15.086 **** 

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
<span style="color:#AA5500">            &quot;EndpointID&quot;: &quot;b62a0d82b23732ff487e41756b098073d9454be2767900b645ac7e5c93d32a5c&quot;,</span>
<span style="color:#AA5500">            &quot;Gateway&quot;: &quot;172.17.0.1&quot;,</span>
<span style="color:#AA5500">            &quot;GlobalIPv6Address&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;GlobalIPv6PrefixLen&quot;: 0,</span>
<span style="color:#AA5500">            &quot;HairpinMode&quot;: false,</span>
<span style="color:#AA5500">            &quot;IPAddress&quot;: &quot;172.17.0.9&quot;,</span>
<span style="color:#AA5500">            &quot;IPPrefixLen&quot;: 16,</span>
<span style="color:#AA5500">            &quot;IPv6Gateway&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;LinkLocalIPv6Address&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">            &quot;LinkLocalIPv6PrefixLen&quot;: 0,</span>
<span style="color:#AA5500">            &quot;MacAddress&quot;: &quot;da:1e:0c:8e:b0:92&quot;,</span>
<span style="color:#AA5500">            &quot;Networks&quot;: {</span>
<span style="color:#AA5500">                &quot;bridge&quot;: {</span>
<span style="color:#AA5500">                    &quot;Aliases&quot;: null,</span>
<span style="color:#AA5500">                    &quot;DNSNames&quot;: null,</span>
<span style="color:#AA5500">                    &quot;DriverOpts&quot;: null,</span>
<span style="color:#AA5500">                    &quot;EndpointID&quot;: &quot;b62a0d82b23732ff487e41756b098073d9454be2767900b645ac7e5c93d32a5c&quot;,</span>
<span style="color:#AA5500">                    &quot;Gateway&quot;: &quot;172.17.0.1&quot;,</span>
<span style="color:#AA5500">                    &quot;GlobalIPv6Address&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">                    &quot;GlobalIPv6PrefixLen&quot;: 0,</span>
<span style="color:#AA5500">                    &quot;GwPriority&quot;: 0,</span>
<span style="color:#AA5500">                    &quot;IPAMConfig&quot;: null,</span>
<span style="color:#AA5500">                    &quot;IPAddress&quot;: &quot;172.17.0.9&quot;,</span>
<span style="color:#AA5500">                    &quot;IPPrefixLen&quot;: 16,</span>
<span style="color:#AA5500">                    &quot;IPv6Gateway&quot;: &quot;&quot;,</span>
<span style="color:#AA5500">                    &quot;Links&quot;: null,</span>
<span style="color:#AA5500">                    &quot;MacAddress&quot;: &quot;da:1e:0c:8e:b0:92&quot;,</span>
<span style="color:#AA5500">                    &quot;NetworkID&quot;: &quot;ec2adf010135e4885496c9e97e12dbc6ddfe52e3d312d8ae75261b7c475789e6&quot;</span>
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
<span style="color:#AA5500">            &quot;SandboxID&quot;: &quot;b2375fb1fff45b5b667b76504cf2d6d60363336de8fc3b5b4fea77bf08bb84ca&quot;,</span>
<span style="color:#AA5500">            &quot;SandboxKey&quot;: &quot;/var/run/docker/netns/b2375fb1fff4&quot;,</span>
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
<span style="color:#AA5500">            &quot;FinishedAt&quot;: &quot;2025-10-05T12:53:08.105077457Z&quot;,</span>
<span style="color:#AA5500">            &quot;OOMKilled&quot;: false,</span>
<span style="color:#AA5500">            &quot;Paused&quot;: false,</span>
<span style="color:#AA5500">            &quot;Pid&quot;: 2669,</span>
<span style="color:#AA5500">            &quot;Restarting&quot;: false,</span>
<span style="color:#AA5500">            &quot;Running&quot;: true,</span>
<span style="color:#AA5500">            &quot;StartedAt&quot;: &quot;2025-10-05T12:54:07.703340805Z&quot;,</span>
<span style="color:#AA5500">            &quot;Status&quot;: &quot;running&quot;</span>
<span style="color:#AA5500">        }</span>
<span style="color:#AA5500">    }</span>
<span style="color:#AA5500">}</span>
Donnerstag 09 Oktober 2025  18:53:58 +0200 (0:00:01.746)       0:03:16.832 **** 
Donnerstag 09 Oktober 2025  18:53:58 +0200 (0:00:00.065)       0:03:16.898 **** 
Donnerstag 09 Oktober 2025  18:53:58 +0200 (0:00:00.057)       0:03:16.955 **** 
Donnerstag 09 Oktober 2025  18:53:58 +0200 (0:00:00.045)       0:03:17.001 **** 
Donnerstag 09 Oktober 2025  18:53:58 +0200 (0:00:00.048)       0:03:17.049 **** 

TASK [traefik : Stop Traefik] *************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/traefik/tasks/main.yml:44</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:53:59 +0200 (0:00:00.624)       0:03:17.674 **** 
Donnerstag 09 Oktober 2025  18:53:59 +0200 (0:00:00.039)       0:03:17.713 **** 
Donnerstag 09 Oktober 2025  18:53:59 +0200 (0:00:00.043)       0:03:17.756 **** 

TASK [transmission : Stop Transmission] ***************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/transmission/tasks/main.yml:44</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:54:00 +0200 (0:00:00.615)       0:03:18.372 **** 
Donnerstag 09 Oktober 2025  18:54:00 +0200 (0:00:00.040)       0:03:18.412 **** 
Donnerstag 09 Oktober 2025  18:54:00 +0200 (0:00:00.045)       0:03:18.458 **** 

TASK [transmission-with-openvpn : Stop Transmission with OpenVPM] *************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/transmission-with-openvpn/tasks/main.yml:64</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:54:00 +0200 (0:00:00.571)       0:03:19.029 **** 
Donnerstag 09 Oktober 2025  18:54:00 +0200 (0:00:00.055)       0:03:19.085 **** 
Donnerstag 09 Oktober 2025  18:54:00 +0200 (0:00:00.043)       0:03:19.129 **** 

TASK [ubooquity : Stop Ubooquity] *********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/ubooquity/tasks/main.yml:42</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:54:01 +0200 (0:00:00.579)       0:03:19.709 **** 
Donnerstag 09 Oktober 2025  18:54:01 +0200 (0:00:00.041)       0:03:19.750 **** 
Donnerstag 09 Oktober 2025  18:54:01 +0200 (0:00:00.042)       0:03:19.793 **** 

TASK [utorrent : Stop uTorrent] ***********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/utorrent/tasks/main.yml:46</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:54:02 +0200 (0:00:00.610)       0:03:20.404 **** 
Donnerstag 09 Oktober 2025  18:54:02 +0200 (0:00:00.051)       0:03:20.455 **** 
Donnerstag 09 Oktober 2025  18:54:02 +0200 (0:00:00.043)       0:03:20.499 **** 

TASK [valheim : Stop Valheim] *************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/valheim/tasks/main.yml:44</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:54:02 +0200 (0:00:00.578)       0:03:21.077 **** 
Donnerstag 09 Oktober 2025  18:54:02 +0200 (0:00:00.046)       0:03:21.123 **** 
Donnerstag 09 Oktober 2025  18:54:02 +0200 (0:00:00.043)       0:03:21.166 **** 
Donnerstag 09 Oktober 2025  18:54:03 +0200 (0:00:00.038)       0:03:21.205 **** 

TASK [virtual_desktop : Stop Virtual Desktop] *********************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/virtual_desktop/tasks/main.yml:37</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:54:03 +0200 (0:00:00.609)       0:03:21.814 **** 
Donnerstag 09 Oktober 2025  18:54:03 +0200 (0:00:00.067)       0:03:21.881 **** 
Donnerstag 09 Oktober 2025  18:54:03 +0200 (0:00:00.039)       0:03:21.921 **** 

TASK [wallabag : Stop Wallabag] ***********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/wallabag/tasks/main.yml:40</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:54:04 +0200 (0:00:00.623)       0:03:22.544 **** 
Donnerstag 09 Oktober 2025  18:54:04 +0200 (0:00:00.042)       0:03:22.586 **** 

TASK [watchtower : Stop Watchtower] *******************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/watchtower/tasks/main.yml:20</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:54:05 +0200 (0:00:00.595)       0:03:23.182 **** 
Donnerstag 09 Oktober 2025  18:54:05 +0200 (0:00:00.049)       0:03:23.231 **** 
Donnerstag 09 Oktober 2025  18:54:05 +0200 (0:00:00.044)       0:03:23.276 **** 

TASK [wireshark : Stop Wireshark] *********************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/wireshark/tasks/main.yml:39</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:54:05 +0200 (0:00:00.593)       0:03:23.869 **** 
Donnerstag 09 Oktober 2025  18:54:05 +0200 (0:00:00.114)       0:03:23.983 **** 
Donnerstag 09 Oktober 2025  18:54:05 +0200 (0:00:00.041)       0:03:24.025 **** 
Donnerstag 09 Oktober 2025  18:54:05 +0200 (0:00:00.040)       0:03:24.065 **** 
Donnerstag 09 Oktober 2025  18:54:05 +0200 (0:00:00.043)       0:03:24.109 **** 
Donnerstag 09 Oktober 2025  18:54:05 +0200 (0:00:00.038)       0:03:24.148 **** 
Donnerstag 09 Oktober 2025  18:54:06 +0200 (0:00:00.043)       0:03:24.191 **** 

TASK [woodpecker-ci : Stop Woodpecker-CI] *************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/woodpecker-ci/tasks/main.yml:78</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:54:06 +0200 (0:00:00.621)       0:03:24.813 **** 
Donnerstag 09 Oktober 2025  18:54:06 +0200 (0:00:00.040)       0:03:24.853 **** 
Donnerstag 09 Oktober 2025  18:54:06 +0200 (0:00:00.045)       0:03:24.899 **** 

TASK [youtubedlmaterial : Stop Youtubedlmaterial] *****************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/youtubedlmaterial/tasks/main.yml:52</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>
Donnerstag 09 Oktober 2025  18:54:07 +0200 (0:00:00.604)       0:03:25.503 **** 
Donnerstag 09 Oktober 2025  18:54:07 +0200 (0:00:00.055)       0:03:25.558 **** 
Donnerstag 09 Oktober 2025  18:54:07 +0200 (0:00:00.035)       0:03:25.594 **** 
Donnerstag 09 Oktober 2025  18:54:07 +0200 (0:00:00.044)       0:03:25.639 **** 

TASK [znc : Stop ZNC] *********************************************************************************************************************************************************************************************
<span style="color:#555555"><b>task path: /media/IT/repos/github/forked/ansible-nas/roles/znc/tasks/main.yml:45</b></span>
<span style="color:#00AA00">ok: [ansible-nas] =&gt; {</span>
<span style="color:#00AA00">    &quot;changed&quot;: false</span>
<span style="color:#00AA00">}</span>

PLAY RECAP ********************************************************************************************************************************************************************************************************
<span style="color:#AA5500">ansible-nas</span>                : <span style="color:#00AA00">ok=171 </span> <span style="color:#AA5500">changed=12  </span> unreachable=0    failed=0    <span style="color:#00AAAA">skipped=306 </span> rescued=0    ignored=0   

Donnerstag 09 Oktober 2025  18:54:08 +0200 (0:00:00.593)       0:03:26.232 **** 
=============================================================================== 
calibreweb : Calibre-web Docker Container ----------------------------------------------------------------------------------------------------------------------------------------------------------------- 36.74s
/media/IT/repos/github/forked/ansible-nas/roles/calibreweb/tasks/main.yml:12 -------------------------------------------------------------------------------------------------------------------------------------
dokuwiki : DokuWiki Docker Container ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- 13.86s
/media/IT/repos/github/forked/ansible-nas/roles/dokuwiki/tasks/main.yml:11 ---------------------------------------------------------------------------------------------------------------------------------------
ansible-nas-general : Update apt-cache --------------------------------------------------------------------------------------------------------------------------------------------------------------------- 7.51s
/media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-general/tasks/main.yml:7 -----------------------------------------------------------------------------------------------------------------------------
geerlingguy.nfs : Ensure directories to export exist ------------------------------------------------------------------------------------------------------------------------------------------------------- 6.02s
/home/dietmar/.ansible/roles/geerlingguy.nfs/tasks/main.yml:19 ---------------------------------------------------------------------------------------------------------------------------------------------------
mosquitto : Create Mosquitto container --------------------------------------------------------------------------------------------------------------------------------------------------------------------- 5.10s
/media/IT/repos/github/forked/ansible-nas/roles/mosquitto/tasks/main.yml:19 --------------------------------------------------------------------------------------------------------------------------------------
homepage : Template config files --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 3.25s
/media/IT/repos/github/forked/ansible-nas/roles/homepage/tasks/main.yml:11 ---------------------------------------------------------------------------------------------------------------------------------------
Gathering Facts -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 2.82s
/media/IT/repos/github/forked/ansible-nas/nas.yml:2 --------------------------------------------------------------------------------------------------------------------------------------------------------------
homepage : Create Homepage Docker Container ---------------------------------------------------------------------------------------------------------------------------------------------------------------- 2.69s
/media/IT/repos/github/forked/ansible-nas/roles/homepage/tasks/main.yml:23 ---------------------------------------------------------------------------------------------------------------------------------------
calibre : Calibre Docker Container ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 1.90s
/media/IT/repos/github/forked/ansible-nas/roles/calibre/tasks/main.yml:12 ----------------------------------------------------------------------------------------------------------------------------------------
freshrss : FreshRSS Docker Container ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- 1.83s
/media/IT/repos/github/forked/ansible-nas/roles/freshrss/tasks/main.yml:12 ---------------------------------------------------------------------------------------------------------------------------------------
portainer : Portainer Docker Container --------------------------------------------------------------------------------------------------------------------------------------------------------------------- 1.83s
/media/IT/repos/github/forked/ansible-nas/roles/portainer/tasks/main.yml:16 --------------------------------------------------------------------------------------------------------------------------------------
tinymm : tinyMediaManager Docker Container ----------------------------------------------------------------------------------------------------------------------------------------------------------------- 1.75s
/media/IT/repos/github/forked/ansible-nas/roles/tinymm/tasks/main.yml:15 -----------------------------------------------------------------------------------------------------------------------------------------
homeassistant : Home Assistant Docker Container ------------------------------------------------------------------------------------------------------------------------------------------------------------ 1.74s
/media/IT/repos/github/forked/ansible-nas/roles/homeassistant/tasks/main.yml:11 ----------------------------------------------------------------------------------------------------------------------------------
vladgh.samba.server : Install Samba packages --------------------------------------------------------------------------------------------------------------------------------------------------------------- 1.64s
/home/dietmar/.ansible/collections/ansible_collections/vladgh/samba/roles/server/tasks/main.yml:12 ---------------------------------------------------------------------------------------------------------------
ansible-nas-docker : Install docker python module ---------------------------------------------------------------------------------------------------------------------------------------------------------- 1.58s
/media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-docker/tasks/main.yml:26 -----------------------------------------------------------------------------------------------------------------------------
vladgh.samba.server : Install Samba VFS extensions packages ------------------------------------------------------------------------------------------------------------------------------------------------ 1.45s
/home/dietmar/.ansible/collections/ansible_collections/vladgh/samba/roles/server/tasks/main.yml:19 ---------------------------------------------------------------------------------------------------------------
geerlingguy.docker : Install Docker packages (with downgrade option). -------------------------------------------------------------------------------------------------------------------------------------- 1.43s
/home/dietmar/.ansible/roles/geerlingguy.docker/tasks/main.yml:27 ------------------------------------------------------------------------------------------------------------------------------------------------
geerlingguy.docker : Ensure additional dependencies are installed (on Ubuntu &lt; 20.04 and any other systems). ----------------------------------------------------------------------------------------------- 1.43s
/home/dietmar/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml:18 ----------------------------------------------------------------------------------------------------------------------------------------
ansible-nas-general : Install some packages ---------------------------------------------------------------------------------------------------------------------------------------------------------------- 1.43s
/media/IT/repos/github/forked/ansible-nas/roles/ansible-nas-general/tasks/main.yml:22 ----------------------------------------------------------------------------------------------------------------------------
geerlingguy.docker : Install docker-compose-plugin (with downgrade option). -------------------------------------------------------------------------------------------------------------------------------- 1.42s
/home/dietmar/.ansible/roles/geerlingguy.docker/tasks/main.yml:44 ------------------------------------------------------------------------------------------------------------------------------------------------
[<span style="color:#00AA00">2025-10-09 18:54:08</span>] (Venv) [<span style="color:#55FF55"><b>dietmar@MiraPi</b></span>] [<span style="color:#5555FF"><b>.../forked/ansible-nas</b></span>] $ 
</pre>
