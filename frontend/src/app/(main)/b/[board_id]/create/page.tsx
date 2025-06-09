"use client";
import { useEffect, useState } from "react";
import Link from "next/link";
import style from "./page.module.scss";
import { useRouter, notFound } from "next/navigation";
import Image from "next/image";
import Checkbox from "@/components/Checkbox";
import { BoardData } from "@/types/board";
import { createThread, getBoard, getSelfUserData } from "@/services/api";

interface CreateThreadProps {
    params: {
        board_id: string;
    };
}

export default function CreateThread({ params }: CreateThreadProps) {
    const { board_id } = params;
    const [data, setData] = useState<BoardData | null>(null);
    const [error, setError] = useState<boolean>(false);

    useEffect(() => {
        const fetchBanned = async () => {
            try {
                const response = await getSelfUserData();
                if (response.data.user.is_banned) {
                    setError(true);
                }
            } catch (error) {
                setError(true);
            }
        };
        const fetchBoard = async () => {
            try {
                const response = await getBoard(board_id);
                setData(response.data);
                console.log(response.data);
            } catch (error) {
                setError(true);
            }
        };
        
        fetchBanned();
        fetchBoard();
    }, []);

    const [title, setTitle] = useState("");
    const [body, setBody] = useState("");
    const [image, setImage] = useState<File | null>(null);
    const [imagePreview, setImagePreview] = useState<string | null>(null);
    const [isSubmitting, setIsSubmitting] = useState(false);
    const [message, setMessage] = useState("");
    const [isAnonymous, setIsAnonymous] = useState(false);
    const router = useRouter();

    if (error) return notFound();

    const handleImageChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        if (event.target.files) {
            const file = event.target.files[0];
            setImage(file);
            setImagePreview(URL.createObjectURL(file));
        }
    };

    const handleSubmit = async (event: React.FormEvent) => {
        event.preventDefault();
        setIsSubmitting(true);
        setMessage("");

        if (!title) {
            setMessage("Please set a title.");
            setIsSubmitting(false);
            return;
        }

        if (title.length > 100) {
            setMessage("Title is too long! Please limit to 100 characters.");
            setIsSubmitting(false);
            return;
        }

        if (!body && !image) {
            setMessage("Please post an image or a body.");
            setIsSubmitting(false);
            return;
        }

        const formData = new FormData();
        formData.append("title", title);
        formData.append("body", body);
        if (image) formData.append("img_upload", image);
        formData.append("anonymous", isAnonymous ? "true" : "false");

        try {
            const response = await createThread(board_id, formData);
            const thread_id = response.data.id;
            router.push(`/b/${board_id}/${thread_id}`);
        } catch (err) {
            setMessage(
                "Something went wrong. Please try again. Error message: " + err
            );
            setIsSubmitting(false);
        }
    };

    return (
        data && (
            <>
                <Link className="subheader" href={`/b/${data?.board_id}`}>
                    /{data?.board_id}/ - {data?.name}
                </Link>
                <h2>Start a New Thread</h2>
                <form onSubmit={handleSubmit}>
                    <div className={style.new_thread__input_divider}>
                        <label htmlFor="thread-new-title">Title</label>
                        <input
                            type="text"
                            id="thread-new-title"
                            value={title}
                            onChange={(e) => setTitle(e.target.value)}
                        />
                    </div>
                    <p className="right">{100 - title.length}</p>
                    <div className={style.new_thread__input_divider}>
                        <label htmlFor="thread-new-text">Content</label>
                        <textarea
                            id="thread-new-text"
                            value={body}
                            onChange={(e) => setBody(e.target.value)}
                        />
                    </div>
                    <div className={style.new_thread__input_divider}>
                        <label htmlFor="thread-new-image">Image</label>
                        <input
                            type="file"
                            id="thread-new-image"
                            onChange={handleImageChange}
                            accept="image/*"
                        />
                        {imagePreview && (
                            <div className={style.new_thread__img_preview}>
                                <Image
                                    src={imagePreview}
                                    alt="Thread Image Preview"
                                    layout="responsive"
                                    width={400}
                                    height={400}
                                />
                            </div>
                        )}
                    </div>
                    {message && <p className="error">{message}</p>}
                    <div className={style.new_thread__input_divider_flexrow}>
                        <button
                            type="submit"
                            className="btn-small btn-pink"
                            disabled={isSubmitting}
                            style={{ marginRight: "20px" }}
                        >
                            {isSubmitting ? "Submitting..." : "Post"}
                        </button>
                        <Checkbox
                            id="anon"
                            text="Post as Anonymous"
                            checked={isAnonymous}
                            onChange={() => setIsAnonymous(!isAnonymous)}
                        />
                    </div>
                </form>
            </>
        )
    );
}
