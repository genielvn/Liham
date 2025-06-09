import path from "path";

/** @type {import('next').NextConfig} */
const nextConfig = {
    webpack: (config) => {
        config.resolve.alias = {
            ...config.resolve.alias,
            "@styles": path.resolve("./styles"), // Define the alias for styles
        };
        return config;
    },
    images: {
        domains: ["127.0.0.1", "localhost"], // Add your domains here
    },
};

export default nextConfig;
