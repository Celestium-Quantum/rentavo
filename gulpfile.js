const gulp = require('gulp');
const { src, dest, series, parallel, watch } = gulp;
const uglify = require('gulp-uglify');
const sass = require('gulp-sass')(require('sass'));

// Task: Minify JavaScript files
function minifyJS() {
    return src('./*.js')
        .pipe(uglify()) // Minify JavaScript
        .pipe(dest('dist/js'));
}

// Task: Watch for changes in files
function watchFiles() {
    watch('./*.js', minifyJS);
}

// Default task (runs all tasks in parallel)
exports.default = series(
    parallel(minifyJS),
    watchFiles
);
