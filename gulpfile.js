const gulp = require('gulp');
const { src, dest, series, parallel, watch } = gulp;
const cleanCSS = require('gulp-clean-css');
const uglify = require('gulp-uglify');
const sass = require('gulp-sass')(require('sass'));

// Task: Copy HTML files to the `dist` folder
function copyHTML() {
    return src('src/**/*.html').pipe(dest('dist'));
}

// Task: Compile SCSS to CSS and minify
function compileSCSS() {
    return src('src/scss/**/*.scss')
        .pipe(sass().on('error', sass.logError)) // Compile SCSS to CSS
        .pipe(cleanCSS()) // Minify CSS
        .pipe(dest('dist/css'));
}

// Task: Minify JavaScript files
function minifyJS() {
    return src('src/js/**/*.js')
        .pipe(uglify()) // Minify JavaScript
        .pipe(dest('dist/js'));
}

// Task: Watch for changes in files
function watchFiles() {
    watch('src/**/*.html', copyHTML);
    watch('src/scss/**/*.scss', compileSCSS);
    watch('src/js/**/*.js', minifyJS);
}

// Default task (runs all tasks in parallel)
exports.default = series(
    parallel(copyHTML, compileSCSS, minifyJS),
    watchFiles
);
