AUTHOR = 'Luis M. Franco'
SITENAME = 'Franco Lab'
SITEURL = 'https://github.io' # 'http://127.0.0.1:8000' #
PATH = 'content'
RELATIVE_URLS = False 
TIMEZONE = 'US/Pacific'
DEFAULT_LANG = 'en'
INDEX_SAVE_AS = 'blog.html'

# Repository path in page links
PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'

# Language pages
LANG_PAGE_URL = '{lang}/pages/{slug}.html'
LANG_PAGE_SAVE_AS = '{lang}/pages/{slug}.html'

# Theme
THEME = 'themes/notmyidea'
THEME_STATIC_DIR = 'theme'

# Translation
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['i18n_subsites']
I18N_SUBSITES = {
    'es': {
        'SITENAME': 'Franco Lab',
        'SOCIAL': [
            ("Linkedin", '/es/pages/underConstruction.html'),
            ("Bluesky", '/es/pages/underConstruction.html'),
            ("Facebook", '/es/pages/underConstruction.html'),
        ]
    }
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Manually define the order and links of your tabs
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

MENUITEMS = {
    'en': (
        ('Research', '/pages/research.html'),
        ('Team', '/pages/team.html'),
        ('Publications', '/pages/publications.html'),
        ('News', '/pages/news.html'),
        ('Join', '/pages/join.html'),
        ('Contact', '/pages/contact.html'),
    ),
    'es': (
        ('Investigación', '/pages/research.html'),
        ('Equipo', '/pages/team.html'),
        ('Publicaciones', '/pages/publications.html'),
        ('Noticias', '/pages/news.html'),
        ('Únete', '/pages/join.html'),
        ('Contacto', '/pages/contact.html'),
    ),
}

# Blogroll
LINKS = [
    ("INB", "https://inb.unam.mx/"),
    ("UNAM", "https://www.unam.mx/"),
]

# Social widget
SOCIAL = [
    ("Linkedin", '/pages/underConstruction.html'),
    ("Bluesky", '/pages/underConstruction.html'),
    ("Facebook", '/pages/underConstruction.html'),
]

# Added by Luis on 261002
ANALYTICS = """
<style>
/* ==========================================================================
    DESKTOP ALIGNMENT FIXES (Aligns LINKS and SOCIAL horizontally)
    ========================================================================== */

/* TARGET ONLY THE SOCIAL CONTAINER: Shifts the Title and Links together */
.social {
    position: relative !important;
    left: -65px !important; /* Adjust this value if you need it to slide more or less to the left */
}

/* Base style resets for both list containers */
.blogroll ul,
.social ul {
    padding-left: 0 !important;
    padding-top: 0 !important;
    list-style: none !important;
    white-space: nowrap !important;
}

/* LEAVE LINKS ALONE: Keep standard margins for the blogroll block */
.blogroll ul {
    margin: 0 !important;
}

.blogroll ul li {
    display: inline-block !important;
    padding: 0 !important;
    margin: 0 12px 0 0 !important;
    line-height: 1.5 !important;
}

/* Reset margins for social list since the parent container handles the shift */
.social ul {
    margin: 0 !important; 
}

/* Tighten individual social items slightly to guarantee they fit on the right */
.social ul li {
    display: inline-block !important;
    padding: 0 !important;
    margin: 0 8px 0 0 !important; /* Tighter gap to maximize screen space */
    line-height: 1.5 !important;
}

/* Strip trailing margins from the final items */
.blogroll ul li:last-child,
.social ul li:last-child {
    margin-right: 0 !important;
}

/* ==========================================================================
    TEAM GRID LAYOUT (Desktop View)
    ========================================================================== */

/* The wrapper that tells the grid to fill horizontal space and wrap when full */
.team-grid {
    display: flex !important;
    flex-wrap: wrap !important;
    gap: 50px !important;          /* Controls the spacing between cards */
    margin-top: 20px !important;
}

/* Individual card behavior */
.team-card {
    flex: 0 0 auto !important;     /* Prevents stretching */
    text-align: center !important;
    width: 200px !important;       /* Change this number to instantly resize all cards */
}

/* Force the image container inside the card to follow this card width */
.team-card .hover-container {
    width: 100% !important;
    max-width: 100% !important;
}

/* Force the image itself to fill the card neatly */
.team-card .hover-container img {
    width: 100% !important;         
    height: auto !important;        /* Keeps proportions perfect (no squishing) */
    object-fit: fill !important;    
    margin: 0 auto !important;      
}

/* Make sure the text under the image matches the card width */
.team-card h2 {
    font-size: 1.1em !important;
    margin-top: 10px !important;
    max-width: 100% !important;     /* Lets the text wrap naturally with the image width */
}

/* Hide the burger icon toggle button on desktop viewports by default */
.burger-menu-toggle {
    display: none !important;
}

/* ==========================================================================
    MOBILE & SMARTPHONE RESPONSIVE OVERRIDES
    ========================================================================== */
@media screen and (max-width: 768px) {
    /* Keep your existing working mobile responsive styles exactly as they are */
    body, #content, .body, #main, #main-content, article, .entry-content {
        width: 100% !important;
        max-width: 100% !important;
        padding: 12px !important;
        margin: 0 !important;
        box-sizing: border-box !important;
        float: none !important;
    }

    #extras, #extras .blogroll, #extras .social, #contentinfo {
        width: 100% !important;
        max-width: 100% !important;
        float: none !important;
        clear: both !important;
        margin-top: 25px !important;
        padding: 10px !important;
        box-sizing: border-box !important;
    }

    /* Reset the relative left shift on mobile screens so it centers cleanly */
    .social {
        left: 0 !important;
    }

    .blogroll ul, .social ul {
        white-space: normal !important; 
        margin: 0 !important; 
    }

    #main img, 
    #main a img, 
    .entry-content img,
    p img,
    figure img,
    .wp-caption img {
        max-width: 100% !important;
        width: 100% !important;
        
        /* Adjust heights only for your content images */
        height: 200px !important;       /* Adjust between 200px and 300px to fit your taste */
        object-fit: cover !important;   /* Crops/scales proportionally without stretching */
        object-position: center !important; 
        float: none !important;          
        display: block !important;       
        margin: 15px auto !important;    
        clear: both !important;
    }

    /* Keep structural containers block-level on mobile */
    figure, .wp-caption {
        max-width: 100% !important;
        width: 100% !important;
        display: block !important;
        float: none !important;
        margin: 15px auto !important;
    }

    p, .row, .gallery, div:has(> img) {
        display: block !important;
        width: 100% !important;
        clear: both !important;
    }

    p img, .row img {
        display: block !important;
        width: 100% !important;
        max-width: 100% !important;
        margin-bottom: 15px !important;
    }

    /* ==========================================================================
        MOBILE TEAM GRID OVERRIDES (Safely nested at the bottom of the query)
        ========================================================================== */
    
    /* 1. Control the mobile width of the overall card box */
    .team-card {
        display: block !important;
        /* Matches your desktop choice, but ensures it scales down on super narrow screens */
        width: 200px !important;           /* Change to match whatever width you chose for desktop! */
    }

    /* 2. Force the hover wrapper inside the card to span full card width */
    .team-card .hover-container {
        width: 100% !important;
        max-width: 100% !important;
    }

    /* 3. Force the mobile engine to scale the PNGs proportionally to fit the card */
    #main .team-card .hover-container img,
    .team-card .hover-container img {
        width: 100% !important;           /* Forces the image to stretch/shrink to the card width */
        height: auto !important;          /* Keeps original aspect ratio flawless with no distortion */
        max-width: 100% !important;
        display: block !important; 
        margin: 0 auto !important;
    }

    /* 4. Keep the team grid horizontal or flowing tightly on mobile if they fit */
    .team-grid {
        display: flex !important;
        flex-direction: row !important;   
        flex-wrap: wrap !important;       
        justify-content: center !important; 
        gap: 15px !important;
    }

    /* ----------------------------------------------------------------------
        BURGER ICON & MOBILE NAV LOGIC
        ---------------------------------------------------------------------- */
    
    /* 1. Turn the banner element relative to anchor our absolute list menu */
    #banner {
        position: relative !important;
        padding-bottom: 5px !important;   /* Creates buffer zone beneath the title for the button */
    }

    /* 2. Style and display the burger icon trigger link */
    header#banner .burger-menu-toggle {
        display: block !important;
        position: absolute !important;
        top: 15px !important;
        right: 15px !important;
        font-size: 32px !important;
        text-decoration: none !important;
        color: #333 !important;
        cursor: pointer !important;
        z-index: 9999 !important;
        font-weight: bold !important;
        line-height: 1 !important;
    }

    /* 3. Hide the main nav list container entirely by default on mobile */
    header#banner .burger-menu-toggle {
        display: block !important;
        position: absolute !important;
        top: auto !important;            /* Breaks free from top-corner stacking rules */
        bottom: 10px !important;         /* Anchors it cleanly underneath 'Franco Lab' */
        left: 20px !important;           /* Matches the left alignment margin of your title text */
        right: auto !important;
        font-size: 32px !important;     
        text-decoration: none !important;
        color: #ffffff !important;       /* FORCES THE HAMBURGER COLOR TO WHITE */
        cursor: pointer !important;
        z-index: 9999 !important;
        font-weight: bold !important;
        line-height: 1 !important;
    }

    /* 4. Target the navigation list container overlay */
    #banner nav > ul {
        display: none !important;       
        position: absolute !important;
        top: auto !important;            /* Changes coordinate maps to drop smoothly from the button position */
        bottom: -275px !important;       /* Extends downward without overlapping text lines */
        left: 55px !important;           /* Aligns dropdown box with the burger button position */
        right: auto !important;
        
        background: #111111 !important;                     /* Background color of burger menu */
        border: 1px solid #333333 !important;               /* Subtle dark border border */
        box-shadow: 0 4px 15px rgba(0,0,0,0.5) !important;  /* Deeper shadow for dark mode styling */
        padding: 8px 0 12px 0 !important;                   /* Safety margins inside the card list */
        margin: 0 !important;
        list-style: none !important;
        width: 220px !important;
        z-index: 9998 !important;
        border-radius: 4px !important;
        float: none !important;
        clear: both !important;
    }

    /* 5. When our JS injects the active class, force the list to display */
    #banner nav > ul.burger-active {
        display: block !important;
    }

    /* 6. Transform side-by-side elements into cleanly stacked blocks */
    #banner nav > ul li {
        display: block !important;       /* Forces block behavior (one per line) */
        float: none !important;          /* Destroys theme horizontal floating */
        clear: both !important;          /* Prevents items from sneaking side-by-side */
        width: 100% !important;          /* Spans full width of the dropdown menu */
        margin: 0 !important;
        padding: 0 !important;
        text-align: left !important;
    }

    #banner nav > ul li a {
        display: block !important;
        padding: 10px 22px !important;
        text-decoration: none !important;
        color: #ffffff !important;
        font-size: 21px !important;
        box-sizing: border-box !important;
        height: auto !important;            /* Overrides any rigid theme element constraints causing text misalignment */
        line-height: 1.4 !important;        /* Forces standard vertical alignment mechanics directly onto the font row */
        vertical-align: middle !important;
    }

    /* Hover Effect: highlight items when touched or hovered on desktop simulation models */
    #banner nav > ul li a:hover {
        background-color: #222222 !important;
    }

    #banner nav > ul li:last-child a {
        border-bottom: none !important;
    }
}
</style>

<script>
document.addEventListener("DOMContentLoaded", function() {
    // 1. Locate the banner header container 
    const bannerContainer = document.querySelector("header#banner");
    if (!bannerContainer) return;

    // 2. Create the white burger menu node element button
    const burgerBtn = document.createElement("a");
    burgerBtn.className = "burger-menu-toggle";
    burgerBtn.innerHTML = "&#9776;"; 
    burgerBtn.href = "javascript:void(0);";
    
    // 3. Inserts the button directly inside the header, right after the main <h1> title text box
    const siteTitle = bannerContainer.querySelector("h1");
    if (siteTitle) {
        siteTitle.parentNode.insertBefore(burgerBtn, siteTitle.nextSibling);
    } else {
        bannerContainer.appendChild(burgerBtn);
    }

    const navList = bannerContainer.querySelector("nav ul");

    // 4. Click trigger behavior toggles
    burgerBtn.addEventListener("click", function(e) {
        e.stopPropagation();
        if (navList) {
            navList.classList.toggle("burger-active");
        }
    });

    // 5. Close menu drawer if user taps anywhere else on the screen layout
    document.addEventListener("click", function() {
        if (navList && navList.classList.contains("burger-active")) {
            navList.classList.remove("burger-active");
        }
    });
});
</script>
"""

DEFAULT_PAGINATION = 10