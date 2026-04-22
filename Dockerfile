# Stage 1: Build static site with Quartz
FROM node:22-slim AS builder

WORKDIR /build

# Install deps first (better layer caching)
COPY portal/package.json portal/package-lock.json ./
RUN npm ci

# Copy Quartz framework source and config
COPY portal/quartz ./quartz
COPY portal/quartz.config.ts portal/quartz.layout.ts portal/tsconfig.json portal/globals.d.ts portal/index.d.ts ./

# Copy wiki content as Quartz content directory
COPY wiki ./content

# Build static site (outputs to public/)
RUN npx quartz build

# Stage 2: Serve with nginx
FROM nginx:alpine

COPY --from=builder /build/public /usr/share/nginx/html
COPY portal/nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
