/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './public/**/*.html',
    './src/**/*.{js,jsx,ts,tsx}',
  ],
  theme: {
    extend: {
      colors: {
        customNavy: '#000035', // Replace with your specific color
      },
      scrollBehavior: ['smooth'],
    },
  },
  plugins: [],
}

