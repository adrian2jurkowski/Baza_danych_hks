import psycopg2

hostname = 'localhost'
database = 'team'
username = 'postgres'
password = 'password'
port_id = 5432
conn = None
cur = None

try:
    conn = psycopg2.connect(
                host = hostname,
                dbname = database,
                user = username,
                password = password,
                port = port_id)
    
    cur = conn.cursor()

    cur.execute('DROP TABLE IF EXISTS players')

    create_script = ''' CREATE TABLE IF NOT EXISTS players (
                            Nr          int PRIMARY KEY,
                            Name        varchar NOT NULL,
                            Position    varchar NOT NULL,
                            Height      int NOT NULL,
                            Weight      int NOT NULL) '''
    
    cur.execute(create_script)

    insert_script = 'INSERT INTO players (Nr, Name, Position, Height, Weight) VALUES (%s, %s, %s, %s, %s)'
    insert_values = [(1, 'Adam W.', 'Goalkeeper', 196, 88), (33, 'Arkadiusz L.', 'Goalkeeper', 192, 85),
                     (47, 'Kamil G.', 'Defender', 184, 75), (5, 'Dawid K.', 'Defender', 186, 92), (36, 'Kamil W.', 'Defender', 186, 75), 
                     (25, 'Patryk N.', 'Defender', 191, 78), (23, 'Jakub M.', 'Defender', 178, 71), (24, 'Damian U.', 'Defender', 180, 75), 
                     (20, 'Michał Z.', 'Defender', 178, 79), (77, 'Kacper A.', 'Midfielder', 182, 75), (17, 'Sławomir Ch.', 'Midfielder', 178, 80), 
                     (10, 'Miłosz D.', 'Midfielder', 182, 72), (18, 'Anthony I.', 'Midfielder', 185, 76), 
                     (14, 'Patryk S.', 'Midfielder', 182, 80), (11, 'Patryk K.', 'Midfielder', 185, 77), 
                     (15, 'Marcin M.', 'Midfielder', 182, 72), (7, 'Krzysztof Ś.', 'Midfielder', 175, 68), 
                     (8, 'Dominik Z.', 'Midfielder', 182, 80), (9, 'Krystian L.', 'Attacker', 186, 84), 
                     (91, 'Hubert K.', 'Attacker', 180, 80), (99, 'Marcin W.', 'Attacker', 197, 88)]
    
    for record in insert_values:
        cur.execute(insert_script, record)
    conn.commit()




except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()