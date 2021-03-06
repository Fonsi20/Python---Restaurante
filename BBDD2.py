import sqlite3

from gi.repository import Gtk

"""
    # Accion que conecta con la BBDD nada mas abrir el programa
"""
try:
    bbdd = 'provinciaslocalidades'
    conex = sqlite3.connect(bbdd)
    cur = conex.cursor()
    print('BASE DE DATOS CONECTADA')

except sqlite3.OperationalError as e:
    print(e)


def cerrarConexion():
    """
        # Accion que cierra la bbdd una vez cierra el programa
    """
    try:
        conex.commit()
        conex.close()
        print('cerrando base de provincias y municipios')
    except sqlite3.OperationalError as e:
        print(e)

def CargarProvincias(cmbProvincia):
    """
        # Accion que carga las provincias de la BBDD
    """
    i = 0
    cur.execute("SELECT provincia FROM Provincias")
    rows = cur.fetchall()
    list = Gtk.ListStore(str)
    for row in rows:
        i = i + 1
        list.append(row)

    for name in list:
        cmbProvincia.append_text(name[0])

    conex.commit()

def CargarMunicipios(cmbCiudad,nombre):
    """
        # Accion que carga los municipios de la BBDD según que provincia escogieses antes
    """
    i = 0
    cur.execute("SELECT M.Municipio FROM Municipios as M INNER JOIN Provincias as P on M.provincia_id = P.id where P.Provincia=?",(nombre,))
    list = Gtk.ListStore(str)
    all_rows = cur.fetchall()
    cmbCiudad.set_sensitive(True)
    for row in all_rows:
        i = i + 1
        list.append([row[0]])

    for name in list:
        cmbCiudad.append_text(name[0])

    conex.commit()