# --- STAGE 1: BUILD THE DOCUSAURUS SITE ---
# Use a Node.js image as the builder environment
FROM node:20-alpine AS build

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json (or yarn.lock) first to leverage Docker caching.
# This step only re-runs if the dependencies change.
COPY package*.json ./
# If you are using Yarn, use the next line instead:
# COPY package.json yarn.lock ./

# Install dependencies
RUN npm install
# If you are using Yarn, use the next line instead:
# RUN yarn install

# Copy the rest of the application source code
COPY . .

# Build the Docusaurus project
# The output is typically placed in the 'build' directory
RUN npm run build
# If you are using Yarn, use the next line instead:
# RUN yarn build


# --- STAGE 2: SERVE THE STATIC FILES (PRODUCTION IMAGE) ---
# Use a lightweight Nginx image for serving the static files
FROM nginx:alpine AS production

# Remove the default Nginx index page
RUN rm -rf /usr/share/nginx/html/*

# Copy the built static files from the 'build' stage into the Nginx public directory
# Docusaurus build output is usually in 'build'
COPY --from=build /app/build /usr/share/nginx/html

# Expose the port Nginx runs on
EXPOSE 80

# The default Nginx command to start the web server is used, so no CMD instruction is needed,
# but if you need one, it would look like this:
# CMD ["nginx", "-g", "daemon off;"]