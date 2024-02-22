/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */

module.exports = {
    content: [
        /**
         * HTML. Paths to Django template files that will contain Tailwind CSS classes.
         */

        /*  Templates within theme app (<tailwind_app_name>/templates), e.g. base.html. */
        '../templates/**/*.html',

    ],
    theme: {
        extend: {},
    },
    
    daisyui: {
        themes: [
            {
              mytheme: {
                    "primary": "#2563eb",
                    "secondary": "#6d28d9",
                    "accent": "#15803d",
                    "neutral": "#2563eb",
                    "base-100": "#ffffff",
                    "info": "#60a5fa",
                    "success": "#22c55e",
                    "warning": "#facc15",
                    "error": "#be123c",
                    "--rounded-box": "0.4rem", // border radius rounded-box utility class, used in card and other large boxes
                    "--rounded-btn": "0.4rem", // border radius rounded-btn utility class, used in buttons and similar element
                    "--rounded-badge": "0.4rem", // border radius rounded-badge utility class, used in badges and similar
                    "--animation-btn": "0.25s", // duration of animation when you click on button
                    "--animation-input": "0.2s", // duration of animation for inputs like checkbox, toggle, radio, etc
                    "--btn-focus-scale": "0.95", // scale transform of button when you focus on it
                    "--border-btn": "1px", // border width of buttons
                    "--tab-border": "1px", // border width of tabs
                    "--tab-radius": "0.5rem", // border radius of tabs
                },
            },
          ],
        base: true, // applies background color and foreground color for root element by default
        styled: true, // include daisyUI colors and design decisions for all components
        utils: true, // adds responsive and modifier utility classes
        rtl: false, // rotate style direction from left-to-right to right-to-left. You also need to add dir="rtl" to your html tag and install `tailwindcss-flip` plugin for Tailwind CSS.
        prefix: "", // prefix for daisyUI classnames (components, modifiers and responsive class names. Not colors)
        logs: true, // Shows info about daisyUI version and used config in the console when building your CSS
    },
    plugins: [
        require("@tailwindcss/typography"),
        require("daisyui"),
    ],
}
