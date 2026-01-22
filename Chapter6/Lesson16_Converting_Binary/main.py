def binary_string_to_int(num_servers, num_players, num_admins):
    num_server_int = int(num_servers, 2)
    num_player_int = int(num_players, 2)
    num_admin_int = int(num_admins, 2)
    return (num_server_int, num_player_int, num_admin_int)
