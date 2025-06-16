# Install dependencies and build Next.js
FROM node:20-alpine AS builder

WORKDIR /app

COPY ./ ./

RUN npm install && npm run build

# Serve with a distroless image
FROM node:20-alpine AS runner

WORKDIR /app

COPY --from=builder /app ./

EXPOSE 3000

CMD ["npm", "run", "start"]