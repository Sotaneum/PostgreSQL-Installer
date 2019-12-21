-->Table<--
--<m_installer_Information>--
CREATE TABLE m_installer_information(
   sql json,
   version text
)
WITH (
   OIDS = TRUE
);
--<m_installer_Information>--
-->Function<--
--<m_installer_update>--
CREATE OR REPLACE FUNCTION m_installer_update(
	)
    RETURNS TEXT
    LANGUAGE 'plpython3u'

    COST 100
    VOLATILE 
AS $BODY$
    # -- ==========================================================
    # --    Installer

    # --    Copyright 2019 LEE DONG GUN(2019.12.22)
    # -- ==========================================================

    from postgresql_installer import Installer

    installer = Installer(plpy)
    return installer.update()[1]

$BODY$;

ALTER FUNCTION m_installer_update();
--<m_installer_update>--
--<m_installer_uninstall>--
CREATE OR REPLACE FUNCTION m_installer_uninstall(
	)
    RETURNS TEXT
    LANGUAGE 'plpython3u'

    COST 100
    VOLATILE 
AS $BODY$
    # -- ==========================================================
    # --    Installer

    # --    Copyright 2019 LEE DONG GUN(2019.12.22)
    # -- ==========================================================

    from postgresql_installer import Installer

    installer = Installer(plpy)
    return installer.uninstall()[1]

$BODY$;

ALTER FUNCTION m_installer_uninstall();
--<m_installer_uninstall>--
--<m_installer_pylib_update>--
CREATE OR REPLACE FUNCTION m_installer_pylib_update(
	)
    RETURNS TEXT
    LANGUAGE 'plpython3u'

    COST 100
    VOLATILE 
AS $BODY$
    # -- ==========================================================
    # --    Installer

    # --    Copyright 2019 LEE DONG GUN(2019.12.22)
    # -- ==========================================================

    from postgresql_installer import Installer

    installer = Installer(plpy)
    return installer.python_lib_update()[1]

$BODY$;

ALTER FUNCTION m_installer_pylib_update();
--<m_installer_pylib_update>--
--<m_installer_delete_cache>--
CREATE OR REPLACE FUNCTION m_installer_delete_cache(
	)
    RETURNS TEXT
    LANGUAGE 'plpython3u'

    COST 100
    VOLATILE 
AS $BODY$
    # -- ==========================================================
    # --    Installer

    # --    Copyright 2019 LEE DONG GUN(2019.12.22)
    # -- ==========================================================

    from postgresql_installer import Installer

    installer = Installer(plpy)
    return installer.remove_cache()[1]

$BODY$;

ALTER FUNCTION m_installer_delete_cache();
--<m_installer_delete_cache>--