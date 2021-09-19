FROM node:14.17

WORKDIR /website

COPY . .

RUN npm install

EXPOSE 3000

RUN npm run build

ENTRYPOINT [ "npm", "run", "start" ]