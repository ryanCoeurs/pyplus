def test_find_prompt(netmiko_connect):
    assert netmiko_connect.find_prompt() == "arista1#"


def test_show_version(netmiko_connect):
    assert "4.20.10M" in netmiko_connect.send_command("show version")
