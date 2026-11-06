# Safe decoy VM plan (offline-first)

This plan is for learning system administration and defensive monitoring, not for running malware or exposing a honeypot to the internet. A VM is not automatically isolated: its virtual network and host-integration features determine what it can reach.

## Recommended beginner setup

1. Use a reputable hypervisor and create a fresh, fully updated guest from a trusted operating-system image.
2. Prefer an **internal/isolated virtual network with no uplink** for a decoy that does not need internet access. Confirm the hypervisor's exact network-mode behavior in its documentation.
3. Do not use bridged networking. Do not configure port forwarding. Avoid host-only networking if the goal is no guest-to-host connectivity; host-only networks commonly permit communication with the host.
4. Disable shared folders, shared clipboard, drag-and-drop, USB passthrough, and automatic device mounting. Do not put personal files, browser profiles, SSH keys, passwords, or other host secrets in the guest.
5. Use a separate, non-privileged guest account and a dedicated virtual disk. Keep snapshots so the guest can be reverted to a known clean state.
6. Take a clean snapshot before experiments. After a lab session, power down and revert rather than trusting that cleanup removed every change.
7. Keep the host OS and hypervisor updated. Store no sensitive data in the VM and do not log into personal accounts from it.

## If the guest needs updates

The safest beginner option is to update the guest before isolating it, then shut it down and switch it back to the isolated network. Verify the network mode after changing it. Avoid adding an internet-connected network adapter just for convenience.

If a legitimate lab requires controlled connectivity, use a separate disposable device or a properly configured, dedicated lab network with explicit egress restrictions and no route to the home LAN. Get help from someone experienced with network isolation; ordinary NAT is not the same as complete isolation, and a misconfigured rule can expose the guest or host.

## Before each session, verify

- The VM is not bridged and has no port-forward rules.
- The guest has no shared folders, clipboard, drag-and-drop, or personal credentials.
- The virtual network is the intended isolated network and has no unexpected uplink.
- No real home devices or third-party systems are being targeted.
- You can revert to the clean snapshot afterward.

## Important limits

Virtualization reduces risk but does not make risk zero. Hypervisor vulnerabilities, configuration mistakes, and unsafe files can still create problems. This plan is not a guide to deploying an internet-facing honeypot. Do not expose a decoy to the internet from your everyday PC or home network.
