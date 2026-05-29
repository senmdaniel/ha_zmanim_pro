from homeassistant import config_entries


class ZmanimProConfigFlow(
    config_entries.ConfigFlow,
    domain="ha_zmanim_pro",
):
    VERSION = 1

    async def async_step_user(self, user_input=None):

        return self.async_create_entry(
            title="HA Zmanim Pro",
            data={},
        )
