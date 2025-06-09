import React from "react";
import Image from "next/image";
import style from "./UserBanner.module.scss";
import banner from "@/public/default_banner.jpg";
import icon from "@/public/default_basil.jpg";
import { UserData } from "@/types/user";

interface UserBannerProps {
    data: UserData | undefined;
}

export default function UserBanner({ data }: UserBannerProps) {
    return (
        <div className={style.banner__box}>
            <Image
                src={
                    data?.profile_banner
                        ? `http://127.0.0.1:8000${data?.profile_banner}`
                        : banner
                }
                className={style.banner__cover}
                alt="cover"
                objectFit="cover"
                height={500}
                width={500}
            />
            <div className={style.banner__details}>
                <Image
                    src={
                        data?.profile_picture
                            ? `http://127.0.0.1:8000${data?.profile_picture}`
                            : icon
                    }
                    height={120}
                    width={120}
                    alt="profile-pic"
                    className={style.banner__image}
                    
                ></Image>
                <div className={style.banner__text}>
                    <div className={style.banner__text_user}>
                        {data?.username}
                    </div>
                    <div className={style.banner__text_school}>
                        {data?.university}
                    </div>
                </div>
            </div>
        </div>
    );
}
