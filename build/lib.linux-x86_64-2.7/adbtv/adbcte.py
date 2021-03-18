"""AdbTV Constants functions

This functions allows the user to easy get the application names, key codes and view actions,
for the most common apps used in android TV.
"""

from typing import Union

def app(app_name: Union[str, int]) -> Union[str, None]:
    """
    Return the package name of an Android application. See "application names".

    Parameters
    ----------
    app_name : str | int
        The application name from "application names" list
        or the correspondent index

    Returns
    -------
    package : str
        The name of the package in Android

    Raises
    ------
    TypeError
        If `package` type isn't str or int
    
    Examples
    --------
    >>> apps('NETFLIX')
    com.netflix.ninja
    >>> apps(37)
    com.netflix.ninja
    
    """
    pkg_list = [ 
        ['AE_TV', 'com.aetn.aetv.watch'],
        ['AMZ_PRIME', 'com.amazon.avod.thirdpartyclient'],
        ['AMZ_VIDEO', 'com.amazon.avod'],
        ['APPLE_TV', 'com.apple.atve.sony.appletv'],
        ['APPLE_TV_FIRETV', 'com.apple.atve.amazon.appletv'],
        ['ATV_LAUNCHER', 'com.google.android.tvlauncher'],
        ['BELL_FIBE', 'com.quickplay.android.bellmediaplayer'],
        ['COMEDY_CENTRAL', 'com.vmn.android.comedycentral'],
        ['DAILYMOTION', 'com.dailymotion.dailymotion'],
        ['DEEZER', 'deezer.android.tv'],
        ['DISNEY_PLUS', 'com.disney.disneyplus'],
        ['DS_PHOTO', 'com.synology.dsphoto'],
        ['DS_VIDEO', 'com.synology.dsvideo'],
        ['ES_FILE_EXPLORER', 'com.estrongs.android.pop'],
        ['FACEBOOK', 'com.facebook.katana'],
        ['FAWESOME', 'com.future.moviesByFawesomeAndroidTV'],
        ['FIREFOX', 'org.mozilla.tv.firefox'],
        ['FIRETV_PACKAGE_LAUNCHER', 'com.amazon.tv.launcher'],
        ['FIRETV_PACKAGE_SETTINGS', 'com.amazon.tv.settings'],
        ['FIRETV_STORE', 'com.amazon.venezia'],
        ['FOOD_NETWORK_GO', 'tv.accedo.foodnetwork'],
        ['FRANCE_TV', 'fr.francetv.pluzz'],
        ['GOOGLE_CAST', 'com.google.android.apps.mediashell'],
        ['GOOGLE_TV_LAUNCHER', 'com.google.android.apps.tv.launcherx'],
        ['HAYSTACK_NEWS', 'com.haystack.android'],
        ['HBO_GO', 'eu.hbogo.androidtv.production'],
        ['HBO_GO_2', 'com.HBO'],
        ['HULU', 'com.hulu.plus'],
        ['IMDB_TV', 'com.amazon.imdb.tv.android.app'],
        ['IPTV', 'ru.iptvremote.android.iptv'],
        ['IPTV_SMARTERS_PRO', 'com.nst.iptvsmarterstvbox'],
        ['JELLYFIN_TV', 'org.jellyfin.androidtv'],
        ['KODI', 'org.xbmc.kodi'],
        ['LIVE_CHANNELS', 'com.google.android.tv'],
        ['MIJN_RADIO', 'org.samsonsen.nederlandse.radio.holland.nl'],
        ['MOLOTOV', 'tv.molotov.app'],
        ['MX_PLAYER', 'com.mxtech.videoplayer.ad'],
        ['NETFLIX', 'com.netflix.ninja'],
        ['NLZIET', 'nl.nlziet'],
        ['NOS', 'nl.nos.app'],
        ['NPO', 'nl.uitzendinggemist'],
        ['OCS', 'com.orange.ocsgo'],
        ['PLAY_GAMES', 'com.google.android.games'],
        ['PLAY_MUSIC', 'com.google.android.music'],
        ['PLAY_STORE', 'com.android.vending'],
        ['PLAY_VIDEOS', 'com.android.videos'],
        ['PLEX', 'com.plexapp.android'],
        ['PLUTO', 'tv.pluto.android'],
        ['PRIME_VIDEO', 'com.amazon.amazonvideo.livingroom'],
        ['PRIME_VIDEO_FIRETV', 'com.amazon.firebat'],
        ['RAVE', 'com.wemesh.android'],
        ['SETTINGS', 'com.android.tv.settings'],
        ['SMART_YOUTUBE_TV', 'com.liskovsoft.videomanager'],
        ['SONY_ACTION_MENU', 'com.sony.dtv.scrums.action'],
        ['SONY_ALBUM', 'com.sony.dtv.osat.album'],
        ['SONY_BRAVIA_SYNC_MENU', 'com.sony.dtv.braviasyncmenu'],
        ['SONY_BRAVIA_TUTORIALS', 'com.sony.dtv.bravialifehack'],
        ['SONY_DISCOVER', 'com.sony.dtv.discovery'],
        ['SONY_HELP', 'com.sony.dtv.smarthelp'],
        ['SONY_INTERNET_BROWSER', 'com.vewd.core.integration.dia'],
        ['SONY_MUSIC', 'com.sony.dtv.osat.music'],
        ['SONY_SCREEN_MIRRORING', 'com.sony.dtv.networkapp.wifidirect'],
        ['SONY_SELECT', 'com.sony.dtv.sonyselect'],
        ['SONY_TIMERS', 'com.sony.dtv.timers'],
        ['SONY_TV', 'com.sony.dtv.tvx'],
        ['SONY_VIDEO', 'com.sony.dtv.osat.video'],
        ['SPORT1', 'de.sport1.firetv.video'],
        ['SPOTIFY', 'com.spotify.tv.android'],
        ['STEAM_LINK', 'com.valvesoftware.steamlink'],
        ['SYFY', 'com.amazon.webapps.nbc.syfy'],
        ['T2', 'tv.perception.clients.tv.android'],
        ['TED', 'com.ted.android.tv'],
        ['TELECINE_BR', 'br.telecine.androidtv'],
        ['TERMUX', 'com.termux'],
        ['TIDAL', 'com.aspiro.tidal'],
        ['TUNEIN', 'tunein.player'],
        ['TVHEADEND', 'de.cyberdream.dreamepg.tvh.tv.player'],
        ['TWITCH', 'tv.twitch.android.app'],
        ['TWITCH_FIRETV', 'tv.twitch.android.viewer'],
        ['VEVO', 'com.vevo.tv'],
        ['VH1', 'com.mtvn.vh1android'],
        ['VIMEO', 'com.vimeo.android.videoapp'],
        ['VLC', 'org.videolan.vlc'],
        ['VOYO', 'com.phonegap.voyo'],
        ['VRV', 'com.ellation.vrv'],
        ['WAIPU_TV', 'de.exaring.waipu.firetv.live'],
        ['WATCH_TNT', 'com.turner.tnt.android.networkapp'],
        ['YOUTUBE', 'com.google.android.youtube.tv'],
        ['YOUTUBE_FIRETV', 'com.amazon.firetv.youtube'],
        ['YOUTUBE_KIDS', 'com.google.android.youtube.tvkids'],
        ['YOUTUBE_KIDS_FIRETV', 'com.amazon.firetv.youtube.kids'],
        ['YOUTUBE_MUSIC', 'com.google.android.youtube.tvmusic'],
        ['YOUTUBE_TV', 'com.google.android.youtube.tvunplugged'],
        ['ZIGGO', 'com.ziggo.tv']]
    if type(app_name) == int:
            return(pkg_list[int(app_name)][1])
    elif type(app_name) == str:
        for index in range(89):
            if str(pkg_list[index][0]) == app_name:
                package = pkg_list[index][1]
                return(package)
    else:
        raise TypeError()

def view_action(app_name: Union[str, int]) -> Union[str, None]:
    """
    Return the action for view given a name of an Android application. See "application names".

    Parameters
    ----------
    app_name : str | int
        The package name from "application names" list
        or the correspondent index

    Returns
    -------
    action : str
        The name of action for the given package in Android

    Raises
    ------
    TypeError
        If `action` type isn't str or int
    
    Examples
    --------
    >>> view_action('NETFLIX')
    .MainActivity
    >>> view_action(37)
    .MainActivity
    """
    view_act_list = [ 
        ['AE_TV', 'com.aetn.aetv.watch'],
        ['AMZ_PRIME', 'com.amazon.avod.thirdpartyclient'],
        ['AMZ_VIDEO', 'com.amazon.avod'],
        ['APPLE_TV', 'com.apple.atve.sony.appletv'],
        ['APPLE_TV_FIRETV', 'com.apple.atve.amazon.appletv'],
        ['ATV_LAUNCHER', 'com.google.android.tvlauncher'],
        ['BELL_FIBE', 'com.quickplay.android.bellmediaplayer'],
        ['COMEDY_CENTRAL', 'com.vmn.android.comedycentral'],
        ['DAILYMOTION', 'com.dailymotion.dailymotion'],
        ['DEEZER', 'deezer.android.tv'],
        ['DISNEY_PLUS', 'com.disney.disneyplus'],
        ['DS_PHOTO', 'com.synology.dsphoto'],
        ['DS_VIDEO', 'com.synology.dsvideo'],
        ['ES_FILE_EXPLORER', 'com.estrongs.android.pop'],
        ['FACEBOOK', 'com.facebook.katana'],
        ['FAWESOME', 'com.future.moviesByFawesomeAndroidTV'],
        ['FIREFOX', 'org.mozilla.tv.firefox'],
        ['FIRETV_PACKAGE_LAUNCHER', 'com.amazon.tv.launcher'],
        ['FIRETV_PACKAGE_SETTINGS', 'com.amazon.tv.settings'],
        ['FIRETV_STORE', 'com.amazon.venezia'],
        ['FOOD_NETWORK_GO', 'tv.accedo.foodnetwork'],
        ['FRANCE_TV', 'fr.francetv.pluzz'],
        ['GOOGLE_CAST', 'com.google.android.apps.mediashell'],
        ['GOOGLE_TV_LAUNCHER', 'com.google.android.apps.tv.launcherx'],
        ['HAYSTACK_NEWS', '.tv.ui.LoadingActivity'],
        ['HBO_GO', 'eu.hbogo.androidtv.MainActivity'],
        ['HBO_GO_2', 'com.HBO'],
        ['HULU', '.MainActivity'],
        ['IMDB_TV', 'com.amazon.imdb.tv.android.app'],
        ['IPTV', 'ru.iptvremote.android.iptv'],
        ['IPTV_SMARTERS_PRO', 'com.nst.iptvsmarterstvbox'],
        ['JELLYFIN_TV', 'org.jellyfin.androidtv'],
        ['KODI', '.Splash'],
        ['LIVE_CHANNELS', 'com.google.android.tv'],
        ['MIJN_RADIO', 'org.samsonsen.nederlandse.radio.holland.nl'],
        ['MOLOTOV', 'tv.molotov.app'],
        ['MX_PLAYER', 'com.mxtech.videoplayer.ad'],
        ['NETFLIX', '.MainActivity'],
        ['NLZIET', 'nl.nlziet'],
        ['NOS', 'nl.nos.app'],
        ['NPO', 'nl.uitzendinggemist'],
        ['OCS', 'com.orange.ocsgo'],
        ['PLAY_GAMES', 'com.google.android.apps.play.games.app.atv.features.home.v1.HomeV1Activity'],
        ['PLAY_MUSIC', 'com.google.android.music.tv.lockout.FsiActivity'],
        ['PLAY_STORE', 'com.google.android.finsky.tvmainactivity.TvMainActivity}'],
        ['PLAY_VIDEOS', 'com.google.android.apps.play.movies.tv.usecase.home.TvHomeActivity'],
        ['PLEX', 'com.plexapp.plex.activities.SplashActivity'],
        ['PLUTO', '.leanback.controller.LeanbackSplashOnboardActivity'],
        ['PRIME_VIDEO', 'com.amazon.ignition.IgnitionActivity'],
        ['PRIME_VIDEO_FIRETV', 'com.amazon.firebat'],
        ['RAVE', 'com.wemesh.android.Activities.OverscanActivity}'],
        ['SETTINGS', 'com.android.tv.settings'],
        ['SMART_YOUTUBE_TV', 'com.liskovsoft.videomanager'],
        ['SONY_ACTION_MENU', 'com.sony.dtv.scrums.action'],
        ['SONY_ALBUM', 'com.sony.dtv.osat.album'],
        ['SONY_BRAVIA_SYNC_MENU', 'com.sony.dtv.braviasyncmenu'],
        ['SONY_BRAVIA_TUTORIALS', 'com.sony.dtv.bravialifehack'],
        ['SONY_DISCOVER', 'com.sony.dtv.discovery'],
        ['SONY_HELP', 'com.sony.dtv.smarthelp'],
        ['SONY_INTERNET_BROWSER', 'com.vewd.core.integration.dia'],
        ['SONY_MUSIC', 'com.sony.dtv.osat.music'],
        ['SONY_SCREEN_MIRRORING', 'com.sony.dtv.networkapp.wifidirect'],
        ['SONY_SELECT', 'com.sony.dtv.sonyselect'],
        ['SONY_TIMERS', 'com.sony.dtv.timers'],
        ['SONY_TV', 'com.sony.dtv.tvx'],
        ['SONY_VIDEO', 'com.sony.dtv.osat.video'],
        ['SPORT1', 'de.sport1.firetv.video'],
        ['SPOTIFY', '.SpotifyTVActivity'],
        ['STEAM_LINK', 'com.valvesoftware.steamlink.SteamShellActivity'],
        ['SYFY', 'com.amazon.webapps.nbc.syfy'],
        ['T2', 'tv.perception.clients.tv.android'],
        ['TED', 'com.ted.android.tv'],
        ['TELECINE_BR', 'tele.cine.tv.MainActivity'],
        ['TERMUX', 'com.termux.app.TermuxActivity'],
        ['TIDAL', 'com.aspiro.wamp.tv.TvLauncherActivity'],
        ['TUNEIN', 'tunein.player'],
        ['TVHEADEND', 'de.cyberdream.dreamepg.tvh.tv.player'],
        ['TWITCH', 'tv.twitch.android.apps.TwitchActivity'],
        ['TWITCH_FIRETV', 'tv.twitch.android.apps.TwitchActivity'],
        ['VEVO', 'com.vevo.tv'],
        ['VH1', 'com.mtvn.vh1android'],
        ['VIMEO', 'com.vimeo.android.videoapp'],
        ['VLC', 'org.videolan.vlc'],
        ['VOYO', 'com.phonegap.voyo'],
        ['VRV', 'com.ellation.vrv'],
        ['WAIPU_TV', 'de.exaring.waipu.firetv.live'],
        ['WATCH_TNT', 'com.turner.tnt.android.networkapp'],
        ['YOUTUBE', 'com.google.android.apps.youtube.tv.activity.ShellActivity'],
        ['YOUTUBE_FIRETV', 'com.amazon.firetv.youtube'],
        ['YOUTUBE_KIDS', 'com.google.android.youtube.tvkids'],
        ['YOUTUBE_KIDS_FIRETV', 'com.amazon.firetv.youtube.kids'],
        ['YOUTUBE_MUSIC', 'com.google.android.youtube.tvmusic'],
        ['YOUTUBE_TV', 'com.google.android.youtube.tvunplugged'],
        ['ZIGGO', 'com.lgi.horizongo.core.activity.splash.SplashActivity']]
    if type(app_name) == int:
            return(view_act_list[int(app_name)][1])
    elif type(app_name) == str:
        for index in range(89):
            if str(view_act_list[index][0]) == app_name:
                action = view_act_list[index][1]
                return(action)
    else:
        raise TypeError()

# ADB key event codes
# https://developer.android.com/reference/android/view/KeyEvent

def key(key_name: Union[str, int]) -> Union[str, None]:
    """
    Return the key code of a given command (e.g. from remote control). See "key names".

    Parameters
    ----------
    key_name : str | int
        The code name from "keys list" list
        or the correspondent index

    Returns
    -------
    code : str
        The code of keys list

    Raises
    ------
    TypeError
        If `key_name` type isn't str or int
    
    Examples
    --------
    >>> key('ENTER')
    66
    >>> key(9)
    66
    """
    key_list = [
        ['BACK', 4],
        ['BLUE', 186],
        ['CENTER', 23],
        ['COMPONENT1', 249],
        ['COMPONENT2', 250],
        ['COMPOSITE1', 247],
        ['COMPOSITE2', 248],
        ['DOWN', 20],
        ['END', 123],
        ['ENTER', 66],
        ['ESCAPE', 111],
        ['FAST_FORWARD', 90],
        ['GREEN', 184],
        ['HDMI1', 243],
        ['HDMI2', 244],
        ['HDMI3', 245],
        ['HDMI4', 246],
        ['HOME', 3],
        ['INPUT', 178],
        ['LEFT', 21],
        ['MENU', 82],
        ['MOVE_HOME', 122],
        ['MUTE', 164],
        ['NEXT', 87],
        ['PAIRING', 225],
        ['PAUSE', 127],
        ['PLAY', 126],
        ['PLAY_PAUSE', 85],
        ['POWER', 26],
        ['PREVIOUS', 88],
        ['RED', 183],
        ['RESUME', 224],
        ['REWIND', 89],
        ['RIGHT', 22],
        ['SAT', 237],
        ['SEARCH', 84],
        ['SETTINGS', 176],
        ['SLEEP', 223],
        ['SPACE', 62],
        ['STOP', 86],
        ['SUSPEND', 276],
        ['SYSDOWN', 281],
        ['SYSLEFT', 282],
        ['SYSRIGHT', 283],
        ['SYSUP', 280],
        ['TEXT', 233],
        ['TOP', 122],
        ['UP', 19],
        ['VGA', 251],
        ['VOLUME_DOWN', 25],
        ['VOLUME_UP', 24],
        ['WAKEUP', 224],
        ['YELLOW', 185]]
    if type(key_name) == int:
        return(key_list[int(key_name)][1])
    elif type(key_name) == str:
        for index in range(len(key_list)):
            if str(key_list[index][0]) == key_name:
                code = key_list[index][1]
                return(code)
    else:
        raise TypeError()

def alfa_key(alfa: Union[str, int]) -> Union[str, None]:
    """
    Return the numeric value of a possible alfanumeric key name. See "alfanumeric key names".

    Parameters
    ----------
    alfa : str | int
        The package name from "alfa numeric names" list
        or the correspondent index

    Returns
    -------
    alfa_code : str
        The correspondent alfa numeric code

    Raises
    ------
    TypeError
        If `alfa` type isn't str or int
    
    Examples
    --------
    >>> alfa_key('A')
    29
    >>> alfa_key(10)
    29
    """
    alfa_key_list = [
        ['0', 7],
        ['1', 8],
        ['2', 9],
        ['3', 10],
        ['4', 11],
        ['5', 12],
        ['6', 13],
        ['7', 14],
        ['8', 15],
        ['9', 16],
        ['A', 29],
        ['B', 30],
        ['C', 31],
        ['D', 32],
        ['E', 33],
        ['F', 34],
        ['G', 35],
        ['H', 36],
        ['I', 37],
        ['J', 38],
        ['K', 39],
        ['L', 40],
        ['M', 41],
        ['N', 42],
        ['O', 43],
        ['P', 44],
        ['Q', 45],
        ['R', 46],
        ['S', 47],
        ['T', 48],
        ['U', 49],
        ['V', 50],
        ['W', 51],
        ['X', 52],
        ['Y', 53],
        ['Z', 54]]
    if type(alfa) == int:
        return(alfa_key_list[int(alfa)][1])
    elif type(alfa) == str:
        for index in range(len(alfa_key_list)):
            if str(alfa_key_list[index][0]) == alfa:
                alfa_code = alfa_key_list[index][1]
                return(alfa_code)
    else:
        raise TypeError()