const path = require('path');
const webpack = require('webpack');

const nodeEnv = process.env.NODE_ENV || 'development';
const isDevEnv = nodeEnv === 'development';
const publicPathRoot = process.env.PUBLIC_PATH_ROOT || 'http://localhost:8000/static/build'

module.exports = {
    entry: path.resolve(__dirname, 'video/static/vue/site.js'),
    output: {
        path: path.resolve(__dirname, 'storage/static/build/site'),
        publicPath: `${publicPathRoot}/site/vue/`,
        filename: 'site.bundle.js',
        chunkFilename: '[name].bundle.js'
    },
    mode: nodeEnv,
    devtool: isDevEnv ? 'cheap-module-eval-source-map' : 'source-map',
    module: {
        rules: [ {
            test: /\.vue$/,
            loader: 'vue-loader'
        }, {
            test: /\.js$/,
            exclude: /node_modules/,
            loader: 'babel-loader'
        }, {
            test: /\.scss$/,
            use: ['style-loader', 'css-loader', 'sass-loader']
        }, {
            test: /\.(png|jpe?g|gif|svg|[ot]tf|eot|woff2?)$/,
            loader: 'file-loader',
            options: {
                name: 'assets/[name].[ext]'
            }
        }, {
            test: /zepto-(\d\.){3}(min\.)?js$/,
            loader: 'exports-loader',
            query: {
                Zepto: true
            }
        } ]
    },
    resolve: {
        alias: {
            // stylesheets: path.resolve(__dirname, 'src/stylesheets/sass'),
            // images: path.resolve(__dirname, 'src/static-media/img'),
            // fonts: path.resolve(__dirname, 'src/static-media/fonts'),
            // core: path.resolve(__dirname, 'src/plex/plex/core/static/core'),
            // contrib: path.resolve(__dirname, 'storage/static/contrib'),
            // sileo: path.resolve(__dirname, 'src/sileo/sileo/static/sileo'),

            // aliases to vue subdirectories
            source: path.resolve(__dirname, 'video/static/vue'),
            components: path.resolve(__dirname, 'video/static/vue/components'),

            // aliases to amd modules for compatibility
            // zepto: path.resolve(__dirname, 'storage/static/core/js/lib/zepto/zepto-1.1.6.min.js'),
            // stapes: path.resolve(__dirname, 'storage/static/core/js/lib/stapes/stapes-0.8.1-min.js'),
            // promise: path.resolve(__dirname, 'storage/static/core/js/lib/promise-polyfill/Promise.js')
        }
    }
};
